# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()
#print(email_one)
def censor(email_1, phrase):
  censored=email_1.replace(phrase, "xxxx")
  return censored

test="The quick brown fox jumped over the lazy brown dog"

#print(test.replace("fox", ""))

#print(censor(email_one, "learning algorithms"))

def censor2(content, censored_words):
  for word in range(0,len(censored_words)):
    if word==0:
      censored=content.replace(censored_words[word], "X"*len(censored_words[word]))
      censored=censored.replace(censored_words[word].title(), "X"*len(censored_words[word]))
      censored=censored.replace(censored_words[word].upper(), "X"*len(censored_words[word]))
    else:
      censored=censored.replace(censored_words[word],"X"*len(censored_words[word]))
      censored=censored.replace(censored_words[word].title(), "X"*len(censored_words[word]))
      censored=censored.replace(censored_words[word].upper(), "X"*len(censored_words[word]))
  return censored

#print(email_two)

proprietary_terms=["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "herself", "her"]

testlist=["quick", "fox"]
#print(censor2(email_two,proprietary_terms))

#print(email_three)
negative_words = ["concerned", "behind", "dangerous", "danger", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressing", "distressed", "concerning", "horrible", "horribly", "questionable", ]

def censor_negs(content, neglist):
  #remove proprietary info from before. Including titles.
  censor=censor2(content,proprietary_terms)
  appearances=[]
  for neg in range(0,len(neglist)):
    #find first appearance
    ind1=content.find(neglist[neg])
    ind2=content.find(neglist[neg].title())
    indu=content.find(neglist[neg].upper())
    #add to list, and look for second occurence
    if ind1>-1:
      ind3=content.find(neglist[neg],(ind1+1))
      if ind1 not in appearances:
        appearances.append(ind1)
      if ind3>0 and ind3 not in appearances:
        #if second occurance appears, add to list
        appearances.append(ind3)
    if ind2>-1:
      #if capital first letter appears add to list and look for second occurance
      
      ind4=content.find(neglist[neg].title(),(ind2+1))
      if ind2 not in appearances:
        appearances.append(ind2)
      if ind4>0 and ind4 not in appearances:
        #if second occurance occurs, add to list
        appearances.append(ind4)
    if indu>-1:
      #look for all caps
      indu2=content.find(neglist[neg].upper(),(indu+1))
      if indu not in appearances:
        appearances.append(indu)
      if indu2>0 and indu2 not in apperances:
        appearances.append(indu2)
    appearances.sort()
  censored_start=censor[0:appearances[2]]
  censored_end=censor[appearances[2]:]
  for neg in range(0,len(neglist)):
    censored_end=censored_end.replace(neglist[neg], "X"*len(neglist[neg]))
    censored_end=censored_end.replace(neglist[neg].title(), "X"*len(neglist[neg]))
  censored_joined="".join([censored_start,censored_end])
  return censored_joined

email_3_revised=censor_negs(email_three,negative_words)

#print(email_3_revised)
print(email_four)
def total_censor(content):
  censor=censor_negs(content,negative_words)
  censor_words=censor.split(" ")
  number_of_x=[]
  for secret in range(0,len(proprietary_terms)):
    #find length of each string in proprietary terms
    length=len(proprietary_terms[secret])
    if length not in number_of_x:
      number_of_x.append(length)
  for neg in range(0,len(negative_words)):
    #find length of each string in negative words
    length=len(negative_words[neg])
    if length not in number_of_x:
      number_of_x.append(length)
  #find words that are a bunch of X for all the words, for all the lengths listed 

  #create a list of list values that are all x
  all_xs=[]
  #create a list of all new index to censor
  new_censor_inds=[]
  for length in range(0,len(number_of_x)):
    for word in range(0,len(censor_words)):
      if censor_words[word]==number_of_x[length]*"X":
        all_xs.append(word)
  all_xs.sort()
  for x in range(0,len(all_xs)):
    if all_xs[x]-1 not in all_xs and all_xs[x]+1 not in all_xs:
      new_censor_inds.append(all_xs[x]-1)
      new_censor_inds.append(all_xs[x]+1)
    elif all_xs[x]-1 not in all_xs and all_xs[x]+1 in all_xs:
      new_censor_inds.append(all_xs[x]-1)
    elif all_xs[x]-1 in all_xs and all-xs[x]+1 not in all_xs:
      new_censor_inds.append(all_xs[x]+1)
  for spot in range(0, len(new_censor_inds)):
    id=new_censor_inds[spot]
    new_length=len(censor_words[id])
    censor_words[id]=new_length*"X"
  new_email=" ".join(censor_words)

  
  return new_email


print(total_censor(email_four))
    





