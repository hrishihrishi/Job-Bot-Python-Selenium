


###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "all resumes/default/resume.pdf"      # (In Development)

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience? 
years_of_experience = "2"          # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "No"               # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = "https://hrishihrishi.github.io/"                        # "www.example.bio" or "" and so on....

# Please provide the link to your LinkedIn profile.
linkedIn = "https://linkedin.com/in/hrishikesh-h-96a6a4366"       # "https://www.linkedin.com/in/example" or "" and so on...

# Do you ALREADY have permission to work in the country you are applying to? (Eg: citizen, permanent resident, or a valid work visa such as H-1B or OPT)
# This is NOT `require_visa`, which asks whether you need sponsorship. Someone on a valid work visa answers "Yes" to both.
legally_authorized = "Yes"         # "Yes" or "No"

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "Other"



## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = 600000          # 80000, 90000, 100000 or 120000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
'''

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = 600000            # 800000, 900000, 1000000 or 1200000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
'''

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg: 
# currency = "INR"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = 1                  # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
'''
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months), 
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
'''

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "SDE with Experience in MERN stack, Java, Springboot, SQL, Typescript, React.js, Node.js, Next.js, MongoDB"

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """
Software Engineer | Java | Go | Python | JavaScript | Spring Boot | Backend | AWS Cloud | DSA
Passionate about designing and building high-performance and reliable backend systems. Skilled in writing clean, efficient code and solving complex problems using DSA.

🔹 Core Skills & Tech:
Programming: Java, Go, Python, JavaScript
Frameworks: Spring Boot, FastAPI, React.js
Backend & Databases: REST APIs, PostgreSQL, MySQL, MongoDB

🔹 What I Do:
Build robust microservices with Spring Boot & Go
Develop RESTful & real-time APIs
Work with distributed systems and cloud-native applications
Solved 350+ DSA problems .
Currently diving deeper into system design, backend architecture, and cloud infrastructure to prepare for SDE roles in top tech companies.
Do connect if you’re hiring fullstack engineering or just frontend or backend developers.
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
Dear Hiring Team,
I’m Hrishikesh H, software developer with 1+yrs of experience in fullstack and AI system engineering. I currently reside in Bengaluru and actively looking for in-office or work from home opportunities.

In my recent work, I’ve focused heavily on engineering and managing efficient architectures, optimizing system performance, and writing clean, maintainable code. Over the course of my career, I have worked across different stages of product development—from initial feature design to deployment and continuous optimization. Whether the challenge involves streamlining backend logic, refining the user experience, or handling data pipelines, I enjoy taking end-to-end ownership of my work and collaborating with cross-functional teams to hit business goals.

I am highly comfortable adapting to new tools, tech stacks, and development environments depending on what the project demands. I’d love the opportunity to talk more about how my background aligns with what your team is currently building.
I’ve attached my resume, and you can also check out some of my work on my GitHub or LinkedIn profiles linked below.
Thanks for your time and consideration.
Best regards,
Hrishkesh H
Bengaluru
8217273480
hrishi.halesh.18@gmail.com
www.linkedin.com/in/hrishikesh-h-96a6a4366
https://github.com/hrishihrishi
"""

# Information about you that the AI can use when answering application questions.
# Put anything an answer might need here, for example: name, years of experience,
# key skills, location, work authorization, and so on. Use \n for line breaks.
user_information_all = """
Priority: Plain MERN stack jobs(no AI etc), Fullstack Javascript/Node, Fullstack Java+Javascript. 
You can apply to fresher roles too and any role under 2 years experience
IMPORTANT INFO: Please prioritze medium to big non-laying-off companies like banks, biotech etc whose main product is not website, but any mid-big sized company is good just apply it.
Name: Hrishikesh H.
Experience: 1 year working in startups and mid sized companies.
Skills: MERN, Next.js, React.js, AWS, Java, Typescript, Javascript, Tailwind css, Google analytics, Spring framework, Redis, Postgres, docker, mongodb, SQL.
Location: Bengaluru
Available for: Remote, hybrid and onsite in any city in India.
Expected CTC: 600000+
Current CTC: 600000
"""
'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Name of your most recent employer
recent_employer = "Flowcall" # "", "Lala Company", "Google", "Snowflake", "Databricks"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = "10"             # Any number between "1" to "10" including 1 and 10, put it in quotes ""
##



# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = False         # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = True    # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False, Note: True or False are case-sensitive







############################################################################################################
'''
THANK YOU for using my tool 😊! Wishing you the best in your job hunt 🙌🏻!

Sharing is caring! If you found this tool helpful, please share it with your peers 🥺. Your support keeps this project alive.

Support my work on <PATREON_LINK>. Together, we can help more job seekers.

As an independent developer, I pour my heart and soul into creating tools like this, driven by the genuine desire to make a positive impact.

Your support, whether through donations big or small or simply spreading the word, means the world to me and helps keep this project alive and thriving.

Gratefully yours 🙏🏻,
Hrishikesh H
'''

# --- Load user settings saved by the local control panel (user_config.json).
# --- No-op if that file is absent: values fall back to the defaults above.
from config import _overrides as _o
_o.apply(__name__, globals())
############################################################################################################