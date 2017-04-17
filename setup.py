from setuptools import setup, find_packages
setup(name='pixiedust_wcs_analysis',
	  version='0.1',
	  description='Pixie App POC for analyzing performance of Watson Conversation Classification',
	  url='https://github.com/ibm-cds-labs/pixiedust_wcs_analysis',
	  install_requires=['pixiedust'],
	  author='David Taieb, Dan O\'Connor',
	  author_email='david_taieb@us.ibm.com, dan_oconnor@us.ibm.com',
	  license='Apache 2.0',
	  packages=find_packages(),
	  include_package_data=False,
	  zip_safe=False
)
