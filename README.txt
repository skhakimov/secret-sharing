This is an implementation of Shamir Secret Sharing Scheme.

Only standard python libraries are being used. 
No need to install additional modules.

The program consists of following files:
interpolate.py: file that contains the interpolate class
secret.py: file that contains the class to generate a secret
threshold_scheme.py: contains functions to recover and generate secrets. 
GUI.py: User Interface for the program

**********************************************************
To run, go to the code directory and type into command line:

python GUI.py

1) To generate shares, input: 
Number of total shares 
Number of required shares
Secret string consisting of ASCII characters.

2) To recover secret: provide shares that are enough to recover the secret.

**********************************************************
Optionally, the program can be run from the command line.

1) To generate shares, use:  
python theshold_scheme.py generate <filename> -o <output>
<filename> must be a text file with: 
1st line = required number of shares
2nd line = total number of shares
3rd line = secret passphrase
<output> is a name of a file where shares will be written to.

2) To recover shares, use: 
python theshold_scheme.py recover <filename> -o <output>
<filename> must be a text file with separate share on each line.
<output> is a name of a file where secret will be written to.


Author: Samir Khakimov