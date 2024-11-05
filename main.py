import re
import long_responses as long

print("Bot: hola, soy fAI en que te puedo ayudar :)")

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    #-------------------------------------------------------------------------------------------------------
    response('hey, whats up', ['hey','hola'], single_response=True)
    response('bye, que te vaya bien', ['bye', 'adios'], single_response=True)
    response('im good thanks, and you?', ['como', 'estas'], required_words=['como', 'estas'])
    response('Siempre a la orden', ['thank', 'thanks', 'gracias'], single_response=True)
    response('Gracias!', ['i', 'love', 'code', 'palace'], required_words=['code', 'pialace'])
    response('soy lo mejor de este mundo', [ 'quien'], single_response=True)
    response('fue jeaniber por gay', [ 'quien', 'fue'], required_words=['fue','quien'])

    # Longer responses
    response(long.R_ADVICE, ['dame', 'consejo'], required_words=['consejo'])
    response(long.R_ONE, ['1'], single_response= True)
    response(long.R_TWO, ['2'], single_response= True)
    response(long.R_TREEH, ['3'], single_response= True)
    response(long.R_FOUR, ['4'], single_response= True)

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))