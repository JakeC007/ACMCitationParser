def main():
  print("****************************BEGIN****************************")
  outputlst = []
  outputentry = ""
  cntr = 0
  fInput = open('input.txt', 'r')
  lines = fInput.read().splitlines()
  fInput.close() 
  for line in lines:
    if line == "": #skip newline char lines which show up as empty
      continue
    words = line.split()
    if words[0] != "keywords:":
      outputentry += line #+ '\n'
      cntr+=1
    if cntr == 3:
      outputlst.append(outputentry + '\n')
      outputentry = ""
      cntr = 0
  for entry in outputlst:
    print(entry)
  print("Number of entries %d" %(len(outputlst)))

  fOutput = open("output.txt", 'x')
  fOutput.writelines(outputlst) 


main()
