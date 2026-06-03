from flask import Flask,render_template

app = Flask(__name__)



cards=[
    {
        "img":"images/cardFirst.png",
        "title":"History",
        "content":"Explore the past and learn about our history.",
        "record":"120+ topics",
        "recordColor":"text-yellow-800",

    },

    {
        "img":"images/cardSecond.png",
        "title":"Geography",
        "content":"Discover the world, Countries and more.",
        "record":"150+ Topics",
        "recordColor":" text-green-500",

    },

    {
        "img":"images/cardThird.png",
        "title":"Science",
        "content":" learn about amazing science facts",
        "record":"180+ topics",
        "recordColor":"text-blue-800",

    },

    

    {
        "img":"images/cardForth.png",
        "title":"Computer",
        "content":"Computer basics to advanced knowledge",
        "record":"90+ Topics",
        "recordColor":"text-purple-700",

    },

    {
        "img":"images/cardSecond.png",
        "title":"Geography",
        "content":"Discover the world, Countries and more.",
        "record":"150+ Topics",
        "recordColor":" text-green-500",

    },


   {
        "img":"images/cardSecond.png",
        "title":"Geography",
        "content":"Discover the world, Countries and more.",
        "record":"150+ Topics",
        "recordColor":" text-green-500",

    },


]


testCards=[

    {
        "background":"bg-gradient-to-br from-blue-400 to-slate-800/90",
        "number":"10",
        "content":"Questions"
    },
     
     {
         "background":"bg-gradient-to-br from-purple-400 to-slate-800/90",
        "number":"2:00",
        "content":"Mintues"
    },
     
     {
         "background":"bg-gradient-to-br from-orange-400 to-slate-800/90",
        "number":"100",
        "content":"Points"
    },

      {
          "id":"card",
         "background":"bg-gradient-to-br from-green-400 to-slate-800/90",
        "content":"Click here before start"
    },
     
]




##why choose us cards

whycards=[
    {
        "title":"Subject Wise Learning",
        "icon":"fa-solid fa-book-open",
        "content":"Explore General Knowledge topic by topic with well-organized learning resources and quizzes.",
        "background":"hover:border-purple-500 ",
        "iconColor":"bg-gradient-to-br from-purple-900 to-slate-200/20 ",
        "iconborder":" border border-purple-500",
        "headingColor":"text-purple-500",
    },

    {
        "title":"Daily Quiz Challenges",
        "icon":"fa-solid fa-bolt",
        "content":"Test your knowledge every day with exciting quizzes designed to improve your GK skills.",
        "background":"hover:border-green-500 ",
        "iconColor":"bg-gradient-to-br from-green-900 to-slate-200/20",
        "iconborder":"border border-green-500",
        "headingColor":"text-green-500",
    },

      {
        "title":"Quick Time & Interactive",
        "icon":"fa-solid fa-rocket",
        "content":"Enjoy a smooth and engaging learning experience with interactive content and activities.",
        "background":"hover:border-yellow-500 ",
        "iconColor":"bg-gradient-to-br from-yellow-900 to-slate-200/20",
        "iconborder":"border border-yellow-500",
        "headingColor":"text-yellow-500",
    },

      {
        "title":"Improve Your Skills",
        "icon":"fa-solid fa-medal",
        "content":"Track your progress, strengthen weak areas, and become more confident in General Knowledge.",
        "background":"hover:border-blue-500 ",
        "iconColor":"bg-gradient-to-br from-blue-900 to-slate-200/20",
        "iconborder":"border border-blue-500",
        "headingColor":"text-blue-500",
    },


    

]

##learn page header small 3 card

learnCards=[
    {
        "icon":"fa-solid fa-book-open",
        "content":"Topics",
        "number":"100+",
    },

    {
        "icon":"fa-solid fa-file-lines",
        "content":"Articles",
        "number":"500+",
    },

    {
        "icon":"fa-solid fa-bullseye",
        "content":"Learners",
        "number":"10K",
    },

]

##again new cards from learn page
learnCards2=[

    {
        "icon":"fa-regular fa-file-lines",
        "content":"Learn important GK concepts through clear and easy-to-understand notes.",
        "heading":"Concept Notes",
        "iconColor":"text-green-400",
        "iconBG":" bg-gradient-to-br from-green-700 to-slate-950/20",
        "iconBorder":" border  border-green-400",
    },


     {
        "icon":"fa-solid fa-book",
        "content":"Discover  key information that improve your general knowledge.",
        "heading":"Important Facts",
        "iconColor":"text-purple-400",
        "iconBG":" bg-gradient-to-br from-purple-700 to-slate-950/20",
        "iconBorder":" border border-purple-400",
    },

     {
        "icon":"fa-solid fa-lightbulb",
        "content":"Prepare effectively for competitive exams with focused GK topics and practice.",
        "heading":"Exam Preparation",
        "iconColor":"text-sky-400",
        "iconBG":" bg-gradient-to-br from-sky-700 to-slate-950/20",
        "iconBorder":" border border-sky-400",
    },




     {
        "icon":"fa-solid fa-bullseye",
        "content":"Build a strong knowledge habit by learning something new every day.",
        "heading":"Daily Learning",
        "iconColor":" text-orange-400",
        "iconBG":"bg-gradient-to-br from-orange-700 to-slate-950/20",
        "iconBorder":"border border-orange-400",
    },


     {
        "icon":"fa-regular fa-calendar-days",
        "content":"Access useful learning materials, references and curated GK content.",
        "heading":"Study Resources",
        "iconColor":"text-cyan-400",
        "iconBG":" bg-gradient-to-br from-cyan-700 to-slate-950/20",
        "iconBorder":" border border-cyan-400 ",
    },


     {
        "icon":"fa-regular fa-bookmark",
        "content":"Explore the most popular and frequently asked General Knowledge topics.",
        "heading":"Top GK Topics",
        "iconColor":" text-red-400 ",
        "iconBG":" bg-gradient-to-br from-red-700 to-slate-950/20",
        "iconBorder":" border border-red-400",
    },
]









@app.route("/")
def home():
    return render_template("index.html", cards=cards , testCards=testCards,whycards=whycards)


@app.route("/Learn")
def Learn():
    return render_template("Learn.html",learnCards=learnCards,learnCards2=learnCards2)

@app.route("/Categories")
def Categories():
    return render_template("Categories.html")
















if __name__ == "__main__":
    app.run(debug=True)