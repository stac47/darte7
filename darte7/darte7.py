#!/usr/bin/env python3
# vi:set fileencoding=utf-8 :

"""
Created on 2014-06-14

@author : Laurent Stacul
"""
import json
import argparse
from urllib.parse import urlparse, parse_qs
from urllib.request import urlopen
from darte7 import __version__

TVGUIDE = "http://arte.tv/papi/tvguide/videos/stream/player/F/" + \
    "{}_PLUS7-F/ALL/ALL.json"


def extract_json_tvguide(url):
    """ From the URL given on http://www.arte.tv/guide/fr/plus7, this function
    the JSON TV guide where all the videos urls are stored."""

    parsed = urlparse(url)
    query = parsed.query
    video_id = parse_qs(query)["em"][0]
    http_response = urlopen(TVGUIDE.format(video_id))
    s = http_response.read().decode("utf-8")
    video_metadata = json.loads(s)
    return video_metadata['videoJsonPlayer']['VSR']['HTTP_REACH_EQ_1']['url']


def main():
    description = "Arte+7 Download Helper, version {}".format(__version__)
    epilog = "This software is not linked to Arte channel."
    parser = argparse.ArgumentParser(description=description,
                                     epilog=epilog)
    parser.add_argument("url", help="The URL of the video on Arte+7 site")
    args = parser.parse_args()
    print(extract_json_tvguide(args.url))

if __name__ == "__main__":
    main()
