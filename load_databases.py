import json

class Stance:
    
    def __init__(self, issue, side, importance, source, srctype):
        self.issue = issue
        self.side = side
        self.importance = importance
        self.source = source
        self.srctype = srctype

    def __repr__(self) -> str:
        return f"Stance({self.issue}, {self.side}, {self.importance}, {self.source})"

    def __lt__(self, __o: object) -> bool:
        return self.importance < __o.importance

    def __eq__(self, __o: object) -> bool:
        return self.side + self.issue == __o.side + __o.issue

class Relation:

    def __init__(self, group, side, importance, source, srctype):
        self.group = group
        self.side = side
        self.importance = importance
        self.source = source
        self.srctype = srctype

    def __repr__(self) -> str:
        return f"Relation({self.group}, {self.side}, {self.importance}, {self.source})"

    def __lt__(self, __o: object) -> bool:
        return self.side + self.importance + self.group < __o.side + __o.importance + __o.group

class Bill:

    def __init__(self):
        self.name = None 
        self.english = None 
        self.french = None 
        self.bnumber = None
        self.dateOfVote = None
        self.presPos = None
        self.voteTally = None
        self.testBill = None
        self.session = None 
        self.synonyms = []
        self.isa = None 
        self.majorityFactor = None
        self.issues = None
        self.importance = None
        self.stanceFor = [] 
        self.stanceAgn = []
        self.iStanceFor = []

        self.status = None
        self.dateOpen = None
        self.symbol = None
        self.remarks = None

class Member:

    def __init__(self):
        self.name = None
        self.fname = None
        self.lname = None
        self.englishShort = None
        self.notes = None
        self.gender = None
        self.votes = None
        self.newVotes = None
        self.stances = []
        self.issues = None
        self.credo = []
        self.groups = None
        self.relations = []
        self.proRelStances = []
        self.conRelStances = []
        self.stanceSortKey = None
        self.district = None
        self.termStart = None
        self.termEnd = None
        self.party = None
        self.committees = None

        self.status = None
        self.dateOpen = None
        self.symbol = None
        self.remarks = None

class Group:

    def __init__(self):
        self.name = None
        self.notes = None
        self.gender = None
        self.issues = None
        self.sortKey = None
        self.stances = []
        self.credo = []
        self.english = None
        self.englishShort = None
        self.proEnglish = None
        self.conEnglish = None
        self.french = None
        self.frenchShort = None
        self.proFrench = None
        self.conFrench = None
        self.number = None
        self.synonyms = []
        self.proStances = []
        self.conStances = []
        self.norm = []
        self.isa = None
        self.isaDepth = None
        self.instances = None

        self.status = None
        self.dateOpen = None
        self.symbol = None
        self.remarks = None

class Issue:

    def __init__(self):
        self.name = None
        self.type = None
        self.sortKey = None
        self.synonyms = []
        self.isa = None
        self.isaDepth = None
        self.instances = None
        self.polarity = None
        self.english = None
        self.englishShort = None
        self.proEnglish = None
        self.conEnglish = None
        self.french = None
        self.frenchShort = None
        self.proFrench = None
        self.conFrench = None
        self.number = None
        self.groups = None
        self.proStances = []
        self.conStances = []
        self.norm = []
        self.opposite = None
        self.notes = None

        self.status = None
        self.dateOpen = None
        self.symbol = None
        self.remarks = None


bill_db = {}
group_db = {}
issues_db = {}
members_db = {}


with open('db/bills.json') as json_file:
    data = json.load(json_file)

    for u in data:
        object = Bill()

        for sym in u.keys():
            if sym == "NAME":
                object.name = u[sym]
            if sym == "ENGLISH":
                object.english = u[sym]
            if sym == "BNUMBER":
                object.bnumber = u[sym]
            if sym == "SYNONYMS":
                object.synonyms = u[sym]
            if sym == "DATE-OF-VOTE":
                object.dateOfVote = u[sym]
            if sym == "VOTE-TALLY":
                object.voteTally = u[sym]
            if sym == "PRES-POS":
                object.presPos = u[sym]
            if sym == "SESSION":
                object.session = u[sym]
            if sym == "MAJORITY-FACTOR":
                object.majorityFactor = u[sym]
            if sym == "ISSUES":
                object.issues = u[sym]
            if sym == "IMPORTANCE":
                object.importance = u[sym]
            if sym == "STANCE-FOR":
                for i in u[sym]:
                    x = i.split(' ')
                    object.stanceFor.append(Stance(x[0], x[1], x[2], x[3], x[4]))
            if sym == "STANCE-AGN":
                for i in u[sym]:
                    x = i.split(' ')
                    object.stanceAgn.append(Stance(x[0], x[1], x[2], x[3], x[4]))
            if sym == "STATUS":
                object.status = u[sym]
            if sym == "DATE-OPEN":
                object.dateOpen = u[sym]
            if sym == "SYMBOL":
                object.symbol = u[sym]
            if sym == "REMARKS":
                object.remarks = u[sym]

        bill_db[object.bnumber] = object


