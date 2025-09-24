DAYS =["mon","tue","wed","thu","fri"]
PERIODS_PER_DAY =6
SLOTS =[(d,p) for d in
range(len(DAYS)) for p in
        range(PERIODS_PER_DAY)]
CLASSES =["classA","classB"]
SUBJECTS ={"Math": {"teacher": "Muthaiyan","periods_per_week":4},
           "Science":{"teacher":"Saranya","periods_per_week":3},
           "English":{"teacher":"Keerthika","periods_per_week":5},
           "History":{"teacher":"Kavitha","periods_per_week":2},
           }
ROOMS =["Room1","Room2"]

CLASS_SUBJECTS ={c:
list()

