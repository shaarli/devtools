Shaarli devtools
================

Scripts and utilities to assist Shaarli development, testing and debugging.

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
