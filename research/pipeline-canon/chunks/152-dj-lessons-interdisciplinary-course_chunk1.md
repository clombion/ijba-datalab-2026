<!-- chunk: 1/1 | source: 152-dj-lessons-interdisciplinary-course.md | words: 5304 -->
<!-- headings: **Data Journalism: Lessons Learned While Designing an** **Interdisciplinary Service Course** -->

# **Data Journalism: Lessons Learned While Designing an** **Interdisciplinary Service Course**


Christopher Plaue
The University of Georgia
Athens, GA
plaue@uga.edu


**ABSTRACT**
We present the design and implementation of an interdisciplinary
service course on data journalism, a first-ever collaboration
between the computer science department and college of
journalism at our institution. The course covered the basics of
dataset acquisition, cleaning, and analysis, and taught key
programming and web development concepts. Students created an
online portfolio of exercises, culminating in a news story and data
visualization. The course was well received by students coming
from a variety of backgrounds. We provide recommendations for
future iterations of this course.


**Categories and Subject Descriptors**
K.3.2 [Computers and Information Science Education]: Computer
Science Education – Curriculum - Literacy.


**General Terms**
Design, Experimentation.


**Keywords**
Data journalism; non-majors; curriculum; visualization.


**1.** **INTRODUCTION**
The computer science education community has long researched
the merits of interdisciplinary coursework. Much of this research
involves combining STEM fields, such as biology, physics, or
mathematics, with computer science concepts. In addition, the
education community is active in researching the design of datacentric courses, such as data mining, database design, and data
science. Many of the courses focused on data organization and
processing target upper-level undergraduate computer science
majors.


In this article, we describe the design, implementation, and
evaluation of an experimental service course on data-driven
journalism (referred to as data journalism) [9]. This one-semester
course introduces core computing and data processing concepts to
graduate-level journalism students who have had minimal
exposure to advanced mathematical and computer science
concepts. Over a 15-week semester, the data journalism course
covered four broad topics: data acquisition, data cleaning,
programming fundamentals (variables, control structures,


Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or
distributed for profit or commercial advantage and that copies bear this notice and
the full citation on the first page. Copyrights for components of this work owned
by others than ACM must be honored. Abstracting with credit is permitted. To
copy otherwise, or republish, to post on servers or to redistribute to lists, requires
prior specific permission and/or a fee. Request permissions from
Permissions@acm.org.
_SIGCSE '15_, March 4–7, 2015, Kansas City, MO, USA
Copyright 2015 ACM 978-1-4503-2966-8/15/03...$15.00
http://dx.doi.org/10.1145/2676723.2677263


Lindsey R. Cook
U.S. News & World Report
Washington, DC
lcook@usnews.com


functions), web development (HTML/CSS), and data presentation
(UX design, JavaScript, HTML, CSS, and tools for making
interactives such as TileMill). Class time consisted of a mix of
lecture, interactive activities, self-paced lab exercises, and guest
speakers. Throughout the semester, students worked on selecting a
news story on a health topic. Students produced a final news
package with a written article and accompanying data
visualization using acquired data sets.


We conducted quizzes at the beginning and end of the semester to
gauge student performance. In addition, 55% of the class was
interviewed at the end of the semester to gain course feedback
beyond traditional course evaluations. Overall, all students
indicated that skills obtained in this course allowed them to
become more competitive in their fields and knowledgeable
talking with peers. We present lessons learned and suggestions for
course revisions for future course sections.


**2.** **RELATED WORK**
Data journalism is defined as a workflow that consists of:

 - obtaining datasets via scraping or Freedom of Information
Act Requests

 - cleaning (i.e. correcting errors and structuring data) and
manipulating large datasets (i.e. using similar fields to
combine relevant datasets)

 - producing original data analysis using statistical concepts,

 - designing graphics, visualizations, or multimedia
accompaniments

 - using statistics to tell stories and illustrate concepts in an
