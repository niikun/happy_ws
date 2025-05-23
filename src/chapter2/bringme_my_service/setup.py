from setuptools import find_packages, setup

package_name = 'bringme_my_service'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='niikun0209@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'bringme_service_node = bringme_my_service.bringme_service_node:main',
            'bringme_client_node  = bringme_my_service.bringme_client_node:main',
        ],
    },
)
