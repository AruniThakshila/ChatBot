import re
import long_responses as long

def message_Probability(user_message,recognised_words,single_response=False,required_words=[]):
    message_certainty=0
    has_required_word=True
    
    #Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty+=1

    #Calculate the percent of recognised words in a user message
    percentage=float(message_certainty)/float(len(recognised_words))     

    for word in required_words:
        if word not in user_message:
            has_required_word=False
            break

    if has_required_word or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list={}

    def response(bot_response,list_of_words,single_response=False,required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response]=message_Probability(message,list_of_words,single_response,required_words)

    #Response ....................................
    response('Hello!',['hello','hi','sup','hey','heyo'],single_response=True)
    response('I\'m doing fine, and you?',['how','are','you','doing'],required_words=['how'])
    response('Thank you!',['i','love','code','palace'],required_words=['love'])
    response('Nice name',['my','name','is',' '],required_words=['name'])
    response('My name is Elza',['what','is','name',' '],required_words=['name','your'])
    response('Certainly! What genre are you in the mood for? I can suggest some great films based on your preferences.',['tell','good','movie',' '],required_words=['movie','good'])
    response(' Im sorry, I dont have real-time data. You can check a weather website or app for the latest updates.',['what','is','the','weather'],required_words=['weather'])
    response('Why dont scientists trust atoms? Because they make up everything!',['tell','me','a','joke'],required_words=['joke'])
    response('I dont have personal preferences, but Im here to help with any questions you have.',['what','is','your','favourite'],required_words=['your','favourite'])
    response(' Im just a computer program, but Im here and ready to assist you!',['how','are','you','doing'],required_words=['how','doing'])
    response('Im just a chatbot so I cant sing',['sing','a','song'],required_words=['song'])
    response('just like you',['you','are','a','idiot'],required_words=['idiot'])
    response('I do not learn or update my knowledge in real-time. My responses are based on pre-existing data, and I do not have the ability to acquire new information independently.',['new','information','you','know'],required_words=['new','information'])
    response(' The future of AI holds potential advancements in various fields, from healthcare to technology. However, ethical considerations, privacy concerns, and responsible development will be crucial in shaping its impact',['what is','future','artifical intelligence'],required_words=['future','artificial inteligence'])
    response('While I strive for accuracy, I may not always be correct. It is advisable to cross-check information, especially for critical decisions, and use me as a supplementary source of information.',['can','','information','you','provide'],required_words=['trust','information','you','provide'])
    response(' I simulate human-like text generation, but I dont have consciousness, emotions, or self-awareness. I am a tool created by humans to assist with various tasks.',['are','you','like','human'],required_words=['you','like','human'])
    response('I can offer tips on job searching, resume building, and interview preparation. What type of job are you looking for?',['help','me','a','job'],required_words=['find','job'])
    response('I dont have access to your location, but I can recommend popular restaurants in your city. Where are you located?',['fine','restaurants','near','me'],required_words=['near','me'])
    response('Im just a machine, but thanks for asking! How can I assist you today?',['How','are','you'],required_words=['how','are','you'])
    response('It is not in my database',['remember','my','preferences'],required_words=['preferences'])
    response('"I can provide information, answer questions, and assist with various tasks. Try asking me about news, weather, or anything else you are curious about',['what','can','you','do'],required_words=['what','can','do'])
    response('Drink water, take a break, or rest in a quiet, dark room. If the headache persists, consider over-the-counter pain relievers.',['I','have','a','headache.'],required_words=['headache'])
    response(long.R_EATING,['what','you','eat'],required_words=['you','eat'])
    

    best_match=max(highest_prob_list,key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match]< 1  else best_match                  

def get_response(user_input):
    split_message=re.split(r'\s+|[,;?!.-]\s*',user_input.lower())
    response=check_all_messages(split_message)
    return response
while True:
    print('Elza: ' + get_response(input('You: ')))