easy-to-understand way

 - creating media that has value for readers [9]

Thus, data journalism is inherently interdisciplinary and involves
aspects of computation as well as large data sets and processing.
In this section, we frame data journalism as a natural extension to
the existing body of literature on interdisciplinary computing
work, designing curricula involving data, barriers to enrollment,
and the importance of guest speakers.


_Role and Nature of Interdisciplinary Work_ : Computer science is
increasingly becoming interdisciplinary, and the research
community has long discussed and explored the benefits of
including interdisciplinary courses within curriculums. Formally,
Cassell defines interdisciplinary within computing fields as
“collaborative efforts involving at least two fields, with at least
one of them being computing” [4]. Several benefits are noted for
both majors and non-majors, where the former gain context for
how their technical skills can be applied in real world settings, and
the latter find the acquisition of new technical skills to extend
their craft [3]. Additionally, researchers note a correlation


between interdisciplinary computing courses and the recruitment
of more women to computing—an underrepresented population

[7]. Furthermore, interdisciplinary courses are attractive to high
caliber students [13].


We note that many of the interdisciplinary courses discussed in
the CS education community focus on combining computing
fundamentals with STEM fields, such as mathematics, physics,
biology, or chemistry. Additional work combines computing
concepts with the arts, humanities, and social sciences [e.g. 12].
Our work extends computing interdisciplinary courses by
focusing on journalism, which does not appear to have been
heavily explored in the computing education community.


_Data Processing and Science Courses:_ The explosion and
availability of data has sparked much academic research on
designing computing tools and workflows to manage and process
data. Subsequently, much work in the education community aims
on designing and implementing courses involving data
management, processing, and visualization. For instance, Sullivan
describes an introductory course designed to teach non-majors
several methods for processing large data collections [14]. Other
research outlines strategies to incorporate large data sets into
introductory-level computer science courses to provide real-world
applications [2] or simply the application of data processing to
specific domains such as healthcare, business, and security [16].


Additionally, entire curriculums are focusing on data science, a
term by Cleveland to describe an interdisciplinary expansion of
statistics involving data analysis collaborations in multiple subject
areas [5]. In their paper describing their data science degree
program, Anderson _et al_ note that at least 19 academic programs
of study exist pertaining to data science [1].


Data journalism is a natural extension to explore for
interdisciplinary course design, since it stresses the investigation
of large data sets, emphasizing communication and story telling.


_Practical Knowledge in the Classroom._ Interdisciplinary courses
provide “real-world” applications for concepts learned in class.
However, we note that many other disciplines offer some sort
formalized practical experience as part of the curriculum. For
instance, pharmacy students are required to perform clinical
rotations and primary education majors are required to student
teach. Many computing curriculums do not have formal
mechanisms for bridging the gap between the curriculum and
professional practice, but rely on (optional) uses of guest
speakers, adjunct faculty, mentors, internships, and class projects
to bridge the gap between theory and practice [8].


In journalism education, Columbia University Dean Nicholas
Lemann suggested a “teaching hospital” model in 2009, sparking
much discussion in that community [11]. In this model, student
work in a newsroom setting during class producing stories or
projects as they would in a real newsroom. These stories are
published for real audiences. The journalism curriculum at our
institution implemented this model of education both for its
broadcast journalism majors, but also in the graduate Health and
Medical Journalism program, where students submit class
assignments to be published in journalism outlets.


As the students in our course were in a program leveraging the
teaching hospital model, we were expected to incorporate aspects
of this model in the data journalism class. In particular, by using
some flipped-classroom strategies, we used class time for students
to work on their news stories and visualizations and collaborate
with each other. We encouraged, but did not require, students to


submit their stories to publication venues. We frequently had a
faculty member with extensive journalism experience sit in on
class to provide context to the real-world applications.


