# logmailer
This is a simple python3 terminal program to send a suricata log file generated by a linux and/or unix system.

# How to use

## Please ensure that typer is installed!! 
- pip install typer

### Save surifast2csv.py and configure the required parameters as indicated in the code.
### surifast2csv may only be used to convert Suricata logs to csv, unless otherwise configured in the outfile write method. See code for more.
### Save mail2ad to your server and run as follows:
- Configure path to file to be attached.\
- sudo python3 mail2ad.py\
- Once executed, will you be presented with the following requirements:
##### Subject:
##### Body:
##### Sender email address:
##### Recipient email address:
##### Password:
##### Port:
##### Smtp Server:

### Once confirmed, an email will be sent to the specified email address provided that the password, port and server are correct!

# Alternatively:
- The program may be adpated for use as a script and scheduled as a cron job.
