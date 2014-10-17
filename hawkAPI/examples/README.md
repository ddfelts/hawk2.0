hawk2.0
=======

Using scripts

<h2>failedattempts</h2>

Finds all failed attempts.

    $ ./failedattempts -h
      optional arguments:
      -h, --help            show this help message and exit
      -u USER, --user USER  Username
      -p PASSW, --passw PASSW
                        Password
      -i SERVER, --server SERVER
                        The hawk server IP
      -c CLIENT, --client CLIENT
                        The client name
      -d DIR, --dir DIR     location to store
      -s START, --start START
                        Start Date
      -e END, --end END     End Date
      -db, --debug          Set Debug on
      -l LIMIT, --limit LIMIT
                        Set Limit of return
      -t TYPE, --type TYPE  type of failure (login,action) default login
      -o OUTPUT, --output OUTPUT
                        output type (console,csv,xlsx) default console

<h2>SearchIPSrc</h2>

Used to search by Source

    $ ./SearchIPSrc
    optional arguments:
    -h, --help            show this help message and exit
    -u USER, --user USER  Username
    -p PASSW, --passw PASSW
                        Password
    -c SERVER, --server SERVER
                        The hawk server IP
    -g CLIENT, --client CLIENT
                        Client name
    -s START, --start START
                        Start Date of search
    -e END, --end END     End Date of search
    -i IP, --ip IP        IP address to search for
    -l LIMIT, --limit LIMIT
                        Set Limit of return
    -d, --debug           Set Debug on
    -b, --convert         return from utc to localtime
    -a, --payload         add payload 

<h2>SearchIPDst</h2>

Used to search by Destination

     $ ./SearchIPDst
     optional arguments:
     -h, --help            show this help message and exit
     -u USER, --user USER  Username
     -p PASSW, --passw PASSW
                         Password
     -c SERVER, --server SERVER
                         The hawk server IP
     -g CLIENT, --client CLIENT
                         Client name
     -s START, --start START
                         Start Date of search
     -e END, --end END     End Date of search
     -i IP, --ip IP        IP address to search for
     -l LIMIT, --limit LIMIT
                         Set Limit of return
     -d, --debug           Set Debug on
     -b, --convert         return from utc to localtime
     -a, --payload         add payload

<h2>SearchResource</h2>

Used to search by resource_addr

      $ ./SearchIPResource
      optional arguments:
      -h, --help            show this help message and exit
      -u USER, --user USER  Username
      -p PASSW, --passw PASSW
                          Password
      -c SERVER, --server SERVER
                          The hawk server IP
      -g CLIENT, --client CLIENT
                          Client name
      -s START, --start START
                          Start Date of search
      -e END, --end END     End Date of search
      -i IP, --ip IP        IP address to search for
      -l LIMIT, --limit LIMIT
                          Set Limit of return
      -d, --debug           Set Debug on
      -b, --convert         return from utc to localtime
      -a, --payload         add payload
 
