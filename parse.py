"""
IEEE Citation Parser
Written by Jake Chanenson on July 1, 2020

@params: ensure that the file to parse is titled input.txt and is at same folder level as this python file
@output: creates formatted text so when you paste it into a spreadsheet each citation has its own cell with buffer cells on either side
Note: yes write to csv exists but this is a quick and dirty tool that far quicker than importing a csv file every time I generate a new list of entries 
"""

def main():
  outputlst = []
  outputentry = ""
  cntr = 0
  
  #read from file
  fInput = open('input.txt', 'r')
  lines = fInput.read().splitlines()
  fInput.close() 
  
  for line in lines:
    if line == "": #skip newline char lines which show up as empty
      continue
    words = line.split()
    if words[0] != "keywords:":
      outputentry += line + " " 
      cntr+=1
    if cntr%3 == 0: # if all three citation elements are in the str, add to lst
      outputlst.append(outputentry + '\n')
      outputlst.append('\n')
      outputentry = ""
      
      #cntr = 0 #reset count for elements in citation

  #write to file
  fOutput = open("output.txt", 'w')
  fOutput.writelines(outputlst) 
  fOutput.close()
  print("Citations parsed and put in output.txt")
  print(print("Number of entries: %d" %(cntr/3)))

if __name__ == "__main__":
  main()
