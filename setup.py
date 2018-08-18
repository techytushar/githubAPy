import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(name='githubAPy',
      description='Python wrapper to easily communicate with the GitHub API',
      long_description=long_description,
      long_description_content_type="text/markdown",
      version='0.4',
      url='https://github.com/techytushar/githubAPy',
      author='Tushar Mittal',
      author_email='chiragmittal.mittal@gmail.com',
      license='GNU General Public License v3 (GPLv3)',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 3'
      ],
      keywords='github api python wrapper',
      packages=setuptools.find_packages(),
      install_requires=[
          'requests',
      ]
)
