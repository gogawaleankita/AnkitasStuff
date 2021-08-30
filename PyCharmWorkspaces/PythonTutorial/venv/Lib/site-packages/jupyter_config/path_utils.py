import sys
import glob
import os
import re 
import itertools

from notebook.nbextensions import NBCONFIG_SECTIONS
import jupyter_core.paths as jpaths

def valid_gen_conf_file(file_path, name_regex):
    file_name = os.path.basename(file_path)
    return (os.path.isfile(file_path) 
            and name_regex.match(file_name))
            
def generate_potential_paths():
    """Generate all of the potential paths available in the current context.
    
    
    """
    base_conf_paths = list(filter(os.path.isdir, jpaths.jupyter_config_path()))
        
    nbconfig_base_paths = list(filter(os.path.isdir, (os.path.join(d, 'nbconfig') 
                                                      for d in base_conf_paths)))
    conf_d_paths = list(filter(os.path.isdir, (os.path.join(d, 'jupyter_notebook_config.d') 
                                                            for d in base_conf_paths)))
    for d in nbconfig_base_paths:
        config_path_segment = list(filter(os.path.isdir, (os.path.join(d, section+'.d') 
                                                          for section in NBCONFIG_SECTIONS)))
        conf_d_paths.extend(config_path_segment)
    
    
    return {'base_conf_paths': base_conf_paths,
            'nbconfig_base_paths': nbconfig_base_paths,
            'conf_d_paths': conf_d_paths,
            }
    
        
def search_jupyter_paths():
    
    potential_paths = generate_potential_paths()
    
    base_conf_re = re.compile(r"jupyter_(\w*_|)config\.(json|py)")
    local_conf_file_list = [f for f in glob.iglob("*")
                           if valid_gen_conf_file(f, base_conf_re)]
    
    base_conf_file_list = [f for d in potential_paths['base_conf_paths']
                           for f in glob.iglob(d+"/*")
                           if valid_gen_conf_file(f, base_conf_re)]
    
    
    nbconfig_pattern = r"({})\.json".format("|".join(n for n in NBCONFIG_SECTIONS))
    nbconfig_re = re.compile(nbconfig_pattern)
    nbconfig_file_list = [f for d in potential_paths['nbconfig_base_paths']
                          for f in glob.iglob(d+"/*")
                          if valid_gen_conf_file(f, nbconfig_re)]


    confd_re= re.compile(r"\w*\.json")
    confd_file_list = [f for d in potential_paths['conf_d_paths']
                       for f in sorted(glob.iglob(d+"/*"), reverse=True)
                       if valid_gen_conf_file(f, confd_re)]
    filename_iterator = itertools.chain(local_conf_file_list,
                                        base_conf_file_list,
                                        nbconfig_file_list,
                                        confd_file_list)
    for filename in filename_iterator:
        yield filename

    
def resolve_filepath(file_path):
    if os.path.realpath(file_path) != file_path:
        real_file_path = " -> {}".format(os.path.realpath(file_path))  
    else: 
        real_file_path = ""
    return "{}{}".format(file_path, real_file_path) 