_Barriers to Enrollment: The Stigma of Computer Science:_ A
challenge faced when designing interdisciplinary courses is
attracting non-majors. As Davis _et al_ note, the stigma and
stereotypes of computer science courses may deter participation or
enrollment in these courses [6], particularly amongst
underrepresented populations. At our institution, for instance, the
Bachelor of Science in Computer Science major consists of
approximately 84% males, while the Bachelor of Arts in
Journalism major is about 72% female. We encountered some
barriers to enrollment that we speak more about in Section 3.2.


_Journalism: Past and Future._ As a discipline, journalism presents
several obstacles in designing interdisciplinary courses that are
not as prevalent in STEM fields, including minimal exposure to
mathematics and computer science classes. In a survey of the
journalism curriculum of five highly regarded institutions
(Northwestern, Missouri, Arizona State, University of North
Carolina, and University of Georgia), we note that all disciplines
do not require mathematics courses beyond the core requirements
of each institution. Furthermore, none of these curricula require
any computer science or general computing courses taught
through a computer science department. Within the journalism
curriculum of these schools, students are, not surprisingly, heavily
exposed to communication and story-telling concepts. In contrast,
many computer science programs, especially ABET-accredited,
only have students take one or two classes to allow students to
develop communication skills.


However, Northwestern does recommend (but does not require)
introductory level computer programming courses, an
introductory data management and information processing, and
human-computer interaction course for journalism students
interested in computational journalism [15]. Our proposed service
course presents key concepts of introductory programming, data
management, and human-computer interaction concepts.


We note evidence indicating a sharp increase in the level of
interest of data journalism skills. The National Institute for
Computer-Assisted Reporting (NICAR), a top conference on data
journalism, has seen attendance nearly triple from 335 to 997 over
2004 to 2014. Also, NICAR has seen an increase in the number of
women coders. Major news organizations, including The
Washington Post, The New York Times, and Gannett, are
expanding desks for interactive graphics, which require the
expertise of journalists with coding skills. As the Nieman
Foundation at Harvard notes, the number of data journalists
having reporting and coding skills is quite low, leading them to be
dubbed “journalism unicorns” [10].


**3.** **COURSE DESIGN**
**3.1** **History and Inception**
The Health and Medical Journalism (HMJ) graduate program at
The University of Georgia is at two-year, non-thesis Master of
Arts degree that emphasizes professional training, multimedia
skills, and research. Students in the HMJ program have access to
interdisciplinary collaborations, namely through the College of
Public Health and the Georgia Regents University Medical
Partnership. In 2012, Patricia Thomas, the director of the HMJ
program, took note at a conference that reporters who manipulated
data sets, code, and tell stories through interactive graphics were
well-received by symposium attendees. As a result, she reached


**Figure 1. Classroom setup for JOUR 7800.**


out to the computer science department to start the first-ever
collaboration between the College of Journalism and the
Department of Computer Science, housed in the College of Arts
and Sciences.

JOUR 7800 was designed in collaboration between a computer
science faculty member with expertise in information
visualization and human-computer interaction, a journalism
faculty member with extensive professional experience, and a
senior-undergraduate journalism major who was also minoring in
computer science. This undergraduate student had substantial
reporting experience and had interned with The Washington
Post’s interactivity team.
**3.2** **Course Goals**
JOUR 7800 was proposed to expose students to the process of
acquiring, cleaning, and analyzing large data sets, as well as
learning the essentials of user-centered design in order to create
effective visualizations for news stories. As a survey course, the
initial learning outcomes included:

 - using Microsoft Excel to import, clean up, and perform
initial analyses of data

 - learning the essentials of programming (via JavaScript) and
web development (via HTML, and CSS)

 - applying the Wehrend and Lewis analytical framework to
explore relationships in data

 - using investigative tools such as Google Refine

 - applying the principles of user-centered design in order to
create effective visualizations to tell a story

 - searching through government databases effectively

 - designing and executing a Freedom of Information Act
(FOIA)

 - creating an effective, interactive visualization

 - creating an interactive map

