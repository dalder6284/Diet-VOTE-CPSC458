### DIET VOTE: A replication of the roll call prediction program VOTE procedures.

#### Translated from LISP to Python by Diego Alderete

Hello. In this program, I undertook the task of replicating the publicly
available LISP program VOTE by Stephen Slade and recreated it (to a much
simpler degree) in Python as my final project for CPSC 458: Automated
Decision Systems.

VOTE is a database of bills, members of Congress, issues, and political
groups. In addition to storing basic information like the name of a
member or a bill, it stores the goals of these items and their relation
to other items. This allows vote to draft decisions based on goals of
agents, and with relationships to other agents and items, infer possible
deeper goals of agents that were not explicitly stated.

While the original VOTE program consisted of functions pertaining to
natural language generation, database manipulation, and analysis of
decisions made, this program is much less complicated due to time
constraints and due to LISP being difficult to understand for an
unexperienced first-year computer science student. I did not include any
of the above mentioned, and there are fewer strategies that the
`<code>`{=html}vote`</code>`{=html} function runs through.

I have, however, put the BILLS, GROUPS, ISSUES, MEMBERS, and STRATEGIES
files into a standardized JSON format as a gift for all future students
of this class. Originally, all these agents and relationships were
hard-coded into a LISP program that inserted them into the databases
individually. They are now neatly organized into JSON format! Have fun!

While everyone in the class has definitely read the book, there would be
no sense in explaining how the program works, but I will do it anyways
for posterity.

#### **VOTE\'S Algorithm**

VOTE works like this in the simplest terms:

1.  Every member\'s stances (or goals) are determined by their voting
    records. They are for the goals of the bills they have voted for,
    and they are against the goals of the bills they have voted against.

2.  Each member also has inferred stances. These inferred stances come
    from the goals of their allies. If their friend or constituents like
    a certain thing, they will most likely like that certain thing, too.

3.  Each bill also has stances.

4.  After gathering our stances for the member, we find which ones are
    relevant to the bill.

5.  Using these relevant stances, we use various strategies to see if we
    can make a decision.

The load_databases.py takes in the JSON
files and makes the databases for bills, groups, issues, and members.
Using these, we find and connect stances in cg.py.

#### **How to run a VOTE**

Run the following command in your shell with
`cg.py`, `load_databases.py`, and the database
folder all being in the same directory.

``` python
python -i cg.py
```


This will run cg.py and
load_databases.py (since it is imported
by former). The -i argument leaves your
interpreter open, so you can run the vote
function with all databases loaded.

``` python
>>> vote("Morris K. Udall", "Flag Desecration")
```


``` python
This is the sample output of a decision.
```

