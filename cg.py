from load_databases import *



class Decision:

    def __init__(self) -> None:
        self.isaDepth = None
        self.sortKey = None
        self.bill = None
        self.member = None
        self.forStances = []
        self.agnStances = []
        self.negForStances = []
        self.negAgnStances = []
        self.conRelForStances = []
        self.conRelAgnStances = []
        self.noUpdate = None
        self.numberFor = None
        self.numberAgn = None
        self.groupFor = []
        self.groupAgn = []
        self.forNorms = []
        self.agnNorms = []
        self.forBnorms = []
        self.agnBnorms = []
        self.splitGroup = []
        self.splitRecord = None
        self.splitCredo = None
        self.MIStance = None
        self.MIGroup = None
        self.MICredo = None
        self.MIRecord = None
        self.MINorm = None
        self.strategy = None
        self.result = None
        self.reason = None
        self.downside = None
        self.downsideRecord = None

def dbRetrieve(item, database):
    try:
        return database[item]
    except KeyError:
        return None

def deliverDecision(decision, side, strat):

    print("*" * 70)
    print(f"{'Member:':<30}", f"{decision.member.name:<40}")
    print(f"{'Bill:':<30}", f"{decision.bill.name:<40}")
    for line in decision.bill.remarks:
        print(f"{'':<30}",f"{line:<40}")
    print("*" * 70)

    
    print(f"{'Member:':<30}{decision.member.name:<40}")
    
    print(f"{'Stances:':<30}")
    for line in decision.member.stances:
        print(f"{'':<30}",f"{str(line):<40}")
    
    print(f"{'Relations:':<30}")
    for line in decision.member.relations:
        print(f"{'':<30}",f"{str(line):<40}")

    print(f"{'Pro-Rel-Stances:':<30}")
    for line in decision.member.proRelStances:
        print(f"{'':<30}",f"{str(line):<40}")
    
    print(f"{'Pro-Con-Stances:':<30}")
    for line in decision.member.conRelStances:
        print(f"{'':<30}",f"{str(line):<40}")


    print("*" * 70)
    print(f"{'Bill:':<30}", f"{decision.bill.name:<40}")

    print(f"{'For-Stances:':<30}")
    for line in decision.bill.stanceFor:
        print(f"{'':<30}",f"{str(line):<40}")

    print(f"{'Agn-Stances:':<30}")
    for line in decision.bill.stanceAgn:
        print(f"{'':<30}",f"{str(line):<40}")
    print("*" * 70)

    print(f"{'Result:':<30}", f"{str(side):<40}")
    if (side == "FOR"):
        for line in decision.forStances:
            print(f"{'':<30}",f"{str(line):<40}")
    elif (side == "AGN"):
        for line in decision.agnStances:
            print(f"{'':<30}",f"{str(line):<40}")
    print(f"{'Strategy:':<30}", f"{strat:<40}")
    

    

    
    


def vote(member, bill):
    # Create Decision object.
    decision = Decision()

    decision.member = dbRetrieve(member, members_db)
    decision.bill = dbRetrieve(bill, bill_db)

    if not decision.member:
        print("INVALID MEMBER")
        return

    if not decision.bill:
        print("INVALID BILL")
        return

    # Initialize decision
    initializeDecision(decision)

    # Go through each decision strategy until one passes.

    # ==================================================================
    #       0   Popular decision                        [A] @(POPULAR)
    # 
    #   Remarks:       Vote is consistent with major constituencies.
    #   Quote:         I just try to vote my district.
    #                  I was sent to Washington to represent the way people back home feel.
    #                  This is what the vast majority want.
    #                  I owe it to my constiuents if they feel that strongly about it. [Delegate stance]
    #   Rank:          "A"
    #   Test:          All stances on one side of bill.
    #   Test-code:     STRAT-POPULAR
    #   Example:       (VOTE 'BRUCE 'PLANT-CLOSING)
    # ==================================================================

    if (decision.agnStances and not decision.forStances):
        deliverDecision(decision, "AGN", "POPULAR-DECISION")
        return decision
    elif (decision.forStances and not decision.agnStances):
        deliverDecision(decision, "FOR", "POPULAR-DECISION")
        return decision

    # ==================================================================
    #       3   Not constitutional                      [B]  (NOT-CONSTITUTIONAL)
    # 
    #   Remarks:       Vote against a measure that would be struck down by
    #                  the Supreme Court.
    #   Rank:          "B"
    # ==================================================================

    
    if(decision.MICredo == decision.MIGroup == decision.MIStance):
        total = len(decision.agnStances)
        count = 0
        for stance in decision.agnStances:
            if stance.issue == "CONSTITUTION":
                count += 1
        if total == count:
            deliverDecision(decision, "AGN", "NOT-CONSTITUTIONAL")
            return decision

    # ==================================================================
    #       4   Unimportant Bill                        [B]   (UNIMPORTANT-BILL)
    #   
    #   Date-open:     Monday, May 22, 1989
    #   Symbol:        STRATEGY.681
    #   Name:          "Unimportant Bill"
    #   Sort-key:      "BUnimportant Bill"
    #   Synonyms:      (UNIMPORTANT-BILL)
    #   Isa-depth:     ""
    #   Remarks:       Not much riding on this bill.
    #   
    #   Quote:         [Morrison:] some things that are close calls are not treated
    #                  as close calls because they're not important enough.  I mean
    #                  its very different if there's enough riding -- either substantively
    #                  or politically -- on a vote.  You might have exactly the same
    #                  tensions among the various priorities if you were to pull 
    #                  this up, but it might be about how you spend $100,000 and you
    #                  say, fuck this.
    #   
    #   Rank:          "B"
    #   Test:          Importance of bill is minimal.
    # ==================================================================

    if(decision.MIGroup and decision.MIStance):
        if(decision.MIGroup.side == decision.MIStance.side):
            if (decision.MIGroup.side == "AGN"):
                if decision.bill.importance == "C":
                    deliverDecision(decision, "AGN", "UNIMPORTANT-BILL")
                    return decision
            elif (decision.MIGroup.side == "FOR"):
                if decision.bill.importance == "C":
                    deliverDecision(decision, "FOR", "UNIMPORTANT-BILL")
                    return decision

    # ==================================================================
    #         15  Simple consensus                        [C] @ (SIMPLE-CONSENSUS)
    #   
    #   Status:        "Active"
    #   Date-open:     Thursday, May 11, 1989
    #   Symbol:        STRATEGY.1018
    #   Name:          "Simple consensus"
    #   Sort-key:      "CSimple consensus"
    #   Synonyms:      (SIMPLE-CONSENSUS)
    #   Isa-depth:     ""
    #   Remarks:       The most important issues/groups/norms etc. concur.
    #   
    #   Rank:          "C"
    #   Test:          Check all most important features
    #   
    #   Test-code:     STRAT-SIMPLE-CONSENSUS
    # ==================================================================

    if(decision.MIGroup and decision.MIStance):
        if (decision.MIGroup.side == decision.MIStance.side):
            if (decision.MICredo):
                if (decision.MICredo.side == decision.MIStance.side):
                    deliverDecision(decision, decision.MIGroup, "SIMPLE-CONSENSUS")
                    return decision
    
    # ==================================================================
    #       19  No decision                             [E] @(NO-DECISION)
    #   Test-code:   STRAT-NO-DECISION
    #   Remarks:     No previous decision was triggered.
    #   Test:        Always true.
    # ==================================================================

    deliverDecision(decision, None, "NO-DECISION")
    return decision