The head of the Health and Medical Journalism program at UGA
recruited students for the class via word of mouth. Since students
expressed hesitation at taking a computing concepts course, JOUR
7800 was marketed as an experimental course, and as such, would
be a pass-fail elective at the 7000 level. The course was designed
assuming no prior programming experience. Nine graduate
students enrolled in the pilot class.


**3.3** **Class Structure**
_3.3.1_ _Facility_
JOUR 7800 met for a three-hour session one day each week over
Spring 2014 semester. This format was required due to
scheduling availability of the hybrid discussion-computer
laboratory facility (Figure 1). This classroom houses 15
workstations based along the periphery of the classroom and
supports students working individually, or be seated in a
discussion-friendly format around a large center table. The
classroom was equipped with a projector.
_3.3.2_ _Student Information_
The course population was predominately female (2 male) and
approximately split between first and second year graduate
students. The majority of students had earned an undergraduate
degree in liberal arts (English, journalism or history). Three
students had science backgrounds and earned their undergraduate
degrees in biology, biochemisty and neurobiology.

At the beginning of the semester, the class completed a
questionnaire to self-rate themselves for various scenarios of
using technology (Table 1a). In large, students were strong users
of technology; most (7 of 9) had taken a general computing class
as undergraduates. No one in the class had taken a programming
class and the class was split on attitudes towards mathematics.

The second part of the questionnaire included pop-quiz questions
regarding coding concepts and Excel formulas (Table 1b). In
large, students knew basic Microsoft Excel and descriptive
statistical measures (e.g. when to use a median, mean, and
standard deviations), but largely did not understand the more
technical concepts related to HTML and while loops.
_3.3.3_ _Class Format_
The three-hour block was divided between lecture, presentations,
guest speakers, and hands-on laboratories. Students would present
their homework results at the beginning of the next class period.
_3.3.4_ _Guest Speakers_
To incorporate practical knowledge within the classroom, four
guest speakers were invited to give one-hour talks. The invited
guest speakers included:


**Table 1: Student Demographic Information**


|Part A: Self-Ratings|No. PositiveResponses|
|---|---|
|I am confident in my abilities to use asearch information to find information|9 (100.0%)|
|I have experience using photo editingsoftware to remove red eye from a digitalpicture|8 (88.9%)|
|I have set up a home wireless network|5 (55.6%)|
|**Part B: Code and Formula Questions**||
|Able to correctly identify a line of code asbeing HTML|6 (66.7%)|
|Able to identify how many times a while-loop repeats|1 (11.1%)|
|Able to correctly identify which Excelformula sums up 10 cells|7 (87.5%)|
|Able to correctly identify a relative column,absolute cell reference in Excel|4 (50.0%)|
|Able to correctly identify the hexadecimalrepresentation for the color blue|1 (11.1%)|


**Table 2: Course Activities and Associated Content**


Unit Course Activities Associated Content
Data - Search through government databases for relevant data sets Acquisition - Prepare a public information request (e.g. FOIA)


~2 weeks


- Search through government databases for relevant data sets

- Prepare a public information request (e.g. FOIA)

- Discuss the challenges associated with public information
requests


- Guest speaker with extensive experience as a journalist
submitting FOIA requests

- Guest speaker with extensive experience receiving and
providing data requested


Data Cleaning - Use Microsoft Excel and Google Refine to spot errors and - Lab on advanced formulas and pivot table usage in Microso

reformat data sets Excel

         - Know characteristics of suspicious data          - Guest speaker with domain knowledge of data security an

~ 2 weeks

integrity
Programming - Create a web page using HTML and CSS - Code Academy units on HTML, CSS, and JavaScript
& Web - Use Scalar Vector Graphics - Lecture notes on computational thinking and introducin
Fundamentals - Write a method using JavaScript to accomplish a goal, using JavaScript
~ 5 weeks selection statements, loops, output, etc.


- Weinschenk, S. _100 Things Every Designer Needs to_ Know
About People. ISBN: 978-03217675350

