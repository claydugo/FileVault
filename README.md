[//Author]: # (Clay Dugo)
[//Class]:  # (CSC475)
[//Prof.]:  # (Dr. Sudip Mittal) 
[//Date]:   # (Febuary 14th, 2020)
# FileVault
### CSC475 Assignment 1
Task – Creating a file vault.

File vaults are software programs that encrypt/decrypt user files so that they are protected against various attacks. Generally, these are a part of the OS disk encryption programs and supported by hardware chips that offload these computationally heavy tasks away from the main CPU(s). These chips are called security [co-processors](https://en.wikipedia.org/wiki/Secure_cryptoprocessor). For this HW however you will be implementing a software only version of the concept. You are free to use any programming language of your choice and encouraged to use standard crypto libraries.

Please use symmetric algorithms to implement your file vault. This implementation should use DES, 3DES, and AES crypto algos. The input files should be placed in a folder that is accessed and read by the program. The program should ask the user what algorithm to use for encryption & decryption (user can choose between the 3 options). If a key is needed, that should also be taken as an input using the command line. The encrypted/decrypted files should be put in a separate folder. If you need examples of input files, I suggest you download various books in .text format from the [Gutenberg](https://www.gutenberg.org/) library. These are open source books. 

Students are also required to measure the time taken by the encryption and decryption process for the 3 algorithms. Please turn in a graph that shows the time taken. Please note that the time taken also depends on the programming language you use and the specific crypto library.

Turn in your code and various screenshots that show your program in execution.

### Implementation
Instead of prompting the user many times I decided to have the program infer things from what the user inputs. 

First, the program checks if `nonce.py` exists and if it does not it creates it. Then it checks if `nonce` is set to a value. If it is the program can assume the user is attempting to decrypt the file.

Since the algorithms use different key sizes there is no reason to prompt the user for an algorithm and rather infer it from the inputted key length. 

I chose to set invalid key sizes when encrypting to default to AES and generate a key for the user.

Otherwise the program takes the user input of the key and file name, decides which algorith to use, encrypts the file, and writes the nonce (and tag if using AES) to `nonce.py` for usage when decrypting.

When decrypting the program takes the user input of the file name and key, reads the nonce (and tag if using AES) and decrpyts the file.

##### Optional:
If a user gives an invalid key the program generates a random key and encrypts with AES.


### Usage

`python3 vault.py <FILENAME> <key>`

or

`./vault.py <FILENAME> <key>`


### Addtional Thoughts

This is testing working on .txt, .zip, and .jpg files all perfectly. 
