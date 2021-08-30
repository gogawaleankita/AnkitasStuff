import re
import os

from jupyter_core.application import JupyterApp, base_aliases, base_flags
from traitlets.config import catch_config_error

from ._version import __version__
from .path_utils import search_jupyter_paths, resolve_filepath

config_aliases = {}
config_aliases.update(base_aliases)

config_flags = {}
config_flags.update(base_flags)

class JupyterConfigListApp(JupyterApp):
    name = "jupyter-config-list"
    description = """List the jupyter configuration files that will be found 
if you run a JupyterApp in the current context."""
    
    def start(self):
        for file_name in search_jupyter_paths():

            print(resolve_filepath(file_name))

class JupyterConfigSearchApp(JupyterApp):
    name = "jupyter-config-search"
    description = """Search for a provided term in the jupyter configuration files 
that will be found if you run a JupyterApp in the current context."""
    
    def start(self):
        search_term = self.extra_args[0]
        assert len(search_term) > 0
        
        # go through files,
        # if search term found in file
        # print name, line_no, content
        for file_name in search_jupyter_paths():
            print_indexed_content(file_name=file_name, search_term=search_term)

class JupyterConfigApp(JupyterApp):
    name = "jupyter-config"
    description = "A Jupyter Application for searching in and finding config files."
    # aliases = config_aliases
    # flags = config_flags
    version = __version__
    
    subcommands = dict(
        list=(JupyterConfigListApp, JupyterConfigListApp.description),
        search=(JupyterConfigSearchApp, JupyterConfigSearchApp.description),
    )
    
    @catch_config_error
    def initialize(self, argv=None):
        super(JupyterConfigApp, self).initialize(argv)
        if not self._dispatching:
            self.print_help(False)

    
def print_indexed_content(file_name='', search_term=''):
    with open(file_name,"r") as f:
        if search_term in f.read():
            f.seek(0)
            line_numbers_match = []
            for line_no, text in enumerate(f,1):
                if search_term in text:
                    line_numbers_match.append((line_no,text.strip()))
            output = ["{}: {}".format(x,y) for x,y in line_numbers_match]
            print(resolve_filepath(file_name) + "\n" + "\n".join(output),"\n")


main = launch_new_instance = JupyterConfigApp.launch_instance
