# IEEE Citation Parser 
This is a quick and dirty little script that I wrote to help me parse IEEE plain texts citations for a spreadsheet. 
The premise is simple: 
* the script takes in a list of plain text citations from IEEE
* the script strips the keywords from the citation because I don't need that for the sorting document 
* the script outputs a `.txt` file called `output.txt` that when pasted into a spreadsheet program will paste each citation in a cell with an empty cell padding between each entry

## How to use
1. Clone the repo
2. Create a the file `input.txt` at the root level of the repo
2. Copy the plain text citations from IEEE
3. Paste the citations into `input.txt`
4. Run the program
5. Copy the contexts of `output.txt`

