=============
Price tracker
=============

Quickstart
==========

1. Install all dependencies::

    python setup.py develop


2. Configure environment variables::

    export MONGO_URI='mongodb://<dbuser>:<dbpassword>@<host>:<port>/<db>'

    (optional)
    export HTTP_PROXY='http://localhost:1234'
    export SPIDER_URLS_FILE='/home/user/spider_urls.txt'

3. Run crawler::
  
    $ run_crawler