- Murray, S. _Interactive Data Visualizations for the Web_

- Wehrend and Lewis. “A Problem-Oriented Classification o
Visualization Techniques”, Proc. Vis 90, pp 139-143.

- Amar, et al.  “Low Level Components of Analytic Activity i
Information Visualization,” Proc. _Vis_ _05_, pp 111-117.

- Tufte, E. “Visual and Statistical Thinking: Displays of
Evidence for Making Decisions”, from _Visual Explanations_ .


Data Cleaning


- Use Microsoft Excel and Google Refine to spot errors and
reformat data sets

- Know characteristics of suspicious data


- Create a web page using HTML and CSS

- Use Scalar Vector Graphics

- Write a method using JavaScript to accomplish a goal, using
selection statements, loops, output, etc.

- Create a barchart and map using Google Fusion Tables and
embed the HTML code in a Web Page

- Create an interactive map using TileMill and Moustache

- Create wireframes of Websites and data visualizations

- Create a bar chart using D3 and JavaScript

- Use the Wehrend and Lewis analytical framework to explore and
report relationships in data

- Describe proper visualization techniques to effectively convey
data, including multi-variate and time-series data.


~ 2 weeks


- Code Academy units on HTML, CSS, and JavaScript

- Lecture notes on computational thinking and introducin
JavaScript


Data
Presentation


~ 5 Weeks


 - an expert on designing and executing Freedom of
Information Act requests

 - the Open Records Manager for the University of Georgia,
who is responsible for responding to requests for
information from the University under the State of
Georgia’s Open Records Act

 - a computer science faculty member specializing in
information and data security, discussing issues impacting
the trust of data provided

 - a data journalist from the Washington Post discussing her
background and the set-up and skill variations on interactive
graphics teams in major newsrooms
**3.4** **Software Packages**
One goal for the class was to minimize purchases of additional
software. Thus, software packages used in the course were either
freely available or were provided through the university. In
particular, JOUR 7800 used Microsoft Excel, GitHub, TileMill,
Google Refine, Google Fusion Tables, QGIS, and Data-Driven
Documents (D3).

To the best of our knowledge, there is no one textbook that covers
all of the topics of this course. In particular, general computing
textbooks cover a substantial amount of additional material that is
not covered in the class. The two required texts for the class were
Murray’s _Interactive Data Visualization for the Web_ and
Weinschenk’s _100 Things Every Designer Needs to Know About_
_People_, supplemented with selected Fair Use book chapters or
conference papers.
**3.5** **Course Content**
The general breakdown of content with associated resources is
provided in (Table 2).
_3.5.1_ _Data Acquisition_
The unit on data acquisition focused on locating, examining and
searching through government data sets. In-class exercises
primarily used datasets obtained from HealthData.gov and


FDA.gov. To provide practical knowledge about gaining data
through public information requests, we had two guest speakers
provide their expertise from drastically different viewpoints: the
journalist submitting requests and the administrator at our
institution who receives requests.
_3.5.2_ _Data Cleaning_
Data sets are often “dirty” where it may be formatted incorrectly
or inconvenient for data processing. In addition, data sets may
contain erroneous data. Our data-cleaning unit focused on using
Google Refine and advanced features of Microsoft Excel to spot
questionable data and reformat data. Specific topics included:

 - using conditional rules to highlight data that exceeds the
expected range

 - using advanced Excel formulas including VLOOKUP,
RIGHT, LEFT, SEARCH to combine and format data

 - using Excel formulas to change contents of a cell into more
useful formats (e.g. convert a date in the format of 2/13/2014
into 4 columns with a weekday, day, month, and year)

 - identifying characteristics of suspicious and/or misleading
data.

 - using Google Refine to correct spelling mistakes in handentered data
