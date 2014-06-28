darte7: Downloader for Arte+7
=============================

This simple program returns the URL of downloadable resources on Arte+7 site.

You simply have to go to http://www.arte.tv/guide/fr/plus7/, select the show
you want to download. darte7 can then be used with programs like wget or curl
to download the film.

For instance::

    wget `darte7 http://www.arte.tv/guide/fr/plus7/?em=044964-000`.
