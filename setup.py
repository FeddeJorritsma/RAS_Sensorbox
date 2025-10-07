# Make sure these imports are at the top of the file
import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'main_package'

setup(
    # ... other settings like name, version, etc.
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # --- THIS IS THE LINE YOU NEED TO ADD ---
        # It finds all files in your 'launch' folder and installs them
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jouw_naam',
    maintainer_email='jouw_email@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)