.. Darte7 documentation master file, created by
   sphinx-quickstart on Sat Jun 28 09:15:01 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Darte7's documentation!
==================================

Darte7 will help you downloading video resources on Arte+7
(http://www.arte.tv/guide/fr/plus7/).

Getting Started
---------------

*darte7* is a simple Python script which aims at giving the URL of a
downloadable video from the Arte+7 site.

Basically, the first step consists in browsing the http://www.arte.tv/guide/fr/plus7/ and use the URL to determine the URL of the linked video.

Example::

    stac@mercure:~/Films/documentaires/arte7$ darte7 http://www.arte.tv/guide/fr/plus7/?em=048693-000
    http://artestrsmv.rd.llnwd.net/o35/nogeo/tvguide_reach/048693-000-A_HQ_2_VOF_01347163_MP4-1500_AMM-Reach.mp4

This can easily be coupled to a downloader software like wget or curl::

    stac@mercure:~/Films/documentaires/arte7$ wget `darte7 http://www.arte.tv/guide/fr/plus7/?em=048693-000` -O Le_système_Ponzi.mp4

That's all folks ! You cannot do simpler.
