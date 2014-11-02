facebookChatCounter
===================
INTRODUCTION : 

Counts the words typed by you against a specified user (friend of yours) and the percentage of your involvement in the chat.


TO DO :

 * Install python in your system :P
 * take access token from https://developers.facebook.com/tools/explorer
    grant privileges according to whatever you want to change yourself.
    make sure you give access to read_mailbox in extended permissions.
 * specify this token in the facebookChatHelper.py
 * specify the person you are interested to count against.
 
 ISSUES : 
 Graph API seems to not give all the data of conversations, and within a conversation too right now. 
 But you can get at least some idea with the small data it is giving right now.
 
 RANT :
 Graph API sucks. :D 
 FQL is deprecated, which in-turn was much better at getting things done.