def initializeDecision(decision):
    pass
    # Print header.

    inferStances(decision)

    # for the decision, get the stances from the member's stances that match the for/agn of the bill.
    # for each stance the member has, check if it is in the PRO or AGN consequences of the bill.
    #   if it is in the pro, add the member's stance to the decisionForStances
    #   if it is in the con, add the member's stance to the decisionConStances

    for bstance in decision.bill.stanceFor:
        for mstance in decision.member.stances:
            if bstance == mstance:
                decision.forStances.append(mstance)
                if not decision.MIStance:
                    decision.MIStance = mstance
                elif decision.MIStance < mstance:
                    decision.MIStance = mstance
        for mstance in decision.member.proRelStances:
            if bstance == mstance:
                decision.forStances.append(mstance)
                if not decision.MIGroup:
                    decision.MIGroup = mstance
                elif decision.MIGroup < mstance:
                    decision.MIGroup = mstance
        for mstance in decision.member.credo:
            if bstance == mstance:
                decision.forStances.append(mstance)
                if not decision.MICredo:
                    decision.MICredo = mstance
                elif decision.MICredo < mstance:
                    decision.MICredo = mstance

    for bstance in decision.bill.stanceAgn:
        for mstance in decision.member.stances:
            if bstance == mstance:
                decision.agnStances.append(mstance)
                if not decision.MIStance:
                    decision.MIStance = mstance
                elif decision.MIStance < mstance:
                    decision.MIStance = mstance
        for mstance in decision.member.proRelStances:
            if bstance == mstance:
                decision.agnStances.append(mstance)
                if not decision.MIGroup:
                    decision.MIGroup = mstance
                elif decision.MIGroup < mstance:
                    decision.MIGroup = mstance
        for mstance in decision.member.credo:
            if bstance == mstance:
                decision.agnStances.append(mstance)
                if not decision.MICredo:
                    decision.MICredo = mstance
                elif decision.MICredo < mstance:
                    decision.MICredo = mstance

    decision.agnStances.sort()
    decision.forStances.sort()


def inferStances(decision):
    if decision.member.stances == []:
        for vote, stance in decision.member.votes:
            for bill in bill_db.keys():
                if vote in bill_db[bill].synonyms:
                    if stance == "FOR":
                        # add for stances of bill to member stances
                        for x in bill_db[bill].stanceFor: 
                            decision.member.stances.append(x)
                    elif stance == "AGN":
                        # add agn stances of bill to member stances
                        for x in bill_db[bill].stanceAgn: 
                            decision.member.stances.append(x)
    
    if decision.member.proRelStances == []:
        for relation in decision.member.relations:
            if relation.side == "PRO":
                for grp in group_db.keys():
                    if group_db[grp].synonyms:
                        if relation.group in group_db[grp].synonyms:
                            for stance in group_db[grp].stances: 
                                decision.member.proRelStances.append(stance)
            elif relation.side == "CON":
                for grp in group_db.keys():
                    if group_db[grp].synonyms:
                        if relation.group in group_db[grp].synonyms:
                            for stance in group_db[grp].stances: 
                                decision.member.conRelStances.append(stance)

f = vote("Morris K. Udall", "HR-2978")

