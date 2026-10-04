from CTFd import create_app
from CTFd.models import Challenges, Flags, db

app = create_app()

challenges_data = [
    {
        "name": "Look Closer",
        "category": "Web",
        "value": 50,
        "connection_info": "http://localhost:8001",
        "description": "Welcome to the University Cybersecurity Club portal!<br><br>The developer was working on this site and left some notes behind in the source code. Can you find what was left behind?<br><br><b>Challenge URL:</b> <a href='http://localhost:8001' target='_blank'>http://localhost:8001</a>",
        "flag": "FLAG{VIEW_SOURCE_IS_POWER}"
    },
    {
        "name": "Robots Don't Lie",
        "category": "Web",
        "value": 50,
        "connection_info": "http://localhost:8002",
        "description": "We are building a secure member directory for the club. We don't want search engines crawling our administrative areas.<br><br>How do websites tell web crawlers where not to go?<br><br><b>Challenge URL:</b> <a href='http://localhost:8002' target='_blank'>http://localhost:8002</a>",
        "flag": "FLAG{ROBOTS_DONT_PROTECT_SECRETS}"
    },
    {
        "name": "Secret Door",
        "category": "Web",
        "value": 75,
        "connection_info": "http://localhost:8003",
        "description": "The club navigation menu had a special admin portal link removed from the visible UI. Can you find where it leads?<br><br><b>Challenge URL:</b> <a href='http://localhost:8003' target='_blank'>http://localhost:8003</a>",
        "flag": "FLAG{HIDDEN_IN_PLAIN_SIGHT}"
    },
    {
        "name": "Cookie Monster",
        "category": "Web",
        "value": 75,
        "connection_info": "http://localhost:8004",
        "description": "The welcome portal checks a cookie named `role=guest` to determine if you can access the VIP lounge.<br><br><b>Challenge URL:</b> <a href='http://localhost:8004' target='_blank'>http://localhost:8004</a>",
        "flag": "FLAG{COOKIES_ARE_NOT_AUTHORIZATION}"
    },
    {
        "name": "The Client Knows Everything",
        "category": "Web",
        "value": 75,
        "connection_info": "http://localhost:8005",
        "description": "This portal has a password-protected verification check implemented entirely in client-side JavaScript.<br><br><b>Challenge URL:</b> <a href='http://localhost:8005' target='_blank'>http://localhost:8005</a>",
        "flag": "FLAG{CLIENT_SIDE_VALIDATION_IS_DEAD}"
    },
    {
        "name": "Who Am I?",
        "category": "Web",
        "value": 100,
        "connection_info": "http://localhost:8006",
        "description": "The club profile viewer uses a simple URL parameter (`/profile?id=1`) to show user details. Can you view someone else's profile?<br><br><b>Challenge URL:</b> <a href='http://localhost:8006' target='_blank'>http://localhost:8006</a>",
        "flag": "FLAG{IDOR_EXPOSES_SECRETS}"
    },
    {
        "name": "Say Something",
        "category": "Web",
        "value": 100,
        "connection_info": "http://localhost:8007",
        "description": "A welcome guestbook allows new members to leave public messages, but input sanitization is missing.<br><br><b>Challenge URL:</b> <a href='http://localhost:8007' target='_blank'>http://localhost:8007</a>",
        "flag": "FLAG{XSS_INJECTION_SUCCESS}"
    },
    {
        "name": "Broken Login",
        "category": "Web",
        "value": 150,
        "connection_info": "http://localhost:8008",
        "description": "The legacy member login portal constructs SQL queries directly from user input. Bypass authentication to get the flag!<br><br><b>Challenge URL:</b> <a href='http://localhost:8008' target='_blank'>http://localhost:8008</a>",
        "flag": "FLAG{SQL_INJECTION_BYPASS}"
    },
    {
        "name": "Hack the Club",
        "category": "Web",
        "value": 250,
        "connection_info": "http://localhost:8009",
        "description": "The ultimate welcome challenge! Chain your skills (recon, cookies, base64) to hack the club president's dashboard.<br><br><b>Challenge URL:</b> <a href='http://localhost:8009' target='_blank'>http://localhost:8009</a>",
        "flag": "FLAG{WELCOME_TO_CYBERSECURITY_2026}"
    }
]

with app.app_context():
    existing = Challenges.query.all()
    print(f"Current challenges in DB: {len(existing)}")
    for data in challenges_data:
        # Check if challenge with this name already exists
        exists = Challenges.query.filter_by(name=data["name"]).first()
        if not exists:
            print(f"Adding challenge: {data['name']}")
            chal = Challenges(
                name=data["name"],
                description=data["description"],
                connection_info=data["connection_info"],
                value=data["value"],
                category=data["category"],
                state="visible",
                type="standard"
            )
            db.session.add(chal)
            db.session.commit()
            
            flag = Flags(
                challenge_id=chal.id,
                content=data["flag"],
                type="static"
            )
            db.session.add(flag)
            db.session.commit()
        else:
            print(f"Challenge already exists: {data['name']}")
    print("Challenge seeding check complete!")
