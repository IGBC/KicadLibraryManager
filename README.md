# KicadLibraryManager
Package Manager for Kicad Libraries

This is an experimental project to create a static library manager for KiCAD projects. 
It genererates a static version of the libraries stored on KiCAD's github, strips un-needed files and then stores the resultant tree with an index of the git hashes of the repo's used.

Future functionality will allow the user to rebuild damaged librarys from the git commit information, and configure which libraries are installed.
