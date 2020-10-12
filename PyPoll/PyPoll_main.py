#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd

# read a file
data_file = pd.read_csv("Resources/PyPoll.csv")

print(data_file)

#total votes
total_votes = len(data_file)

#total number of votes canidate got
candidate_votes = data_file["Candidate"].value_counts()

#percentage of votes
percentage_votes = (candidate_votes/total_votes)*100

#finding winner

# announce the winner
winner = candidate_votes.idxmax()


#RESULTS
print("ELECTION RESULTS:")
print("-----------------------------")
print("Total Votes:", str(total_votes))
print("-------------------------")
print("Votes each Canidate Received:")
print(candidate_votes)
print("-------------------------")
print("Percentage of Votes Received:")
print(percentage_votes)
print("-------------------------")
print("Winner of the Election:")
print(winner)




# In[44]:


# convert the output into a text file
file = open('pypoll.txt','w')
file.write("Election results")
file.write("\n....................................................................................")
file.write("\nTotal votes: "(total_votes)
file.write("\n....................................................................................")
file.write("\nVotes Each Candidate Received: " (candidate_votes)
file.write("\n....................................................................................")
file.write("\nPercentage of Votes Received: " (percentage_votes))
file.write("\n....................................................................................")
file.write("\nwinner: " (winner))
file.close()


# In[ ]:




