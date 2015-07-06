# The GogoKit Python Toolkit

[![Build Status](https://travis-ci.org/viagogo/gogokit.py.svg?branch=master)][travis]

[travis]: https://travis-ci.org/viagogo/gogokit.py
[apidocs]: http://developer.viagogo.net
[submitanissue]: https://github.com/viagogo/gogokit.py/issues
[apidocsgettingstarted]: http://developer.viagogo.net/#getting-started

Python toolkit for working with the viagogo API. Our [developer site][apidocs]
documents all of the viagogo APIs.


## Installation

Install via pip

    pip install --upgrade gogokit

... or

    easy_install --upgrade gogokit


## Usage

See our [developer site][apidocsgettingstarted] for more examples.

```python
from gogokit import ViagogoClient

# All methods require OAuth2 authentication. To get OAuth2 credentials for your
# application, see http://developer.viagogo.net/#authentication.
client = ViagogoClient(YOUR_CLIENT_ID, YOUR_CLIENT_SECRET)


# Get an access token. See http://developer.viagogo.net/#getting-access-tokens
token = client.oauth.get_client_access_token()
client.set_token(token)


# Get a list of events, categories, venues and metro areas that match the given
# search query
search = client.search.get_search_results({ "query": "Real Madrid" })

# Get the different event genres (see http://developer.viagogo.net/#entities)
genres = client.category.get_genres()
```


## How to contribute

All submissions are welcome. Fork the repository, read the rest of this README
file and make some changes. Once you're done with your changes send a pull
request. Thanks!


## Need Help? Found a bug?

Just [submit a issue][submitanissue] if you need any help. And, of course, feel
free to submit pull requests with bug fixes or changes.


## Supported Python Versions

This library aims to support and is [tested against][travis] the following Python
implementations:

* Python 2.6
* Python 2.7
* Python 3.3
* Python 3.4

If something doesn't work on one of these python versions, it's a bug.

This library may inadvertently work (or seem to work) on other Python
implementations, but support will only be provided for the versions listed
above.

If you would like this library to support another Python version, you may
volunteer to be a maintainer. Being a maintainer entails making sure all tests
run and pass on that implementation. When something breaks on your
implementation, you will be responsible for providing patches in a timely
fashion. If critical issues for a particular implementation exist at the time
of a major release, support for that Python version may be dropped.
