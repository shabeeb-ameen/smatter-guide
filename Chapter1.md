# Chapter 1: Running Python Scripts

In this chapter, we outline some tips on running python scripts in your shell session on smatter. That is, the terminal you ssh into with

    ssh <username>@smatter-login.syr.edu

**Crucially, this discussion is *not* about how to submit jobs with Condor. For that, please see the next chapter.**

Now, strictly speaking, running python scripts on your shell session is not really necessary. You can always submit any python script as a Condor job. However, it may sometimes be useful for some quick scripting tasks.

## Installing Miniconda

If you log in to your smatter shell session and enter

    python3 --version

you may have some python3 installation available.

However, you may not have python's package manager, pip. You can confirm with

    pip3 --version

As a result, any python scripts you run with this python installation can only include core python library (which do not, for example, include numpy!)

Since you do not have sudo access to smatter, a good course of action to get a python installation with pip is to install miniconda. Please follow the instructions in https://docs.anaconda.com/free/miniconda/index.html

(I will flesh out this section with more details on how to install miniconda. For now if you are doing this and need help, please contact me.)

## Initializing Conda Environment

I use

    source ~/.bashrc

Once your Conda environment is initialized you can use the python installation in this environment. This should have pip, which you can verify with the above commands

(more full details on this are pending for now.)