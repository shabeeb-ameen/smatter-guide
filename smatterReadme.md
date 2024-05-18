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

1. Use ssh-keygen (a tool that should ship with your device) to generate a public and private key pair. That is, open a terminal *on your device* and enter

        ssh-keygen -t ed25519 -C "<your_email@example.com>"

Notes:
  + Your email here is merely a label for the ssh key, and you may use any other label of your choosing.
  + The keygen tool lets you choose the filename and location (default location: ~./ssh) and a password for the key (no password by default). To accept the default settings (which I think are adequate) just press enter when prompted (dont type in anything else!)

2. You should now copy *the public key* to the cluster. If you used the defaults, your public key is now probably stored in your computer in ~/.ssh/id_ed25519.pub (please confirm this and change the command below as required). You can copy this to the cluster by entering the following command in the terminal:

        ssh-copy-id -i ~/.ssh/id_ed25519.pub <username>@smatter-login.syr.edu

   This will prompt you for your netID password, but once this process is complete you will no longer need to enter a password for a SSH connection :)
