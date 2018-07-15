Shaarli devtools
================

Scripts and utilities to assist Shaarli development, testing and debugging.

Postman
-------

Resources to test the REST API with the
`Postman <https://www.getpostman.com/>`_ HTTP development environment.

* ``Shaarli-API-v1.postman_collection.json`` contains a collection of HTTP
  requests corresponding to the endpoints of the REST API v1
* ``Shaarli-Template.postman_environment.json`` is an example environment
  that should be duplicated to define instance-specific variables (URL, API
  secrets, etc.)

The API collection comes with a pre-request script to generate a valid JSON Web
Token.

Use it when:

* you want a straightforward tool to interact with the REST API
* you want to test API endpoints
* you want to add new API endpoints

generate_netscape_bookmarks.py
------------------------------

Generates a Netscape-like bookmark export containing fake yet coherent entries
generated through the `Faker <https://github.com/joke2k/faker/>`_ library.

Use it when:

* you want to test Shaarli's bookmark import feature
* you want to test the NetscapeBookmarkParser library
* you want to diagnose performance and/or parsing issues with a large amount of
  data

We use(d) it for:

* https://github.com/shaarli/Shaarli/issues/902
* https://github.com/shaarli/Shaarli/issues/969
* https://github.com/shaarli/Shaarli/issues/985

github_release_to_changelog.py
------------------------------

Retrieves a Github repository's release notes using the Github REST API,
and generates a Markdown-formatted change log.

Use it when:

* you took the time to write Github release notes
* you realize it'd be a good thing to have these release notes as a
  SCM-managed change log

We use(d) it for:

* https://github.com/shaarli/Shaarli/issues/663
