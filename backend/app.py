import json
from flask import Flask, request, render_template, redirect 
from flask import jsonify

from flask_cors import CORS
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)

career_data = {
    'AI ML Specialist': {
        'description': "An AI (Artificial Intelligence) and ML (Machine Learning) Specialist is a professional who specializes in the fields of artificial intelligence and machine learning. These specialists are experts in developing, implementing, and managing AI and ML solutions to solve complex problems and enhance various aspects of business and technology.",
        'data': {
            'Salary Range': '$80,000 - $150,000',
            'Required Skills': ['Machine Learning', 'Python', 'Deep Learning'],
            'Job Growth': 'High demand'
        }
    },
    'API Integration Specialist': {
        'description': "An API Integration Specialist is a tech-savvy professional who specializes in seamlessly connecting different software systems and services by leveraging Application Programming Interfaces (APIs). Their expertise lies in ensuring data flows smoothly between diverse applications, allowing for efficient and real-time communication. These specialists play a crucial role in streamlining processes, enhancing data exchange, and enabling businesses to operate more efficiently in the digital landscape.",
        'data': {
            'Salary Range': '$70,000 - $120,000',
            'Required Skills': ['APIs', 'Integration', 'Programming'],
            'Job Growth': 'Steady demand'
        }
    },
    'Application Support Engineer': {
        'description': "An Application Support Engineer is a vital technical professional responsible for maintaining and ensuring the smooth operation of software applications within an organization. Their primary role is to provide technical assistance, troubleshoot issues, and offer solutions to ensure that software applications run efficiently and meet users' needs. They serve as a bridge between end-users and developers, ensuring that applications are accessible, reliable, and responsive to user requirements.",
        'data': {
            'Salary Range': '$60,000 - $100,000',
            'Required Skills': ['Technical Support', 'Troubleshooting', 'Software Maintenance'],
            'Job Growth': 'Steady demand'
        }
    },
    'Business Analyst': {
        'description': "A Business Analyst is a professional who acts as a translator between business stakeholders and IT teams. They assess business processes, gather and analyze data, and provide actionable insights and recommendations. Their goal is to help organizations make informed decisions, improve processes, and achieve their strategic objectives by leveraging data and technology.",
        'data': {
            'Salary Range': '$70,000 - $120,000',
            'Required Skills': ['Data Analysis', 'Requirements Gathering', 'Business Acumen'],
            'Job Growth': 'High demand'
        }
    },
    'Customer Service Executive': {
        'description': "A Customer Service Executive is a frontline professional responsible for managing and addressing customer inquiries, concerns, and requests. They play a crucial role in ensuring a positive customer experience by providing assistance, resolving issues, and maintaining effective communication. Customer Service Executives typically work in various industries and channels, including call centers, online chat support, email support, and in-person interactions.",
        'data': {
            'Salary Range': '$30,000 - $50,000',
            'Required Skills': ['Customer Service', 'Communication', 'Problem-Solving'],
            'Job Growth': 'Steady demand'
        }
    },
    'Cyber Security Specialist': {
        'description': "A Cyber Security Specialist is a cybersecurity expert responsible for fortifying an organization's digital defenses. They assess and mitigate security risks, implement security measures, monitor networks for threats, investigate incidents, and ensure compliance with security protocols and regulations. These specialists are essential in the ongoing battle to protect sensitive data and maintain the integrity and confidentiality of digital systems and information.",
        'data': {
            'Salary Range': '$80,000 - $140,000',
            'Required Skills': ['Cybersecurity', 'Incident Response', 'Security Auditing'],
            'Job Growth': 'High demand'
        }
    },
    'Data Scientist': {
        'description': "A Data Scientist is a data detective and analytical expert who transforms raw data into actionable insights. They utilize statistical analysis, machine learning, and data visualization techniques to uncover patterns, trends, and knowledge hidden within large and complex datasets. Data Scientists assist businesses in making informed decisions, optimizing processes, and achieving strategic goals through data-driven approaches.",
        'data': {
            'Salary Range': '$90,000 - $160,000',
            'Required Skills': ['Data Analysis', 'Machine Learning', 'Data Visualization'],
            'Job Growth': 'High demand'
        }
    },
    'Database Administrator': {
        'description': "A Database Administrator is a technical expert who oversees databases, ensuring their performance, integrity, and security. They design, implement, and maintain database systems, perform backups, optimize queries, and manage access controls. Database Administrators play a vital role in enabling organizations to store and retrieve data effectively, supporting various applications and business processes.",
        'data': {
            'Salary Range': '$70,000 - $130,000',
            'Required Skills': ['Database Management', 'SQL', 'Database Security'],
            'Job Growth': 'Steady demand'
        }
    },
    'Graphics Designer': {
        'description': "A Graphics Designer is a visual storyteller and problem solver. They use their creativity and design software to produce eye-catching and impactful visuals, including graphics, illustrations, layouts, and multimedia content. Graphics Designers work in various industries, such as marketing, advertising, web development, and publishing, to help convey ideas and messages visually, enhancing the overall user experience and communication.",
        'data': {
            'Salary Range': '$40,000 - $80,000',
            'Required Skills': ['Graphic Design', 'Adobe Creative Suite', 'Creativity'],
            'Job Growth': 'Steady demand'
        }
    },
    'Hardware Engineer': {
        'description': "A Hardware Engineer is an architect of the digital world, responsible for designing and building the physical infrastructure of electronic devices and computer systems. They work on components such as microprocessors, circuit boards, memory chips, and peripherals, ensuring that these components function reliably and efficiently. Hardware Engineers play a vital role in advancing technology by creating the hardware that powers our digital lives.",
        'data': {
            'Salary Range': '$70,000 - $120,000',
            'Required Skills': ['Hardware Design', 'Circuitry', 'Electronics'],
            'Job Growth': 'Steady demand'
        }
    },
    'Helpdesk Engineer': {
        'description': "A Helpdesk Engineer is the first line of assistance for individuals or organizations encountering technical problems. They respond to inquiries, troubleshoot issues, and offer solutions to resolve technical challenges. Helpdesk Engineers are skilled in diagnosing and resolving a wide range of IT-related problems, providing essential support to ensure smooth and efficient operations.",
        'data': {
            'Salary Range': '$40,000 - $70,000',
            'Required Skills': ['Technical Support', 'Problem-Solving', 'Communication'],
            'Job Growth': 'Steady demand'
        }
    },
    'Information Security Specialist': {
                'description': "An Information Security Specialist is a guardian of digital assets, dedicated to protecting an organization's sensitive information from cyberattacks and data breaches. They assess security risks, develop and implement security measures, monitor networks for threats, and respond to security incidents. Information Security Specialists play a critical role in maintaining the confidentiality, integrity, and availability of digital resources, ensuring the organization's resilience against evolving cybersecurity threats.",
        'data': {
            'Salary Range': '$80,000 - $150,000',
            'Required Skills': ['Cybersecurity', 'Security Assessment', 'Incident Response'],
            'Job Growth': 'High demand'
        }
    },
    'Networking Engineer': {
        'description': "A Networking Engineer is like an architect and builder of the digital highways that connect our devices and systems. They design, configure, and maintain computer networks, including local area networks (LANs) and wide area networks (WANs), to facilitate seamless communication and data transfer. Networking Engineers ensure that organizations have reliable, high-performance, and secure network infrastructure, supporting essential operations and connectivity in today's digital world.",
        'data': {
            'Salary Range': '$70,000 - $130,000',
            'Required Skills': ['Network Design', 'Routing', 'Security'],
            'Job Growth': 'Steady demand'
        }
    },
    'Project Manager': {
        'description': "A Project Manager is a strategic leader who orchestrates the successful execution of projects. They define project goals, create plans, allocate resources, manage teams, monitor progress, and mitigate risks to ensure that projects are delivered effectively and efficiently. Project Managers are the driving force behind the achievement of project objectives, ensuring that organizations can adapt, innovate, and thrive in a dynamic business environment.",
        'data': {
            'Salary Range': '$80,000 - $150,000',
            'Required Skills': ['Project Management', 'Team Leadership', 'Risk Management'],
            'Job Growth': 'Steady demand'
        }
    },
    'Software Developer': {
        'description': "A Software Developer is a digital architect and builder who transforms ideas into functional software. They write code, design algorithms, and develop applications that drive computers and devices, enabling them to perform tasks and deliver services. Software Developers work across industries, from web and mobile app development to enterprise software, contributing to technological innovation and improving user experiences.",
        'data': {
            'Salary Range': '$70,000 - $130,000',
            'Required Skills': ['Programming', 'Software Development', 'Problem-Solving'],
            'Job Growth': 'High demand'
        }
    },
    'Software Tester': {
        'description': "A Software Tester is a meticulous detective of the digital world, responsible for evaluating software to find and report any imperfections or issues. They design test cases, execute them, and analyze the results to verify that software functions correctly and meets specified requirements. Software Testers help deliver reliable, bug-free applications, enhancing user satisfaction and trust in software products.",
        'data': {
            'Salary Range': '$50,000 - $100,000',
            'Required Skills': ['Software Testing', 'Test Automation', 'Bug Tracking'],
            'Job Growth': 'Steady demand'
        }
    },
    'Technical Writer': {
        'description': "A Technical Writer is a linguistic architect of knowledge, dedicated to translating complex technical information into accessible and comprehensible documents. They craft user manuals, guides, tutorials, and other forms of documentation that enable individuals to understand and use technical products, processes, or systems effectively. Technical Writers bridge the gap between technical experts and end-users, ensuring clarity and accuracy in communication.",
        'data': {
            'Salary Range': '$50,000 - $90,000',
            'Required Skills': ['Technical Writing', 'Documentation', 'Communication'],
            'Job Growth': 'Steady demand'
        }
    },
}
@app.route('/')
def career():
    return "Hello World"

