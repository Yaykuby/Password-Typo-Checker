# Password-Typo-Checker
An algorithm written in Python to check passwords for and weigh the likelihood of common typos.

# About
This algorithm combines weights produced from a custom Hamming Distance table with a Levenshtein Algorithm implementation to detect and judge certain typos within passwords. A stored password, _s1_, is checked against a newly entered password, _s2_. A custom edit distance score is produced, representing how likely any typos made whilst typing _s2_
are. If the total typo weight totals 1.0 or greater, the password is rejected and the user is not allowed access to their account. These weighted values along with the permittable weighted score threshold are completely customizable to ensure this algorithm can work in custom environments.

# Features
- Calculates password typo likelihoods
- Supports custom Hamming Distance table
- Customizable Levenshtein Algorithm weights

# Quick Start
### Requirements
- Python / Python3
- Your IDE of choice (If you want to customize weights or passwords)

### Downloading
- Copy/Paste into an empty Python file or download the [*Password-Typo-Checker.py*](https://github.com/Yaykuby/Password-Typo-Checker/blob/main/src/Password-Typo-Checker.py) file under [*Password-Typo-Checker*](https://github.com/Yaykuby/Password-Typo-Checker/tree/main)/[*src*](https://github.com/Yaykuby/Password-Typo-Checker/tree/main/src)/ and place it within a directory of your choosing. Then, open that file in the IDE of your choice or navigate to that file using the command line.
- Alternatively, you could clone this repo with git.

### Running
- Run the program in your IDE of choice however it runs files.
- On the command line, run the file with the command *python Password-Typo-Checker.py*
- Regardless of how you run the file, the pre-existing test cases will be shown as output. These test cases and any weights can be edited using your IDE or any text editor.

# Examples
#### Checking _Password321_ against _Password321_
Output: **0.0**
Explanation: These passwords are identical, no differences are found.

#### Checking _kitten_ against _sitting_
Output: **2.5**
Explanation: Changing the _s_ to a _k_ is viewed as an unlikely typo, same with changing the second _i_ to an _e_, thus both these changes add 1.0 weight. Additionally, removing the _g_ from the end of _sitting_ is viewed as a possible typo, therefore it only costs 0.50 weight.
