<<<<<<< HEAD
# Regular_expressions

- For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

## Requirements

General:

- Allowed editors: vi, vim, emacs

- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line

- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable

- The first line of all your Bash scripts should be exactly *#!/usr/bin/env ruby*

- All your regex must be built for the Oniguruma library
=======
**# alu-scripting README**

This repository, named alu-scripting, is a collection of Ruby scripts utilizing regular expressions. Each script focuses on different patterns using the `scan` method to extract specific text from the provided input.

### Regular Exp

The scripts are designed to showcase regular expressions in the context of pattern matching within text data.

### Usage

To run these scripts, ensure you have Ruby installed on your system. Execute each script by passing the desired text as a command-line argument.

#### Examples:

1. **First Script:**
   ```ruby
   #!/usr/bin/env ruby
   puts ARGV[0].scan(/School/).join
   ```
   This script scans the input for the word "School" and prints the result.

2. **Second Script:**
   ```ruby
   #!/usr/bin/env ruby
   puts ARGV[0].scan(/hbt{2,5}n/).join
   ```
   It searches for patterns with 'hbt' followed by 2 to 5 't' and ending with 'n'.

3. **Third Script:**
   ```ruby
   #!/usr/bin/env ruby
   puts ARGV[0].scan(/hb?tn/).join
   ```
   This script looks for patterns with 'hbt', an optional 'b', and 'tn'.

4. **Fourth Script:**
   ```ruby
   #!/usr/bin/env ruby
   puts ARGV[0].scan(/hbt{1,5}n/).join
   ```
   Searches for patterns with 'hbt' followed by 1 to 5 't' and ending with 'n'.

5. **Fifth Script:**
   ```ruby
   #!/usr/bin/env ruby
   puts ARGV[0].scan(/hbt*n/).join
   ```
   This script matches patterns with 'hbt' followed by zero or more 't' and ending with 'n'.
6. **ETC**
### Cloning Steps

To clone this repository and start using the scripts:

1. Open a terminal.

2. Run the following command:
   ```
   git clone https://github.com/lscblack/alu-scripting.git
   ```
3. Run The Following command open script folder
    ```
    cd regular_expressions
    ```
### Author

This collection of scripts was created by **lscblack (Loue Sauveur Christian)**.

### Contribution

Feel free to contribute by adding more scripts that demonstrate different regular expression patterns or by improving the existing ones.

### License

This project is open-source under the MIT License - see the [LICENSE](LICENSE) file for details.
>>>>>>> 1344d66a427a81fc111b5d4cbef668446ed7e34c