```{=ipynb}
**********************************************************************
Member:                        Morris K. Udall
Bill:                          Flag Desecration
                               Bill banning the desecration of the American flag."
**********************************************************************
Member:                       Morris K. Udall
Stances:
                               Stance(CHEMICAL-WEAPONS, CON, B, AMD)   
                               Stance(ELDERLY, PRO, C, HR-4800)        
                               Stance(HANDICAPPED, PRO, C, HR-4800)    
                               Stance(HOMELESSNESS, PRO, C, HR-4800)   
                               Stance(URBAN-RENEWAL, PRO, C, HR-4800)  
                               Stance(CIVIL-RIGHTS, PRO, B, S-557)     
                               Stance(FAIRNESS, PRO, B, S-557)
                               Stance(AGE-DISCRIMINATION, CON, B, S-557)
                               Stance(EDUCATION-RIGHTS, PRO, B, S-557)
                               Stance(PERSIAN-GULF, CON, B, HR-2342)
                               Stance(NON-INVOLVEMENT, PRO, B, HR-2342)
                               Stance(GUN-CONTROL, PRO, B, HR-5210)
                               Stance(CRIME, PRO, B, HR-5210)
                               Stance(COMPASSION, PRO, B, HJR-484)
                               Stance(HUMANITARIANISM, PRO, B, HJR-484)
                               Stance(END-OF-HOSTILITIES, PRO, B, HJR-484)
                               Stance(MILITARY-SOLUTION, CON, C, HJR-484)
                               Stance(SPENDING, CON, B, HR-466)
                               Stance(GAY-RIGHTS, CON, B, HR-5142)
                               Stance(SPENDING, CON, B, HR-5142)
                               Stance(REAGAN, PRO, B, HR-1154)
                               Stance(TRADE-RESTRICTIONS, CON, B, HR-1154)
                               Stance(TAXES, CON, C, HR-1183)
                               Stance(FAIRNESS, PRO, B, HR-1183)
                               Stance(SOCIAL-SECURITY, CON, C, HR-1900)
                               Stance(TAXES, CON, C, HR-1900)
                               Stance(TRADE-DEFICIT, PRO, C, HR-1234)
                               Stance(TRADE-RESTRICTIONS, PRO, C, HR-1234)
                               Stance(LABOR, PRO, C, HR-1234)
                               Stance(IMMIGRATION, PRO, C, HR-1510A)
                               Stance(PRAYER, CON, C, HR-5345)
                               Stance(CONSTITUTION, PRO, B, HR-5345)
                               Stance(ABORTION, PRO, B, HR-3191)
                               Stance(ERA, PRO, B, HJR-1)
                               Stance(WOMENS-RIGHTS, PRO, B, HJR-1)
                               Stance(FAIRNESS, PRO, B, HJR-1)
                               Stance(EQUITY, PRO, B, HJR-1)
                               Stance(IMMIGRATION, CON, B, HR-1510)
                               Stance(MX, CON, B, HR-5167)
                               Stance(DEFENSE-SPENDING, CON, C, HR-5167)
                               Stance(CONTRA-AID, CON, B, HR-2760)
                               Stance(EL-SALVADOR, CON, B, HR-5119)
                               Stance(NUCLEAR-FREEZE, PRO, B, HJR-13)
                               Stance(ARMS-CONTROL, PRO, C, HJR-13)
                               Stance(HELP-WEALTHY, CON, B, HR-3299)
                               Stance(TAXES, PRO, C, HR-3299)
                               Stance(FISCAL-RESPONSIBILITY, PRO, B, HR-3299)
                               Stance(CLEAN-WATER, PRO, B, HR-8)
                               Stance(CLEAN-AIR, PRO, B, HR-8)
                               Stance(TOBACCO-PRICE-SUPPORTS, PRO, B, HR-2100)
                               Stance(SPENDING, PRO, B, HJR-372)
                               Stance(PRIVACY, PRO, B, HR-1524)
                               Stance(GUN-CONTROL, CON, B, HR-4332)
                               Stance(BILL-OF-RIGHTS, PRO, B, HR-4332)
                               Stance(CONTRA-AID, CON, B, HJR-540)
                               Stance(TRADE-RESTRICTIONS, PRO, B, HR-1562)
                               Stance(TEXTILE-INDUSTRY, PRO, B, HR-1562)
                               Stance(SDI, CON, B, HR-4428)
                               Stance(ANGOLA-REBELS, CON, B, HR-4759)
                               Stance(HUMAN-RIGHTS, PRO, B, HR-4759)
                               Stance(PEACE, PRO, B, HR-4759)
                               Stance(DIPLOMACY, PRO, B, HR-4759)
                               Stance(ISOLATIONISM, PRO, B, HR-4759)
                               Stance(TAX-REFORM, PRO, B, HR-3838)
                               Stance(APARTHEID, CON, B, HR-4868)
                               Stance(IMMIGRATION-REFORM, PRO, B, S-1200)
                               Stance(CHILD-CARE, PRO, B, HR-3)
                               Stance(FAMILY, PRO, B, HR-3)
                               Stance(EDUCATION, PRO, C, HR-3)
                               Stance(LABOR, PRO, C, HR-3)
                               Stance(FREE-SPEECH, PRO, B, HJR-350)
                               Stance(BILL-OF-RIGHTS, PRO, A, HJR-350)
Relations:
                               Relation(ADA, PRO, B, MEMBER.1025)
                               Relation(ACLU, PRO, A, MEMBER.1025)
                               Relation(COPE, PRO, B, MEMBER.1025)
                               Relation(LCV, PRO, C, MEMBER.1025)
                               Relation(ACU, CON, B, MEMBER.1025)
                               Relation(NTU, CON, B, MEMBER.1025)
                               Relation(NSI, CON, B, MEMBER.1025)
                               Relation(COC, CON, B, MEMBER.1025)
                               Relation(CEI, CON, B, MEMBER.1025)
                               Relation(DEMOCRATS, PRO, C, MEMBER.1025)
                               Relation(REPUBLICANS, CON, C, MEMBER.1025)
                               Relation(COUNTRY, PRO, C, MEMBER.1025)
Pro-Rel-Stances:
                               Stance(CONTRA-AID, CON, B, ADA)
                               Stance(APARTHEID, CON, B, ADA)
                               Stance(ARMS-CONTROL, PRO, B, ADA)
                               Stance(SOCIAL, PRO, B, ADA)
                               Stance(BORK, CON, B, ADA)
                               Stance(CAPITAL-PUNISHMENT, CON, B, ADA)
                               Stance(CIVIL-RIGHTS, PRO, B, ADA)
                               Stance(CONSTRUCTIVE-ENGAGEMENT, CON, B, ADA)
                               Stance(CREATIONISM, CON, B, ADA)
                               Stance(ERA, PRO, B, ADA)
                               Stance(GUN-CONTROL, PRO, A, ADA)
                               Stance(HOUSING, PRO, B, ADA)
                               Stance(HUMAN-RIGHTS, PRO, B, ADA)       
                               Stance(LABOR, PRO, B, ADA)
                               Stance(MANION, CON, B, ADA)
                               Stance(NUCLEAR-FREEZE, PRO, B, ADA)
                               Stance(OPEN-HOUSING, PRO, B, ADA)
                               Stance(RACISM, CON, B, ADA)
                               Stance(BUSSING, PRO, B, ADA)
                               Stance(SDI, CON, B, ADA)
                               Stance(URBAN, PRO, B, ADA)
                               Stance(VOTING-RIGHTS, PRO, B, ADA)
                               Stance(WEAPONS, CON, B, ADA)
                               Stance(WOMENS-RIGHTS, PRO, B, ADA)
                               Stance(ABORTION, PRO, C, ADA)
                               Stance(BALANCED-BUDGET, CON, C, ADA)
                               Stance(MX, CON, C, ADA)
                               Stance(B-1, CON, C, ADA)
                               Stance(FOOD-STAMPS, PRO, B, ADA)
                               Stance(CLINCH-RIVER, CON, B, ADA)
                               Stance(CIVIL-LIBERTIES, PRO, B, ACLU)
                               Stance(PRIVACY, PRO, B, ACLU)
                               Stance(LEGAL-SERVICES, PRO, C, ACLU)
                               Stance(VOTING-RIGHTS, PRO, C, ACLU)
                               Stance(PRAYER, CON, C, ACLU)
                               Stance(CONSTITUTION, PRO, A, ACLU)
                               Stance(LABOR, PRO, B, COPE)
                               Stance(PLANT-CLOSING, PRO, B, COPE)
                               Stance(CHILD-CARE, PRO, B, COPE)
                               Stance(SPENDING, PRO, B, COPE)
                               Stance(BORK, CON, B, COPE)
                               Stance(SOCIAL, PRO, B, COPE)
                               Stance(TRADE-RESTRICTIONS, PRO, B, COPE)
                               Stance(VOTING-RIGHTS, PRO, C, COPE)
                               Stance(BALANCED-BUDGET, CON, C, COPE)
                               Stance(FOOD-STAMPS, PRO, B, COPE)
                               Stance(ENERGY, PRO, B, LCV)
                               Stance(ENVIRONMENT, PRO, B, LCV)
                               Stance(CLEAN-WATER, PRO, B, LCV)
                               Stance(CLEAN-AIR, PRO, B, LCV)
                               Stance(SUPERFUND, PRO, B, LCV)
                               Stance(CLINCH-RIVER, CON, B, LCV)
                               Stance(ARMS-CONTROL, PRO, B, COUNTRY)
                               Stance(BALANCED-BUDGET, PRO, C, COUNTRY)
                               Stance(INDUSTRY, PRO, C, COUNTRY)
                               Stance(CHILD-CARE, PRO, C, COUNTRY)
                               Stance(CIVIL-LIBERTIES, PRO, C, COUNTRY)
                               Stance(CIVIL-RIGHTS, PRO, C, COUNTRY)
                               Stance(CONSTITUTION, PRO, B, COUNTRY)
                               Stance(CONVENTIONAL-DEFENSE, PRO, C, COUNTRY)
                               Stance(DEFENSE, PRO, C, COUNTRY)
                               Stance(DEFICIT, CON, C, COUNTRY)
                               Stance(DEMOCRACY, PRO, B, COUNTRY)
                               Stance(ENERGY, PRO, C, COUNTRY)
                               Stance(EQUALITY, PRO, B, COUNTRY)
                               Stance(FAIRNESS, PRO, B, COUNTRY)
                               Stance(FREE-ENTERPRISE, PRO, C, COUNTRY)
                               Stance(FREEDOM, PRO, B, COUNTRY)
                               Stance(JOBS, PRO, C, COUNTRY)
                               Stance(HEALTH, PRO, B, COUNTRY)
                               Stance(HOUSING, PRO, C, COUNTRY)
                               Stance(HUMAN-RIGHTS, PRO, C, COUNTRY)
                               Stance(INFLATION, PRO, C, COUNTRY)
                               Stance(JUSTICE, PRO, C, COUNTRY)
                               Stance(LAW-AND-ORDER, PRO, C, COUNTRY)
                               Stance(EDUCATION-RIGHTS, PRO, C, COUNTRY)
                               Stance(SOCIAL-SECURITY, PRO, C, COUNTRY)
                               Stance(UNEMPLOYMENT-INSURANCE, PRO, C, COUNTRY)
                               Stance(VOTING-RIGHTS, PRO, B, COUNTRY)
                               Stance(WOMENS-RIGHTS, PRO, C, COUNTRY)
                               Stance(FUTURE, PRO, C, COUNTRY)
Pro-Con-Stances:
                               Stance(CONTRA-AID, PRO, B, ACU)
                               Stance(DEFENSE, PRO, B, ACU)
                               Stance(BALANCED-BUDGET, PRO, B, ACU)
                               Stance(BORK, PRO, B, ACU)
                               Stance(ERA, CON, B, ACU)
                               Stance(GUN-CONTROL, CON, B, ACU)
                               Stance(LABOR, CON, C, ACU)
                               Stance(MANION, PRO, B, ACU)
                               Stance(PLANT-CLOSING, CON, B, ACU)
                               Stance(BUSSING, CON, B, ACU)
                               Stance(SOCIAL, CON, B, ACU)
                               Stance(SDI, PRO, B, ACU)
                               Stance(VOTING-RIGHTS, CON, B, ACU)
                               Stance(WOMENS-RIGHTS, CON, B, ACU)
                               Stance(TAXES, CON, B, NTU)
                               Stance(TAX-REFORM, PRO, B, NTU)
                               Stance(DEFENSE, PRO, B, NSI)
                               Stance(MX, PRO, B, NSI)
                               Stance(B-1, PRO, B, NSI)
                               Stance(EL-SALVADOR, PRO, B, NSI)
                               Stance(NUCLEAR-FREEZE, CON, C, NSI)
                               Stance(TAXES, CON, B, COC)
                               Stance(DEREGULATION, PRO, B, COC)
                               Stance(SPENDING, CON, B, COC)
                               Stance(BALANCED-BUDGET, PRO, B, COC)
                               Stance(PLANT-CLOSING, CON, B, COC)
                               Stance(LABOR, CON, B, COC)
                               Stance(CLINCH-RIVER, PRO, B, COC)
                               Stance(DEREGULATION, PRO, B, CEI)
                               Stance(FREE-ENTERPRISE, PRO, B, CEI)
                               Stance(PRIVATIZATION, PRO, B, CEI)
**********************************************************************
Bill:                          Flag Desecration
For-Stances:
                               Stance(FLAG-BURNING, CON, B, HR-2978)
                               Stance(PATRIOTISM, PRO, B, HR-2978)
Agn-Stances:
                               Stance(FREE-SPEECH, PRO, B, HR-2978)
**********************************************************************
Result:                        AGN
                               Stance(FREE-SPEECH, PRO, B, HJR-350)
Strategy:                      POPULAR-DECISION
```

### **Possible Improvements**

#### Database Manipulation

While it is completely missing all database functions included in the
original LISP program, the fact that it is running in the Python
interpreter still allows the user to view/edit the databases since they
are just Python dictionaries. For example,

``` python
bill_db["Flag Desecration"]
```

will return the associated values with the flag desecration bill.

#### NLG

Currently, there is no natural language generation. However, this does
not mean that there is no explanation. We are still able to see from the
output what strategies VOTE used to reach its conclusion and what
motives the agent has for its decision.
:::
