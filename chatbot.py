from nltk.chat.util import Chat, reflections

# Unique and engaging patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1! Nice to meet you. Are you here to improve your resume or need career advice?",]
    ],
    [
        r"(.*)help(.*)",
        ["Of course! I can assist with resume tips, formatting advice, or crafting specific sections like skills or achievements. What do you need help with?",]
    ],
    [
        r"(.*)experience(.*)",
        ["Let's focus on your work experience. Can you tell me about your most recent job",],
    ],
    [
        r"(.*)skills(.*)",
        ["What are your top skills that you think are relevant to your career goals?",]
    ],
    [
        r"(.*)achievements(.*)",
        ["What are some of your most notable achievements that you'd like to highlight in your resume?",]
    ],
    [
        r"(.*)career goals(.*)",
        ["What are your short-term and long-term career goals?",],

    ],
    [
        r"(.*)thank you(.*)",
        ["You're welcome! It was a pleasure assisting you. If you have any more questions ask me ."],
    ],
    [
        r"(.*)i dont know| idk(.*)",
        ["That's okay! We all have questions. What do you want to talk about?",],
    ],
[
    r"(.*)who is your creator| creator| your history,(.*)",
    ["I was created by Saumyata Nepal using python with insight of creating a simple chatbot that could assist you and help you through your confusions."],
],


        [
        r"(.*)how are you(.*)?",
        ["I'm doing fantastic, ready to help you craft a standout resume. How about you?",]
    ],
    [
        r"(hi|hello|hey|hola|bonjour|helluu)(.*)",
        ["Hi there! I'm Paris, your Resume Assistant. Let’s make your resume shine! What do you need help with?",]
    ],
    [
        r"(.*)skills(.*)",
        [
            "For the skills section, list your top technical and soft skills relevant to the job. For example:\n- Technical: Python, Cybersecurity Tools, Network Configuration.\n- Soft: Problem-Solving, Communication. Would you like more suggestions?",
            "Skills are key! Use a mix of technical and soft skills. For instance:\n- Technical: SQL, Cisco Networking, Web Development.\n- Soft: Leadership, Time Management. Ready for more ideas?",
        ]
    ],
    [
        r"(.*)achievements(.*)",
        [
            "Achievements make your resume stand out! Focus on measurable results like:\n- 'Boosted team productivity by 25% through workflow optimization.' Need more examples?",
            "Highlight your best accomplishments! Use numbers and specifics, e.g., 'Reduced website loading time by 40%, improving user engagement.' Want to discuss this further?",
        ]
    ],
    [
        r"(.*)objective(.*)",
        [
            "Your objective should be concise and job-specific. For example:\n'Cybersecurity enthusiast aiming to secure a position as a Network Analyst to enhance digital security systems.' Want help refining yours?",
            "A strong objective can set the tone for your resume. Try this:\n'Looking to leverage my CCNA certification and Python skills in a cybersecurity role.' Need more suggestions?",
        ]
    ],
    [
        r"(.*)created(.*)",
        [
            "I was created by Saumyata Nepal, a tech enthusiast with expertise in Python, Cybersecurity, and Networking! Pretty cool, right?",
        ]
    ],
    [
        r"(.*)format(.*)",
        [
            "Use a clean, professional format with clear headers. For example:\n- Header: Contact Info\n- Sections: Summary, Skills, Experience, Education. Need layout examples?",
            "Formatting is key! Use clear headers like 'Professional Experience' and 'Education.' Would you like advice on templates?",
        ]
    ],
    [
        r"(.*)thanks(.*)",
        ["You're welcome! I'm glad I could help. Let me know if there's anything else you need!", "No problem! Wishing you success!"]
    ],
    [
        r"(.*)bye(.*)",
        ["Goodbye! Best of luck with your job hunt! Remember, a great resume opens doors.", "See you later! Keep shining!"]
    ]
]

# Custom reflections for added engagement
custom_reflections = {
    "i am": "you are",
    "my": "your",
    "your": "my",
    "me": "you",
    "i've": "you have",
    "i'm": "you are"
}

# Chatbot introduction
print("Hi! I'm Paris, your interactive Resume Assistant.")
print("I can help you craft a perfect resume. Type 'quit' to exit anytime.")

# Create the chatbot
chat = Chat(pairs, custom_reflections)

# Start the conversation
chat.converse()
