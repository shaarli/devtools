#!/usr/bin/env python3
"""
Generates Netscape bookmark dumps

See:
- https://github.com/shaarli/netscape-bookmark-parser
"""
from argparse import ArgumentParser
from random import randint

from faker import Faker

HEADER = '''<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
It will be read and overwritten.
Do Not Edit! -->
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>'''

START_TAG = '<DL><p>'
END_TAG = '</DL><p>'

T_BOOKMARK_DT = (
    '<DT><A HREF="{url}" ADD_DATE="{date}" PRIVATE="{private}"'
    ' TAGS="{tags}">{title}</A>'
)
T_BOOKMARK_DD = '<DD>{description}'


class FakeBookmark():
    """Bookmark entry generated by Faker"""
    # pylint: disable=too-few-public-methods

    def __init__(self):
        # pylint: disable=no-member
        fake = Faker()
        self.url = fake.uri()
        self.date = fake.unix_time()
        self.private = randint(0, 1)
        self.tags = fake.words(nb=randint(0, 5))
        self.title = fake.sentence(nb_words=randint(1, 10))
        self.description = fake.paragraphs(nb=randint(0, 2))

    def netscape_str(self):
        """Netscape entry representation"""
        bkm = T_BOOKMARK_DT.format(
            url=self.url,
            date=self.date,
            private=self.private,
            tags=' '.join(self.tags),
            title=self.title
        )
        if self.description:
            bkm = '{dd}\n{dt}'.format(
                dd=bkm,
                dt=T_BOOKMARK_DD.format(description='\n'.join(self.description))
            )
        return bkm


def generate_bookmarks(number):
    """Generate a fake Netscape bookmark list"""
    bookmarks = '\n'.join(
        [FakeBookmark().netscape_str() for _ in range(number)]
    )
    return '\n'.join([
        HEADER,
        START_TAG,
        bookmarks,
        END_TAG
    ])


def main():
    """Main entrypoint"""
    parser = ArgumentParser()
    parser.add_argument(
        '-n',
        '--number',
        type=int,
        default=1000,
        help="Number of bookmarks to generate"
    )
    parser.add_argument(
        '-o',
        '--output',
        default='bookmarks.htm',
        help="Output file"
    )

    args = parser.parse_args()

    with open(args.output, 'w') as f_out:
        f_out.write(generate_bookmarks(args.number))


if __name__ == '__main__':
    main()
