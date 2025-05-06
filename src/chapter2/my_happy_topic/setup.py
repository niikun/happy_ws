from setuptools import find_packages, setup

package_name = 'my_happy_topic'

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
    description='A happy topic package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'happy_publisher_node = my_happy_topic.happy_publisher_node:main',
            'happy_subscriber_node = my_happy_topic.happy_subscriber_node:main'
        ],
    },
)
