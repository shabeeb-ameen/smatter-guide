In this guide, contents in angular brackets - including the brackets themselves - are meant to be replaced by the user. For example, if your username is samwise, you should rewrite 
    <username>@mordor.com
as
    samwise@mordor.com

The steps given here should work in MacOS or Linux distros. If you are using Windows - why?
  
#  Logging in:

*If you are on the SU network (e.g using Air Orange or eduroam from SU) the following applies with no extra steps. Otherwise, please set up a VPN connection (contact research computing about setting up Azure VPN)*

Open a terminal and type in

    ssh <username>@smatter-login.syr.edu

This will prompt a password (your netID password, by default).

## Setting up a SSH key

You can avoid having to use your password everytime you log in or transfer files by setting up a SSH key pair with the cluster.

Please note that you need to do this once for each device that you plan to use to access the cluster.

1. Open a terminal on your device and enter

        ssh-keygen -t ed25519 -C "<your_email@example.com>"

Notes:
  + Your email here is merely a label for the ssh key, and you may use any other label of your choosing.
  + ssh-keygen is a key generator tool that should already exist on your computer. When you use the above command, you create a public and private key pair. The keygen tool lets you choose where these are saved (default ~./ssh) and a password for the key (no password by default). To accept the default settings (which I think are adequate) just press enter when prompted (dont type in anything else!)
2. 
