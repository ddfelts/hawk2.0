hawk2.0
=======

Using scripts

<h2>failedattempts:</h2>

   Usage: failedattempts [-h] -u USER -p PASSW -i SERVER -c CLIENT 
                         [-d DIR] -s START -e END [-db] [-l LIMIT]
                         [-t TYPE] -o OUTPUT

   Get failed attempt logins by group

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
     
