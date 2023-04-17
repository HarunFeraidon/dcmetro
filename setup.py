from setuptools import find_packages, setup
import os

with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as f:
    long_description = f.read()

setup(
    name='dcmetro',
    python_requires='>3.9',
    packages=find_packages(include=["src", "src.main"]),
    version='0.1.4',
    description='Console app for sending commands to get live information on the DC Metro',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Harun Feraidon',
    license='MIT',
    entry_points={
        "console_scripts": [
            "dcmetro = src.main.app:DcMetroApp.run_cli",
        ],
    },
    install_requires=[
          'textual[dev]',
          'python-dotenv',
      ],
)