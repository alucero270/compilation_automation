import os

'''
This script will automate the compilation process
of both the GUI and Solver. It will checkout the
latest solver/gui version from the svn on spider
and name the folders after the interface versions.
it will than use the applicable compiler to build
the GUI and solver. It will proceed to strip the
executables (when applicable) and copy them to the
appropriate deployment locations. It will finish
it's execution by launching the Bitrock installation
package creation software, copy the installation
directory to deployment location, and create a compressed
version of the install directory
'''

'''
It will begin by looking to the scripts current directory,
which should be saved as compilation_resources.
'''
temp_ba_location = 'S:\\alex_lucero\\temp_ba_location'

'''
It will then create a temp folder to save the svn checkout
to.
'''
if not os.path.exists(temp_ba_location):
    os.mkdir(temp_ba_location)
os.chdir(temp_ba_location)
print(os.getcwd())
print(os.listdir(temp_ba_location))
'''
It will then perform the checkout, parse the file, and rename it
to the final interface version (ex.Barracuda_VR_17.1.0.i021).
'''
if os.listdir(temp_ba_location) == []:
    svn_checkout = os.system("svn co file:///S:/svnadmin/vault/cpfd_gui/trunk")
os.chdir('./trunk/barracuda')
print(os.getcwd())



'''
Use applicable compiler (make, qmake, CUDA, Visual Studio, etc) to build the GUI and Solver.
'''