_3.5.3_ _Programming Concepts_
This unit first taught students the essentials of web development
by exposing HTML and CSS via assigned lecture notes and selfpaced tutorials. For the tutorials, we selected Codeacademy’s
interactive lessons on HTML and CSS, available free-of-charge at
http://www.codeacademy.com. The Codeacademy tutorials taught
essentials of HTML design and how to use CSS selectors and
positioning while providing guided feedback to students. In this
aspect, we “flipped” the classroom, where individual learning
occurred at home and class time was used for interactive group
activities and for “connecting the dots” between the two
disciplines. Likewise, we introduced essential programming


concepts through a mix of assigned lecture notes and
Codeacademy’s interactive lessons on JavaScript, using class time
for group activities and providing hands-on time for students to
seek assistance with concepts that they found challenging.

The following is a summary of topics covered in this unit:

  - _programming essentials_ : expressions, statements, and
variables; assignments; for-loops, while-loops, basic
I/O, functions

_flow control_ : if statements, switch statements, Boolean
expressions

  - _objects:_ object-oriented thinking

  - _HTML:_ structure, tags, tables

  - _CSS:_ selectors, layout, styles, and rules
_3.5.4_ _Data Reporting and Visualization Techniques_
This unit was taught over a period of about 5 weeks and included
readings based on Edward Tufte and Susan Weinschenck, both of
which feature design principles and recommendations. These
design principles were used in an in-class activity critiquing
visualizations that the students found. In addition, the instructor
taught user-centered design methods. As part of a motivation for
the course, Martin Wattenberg’s Baby Name Wizard was used as
an example of an interactive visualization of a large, public data
set. Students critiqued the Name Wizard along dimensions of
usability, interaction design, and journalistic value.

In addition to the basic chart capabilities in Microsoft Excel, the
following methods of data reporting were presented:

 - _Microsoft Excel Pivot Tables_, for large data set summaries

 - _Google Fusion Tables_ to create basic charts and maps of
data, providing HTML code that can be embedded into Web
pages

 - _TileMill_, an online resource that allows users to design
aesthetically pleasing interactive maps using a CSS-like class
structure, complete with libraries for geographical
landmarks, roads, political boundaries, etc.

 - _Data-Driven Documents_ _(D3),_ a JavaScript library for
creating interactive (and often strikingly beautiful)
visualizations.
**3.6** **Portfolios**
For the second half of the semester, students worked on creating
online portfolios, applying their HTML and CSS skills learned
during lab and homework. Students hosted their portfolios as Web
pages on GitHub, which provides free web hosting. During the
HTML and CSS labs, we walked students through creating a basic
web page. As students completed additional activities, they added
references to the web page. Students also were taught how to use
Git for version control purposes.

The final project in the course consisted of each student picking a
story that he or she wished to focus on, conducting background
research, acquiring and clean data, interviewing multiple sources,
conducting analysis, and turning in completed visualization with
companion story and methods. Many of these students were
investigating stories for other health and medical journalism
classes and were allowed to continue investigating the stories of
interest provided they found new data and created original content
for this class.


**4.** **EVALUATION**
We administered an electronic pop quiz towards the end of the
semester, consisting of JavaScript, HTML, CSS code questions
and concepts, and practical knowledge inventory (e.g. URLs and
resources). The class scored an average score of 75.1 on the exam
(high 92, low of 56), and we provide a summary of performance
on code-specific questions in Table 2.

To gain more insight into students’ experiences in the course, we
offered an extra credit opportunity of having students be
interviewed by the teaching assistant. Interviews consisted of a
series of open-ended questions regarding their backgrounds,
experiences in the course, any plans for using the skills gained in
the course, and recommendations for improvement of the course.
Interviews lasted for approximately 20-30 minutes. Several
themes emerged through comments.

Theme 1: Recognition of the importance for technical skills

