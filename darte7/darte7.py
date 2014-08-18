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


def get_json_metadata(url):
    """ Retrieve the JSON video metadata from Arte+7."""

    parsed = urlparse(url)
    query = parsed.query
    video_id = parse_qs(query)["em"][0]
    http_response = urlopen(TVGUIDE.format(video_id))
    s = http_response.read().decode("utf-8")
    video_metadata = json.loads(s)
    return video_metadata


def extract_json_tvguide(url):
    """ From the URL given on http://www.arte.tv/guide/fr/plus7, this function
    the JSON TV guide where all the videos urls are stored."""

    video_metadata = get_json_metadata(url)
    available_videos = video_metadata['videoJsonPlayer']['VSR']
    for v in available_videos:
        if available_videos[v]["mimeType"] == 'video/mp4' and \
           available_videos[v]["bitrate"] < 1000 and \
           available_videos[v]["versionShortLibelle"] in ('VOF', 'VF') :
            return available_videos[v]['url']


def main():
    description = "Arte+7 Download Helper, version {}".format(__version__)
    epilog = "This software is not linked to Arte channel."
    parser = argparse.ArgumentParser(description=description,
                                     epilog=epilog)
    parser.add_argument("url", help="The URL of the video on Arte+7 site")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="Display only the video metadata JSON document")
    args = parser.parse_args()
    if args.debug:
        video_metadata = get_json_metadata(args.url)
        print(json.dumps(video_metadata, sort_keys=True, indent=4))
    else:
        print(extract_json_tvguide(args.url))

if __name__ == "__main__":
    main()
