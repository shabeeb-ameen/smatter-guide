# Chapter 3: Submitting Condor jobs

HTCondor is a software system developed at UW Madison. I would highly recommend skimming through their manual: 

    https://htcondor.readthedocs.io/en/latest/users-manual/welcome-to-htcondor.html

The basic idea behind HTCondor: utilize all the computers on campus to do compute jobs. When you submit a compute job, HTCondor keeps it on a queue, performing it when computational resources become

Here we will use an illustrative example for submitting multiple jobs on the cluster. The general technique suggested here certainly be improved upon by reading the manual and other resources. 

I will flesh this out with further tips and tricks (as I learn new things!), and please feel free to contact me in the meantime if you have particular suggestions or questions.

## When should you use the cluster?

The computers that make up the cluster are, in fact, quite slow individually (speaking from personal experience, and when compared to a good laptop or PC)

Therefore, the ideal use case is one where you are interested in multiple runs of the same code. When you submit these jobs as individual runs, the code is executed in parallel.


## An example: Prime Factorization.

The code for this example can be found in  "examples/PrimeFactorization" in this repository.

**Task:** Prime factorize the numbers from 42 to 49 (eight numbers).

We will submit these as 8 different jobs.

### Step 1: Write the code and transfer it to the cluster.

Write a Python code that executes with a positive integer input argument and returns a file with an array of prime numbers

For reference, consider the 

### Step 2: 
