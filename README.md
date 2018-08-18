Python package to easily use the GitHub API.

### Installation
Install using `pip3 install githubAPy`

### Usage
* Import the class
`from githubAPy import gapy`
* Create an object and pass the GitHub Access Token
`a = gapy('<access_token_here>')`

Multiple actions are supported

* `a.me` return your information in dict (JSON) format.
* `a.user('<username>')` return the information of a user.
* `a.create_fork('<owner>', '<repository>')` create a fork of the specified repository and returns url of the forked repository if fork successfully created else raises an error.
* `a.update_with_upstream('<owner>', '<repository>')`  updates your forked repository master with the upstream master. Returns `True` if updated successfully else raises an error.

More feature to be added in later versions.
