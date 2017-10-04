#!/usr/bin/env python3
"""
Generates a Markdown changelog from GitHub release notes

See:
- http://keepachangelog.com/en/0.3.0/
- https://developer.github.com/v3/
"""
import json
from argparse import ArgumentParser

import requests

CHANGELOG_HEADER = """# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).
"""
GITHUB_RELEASE_ENDPOINT = 'https://api.github.com/repos/{user}/{repo}/releases'


def generate_changelog(releases):
    """Generates a changelog from GitHub release notes"""
    changelog = ""

    for release in releases:
        changelog += "\n## [{tag}]({url}) - {date}\n{body}\n".format(
            tag=release['tag_name'],
            url=release['html_url'],
            date=release['published_at'].split('T')[0],
            body=release['body'].replace('\r\n', '\n').replace('##', '###')
        )

    return changelog


def main():
    """Main entrypoint"""
    parser = ArgumentParser()
    g_source = parser.add_mutually_exclusive_group()
    g_source.add_argument(
        '-j',
        '--json-file',
        help="JSON file containing GitHub release data"
    )
    g_source.add_argument(
        '-r',
        '--gh-repo',
        help="GitHub repository, e.g.: user/repository"
    )
    parser.add_argument(
        '-o',
        '--output',
        default='CHANGELOG.md',
        help="CHANGELOG file"
    )
    args = parser.parse_args()

    if args.json_file:
        with open(args.json_file) as f_json:
            releases = json.loads(f_json.read())

    elif args.gh_repo:
        user, repo = args.gh_repo.split('/')
        response = requests.get(
            GITHUB_RELEASE_ENDPOINT.format(user=user, repo=repo)
        )
        response.raise_for_status()
        releases = response.json()

    with open(args.output, 'w') as f_output:
        f_output.write(CHANGELOG_HEADER)
        f_output.write(generate_changelog(releases))


if __name__ == '__main__':
    main()

