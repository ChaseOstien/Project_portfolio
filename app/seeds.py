from models import User, Comment, Project, Vote
from db import Session, Base, engine

# drop and rebuild tables when seeds.py is run
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# establish a temporary database connection to perform file operations
db = Session()

# insert users
db.add_all([ # preps changes to be made to the db
    User(username='chaseostien', email='chaseostien@gmail.com', password='password123'),
    User(username='alesmonde0', email='nwestnedge0@cbc.ca', password='password123'),
    User(username='jwilloughway1', email='rmebes1@sogou.com', password='password123'),
    User(username='iboddam2', email='cstoneman2@last.fm', password='password123'),
    User(username='dstanmer3', email='ihellier3@goo.ne.jp', password='password123'),
    User(username='djiri4', email='gmidgley4@weather.com', password='password123')
])

db.commit() # commits changes to db

db.add_all([
    Project(project_name = "Sabor Mexicano", project_description = "MERN Stack, GraphQL.", repo_link = "https://github.com/JakeHowdeshell/react-menu?tab=readme-ov-file", deployed = "https://sabor-mexicano-aded3d6892cd.herokuapp.com/", user_id = 1 ),
    Project(project_name = "Venue Viewer", project_description = "Node.js, MySQL, Handlebars.js, Tailwind CSS.", repo_link = "https://github.com/ChaseOstien/Venue-Viewer", deployed = "https://venue-viewer-team1-69164e361419.herokuapp.com/login", user_id = 1 ),
    Project(project_name = "Tech Blog", project_description = "MVC, Handlebars.js, Sequelize, Express-session.", repo_link = "https://github.com/ChaseOstien/Tech_Blog", deployed = "https://tech-blog-12-2c4e0baa09b6.herokuapp.com/", user_id = 1 ),
    Project(project_name = "E-Commerce-Backend", project_description = "Express.js, Sequelize, MongoDB, Mongoose.", repo_link = "https://github.com/ChaseOstien/E-Commerce-BackEnd", user_id = 1 ),
    Project(project_name = "Content Manager", project_description = "Node.js, Inquirer, MySQL.", repo_link = "https://github.com/ChaseOstien/Content_Manager", user_id = 1 ),
    Project(project_name = "Just Another Text Editor", project_description = "PWA, IndexDB, WebPack, Local Storage.", repo_link = "https://github.com/ChaseOstien/PWA-TextEditor", deployed = "https://j-a-t-e-p-w-a-25155f7ea5a4.herokuapp.com/", user_id = 1 ),
    Project(project_name = "Note Taker", project_description = "Node.js, Express.js, JavaScript.", repo_link = "https://github.com/ChaseOstien/Note_Taker", deployed = "https://note-taker-remindme-1dc60909ba4b.herokuapp.com/", user_id = 1 ),
    Project(project_name = "Cinephile", project_description = "Node.js, Express.js, JavaScript, Bulma.", repo_link = "https://github.com/ChaseOstien/Cinephile", user_id = 1 ),
    Project(project_name = "README Generator", project_description = "Node.js, Inquirer, JavaScript.", repo_link = "https://github.com/ChaseOstien/README_Generator", user_id = 1 ),
    Project(project_name = "Weather Dashboard", project_description = "Node.js, JavaScript, API.", repo_link = "https://github.com/ChaseOstien/Weather-Dashboard", user_id = 1 )
])

db.commit()

db.close() # close the connection to the database