with open('db/groups.json') as json_file:
    data = json.load(json_file)

    for u in data:
        object = Group()

        for sym in u.keys():
            if sym == "NAME":
                object.name = u[sym]
            if sym == "GENDER":
                object.gender = u[sym]
            if sym == "ISSUES":
                object.issues = u[sym]
            if sym == "STANCES":
                for i in u[sym]:
                    x = i.split(' ')
                    object.stances.append(Stance(x[0], x[1], x[2], x[3], x[4]))
            if sym == "ENGLISH":
                object.english = u[sym]
            if sym == "ENGLISH-SHORT":
                object.englishShort = u[sym]
            if sym == "PRO-ENGLISH":
                object.proEnglish = u[sym]
            if sym == "CON-ENGLISH":
                object.conEnglish = u[sym]
            if sym == "FRENCH":
                object.french = u[sym]
            if sym == "NUMBER":
                object.number = u[sym]
            if sym == "SYNONYMS":
                object.synonyms = u[sym]
            if sym == "NORM":
                x = u[sym].split(' ')
                object.norm.append(Stance(x[0], x[1], x[2], x[3], x[4]))
            if sym == "ISA":
                object.isa = u[sym]
            if sym == "STATUS":
                object.status = u[sym]
            if sym == "DATE-OPEN":
                object.dateOpen = u[sym]
            if sym == "SYMBOL":
                object.symbol = u[sym]
            if sym == "REMARKS":
                object.remarks = u[sym]

        group_db[object.name] = object


with open('db/issues.json') as json_file:
    data = json.load(json_file)

    for u in data:
        object = Issue()

        for sym in u.keys():
            if sym == "NAME":
                object.name = u[sym]
            if sym == "TYPE":
                object.type = u[sym]
            if sym == "SYNONYMS":
                object.synonyms = u[sym]
            if sym == "ISA":
                object.isa = u[sym]
            if sym == "POLARITY":
                object.polarity = u[sym]
            if sym == "ENGLISH":
                object.english = u[sym]
            if sym == "ENGLISH-SHORT":
                object.englishShort = u[sym]
            if sym == "PRO-ENGLISH":
                object.proEnglish = u[sym]
            if sym == "CON-ENGLISH":
                object.conEnglish = u[sym]
            if sym == "PRO-STANCES":
                for i in u[sym]:
                    x = i.split(' ')
                    object.proStances.append(Stance(x[0], x[1], x[2], x[3], x[4]))
            if sym == "CON-STANCES":
                for i in u[sym]:
                    x = i.split(' ')
                    object.conStances.append(Stance(x[0], x[1], x[2], x[3], x[4]))
            if sym == "NORM":
                x = u[sym].split(' ')
                object.norm.append(Stance(x[0], x[1], x[2], x[3], x[4]))
            if sym == "OPPOSITE":
                object.opposite = u[sym]
            if sym == "STATUS":
                object.status = u[sym]
            if sym == "DATE-OPEN":
                object.dateOpen = u[sym]
            if sym == "SYMBOL":
                object.symbol = u[sym]
            if sym == "REMARKS":
                object.remarks = u[sym]

        issues_db[object.name] = object


with open('db/members.json') as json_file:
    data = json.load(json_file)

    for u in data:
        object = Member()

        for sym in u.keys():
            if sym == "NAME":
                object.name = u[sym]
            if sym == "GENDER":
                object.gender = u[sym]
            if sym == "ENGLISH-SHORT":
                object.englishShort = u[sym]
            if sym == "VOTES":
                object.votes = u[sym]
            if sym == "CREDO":
                for i in u[sym]:
                    x = i.split(' ')
                    object.credo.append(Stance(x[0], x[1], x[2], x[3], x[4]))
            if sym == "ISSUES":
                object.issues = u[sym]
            if sym == "GROUPS":
                object.groups = u[sym]
            if sym == "RELATIONS":
                for i in u[sym]:
                    x = i.split(' ')
                    object.relations.append(Relation(x[0], x[1], x[2], x[3], x[4]))
            if sym == "STANCE-SORT-KEY":
                object.stanceSortKey = u[sym]
            if sym == "DISTRICT":
                object.district = u[sym]
            if sym == "TERM-START":
                object.termStart = u[sym]
            if sym == "TERM-END":
                object.termEnd = u[sym]
            if sym == "PARTY":
                object.party = u[sym]
            if sym == "COMMITTEES":
                object.committees = u[sym]
            if sym == "STATUS":
                object.status = u[sym]
            if sym == "DATE-OPEN":
                object.dateOpen = u[sym]
            if sym == "SYMBOL":
                object.symbol = u[sym]
            if sym == "REMARKS":
                object.remarks = u[sym]

        members_db[object.name] = object