@app.route('/predict',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
    data = request.get_json()
    name = data.get('values', '')
    lst=[]
    lst=name.split(',')
    lst=[int(i) for i in lst]
    arr=np.array(lst)
    arr=arr.reshape(1,-1)
    print(arr)
    loaded_model = pickle.load(open("backend\careerlast.pkl", 'rb'))
    predictions = loaded_model.predict(arr)
    print(predictions)
    pred = loaded_model.predict_proba(arr)
    print(pred)
    #acc=accuracy_score(pred,)
    pred = pred > 0.05
    #print(predictions)
    i = 0
    j = 0
    index = 0
    res = {}
    final_res = {}
    while j < 17:
        if pred[i, j]:
            res[index] = j
            index += 1
        j += 1
    # print(j)
    #print(res)
    index = 0
    for key, values in res.items():
        if values != predictions[0]:
            final_res[index] = values
            print('final_res[index]:',final_res[index])
            index += 1
    #print(final_res)
    jobs_dict = {0:'AI ML Specialist',
                1:'API Integration Specialist',
                2:'Application Support Engineer',
                3:'Business Analyst',
                4:'Customer Service Executive',
                5:'Cyber Security Specialist',
                6:'Data Scientist',
                7:'Database Administrator',
                8:'Graphics Designer',
                9:'Hardware Engineer',
                10:'Helpdesk Engineer',
                11:'Information Security Specialist',
                12:'Networking Engineer',
                13:'Project Manager',
                14:'Software Developer',
                15:'Software Tester',
                16:'Technical Writer'}
                
    #print(jobs_dict[predictions[0]])
    job = {}
    #job[0] = jobs_dict[predictions[0]]
    index = 1
    data1=predictions[0]
    print(data1)

    return {"result":data1}

if __name__ == '__main__':
    app.run(debug=True) 