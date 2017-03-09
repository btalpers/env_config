from subprocess import call
import os


class Deployment:

    def __init__(self):
        if not self.installed():
            self.install()
        else:
            print "already deployed"


    def installed(self):
        pass

    def install(self):
        pass


class Vundle(Deployment):

    def __init__(self, install_location=None):
        
        self.install_location=install_location

        Deployment.__init__(self)

    def installed(self):
        print self.install_location
        return os.path.isdir(os.path.expanduser(self.install_location))

    def install(self):
    
        call(["git", 
              "clone", 
            "https://github.com/VundleVim/Vundle.vim.git", 
            os.path.expanduser(self.install_location)])


deployments = { "Vundle" : { "install_location" : "~/.vim/bundle/Vundle.vim" } }
    
for deployment in sorted(deployments):
    
    obj = eval(deployment)
    instance = obj(**deployments[deployment])
