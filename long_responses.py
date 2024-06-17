import random

R_EATING="I don't like eating anything because I'm bot obviously"

def unknown():
    response=['Could you please re-pharse that?',
              "...",
              "Sounds about right",
              "Interesting. Tell me more about that.",
              "Hmm, I'm not familiar with that. Could you provide more details?",
              "I see. Can you break it down for me a bit more?",
              "Fascinating! How did you come up with that idea?",
              "That's an interesting take. Can you share more of your thoughts on the matter?",
              "What does that mean?"][random.randrange( 8)]
    return response