Most students said they thought the skills learned in the course
would help them gain employment. Two students who had been
looking for work after graduation said they had already referenced
the class in interviews and were received with great enthusiasm
from potential employers. One student remarked, “... _I even_
_mentioned this when I was applying for this job. The fact that I'm_
_in this class that's all about taking numbers and turning it into_
_meaningful stories. I think that's always useful, being able to take_
_raw data and turn it into something people can connect with_ . ”
Another student remarked that, “… _. Because it is a different way_
_of thinking to sit down and figure out the best way to tell your_
_story, and to know that there are those options available, and how_
_can you go about that and either do it yourself or talk to_
_somebody else about how you want to do this_ .”

One student noted the growth of interest in data journalism:
“ _When [the program director] was first telling us about it [the_
_data journalism class] I was just smiling, because I know that this_
_is what everybody is talking about right now in journalism_ .”
Another student remarked on the potential professional benefits of
the skills obtained in the data journalism class: _“[Building data_
_visualizations] will be useful even if they don't use it on a site and_
_I write about something and I just quickly put together something_
_on say Google Fusion, [employers] would appreciate that I think_
_even if they don't use it. Like, ‘Wow they put something together,_
_maybe we could come up with something even cooler than Fusion_
_graph table’_ ”

Theme 2: Increasingly comfortable, but still reserved, with coding
principles

One student indicated her increase in being comfortable with
coding: “ _Yeah, I think I would feel more comfortable now. Really,_
_just going to this class even though I don't know that I would tell_


**Table 2: Qualitative Assessment Results**


|Col1|No. PositiveResponses|
|---|---|
|Able to identify a line of correct HTMLcode|7 (77.8%)|
|Able to correctly identify an application ofabsolute vs. relative Excel statement|6 (66.7%)|
|Able to correctly identify critical HML tags|7 (77.8%%)8 (88.9%)9 (100%)|
|Able to correctly identify loop output|5 (55.6%)|
|Able to correctly identify correct JavaScriptrelational tests|7 (77.8%)|


_people I can build you any visualization you want. I would at least_
_feel comfortable looking at a [CS] class description and kind of_
_having an idea of ‘OK. What is this class going to teach me?’ Or_
_talking to a professor and getting an idea of whether a class is_
_even within my range of accessibility. I think that definitely after_
_this class I would feel more comfortable looking at different_
_classes and being confident enough to enter something_ .”

Of the five students interviewed, four said they now felt
comfortable enough to take a computer science class from the
computer science department. While students expressed that they
initially felt comfortable in taking JOUR 7800 because it was
offered in the journalism building (“home field advantage”), they
also indicate that the class gave them the confidence and skills
necessary in order to continue studying computer science. We
note that interdisciplinary courses with journalism fields may
represent a way to draw interest in computing from women, since
most journalism programs are predominately female.
**5.** **CONCLUSIONS**
Overall, JOUR 7800 was well received by students. From the
perspective of the computer science instructor, who has a strong
background in information visualization, it was challenge to teach
a class where students did not have strong technical skills, but had
exemplarily communication and story-telling skills.

We offer recommendations for future iterations of this course
including those targeting undergraduates, as well as similarly
designed courses:

 - The class should be taught using an A-F grading scheme.
Since each lesson built upon the skills acquired each week,
an A-F grading scheme would likely encourage students to
complete their homework assignments in a timely fashion,
using graded homework deliverables. The students who
scored weakest on the assessment quiz were often behind on
their assignments while meeting other deadlines.

 - The JOUR 7800 class should change to a traditional lecture +
a lab. The three-hour meeting time was draining for students
and was not robust to unexpected weather closings or
changes in the curriculum. We often had to make
adjustments to the curriculum to adjust to students needs.

 - JOUR 7800 should become a joint JOUR/CSCI prefixed
course. A mix of journalism and computer science students
has the potential to help both populations hone their
analytical and communication skills.

 - The final project should have more milestones to help
students see progress more clearly.

 - An introductory level textbook for programming concepts
