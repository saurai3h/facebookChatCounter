__author__ = 'saurabh'

import requests
import facebook

def main():
    token = 'YOUR_TOKEN_HERE'

    graph = facebook.GraphAPI(token)
    conversations = graph.get_connections("me","conversations")

    # Doesn't take into account the group chats. ( Only one-on-one )
    user_interested = 'YOUR_FRIEND_NAME_HERE'
    myself = 'Saurabh Paliwal'

    while(True):
        try:
            for conversation in conversations['data']:

                # Remove group conversations.
                if(len(conversation['participants']['data']) != 2):
                    continue
                my_conversation = conversation
                valid_conversation = False
                for participants in my_conversation['participants']['data']:
                    if(participants['name'] == user_interested):
                        valid_conversation = True
                        break
                if(valid_conversation == True):

                    words_by_me = 0
                    words_by_user = 0

                    while(True):
                        try:
                            for conversation_data in my_conversation['messages']['data']:
                                if(conversation_data['from']['name'] == myself):
                                    words_by_me += len(conversation_data['message'].split(" "))
                                elif(conversation_data['from']['name'] == user_interested):
                                    words_by_user += len(conversation_data['message'].split(" "))

                            conversation_id = my_conversation['id']
                            next_page = my_conversation['messages']['paging']['next']
                            parameters = next_page.split("?")[1].split("&")
                            limit = parameters[1].split("=")[1]
                            until = parameters[2].split("=")[1]
                            __paging_token = parameters[3].split("=")[1]
                            my_conversation = graph.get_connections("me","conversations",conversation_id=conversation_id,limit=limit,until=until,__paging_token=__paging_token)
                        except(KeyError):
                            break
                    print myself.split(" ")[0] + " typed " + str(words_by_me) + " words."
                    print user_interested.split(" ")[0] + " typed " + str(words_by_user) + " words."
                    print myself.split(" ")[0] + " types " + str((words_by_me*100.0)/(words_by_me+words_by_user)) + " % of the total words in the chat."

            next_url = conversations['paging']['next']
            parameters = next_url.split("?")[1].split("&")
            limit = parameters[1].split("=")[1]
            until = parameters[2].split("=")[1]
            __paging_token = parameters[3].split("=")[1]
            conversations = graph.get_connections("me","conversations",limit=limit,until=until,__paging_token=__paging_token)

        except(KeyError):
            break
    return 0

if __name__ == "__main__":
    main()