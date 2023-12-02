from flask import Flask, request, jsonify,render_template

app = Flask(__name__)

@app.route('/')  
def message():  
      return render_template('bot.html')

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    action = data["queryResult"]["action"]

    response = {}

    ##################### For Area of Interest #####################
    if action == "area_interest":
        response = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "text": [
                                        "➡️ Artificial Intelligence (AI)",
                                        "➡️ Machine Learning",
                                        "➡️ Software Development",
                                        "➡️ Data Science and Big Data",
                                        "➡️ Data Analysis",
                                        "➡️ Python Development",
                                        "➡️ Robotics",
                                    ],
                                    "type": "description",
                                    "title": "Area of Interest",
                                },
                                {
                                    "type": "chips",
                                    "options": [
                                        {"text": "Skills"},
                                        {"text": "Projects"},
                                    ],
                                },
                            ]
                        ]
                    }
                }
            ]
        }

    ##################### For Awards and Honors #####################
    elif action == "award_honor":
        response = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "title": "➡️🥈 2nd Place in Kalamahakumbh Competition",
                                    "type": "info",
                                },
                                {
                                    "type": "info",
                                    "title": "➡️🥈 Runners-up in Tug of War🪢"
                                },
                                {
                                    "title": "➡️🏐🥇 State Level Volleyball Player 🏐🥇",
                                    "type": "info",
                                },
                                {
                                    "title": "➡️🥇 2nd Round Winner in Capgemini Tech-Challenge #2021 🏆👏",
                                    "type": "info",
                                },
                                {
                                    "type": "chips",
                                    "options": [
                                        {
                                            "text": "In how many languages are you conversant?"
                                        },
                                        {
                                            "text": "What are the various hobbies you have?"
                                        },
                                    ],
                                },
                            ]
                        ]
                    }
                }
            ]
        }

    ##################### For Career Objective #####################
    elif action == "career_objective":
        response = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "title": "Career Objective",
                                    "text": [
                                        "👨‍💻 Experienced software developer with a strong background in full-stack web development 🌐, seeking a challenging role where I can leverage my expertise in designing and implementing innovative software solutions 💡. Dedicated to delivering high-quality code 🚀 and driving project success through collaboration 🤝 and problem-solving 🧩. Looking to contribute to a dynamic team 🚀 and advance my career in a forward-thinking tech company 🌟."
                                    ],
                                    "type": "description",
                                },
                                {
                                    "type": "chips",
                                    "options": [
                                        {"text": "Experience"},
                                        {"text": "Area of interest"},
                                    ],
                                },
                            ]
                        ]
                    }
                }
            ]
        }

    ##################### For Contact Details #####################
    elif action == "contact_details":
        response = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "title": "Contact Details:",
                                    "text": [
                                        "Name: Dharmik Nareshkumar Mistry",
                                        "Email: dharmik2518@gmail.com",
                                        "Phone: 7016252776",
                                        "Address: Bilikumbharwad, in front of Vankar Tekra, Bilimora-396321",
                                    ],
                                    "type": "description",
                                },
                                {
                                    "type": "chips",
                                    "options": [
                                        {
                                            "text": "Dharmik Mistry",
                                            "image": {
                                                "src": {
                                                    "rawUrl": "https://static.vecteezy.com/system/resources/previews/021/492/181/original/linkedin-logo-free-download-free-png.png"
                                                }
                                            },
                                            "link": "https://www.linkedin.com/in/dharmik-mistry-9a8309205/",
                                        }
                                    ],
                                },
                                {
                                    "type": "chips",
                                    "options": [
                                        {"text": "References"},
                                        {"text": "Thank You !"},
                                    ],
                                },
                            ]
                        ]
                    }
                }
            ]
        }

    ##################### For Default Welcome Intent #####################
    elif action == "input_welcome":
        response = {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            "Welcome ! 🤝 I'm the 🤖 ResumeBot 🤖, How can I help you today?"],
                    }
                },
                {
                    "text": {
                        "text": ["🤔 What do you want to know about me?"],
                    }
                },
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "type": "chips",
                                    "options": [
                                        {"text": "Introduction"},
                                        {"text": "Education"},
                                        {"text": "Career Objective"},
                                    ],
                                }
                            ]
                        ]
                    }
                },
            ]
        }

    ##################### For Educational-Qualifications #####################
    elif action == "education_qualification":
        response = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "text": [
                                        "🎓 I have completed my Bachelor's degree in Computer Science and Engineering from 'R.N.G. Patel INSTITUTE OF TECHNOLOGY' in Bardoli, with a cumulative grade point average (CGPA) of 8.16. 📚👨‍🎓"
                                    ],
                                    "title": "Bechlor's Degree",
                                    "type": "description",
                                },
                                {
                                    "type": "description",
                                    "title": "High School",
                                    "text": [
                                        "🎓 I completed my high school from 'M & R TATA HIGH SCHOOL' in Bilimora, where I completed my 12th-grade education in the science stream with an academic achievement of 75.2%. 📚🔬📊"
                                    ],
                                },
                                {
                                    "type": "chips",
                                    "options": [
                                        {"text": "Career Objective"},
                                        {"text": "Experience"},
                                    ],
                                },
                            ]
                        ]
                    }
                }
            ]
        }

    ##################### For Exit #####################
    elif action == "exit":
        response = {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            "You're awesome! 😎 If you ever need assistance again, I'll be here. Goodbye for now! 🚀"],
                    },
                }
            ]
        }

    ##################### For Experience #####################
    elif action == "experience":
        response = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "type": "description",
                                    "text": [
                                        "I have prior experience at a product-based company, 'Agami Tech Pvt Ltd,' where I played a vital role in the PHP team. In my position, I focused on 🐞 bug identification and resolution, including manual testing. My skill set encompasses 🌐 HTML, 🎨 CSS, 📜 JavaScript, 🅰️ AngularJS,🐘PHP Laravel, 🅱️ Bootstrap, 🐬 MySQL, and 🐙 Git. This experience provided me with valuable insights into 🐞 bug management and manual testing. I'm enthusiastic about applying these skills to tackle new challenges and opportunities in the future. 💼"
                                    ],
                                    "title": "Agami Tech Pvt Ltd",
                                },
                                {
                                    "title": "Tata Group",
                                    "type": "description",
                                    "text": [
                                        "🚀 I had the privilege of interning remotely with Tata Group in the Data Analysis domain. My primary responsibility was to 📊 extract pertinent information from data sets and transform it into meaningful insights. This involved creating clear and understandable visual charts using data visualization tools such as Microsoft Excel, PowerBI, and Tableau. 📈 I then presented these business insights, complete with the necessary analysis, using slides. 📊 This experience enhanced my skills in  📊Microsoft Excel ,📈 Data analysis, 📊Data visualization, 📊Tableau, 🔍Data Insights"
                                    ],
                                },
                                {
                                    "type": "chips",
                                    "options": [
                                        {"text": "Area of interest"},
                                        {"text": "Skills"},
                                    ],
                                },
                            ]
                        ]
                    }
                }
            ]
        }

    ##################### For Hobbies #####################
    elif action == "hobbies":
        response = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "richContent": [
                            [
                                {"title": "📚 Reading", "type": "info"},
                                {"title": "📷 Photography", "type": "info"},
                                {"title": "🚴‍♂️ Cycling", "type": "info"},
                                {"title": "✈️ Traveling", "type": "info"},
                                {"title": "🏋️‍♀️ Fitness and Exercise", "type": "info"},
                                {"title": "🎹 Playing Piano", "type": "info"},
                                {"title": "🎧 Listening to Music", "type": "info"},
                                {
                                    "type": "chips",
                                    "options": [
                                        {"text": "Strength & Weekness"},
                                        {"text": "Contact Informations"}
                                    ]
                                }
                            ]
                        ]
                    }
                }
            ]
        }

    ##################### For Introduction #####################
    elif action == "introduction":
        response = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "text": [
                                        "👋 Hello, I'm Dharmik Mistry, a 🧑‍💻 Software Developer with over 1 year of experience and aslo like to coding in Python. I'm excited about the opportunity to join Pragnakalp Techlabs and contribute to your development team's success. Outside of work, I'm passionate about 📷 photography and enjoy 🎹 playing the piano. These hobbies enhance my creativity and ⏰ time management skills, contributing to my personal and professional growth. 📚 I also have a keen interest in reading books."
                                    ],
                                    "type": "description",
                                    "title": "Sure, Here's my Intoduction : ",
                                },
                                {
                                    "options": [
                                        {"text": "Education"},
                                        {"text": "Career Objective"},
                                    ],
                                    "type": "chips",
                                },
                            ]
                        ]
                    }
                }
            ]
        }

    ##################### For Languages-known #####################
    elif action == "languages_known":
        response = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "richContent": [
                            [
                                {"title": "➡️English", "type": "info"},
                                {"type": "info", "title": "➡️Gujarati(ગુજરાતી)"},
                                {"type": "info", "title": "➡️Hindi(हिन्दी)"},
                                {
                                    "type": "chips",
                                    "options": [
                                        {
                                            "text": "what are the various hobbies you have?"
                                        },
                                        {
                                            "text": "Tell me about your strength and weakness"
                                        },
                                    ],
                                },
                            ]
                        ]
                    }
                }
            ]
        }

    ##################### For Projects #####################
    elif action == "projects":
        response = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "type": "chips",
                                    "options": [
                                        {
                                            "link": "https://lnkd.in/dT3PtdC3",
                                            "image": {
                                                "src": {
                                                    "rawUrl": "https://media.licdn.com/dms/image/C4D22AQH6m9VjcHW_Dg/feedshare-shrink_1280/0/1660929615477?e=1701907200&v=beta&t=ZP6FvsLZrQacbdcpEiUqYa98IsryM8veywALTx0VEz8"
                                                }
                                            },
                                            "text": "Student Marks Prediction",
                                        },
                                        {
                                            "link": "https://lnkd.in/esKspZWi",
                                            "image": {
                                                "src": {
                                                    "rawUrl": "https://media.licdn.com/dms/image/C4E22AQEOha66xncyIQ/feedshare-shrink_1280/0/1642082082456?e=1701907200&v=beta&t=BrXNvZiD64niG8F8mv0Y7sZuwGW9tF8RJzrstaugnxQ"
                                                }
                                            },
                                            "text": "IPL Data Analysis",
                                        },
                                        {"text": "Awards"},
                                        {"text": "How many languages do you speak ?"},
                                        {
                                            "text": "what are the various hobbies you have?"
                                        },
                                        {
                                            "text": "strength and weakness"
                                        },
                                    ],
                                }
                            ]
                        ]
                    }
                }
            ]
        }

    ##################### For References #####################
    elif action == "references":
        response = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "type": "image",
                                    "rawUrl": "https://media.licdn.com/dms/image/D4D03AQFVFM4ImcyO0A/profile-displayphoto-shrink_400_400/0/1674827151041?e=1704326400&v=beta&t=k8Lw_S4nCxkZoupAQBRGSaHfBpk6CSOaxioKr-wrkWI",
                                },
                                {
                                    "subtitle": "Entrepreneur. ML, NLP, LLMs, ChatGPT, Chatbots, Dialogflow, Python. Founder @ Pragnakalp Techlabs",
                                    "actionLink": "https://www.linkedin.com/in/mittalpatel/",
                                    "title": "Mittal Patel ",
                                    "type": "info",
                                },
                            ]
                        ]
                    }
                }
            ]
        }

    ##################### For Skills #####################
    elif action == "skills":
        response = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "type": "info",
                                    "image": {
                                        "src": {
                                            "rawUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png"
                                        }
                                    },
                                    "title": "Python",
                                },
                                {
                                    "title": "Machine Learning",
                                    "type": "info",
                                    "image": {
                                        "src": {
                                            "rawUrl": "https://nyesteventuretech.com/images/Machine-Learning.jpg"
                                        }
                                    },
                                },
                                {
                                    "image": {
                                        "src": {
                                            "rawUrl": "https://cdn.pixabay.com/photo/2017/08/05/11/16/logo-2582748_960_720.png"
                                        }
                                    },
                                    "type": "info",
                                    "title": "HTML",
                                },
                                {
                                    "image": {
                                        "src": {
                                            "rawUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/CSS3_logo_and_wordmark.svg/1452px-CSS3_logo_and_wordmark.svg.png"
                                        }
                                    },
                                    "title": "CSS",
                                    "type": "info",
                                },
                                {
                                    "title": "JavaScript",
                                    "type": "info",
                                    "image": {
                                        "src": {
                                            "rawUrl": "https://logos-world.net/wp-content/uploads/2023/02/JavaScript-Logo.png"
                                        }
                                    },
                                },
                                {
                                    "type": "info",
                                    "title": "jQuery",
                                    "image": {
                                        "src": {
                                            "rawUrl": "https://w7.pngwing.com/pngs/720/46/png-transparent-jquery-plain-wordmark-logo-icon-thumbnail.png"
                                        }
                                    },
                                },
                                {
                                    "title": "Bootstrap",
                                    "type": "info",
                                    "image": {
                                        "src": {
                                            "rawUrl": "https://img.freepik.com/premium-vector/bootstrap-icon-b-letter-logo_781017-7.jpg"
                                        }
                                    },
                                },
                                {
                                    "title": "PHP Laravel",
                                    "type": "info",
                                    "image": {
                                        "src": {
                                            "rawUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Laravel.svg/1200px-Laravel.svg.png"
                                        }
                                    },
                                },
                                {
                                    "image": {
                                        "src": {
                                            "rawUrl": "https://www.djangoproject.com/m/img/logos/django-logo-positive.png"
                                        }
                                    },
                                    "title": "Django",
                                    "type": "info",
                                },
                                {
                                    "title": "Flask",
                                    "type": "info",
                                    "image": {
                                        "src": {
                                            "rawUrl": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/flask-logo-icon.png"
                                        }
                                    },
                                },
                                {
                                    "title": "MySQL",
                                    "image": {
                                        "src": {
                                            "rawUrl": "https://1000logos.net/wp-content/uploads/2020/08/MySQL-Logo.png"
                                        }
                                    },
                                    "type": "info",
                                },
                                {
                                    "type": "chips",
                                    "options": [
                                        {"text": "Projects"},
                                        {"text": "Awards and Honors"},
                                    ],
                                },
                            ]
                        ]
                    }
                }
            ]
        }

    ##################### For Strength and Weakness #####################
    elif action == "strengths_weakness":
        response = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "type": "description",
                                    "text": [
                                        "💪 Leadership skills",
                                        "🗣️ Communication skills",
                                        "👥 Teamwork and collaboration",
                                        "⏰ Time management",
                                        "💻 Technical skills",
                                        "🎙️ Public speaking",
                                        "🚀 Self-motivation",
                                    ],
                                    "title": "Strengths:",
                                },
                                {
                                    "title": "Weaknesses:",
                                    "text": [
                                        "🤔 Overthinking",
                                        "😓 Difficulty with handling stress",
                                        "🙅 Inflexibility",
                                        "🚫 Difficulty saying 'NO'",
                                        "⌛ Impatience",
                                    ],
                                    "type": "description",
                                },
                                {
                                    "type": "chips",
                                    "options": [
                                        {"text": "Contact Information?"},
                                        {"text": "References"},
                                    ],
                                },
                            ]
                        ]
                    }
                }
            ]
        }
    else:
        response = {
                "fulfillmentText": "Sorry, could you say that again?"
            }
        

    return jsonify(response)





if __name__ == "__main__":
    app.run(debug=True)
