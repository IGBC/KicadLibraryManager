import os
from shutil import rmtree
import urllib.request
import json
from subprocess import call, Popen, PIPE

def get_commit(d):
    p = Popen(['git', '-C', d, 'rev-parse', 'HEAD'], stdout=PIPE)
    output = p.communicate()[0]
    return output.decode().strip()

def remove_if(d, condition):
    for f in os.listdir(d):
        if condition(f):
            if os.path.isfile(os.path.join(d, f)):
                os.unlink(os.path.join(d, f))
            else:
                if 'packages3d' in f:
                    raise Execption('Caught Red Handed')
                rmtree(os.path.join(d, f))   

#save this for later
output_json = {"version": "dev-0.1", "kicad-library": None, "pretties": []}

# Generate a list of the .pretty libraries available
repo_list = []
for repo in json.loads(urllib.request.urlopen("https://api.github.com/orgs/KiCad/repos?per_page=100").read().decode()):
    if repo["name"].endswith(".pretty"):
        repo_list.append(repo)

# Save the original PWD as the working dir
wkdir = os.getcwd();

# Clone base libary repo here
call("git clone https://github.com/KiCad/kicad-library %s" % wkdir, shell=True)
output_json["kicad-library"] = get_commit(wkdir)

# Remove all the garbage in the repo
remove_if(wkdir, lambda f: f not in ['library', 'modules', 'template'])

# Remove build files in  dir/modules
remove_if(os.path.join(wkdir, 'modules'), lambda f: f not in ['packages3d',])  

# Clean the unneeded files from packages3d
for root, dirs, files in os.walk(os.path.join(wkdir, 'modules', 'packages3d')):
    for f in files:
        if not f.endswith(".wrl"):
            os.remove(os.path.join(root, f))

# clone the .pretty repos into dir/modules/[name]
for repo in repo_list:
    call("git clone %s %s" % (repo["clone_url"], os.path.join(wkdir, "modules", repo["name"])), shell=True)
    
    # Get and store commit id
    output_json['pretties'].append({'name': repo["name"],
                                    'commit': get_commit(os.path.join(wkdir, "modules", repo["name"]))})
    
    # Remove everything that is not a kicad_mod file
    remove_if(os.path.join(wkdir, "modules", repo["name"]), lambda f: not f.endswith('.kicad_mod'))

# Dump output file
with open('.KCLIBMETADATA', 'w') as outfile:
    json.dump(output_json, outfile)