that includes interactive feedback would be beneficial. While
Codeacademy is a free resource, we ran into numerous issues
in the JavaScript modules with the interactive feedback
engine. Students often exhibited frustration while completing
these modules. One suggestion would be to use a Pearson
textbook that includes MyProgrammingLab where the
instructor can assign homework or lab assignments that
provide helpful feedback. In addition, the instructor would
have instant access to students’ performance and be better
able to gauge which subject areas students are mastering or
struggling in.
**6.** **ACKNOWLEDGEMENTS**
We especially thank Patricia Thomas and the Knight Foundation
for their exceptional and enthusiastic support of the development


of this course. We also thank the following for their contributions:
Dean Charles N. Davis, Darla Cameron, Mitch Clayton, Barry
Hollander, Kang Li, Cletus Stripling, and the ONA/AP-Google
Scholarship. Lastly, we are most appreciative for the additional
support provided by the UGA President's Venture Fund.
**7.** **REFERENCES**

[1] Anderson, P., Bowring, J., McCauley, R., Pothering, G.,
Starr, C. An undergraduate degree in data science:
curriculum and a decade of implementation experience. In
Proceedings of _SIGCSE ’14_, Atlanta, GA, pp. 145-150.

[2] Bart, A., Tilevich, E., Hal, S., Allevato, T., Shaffer, C.
Transforming introductory computer science projects via
real-time web data. In Proceedings of _SIGCSE ’14_, Atlanta,
GA., pp. 289-294.

[3] Carter, L. Ideas for adding soft skills education to service
learning an capstone courses for computer science students.
In Proceedings of _SIGCSE ’11_, Dallas, TX, pp. 517-522.

[4] Cassel, L. Interdisciplinary computing is the answer: now,
what was the question. _ACM Inroads_, 2, 1, pp. 4-6, 2011.

[5] Cleveland, W. Data science: an action plan for expanding the
technical areas of the field of statistics. _ISI Review_, 69, pp.
21-26, 2001.

[6] Davis, D., Yuen, T., Berland, M. Multiple case study of nerd
identity in a CS1 class. In Proceedings of _SIGCSE ’14_, pp.
325-330.

[7] Fisher, A, and Margolis, J. Unlocking the clubhouse: the
Carnegie Mellon experience. _SIGCSE Bulletin_, 34(2), pp.
79-83, 2002.

[8] Gibbons, T. Course guides: a model for bringing
professionals into the classroom. In Proceedings of _SIGCSE_
_’12_, Raleigh, NC, pp. 105-109.

[9] Gray, J., Chambers, L., Bounegru, L. The data journalism
handbook:.  O’Reilly Media, 2012.

[10] LaFrance, A. Columbia is launching a new post-bac program
to breed journalism unicorns. Nieman Journalism Lab.
Retrieved August 1, 2014, from:
http://www.niemanlab.org/2013/08/columbia-is-launching-anew-post-bac-program-to-breed-journalism-unicorns/

[11] Lemann, M. Journalism schools can push coverage beyond
breaking news. _Chronicle Review, Chronicle of Higher_
_Education._ November 15, 2009.

[12] Manaris, B., McCauley, R., Mazzone, M., Bares, W.
Computing in the arts: a model curriculum. In Proceedings of
_SIGCSE ’14_, Atlanta, GA, pp. 451-456.

[13] Raicu, D. and Furst, J. Enhancing undergraduate education: a
REU model for interdisciplinary research. In Proceedings of
_SIGCSE ’09_, Chattanooga, TN, pp. 468-472.

[14] Sullivan, D. A data-centric introduction to computer science
for non-majors. In Proceedings of _SIGCSE ’13_,  Denver,
CO, pp. 71-76.

[15] Undergraduate Handbook, Medill School of Journalism.
Retrieved on August 1, 2014 from
http://www.medill.northwestern.edu/_pdf/MedillUGRDHand
book1213FINAL.pdf

[16] Zheng, G., Zhang, C., Li, L. Bringing business intelligence to
healthcare informatics curriculum.  In Proceedings of
_SIGCSE ’14_, pp. 205-210.
