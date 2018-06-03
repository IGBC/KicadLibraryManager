class backend:
    
    # API Definitions
    def list_components():
        ''' Returns a list of all component names
            available to the backend '''
        pass
   
    def def_component(name: str, version=None: str):
        ''' Returns a definition of the component for the given
            name. Can return Unknown Component Exception '''
        pass
   
   def get_component(name: str, version=None: str):
       ''' Returns a bytestring containing the KiCAD code 
           for the specified component '''
       pass
   
   def list_footprints():
       ''' Returns a list of all footprint names
           available to the backend '''
       pass
   
   def def_footprint(name: str, version=None: str)
       ''' Returns definition of given footprint '''
       pass
           
   def get_footprint(name: str, version=None: str):
       ''' Returns a tuple containing the bytestring containing the KiCAD code 
           for the specified footprint and the bytestring containing the associated 3D model '''
       pass
