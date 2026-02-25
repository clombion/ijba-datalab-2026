<!-- translated -->
##### **THE** **SWISS ARMY KNIFE OF THE** **REPORTER**

Research tools
in the era of big data


Prepared by David Hidalgo and Fabiola Torres


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


##### **THE** **SWISS ARMY KNIFE OF THE** **REPORTER**

Research tools
in the era of big data


Prepared by David Hidalgo and Fabiola Torres


THE SWISS ARMY KNIFE

OF THE REPORTER


**The Swiss Army Knife of the Reporter**


© David Hidalgo and Fabiola Torres


© Asociación de Periodismo de Investigación OjoPúblico
Jr. Pablo Bermúdez Nro. 150, Int. 11-A, Urb. Santa Beatriz
(Frente Al Parque De La Reserva). Lima - Lima - Lima.


© Consejo de la Prensa Peruana
Calle Ignacio Merino Nro. 616. Lima - Lima - Miraflores

This publication was made possible with the support of the Hivos Foundation and
the International Institute for Democracy and Electoral Assistance - IDEA.


Research: Fabiola Torres and David Hidalgo
Research assistant: Karina Valencia
Design and layout: Kati Sanabria


1st edition, February 2016
Legal Deposit filed at the National Library of Peru No. 2016-01479


Print run: 500 copies


Printed by:
HAPANA CORP S.A.C.
Mza. R Lote. 43, Urb. Santa Elisa, Lima - Lima - Los Olivos
February, 2016.


table of contents


**Foreword**


**I. The journalist's new alphabet: how an encounter with**
**a hacker accelerated the reinvention of journalism.**
Security box: tools to avoid being spied on online / Guide to investigating with data / Open Refine, a software on steroids: how to detect errors among millions of data points / Online catalog: applications developed in Peru / Digital resources for hunting stories: the desktop tools for the investigative reporter.


**II. How to track crimes in a database? Twenty investigations**
**that changed the way journalism is done.**
Investigations with leaked data / Investigations with public data / 6 instruments for telling better stories: how to enrich a narrative with graphics, infographics and even audio / Investigations with constructed databases / The powerful Neo4J: or how to uncover a global fraud with nodes and edges / Digital cartography: resources for locating events and people in the exact place.


**III. The path toward a culture of innovation: the digital**
**laboratories of investigative journalism in Peru.**
Two technologists support journalism / Case study: Intensive Care. News apps or the story that never dies / Workshops for reporters: allied organizations to combine journalism and technology / Habemus or not habemus data: Transparency Law vs. Personal Data Protection Law / The existential dilemma: When is private data a matter of public interest? / The fine print: how to make an effective information request.


**5**


**11**


**39**


**69**


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


foreword


hen OjoPúblico launched online in 2014 we set out to innovate across different areas of journalism
in Peru and Latin America. From improving the publication ## of investigative content and implementing new digital narratives W

to break with traditional formats, to exploring the ideal business model while attempting to build a modern newsroom staffed by journalists and technologists. All united under the following credo: to tell quality stories that other outlets prefer to ignore, uncomfortable investigations for those in power, but relevant to public opinion and necessary for citizens.

"The Swiss Army Knife of the Reporter: research tools in the era of big data" is the first proof in editorial format of this journalistic principle. Sponsored by Hivos of the Netherlands in partnership with the Consejo de la Prensa Peruana (CPP), and written by David Hidalgo and Fabiola Torres, it is a powerful X-ray of the reporter's work in this era of information measured in terabytes. Didactic, rigorous and agile, this manual delves into the best work produced by contemporary data journalism.

In the guide you hold in your hands, you will be able to identify the elite teams of the world press as they set global trends with investigations based on the analysis and visualization of millions of documents. From the Wikileaks leak in 2010 — which triggered the first alliance between two worlds to tell an unprecedented story: Julian Assange's hacker-programmer organization and the newsroom of The Guardian, one of the world's most innovative newspapers — to the global exposés by the International Consortium of Investigative Journalists (ICIJ) on tax havens in subsequent years.

The reader of "The Swiss Army Knife of the Reporter" will tour a selection of the leading data journalism cases at the inter-

THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


national level and will learn about the digital tools most used by the world's best newsrooms to clean, analyze and visualize large quantities of information. From the best-known ones like Open Refine, created by Google more than five years ago and one of my favorites, to more complex ones like Neo4J, used by the OjoPúblico team — this year, in the middle of an election campaign — to create an unprecedented special on the financing of political parties and presidential campaigns in Peru over the past decade.

In the nearly 100-page manual — a kind of chronicle about reporters in transition to the use of technology — the reader will discover that investigative journalists can no longer work in isolation as lone wolves. The symbiosis created with code writers has taken this profession into uncharted territory in the exploration of documents that would previously have been impossible for any news outlet in the world to analyze. We also recall the painstaking work of the few national journalists who tried to work with data during the secretive 1990s, in the midst of the authoritarian government of Alberto Fujimori, through the early years of the new century.

In times when journalists write under the shadow of a media industry declared on the verge of extinction, pressed by the immediate generation of viral content and subjected to the dictatorship of easy internet traffic, "The Swiss Army Knife of the Reporter" offers ideas and solutions for discovering best practices in journalism in the digital age. If in that brief image from the film Spotlight, in which a journalist from the Boston Globe appears in front of a spreadsheet, we can glimpse the origins of investigative journalism in the era of big data, in "The Swiss Army Knife of the Reporter" we will be able to envision our present and, perhaps, our future.


_Óscar Castilla C._
Executive Director

OjoPúblico


prologue


The Swiss Army Knife of the Reporter: research tools in the era of big data" was an effort initially conceived as a practical guide to disseminate and
## promote the use of data by journalists and activists inter- "

ested in exploring, interpreting and cross-checking information available in the infinite digital universe. However, the publication you hold in your hands, prepared by David Hidalgo and Fabiola Torres — Editorial Director and Data Analysis Editor of the Asociación de Periodismo de Investigación OjoPúblico — exceeded our expectations. For the Consejo de la Prensa Peruana it represents, first and foremost, an anthology of the development and power of a journalism genre insufficiently developed in our context. But above all it is a manual that reveals how this profession, by incorporating the use of technology, has produced some of the best investigations of recent times and has ample room to raise its standards for the benefit of citizens and democratic culture.

"The Swiss Army Knife of the Reporter" enters circulation at an opportune moment: 2016 marks a turning point in the matter of citizens' right to access to public information. In the official sphere we observe the growing erosion of anti-corruption mechanisms established to advance fundamental issues such as the fight against the culture of secrecy, deeply entrenched in Peru. Likewise, there is clear non-compliance with the transparency, citizen participation and accountability commitments assumed by Peru within the framework of the Open Government Partnership.

The paradox is that this setback coincided with a shift in priorities established by the governing body in this area, the Public Management Secretariat of the Office of the Prime Minister.

THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


Since mid-2015, this entity has prioritized the implementation of the Strategy for the Opening and Reuse of Open Government Data in Peru, in the context of initiatives deployed by the Peruvian government in order to meet the standards required to join the Organisation for Economic Co-operation and Development (OECD).

Despite the time elapsed, the initiatives proposed by the State are insufficient and inconsistent.

Fortunately, the same cannot be said for other spheres of national life. The country today has a young but dynamic and growing group of activists who use available data to develop tools and produce and release information with the aim of improving the quality of citizens' lives. Examples include the increasingly frequent hackathons, competitions and challenges to reward those who develop applications across all fields. In our country, a significant part of that effort is carried out by Open Data Peru, a community that is already part of the international open data movement and celebrates Open Data Day every March.

For the Consejo de la Prensa Peruana it has been a gratifying experience to join forces with OjoPúblico in the Project for the Promotion of Open Data in Peru, through activities sponsored by the HIVOS Foundation that included, for example, organizing the seminar "Open Data Journalism: the pending agenda of the Peruvian press" in August 2015.

We have no doubt that "The Swiss Army Knife of the Reporter" will become a reference tool for journalists seeking successful precedents, suggestive ideas and effective methods for investigating relevant and unsuspected stories from databases.

For that reason, we extend our sincere thanks to the HIVOS Foundation and to International IDEA, which joined the initiative and made possible the superb edition we present today.


For our institution, this effort coincides with a new area of activities that we began in 2015 and will continue to develop in the coming years: it is the Data Journalism School project, whose objective is to train Peruvian journalists in the use of new technologies and sources of information to enrich their work and its impact on society. It is an initiative supported by IBM, OjoPúblico, Open Data Peru and the Consejo de la Prensa Peruana. We are confident that this effort will yield great and edifying results.


_Kela León Amézaga_

Executive Director
Consejo de la Prensa Peruana


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


**The digital journalism ecosystem**


hen he had already become the most wanted man on the planet, American analyst Edward Snowden sat down with a couple of journalists and calmly recorded a phrase that could be a psalm of the future. "Technology is the greatest equalizer in human history." [1] When he said it, he was hiding in a Moscow hotel room, at risk of being captured for having revealed the greatest clandestine surveillance machinery that had ever existed. Rather than a plea for help, it was a message about the true meaning of the digital revolution. "It helps us adopt new faces, enter new communities, participate in new conversations and discover who we are and who we want to become." Snowden proclaimed a fight against the powers that seek to use technology to decide if we are good or bad people. "It is not governments who should decide. It is us." His way of contributing to that fight was to become the greatest journalistic source of all time.

Snowden is the archetype of this era of global informants. By the time he came to light, soldier Bradley Manning was already imprisoned for having leaked a large number of secrets and Julian Assange was granted asylum at the Ecuadorian embassy in London. Unlike Manning, who left a trail of personal clues before the leak, and Assange, who made activism a cult of personality, Snowden only made his first move after a millimeter-precise calculation that allowed him to appear from nowhere and make statements with a certain visionary air, very well structured, about the repercussions of his leak not for American society, but for every individual on the planet. The core of that strategy was


1 PLATON. "The Most Wanted Man in the World: Edward Snowden in His Own Words – WIRED". Video. At:
https://www.youtube.com/watch?v=LgA7DoptXg0 [Viewed: November 21, 2015]


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


securing the involvement of Glenn Greenwald, a journalist known for his background as a human rights lawyer and for his coverage of the mass espionage carried out by the NSA, the intelligence agency specializing in information gathering and data analysis. The contact between the two is a microcosm of the challenges facing journalism in understanding and reporting matters of public interest in today's digital society. The most famous informant since Deep Throat not only leaked secrets to the journalist. He had to teach him technical resources before getting to work.

The first contact occurred in December 2012. Snowden sent Greenwald an email under a pseudonym that began with a defense of the security of communications between people. Always from anonymity, the author of the message explained to the investigator that using a normal email account put at risk anyone who wanted to send him sensitive information. It was no surprise — stories about internet espionage had generated headlines throughout most of the first decade of the 21st century, and in recent years had focused on the role of online communication giants in facilitating government surveillance in countries with little democratic tradition such as China or Syria. The mysterious source suggested that the journalist install an encryption program, software that allows coding everything from passwords to messages to make it impossible for a third party, agency or government to intercept communications. He even offered to lend a hand if it proved difficult. "I had been wanting to use encryption software for a long time," Greenwald writes in the book _No Place to Hide_, which recounts details of the investigation. "However, the program is complicated, especially for someone like me, not very skilled in programming and computers. It was one of those things for which you never find the right moment." [2]


2 GREENWALD, Glenn. "No Place to Hide. Edward Snowden, the NSA and the U.S. Surveillance State". Barcelona: Ediciones B, 2014.


**Tor Project**

~~https://www.torproject.org/~~

Free software for secure communications. Hides the IP address of the devices used. Allows browsing without being detected or leaving a trace of sites visited or the user's geographic location.


**Cryptocat**

~~https://crypto.cat/~~

Private instant messaging service on the web that can be used from any browser and on mobile phones.


**Mozilla Thunderbird**

~~https://www.mozilla.org/en-US/thunderbird/~~

Free, secure open-source email program for receiving, sending and storing electronic messages. Multiple email accounts can be managed with a single program.


**Enigmail**

~~www.enigmail.net~~

A Thunderbird add-on that allows sending emails protected with encrypted keys. The user retains their own key. To use Enigmail, GNU Privacy Guard (GnuPG) must also be installed.


**"Computers don't**
**make a bad reporter**
**good. What they do**
**is turn a good**
**reporter into a better one".**


**Elliot Jaspin** _, Pulitzer Prize 1979_
_for Investigative Journalism_


**SECURITY**
**BOX**

_[Tools to avoid_
_being spied on_
_online]_


The program Greenwald was referring to is called PGP, standing for _Pretty Good Privacy_. It is a popular tool among hackers and all kinds of people who live at risk of being spied on. It works with a special key that one must exchange with the sender to establish secure contact. "In essence, the program wraps emails in a protective shield that is a password made up of hundreds, even thousands, of random numbers and case-sensitive letters," Greenwald recounts in his book. Even the most advanced decryption programs of the most powerful intelligence agencies would take years to break that protection. Although Greenwald knew its benefits from having written about cases like Wikileaks or Anonymous, he had not incorporated it into his tools and was not prepared to devote time to it.

Days later, the anonymous sender wrote to him again with a series of instructions for installing the program. He even offered to put him in contact with an expert who would help him get started. Greenwald offered to do it, but didn't lift a finger. He had a heavy workload and nothing guaranteed that making the effort would yield a great story in return. Weeks later, the unknown figure persisted in making things easy for him with a video tutorial entitled: "PGP for journalists." Not even that got Greenwald moving. Nor would anything in the following two months. By then, the informant had sought another path to continue with his plans: he looked for documentary filmmaker Laura Poitras for the simple reason that she did use encryption programs. It was Poitras who first learned the dimensions of the source and his secrets. "That's how close I came to missing the most important and transcendental national security leaks in American history," Greenwald would later acknowledge. His luck was that Snowden insisted on working with him.

Some time later, after a series of security measures that included creating new encrypted emails, more keys and the help


of a computer security expert as an intermediary, Laura Poitras herself commissioned this allied technologist to teach Greenwald a still less-known system called _Tails_ (acronym for _The Amnesic Incognito Live System_), which can only be used from a portable device. [3] The expert prepared a special version for the reporter on a blue USB drive and sent it by post to Brazil. It is the

accessory that appears connected to Greenwald's computer

while he interviews Snowden in a Hong Kong hotel room

for the documentary _Citizenfour_. That is how the story began. In his current Twitter profile, Glenn Greenwald notes that he has his PGP public key and its corresponding fingerprint available, a shorter number of just 40 digits that facilitates confirmation of the key. It is also a fingerprint of the learning that his encounter with Snowden represented in a fragment of history in which technology is no longer an accessory but part of the habitat in which human experience unfolds.

Since the most impactful leak of the century, there has been the idea that one day journalists will have to imitate astronomers to capture certainties in the expanding digital universe. Not all of us will write about the espionage of Western secret services or about certain governments' plans to capture the internet — although we should keep it on the agenda — but just as valuable is having the instruments to understand this era of data. Even before the September 11 attacks, it was already known that the largest American intelligence agency was intercepting 1.7 billion communications per day. With Snowden's revelations it became known that in 2013 the same agency managed to capture one trillion metadata that allow us to know everything from what people search for on the internet to what their hobbies are and even what their behavior will be in the near future. That same year, an American professor


3 LEE, Micah. "Ed Snowden taught me to smuggle secrets past incredible danger. Now I teach you". The
Intercept. At: https://theintercept.com/2014/10/28/smuggling-snowden-secrets/ [Viewed: November 22, 2015]


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


calculated that the volume of information stored in the world was 1,200 exabytes, equivalent to covering the entire surface of the United States with books about fifty-two times. [4] There is almost no process that cannot be quantified. How do we comprehend a quantity of data that, put on CDs, would form a tower reaching the Moon?

In essence, a change in the technical capacities and operational thinking of the investigative journalist is required. The classic metaphor of the craft would have to shift from having a toolbox to managing a laboratory kit. "Journalists don't need to learn to program, but they do need to develop a big data mindset, so that they understand that data contains stories that may go untold," says

as the experimental techniques that had changed the way of telling good stories. The new craft includes mastering enough concepts to think of a newsroom as a robotics workshop: encrypt, scrape, refine, visualize. A metalanguage to define how we handle data.

It is not the apps or the software that define journalism's new moment, but the possibility they offer us in _big data_. In this too we resemble astronomers: we face a universe so large that it demands improving our instruments from one day to the next.


4 SCHÖNBERGER, Viktor and Kenneth CUKIER. "Big data, la revolución de los datos masivos". Madrid: Turner, 2013.
5 GONZALO, Marilín. "Los datos masivos (o big data) son el nuevo oro". In eldiario.es (Spain), August 5, 2013. At: http://www.eldiario.es/turing/Big-data_0_161334397.html [Viewed: November 22, 2015]


**"We need to humanize**
**and personalize large**
**datasets in a way that**
**does not distort the**
**complexity or scale of**
**the issues being dealt with".**


**Paul Bradshaw** _, author of the Online_
_Journalism Blog._


**BIG (REALLY BIG) DATA**

At the beginning of the 21st century, American economist Steven Levitt imagined an economics of the strange. It was about finding surprising truths based on the way data was analyzed. Levitt did this by taking to the extreme the logic of asking questions: Why do drug dealers continue to live with their mothers? or what is more dangerous, a gun or a swimming pool? In one of his essays he presented readers with the case of a couple who refuses to send their daughter to a neighbor's house whose father keeps a gun at home, but lets her go to another neighbor who has a pool in the backyard. The question was which decision was correct for the child's safety. Levitt found that according to the statistics, there is one child death for every 11,000 swimming pools, which in a country with 6 million pools means an average of 550 children drowned per year. By contrast, one child dies from a gunshot per 1.5 million weapons. In a country with 200 million guns, the proportion is 175 children killed by gunshot per year. Translation: a girl is statistically more likely to die in a swimming pool than playing with her neighbor's father's gun. If human beings tend to modify their behavior based on small-scale samples, what happens when information overflows our capacity to store it? "The era of big data challenges the way we live and interact with the world," explain Schönberger and Cukier.

Their favorite case was when the world's most famous search engine saved the United States from a global epidemic. When bird flu arrived in that country, health systems collapsed due to lack of timely information to develop strategies. The alert system was too slow to understand the spread of the disease. Around that time, the scientific journal _Nature_ published an article in which Google engineers demonstrated they had found a way to predict the spread of the common flu. The method consisted of combining search trends about symptoms with infor-

THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


**Cleaning**
**and context**


There may be errors of several types: duplicate records, incomplete fields, misspelled words, invisible characters or blank spaces. You need tools to identify and resolve those problems. This is called cleaning the data.

Is the database complete? How many lines of information does it have? Can I clean it with Excel or Open Refine? In what cases should I do it by hand? In what cases should I use higher-capacity managers such as MongoDB?

Do I know and understand all the terms, variables and acronyms that appear in the databases? Are they the same as those used in similar databases? Do the criteria point to the meaning of the question I want to answer, or do I need to see that same data in reverse?


**Verification**


The investigative journalist must apply traditional methodology: going to the necessary places, interviewing the people involved, reviewing new documents to detect the strengths and weaknesses of the database.

Do the data reflect the real condition of the people? Has anything changed in the subject's life — in their health, economic stability, legal situation or their connections?

Does this affect the meaning of the finding? Does it confirm its relevance, accentuate it or relativize it?

What expert can I consult to validate the cross-referencing methodology? Is it possible that the finding is correct but admits more than one interpretation?


**Presentation**


From the outset one must think about the most efficient way to present the findings. There are libraries like d3js.org and software repositories like Github with examples that one can adapt to one's needs.

Is a visualization or an application better? Which one contributes to the meaning of the story?

How should the user experience be? What should the graphic or tool generate in the reader? What elements of my application or visualization make it necessary for the user?

Is it responsive? Will it look good on mobile phones and tablets? Can it be shared? Can it be embedded?


GUIDE
FOR
INVESTIGATING
WITH DATA


Journalist Paul
Bradshaw, author of the
Online Journalism
Blog, proposes that journalistic
work with databases
comprises five stages:
collection, cleaning,
analysis, verification
and presentation of
findings. We can use that
sequence to set up the
following exercise when
starting a project.


**Data**
**collection**


You need to know the formats of the files containing the information and the tools for collecting them. Big data can be obtained through a script, a simple program that allows downloading information in an automated way. This process is known as scraping.

Are there databases on the topic? How and for what purpose were they created? Are they on an official website or do I need to make a freedom of information request?

If the database is on a website, is it downloadable or do I need to scrape it?

What is the best format (Excel, CSV, Json) for requesting a copy of those databases? If the information is in PDF or JPG, how do I convert it to Excel?

If I need to build a new database, what variables should I include and what will I be able to demonstrate?


**Cross-referencing and analysis**


At this stage, the value of your findings depends on the quality of the questions and on the combination of two or more records to find revealing coincidences.

Do my databases have a common concept or code that allows me to cross-reference them: national ID, tax ID, full names?

Does cross-referencing the databases reveal trends, patterns, evolutionary processes over a given period? In what context?

Or, on the contrary, does it reveal atypical behavior? In what context?


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


mation about the historical evolution of the disease. "Others had already tried to do this with internet search terms, but no one had as much data, processing capacity and statistical know-how as Google," the experts write. Just validating the key words or phrases required recreating 450 million

different mathematical models. The result was a group of

45 terms that showed the relationship between the searches of

potential patients and the evolution of the flu. The key detail was that, unlike the traditional method — which could take weeks to retrieve information — Google developed software that achieved that precision in real time.

What can journalists learn from this era in which an algorithm can predict the moment when millions of people will wipe their noses? "_Big data_ refers to things that can be done on a large scale [...] to extract new insights or create new forms of value, in such a way as to transform markets, organizations, the relationships between citizens and governments," say Schönberger and Cukier. Since psychiatrist Carl Jung deciphered how human beings dream, no operation for finding stories in the abstract world has been so powerful.

"Data is sacred," says an old motto of the English newspaper _The Guardian_. Now it is the principle guiding the work of its former digital editor Simon Rogers — the journalist who turned statistics into a Mondrian painting. "Most of the time we act as the bridge between the data (and those desperate to explain it) and the real-world people trying to understand what a story is really about," says Rogers in _Facts are Sacred_, a guide to turning data into visual concepts. In 2011, the team led by Rogers — who now heads Google's digital lab — explained England's civil administrative apparatus as if it were a cluster of colored balloons. At a glance, readers were able to understand a bureaucratic structure that originally


**OPEN REFINE,**
**A SOFTWARE ON**
**STEROIDS**

_[How to detect_
_errors among_
_millions of data points]_


Anyone who works with spreadsheets knows there are **four common problems:** spelling errors, names or

words written in multiple forms, invisible characters or blank spaces. They don't seem complicated for someone using a personal Excel file, but they are a nightmare when handling databases with millions of rows. In these cases, **the most useful tool is Open Refine,** an open-source tool that **allows cleaning and organizing data in just a few steps**. Take as an example a registry of gold-exporting companies. It is possible that the name of a company has been entered in several ways (OrogoldSA, OrogoldS.A. and OroGold). An initial analysis will count them as different companies. **Open Refine finds the matches and allows editing them in a single action** to make them uniform.

In addition, **if an error is made when editing the database, it is possible to revert to the previous state** using the option that shows the history of changes made.
This program can be downloaded from http://openrefine.org/download.html, is compatible with any browser and **is available for Windows, Mac and Linux**. It also allows transforming files of different extensions such as XLS, CSV, JSON, XML, TSV and Google spreadsheets.
**It is a very necessary resource in the investigative reporter's toolbox.** Some journalists usually describe it as "the Excel version on steroids."


OF THE REPORTER OF THE REPORTER


**Open Spending**


**https://openspending.org/**

Website that tracks government spending around the world and presents it in different forms of visualization.


**Investigative Dashboard**


**https://www.investigativedashboard.org/**


###### TEN DATABASES FOR TRACKING MONEY AND OTHER LEADS

A suggestive selection gathered by **OjoPúblico** among attendees at the Global Investigative Journalism Conference 2015.


**CIJ Offshore Leaks Database**


**http://offshoreleaks.icij.org/search**


**OpenCorporates**


**https://opencorporates.com/**

Contains information about 80 million companies and 90 million directors in more than 100 countries. You can search by company name, address and names of directors.


**Personas**
**de interés**


**https://www.personadeinteres.org**

Provides access to judicial files, property records and intelligence reports on people connected to organized crime, drug trafficking, corruption, etc. Contains information about those prosecuted for drug trafficking in Peru.


**Search Systems**


**http://publicrecords.searchsystems.net**

Portal specializing in people searches. Contains more than 55,000 databases organized by date of birth, date of death, marriage, licenses, stocks, mortgages, among other subdivisions.


**FlightAware**


**https://es.flightaware.com/**

A platform for tracking flights and their status worldwide. Offers a downloadable app for mobile phones. Allows searching by airline name, flight number, route and aircraft registration number.


**Marine Traffic**


**http://www.marinetraffic.com**

A real-time updated database that allows tracking the location of any type of vessel or ship, as well as departures, arrivals and routes.


THE SWISS ARMY KNIFE


Contains data on more than 100,000 companies and funds stored in tax havens. It is part of an archive of 2.5 million documents leaked to the International Consortium of Investigative Journalists (ICIJ). THE SWISS ARMY KNIFE


Allows searching for information on shareholders, directors and financial reports of companies around the world. There are links to more than 450 online databases in 120 countries. Platform built by the Organized Crime and Corruption Reporting Project (OCCRP).


Investigation (ICIJ). THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE

OF THE REPORTER OF THE REPORTER


was a list of more than 200,000 names, their positions and salaries. The analysis revealed that at least 90 bureaucrats earned more than the British Prime Minister.

On another occasion, journalists David Leigh and Nick Davies, from _The Guardian_'s investigative team, obtained from Wikileaks a file with detailed information about all military incidents recorded by the American army during the war in Afghanistan. It had been created by soldiers tasked with monitoring operations. The first step was to receive the encrypted information by email. The problem was reviewing the data and finding the story: the file contained a spreadsheet with 91,201 rows. It was a volume too overwhelming to be analyzed by the re-

"gold in a mountain of data," Leigh would say. [6]

By that point, the newspaper had experience with large government-released databases and had even created internal search tools that allowed journalists to search. This time they did the same. The data were filtered according to an order that included date, time, description of the attacks, number of victims and the coordinates where they had occurred. At that point a team of visualizers, headed by Simon Rogers, joined the work. "The Wikileaks project was producing new types of data, so they needed to be extracted with new types of journalism," Leigh wrote alongside Luke Harding, another of the reporters who participated in the investigation. [7] The result was


6 LEIGH, David and Luke HARDING. "Wikileaks y Assange". Barcelona: Ediciones Deusto, 2011.
7 Op. cit.


**"I never begin a**
**process without developing**
**a plan. I use my own**
**matrix, which**
**helps us aim at**
**specific questions".**


**Ginna Morelo** _, Data Editor of_
_El Tiempo (Colombia)_


a map that showed for the first time the evolution of six years of attacks in that country: it then confirmed that the bloody streak had left more civilian than military deaths. [8]

"The Wikileaks story is a combination of the two things: traditional journalistic knowledge and the power of technology, united to tell a mind-blowing story," wrote the duo that reconstructed the case.

Even with these demonstrations of the potential of data, until recently many journalists — even investigative ones — tended to think of technology as an alien language. The mere idea of digging into an Excel file with more than a thousand rows discouraged the traditional hunter of confidential documents. "You don't have to be a programmer," Rogers notes in his book. "You can become a coding virtuoso if you wish, but the main task is to think about data as a journalist rather than as an analyst." No digital tool will replace the exercise of asking what relevant information the data can provide, or what would happen if one mixed one database with another, in the manner of the original economist of the strange. What one cannot do on one's own can be done with allies from the parallel universe.


**THE CODE OF FORCE**

It was only a matter of time before someone invented a space to integrate two ways of looking at information. The idea sprang from a coincidence between a young correspondent and two veteran journalists. Burt Herman was an Associated Press reporter who had spent twelve years traveling to sensitive parts of the world, from Korea and some countries of the former Soviet Union to the turbulent Iraq and Afghanistan. Between 2008 and 2009, Herman left the agency and opted for a fellowship to explore journalistic innovations at Stanford University. From there, in the digital vortex of Silicon Valley, he began organizing meetings of people interested in


8 ROGERS, Simon. "Facts are sacred". London: Faber and Faber Limited, 2013.


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


journalism and technology. Around the same time, Aron Pilhofer, editor of _The New York Times_, and Rich Gordon, professor at Northwestern University, launched from Massachusetts a call to form a network that would develop digital applications and tools to process information. Both initiatives coincided on one concept: uniting the hacks — a term alluding to journalists' ability to produce texts in series — with the hackers, who are prolific writers of source code, the set of instructions that makes machines run. [9]

Such a cross of languages would make for a _Star Wars_ episode: it is as if two alien races — each with respect to the other, at least — had reached an agreement to fulfill a mission. The only possible way is to exchange knowledge: journalists learn from hackers the jargon and principles governing cyberspace and in exchange they train them to use their skills to make sense of information. The proof is in Burt Herman's own experience. While on his fellowship, he came into contact with Belgian programmer Xavier Damman and together they set out to create a tool that would harness the informative potential of social networks. The result was Storify, an application that allows gathering photos, videos, tweets and links to tell a story that can be embedded in any website. "The way to make sense of social media is through human curation with the help of technology," Herman has said.

This alliance is already generating changes in global journalism: the HacksHackers community has chapters in cities on every continent. In each place it has facilitated the creation of tools that allow processing large quantities of information. At the beginning of 2014, for example, the chapter in Rosario, Argentina, gathered data from the Ministry of Justice, police reports and press articles and built an interactive map where one can see the


9 HIDALGO, David. "Periodistas buscan hackers (de los buenos)". At: http://hhlima.info/node/8 [Viewed:
November 25, 2015]


**"When I design a**
**spreadsheet for a story**
**I think about the goals: what**
**I want to know and what**
**the possible patterns in**
**the data are".**


**Lise Olsen** _, investigative reporter for_
_the Houston Chronicle._


**ONLINE**
**CATALOG**


_[Journalistic_
_applications_
_developed_
_by OjoPúblico]_


**Fondos de Papel**

~~http://fondosdepapel.ojo-publico.com/~~

Interactive report offering an unprecedented profile of the private financing of Peru's political parties and their presidential candidates in the 2006, 2011 and 2016 campaigns.


**Billetón electoral**

~~http://ojo-publico.com/sites/apps/billeton-electoral/~~

Application that makes economic inequality visible by comparing users' income with those of the main Peruvian presidential candidates in the 2016 elections.


**Congreso Airlines**

~~http://ojo-publico.com/sites/apps/congreso-airlines/~~

Application showing the international trips of 113 Peruvian congresspeople and the expenses incurred by the Legislative Branch to cover them between 2011 and 2015.


**Cuentas Juradas**

~~http://cuentasjuradas.ojo-publico.com/~~

Platform showing the evolution of assets declared between 2003 and 2014 by 38 Lima mayors seeking re-election and 23 former mayors who wanted to return to power in the 2014 municipal elections.


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


exact point at which each homicide occurred the previous year. "The purpose of the project was to create a platform that would allow demonstrating, through data visualization, the increase in social violence in the city," wrote Ezequiel Clerici, one of the organizers of that community. Earlier, in 2011, the Buenos Aires chapter created an application that allowed following the results of the presidential elections in real time: simply mark on a map the place of interest and you get the corresponding data. In each case the final axiom of the information age is fulfilled: the problem is not the changes in the journalist's methods, but what we understand by doing journalism.

As is to be expected in the era of big data, the potential is enormous. In June 2014, several chapters in Latin America joined in a regional hackathon to generate tools that would allow journalists to monitor the use of public funds. The activity was named with the expression that has always guided the best journalism: "Follow the money." The Lima chapter gathered more than fifty members who locked themselves for twelve hours in the auditorium of a technology-focused teaching institute. The session involved forming mixed teams of journalists and developers to analyze hard data from various databases and convert it into news. In essence, it was about finding the sexy side of an Excel table.

At the end of the afternoon, the community presented seven projects ranging from analysis of how funds from the Ministry of the Environment are invested to a calculation of the money the State allocates to the Catholic Church. One of the most interesting tools was an application that allowed searches of databases and specialized websites to identify links between government officials and organized crime and their possible connection to public funds. Another was an application that allowed systematizing data on the State's main suppliers and how much money they had billed the country. Had it not been for that meeting, which functioned as a


**THE VOLUME**
**OF DATA**
**IN THE DIGITAL**
**UNIVERSE**


**1 Petabyte (1 PB)**
All the information
that Google processed
in 2010.


**1.2 Zettabytes (1.2 ZB)**
Total amount of information
that existed in the digital
universe in 2010.


**Five Megabytes**
**(5 MB)** All the
works of William


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


workshop for the curious, the information would remain buried in disconnected files. "This group brings together all these people: those who are working to help people make sense of their world," says a statement on the original HacksHackers page.


**THE ALLIES**

One October afternoon in 2010, Costa Rican engineer Rigoberto Carvajal decided to quit his job at a software development corporation to join journalism. Through a friend he had learned that the newspaper La Nación was looking for a programmer for its Investigative Unit. Carvajal applied out of curiosity to find out how someone like him could be useful for uncovering secrets. After a first interview, he was convinced it was the right place. "I studied programming because I really enjoy solving problems, and from journalism you can do it for nobler ends than increasing a company's profits," says Carvajal, who is now one of the database experts at the International Consortium of Investigative Journalists (ICIJ). [10]

The project for which he had been recruited was a challenge for a Latin American newspaper at that time: gathering all the public databases of his country to analyze them, gain new knowledge and find relevant stories to investigate. The computer specialists on the team had to have the same audacity and passion for truth as the journalists. In the job interview, Carvajal mentioned that on one occasion he managed to locate a person of whom he only had the name, thanks to his resourcefulness in contacting people who gave him the right information. His first test demonstrated that he retained the skill. When asked to identify Shakira's properties in the US, the programmer searched for the singer's real name and immediately tracked it through property records until he achieved his objective. Over time, Rigoberto Carvajal — a science fiction enthusiast — transformed into a kind of _Spock_,


10 Interview with Rigoberto Carvajal.


the character between human and alien from _Star Trek_: a hybrid between computing and journalism.

"Going back to what I used to do in programming, on the commercial side, would be like going back to the dark side of the force," he says, alluding to another of his favorite films.

The same spirit animated British programmer Dan O'Huiginn when he set out to download all of Panama's public register in 2008 for an investigation into arms traffickers. Until then, the official website only allowed searches based on company names.

That was a limitation for the work

of reporters tracking suspicious figures.

O'Huiginn extracted data from more than 300,000 companies, organized the information, and used it to create a site that accepted searches based on individuals' names. [11] The programmer usually explains that this work had nothing to do with illegal piracy. He simply used his technical skills to automate data collection. "I don't mind being called a hacker in the literal sense," he said when Panamanian media were surprised that an unknown individual, from a terminal on another continent, had achieved such access. His essence, he explained, is that of "a person who enjoys exploring the details of programmable systems and how to extend their capabilities, unlike most users who prefer to learn only the minimum necessary." [12]

The site created by Dan O'Huiginn, which receives 2,000 daily visits, allowed investigative journalists from many countries to verify whether officials under suspicion of illicit enrichment and corruption had properties secretly registered in Panama. Using this tool, in 2011 reporter Khadija Ismayilova demonstrated that the daughters of Azerbaijan's president, Ilham Aliyev, ran a telecommunications company through _offshore_ entities.


11 http://ohuiginn.net/panama/ [Viewed: November 22, 2015]
12 "El Registro Público solicitó que eliminara mi web". In Diario La Estrella (Panama), October 6, 2013.
At: http://laestrella.com.pa/panama/nacional/registro-publico-solicito-eliminara/23502395. [Viewed:
November 22, 2015]


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


That corporation had more than one and a half million subscribers, covered 80 percent of the country's territory, and at the time was the sole provider of 3G services. The site also allowed identification of the _offshore_ companies of former Egyptian president Hosni Mubarak, and furthermore provided evidence that connected five people to the murder of the former governor of Panama Province, Darío Fernández. All were convicted.

Since 2010, programmer O'Huiginn decided to devote himself entirely to working with investigative journalists. He has been a fellow of the _African Network of Centers for Investigative Reporting_ and collaborated on projects of the _Organized Crime and Corruption Reporting Project_ (OCCRP). Today he lives in Germany and works on the Openoil project, the first open data map of oil concessions in 18 Middle Eastern countries.

"If done right, people really have a lot of appetite for seeing data," says Scott Klein, a reference figure in investigative data journalism. [13] "It is enough to see how many people understand — and love — incredibly sophisticated and impenetrable sports statistics." If the average reader is prepared to read sports pages that look like stock market reports, why wouldn't they find utility in a tool that examines the health system or the quality of the water they drink in their locality?

Klein is editor of _ProPublica_, one of the most innovative media outlets in the United States. In 2010 he was given the mission of building a project that seemed to come from a Silicon Valley laboratory: the news apps department. It was a team made up of reporters and technologists who would work together to do journalism using software. One of their most impactful projects was _Dollars for Docs_, which revealed payments totaling 258 million dollars to doctors who promoted the products of seven pharmaceutical compa-


13 Cited in HOWARD, Alexander B. "El arte y la ciencia del periodismo de datos". Tow Center for Digital
Journalism (Translation by La Nación DATA).


**DIGITAL**
**RESOURCES**
**FOR HUNTING**
**STORIES**

_[Desktop tools for_
_the investigative_
_reporter]_


**ScraperWiki**

~~https://scraperwiki.com/~~

Online platform that allows downloading information from the web and grouping it in an orderly fashion in a database (Excel, CSV, etc.). Offers the possibility for anyone to create their own script according to their interests.


**DocumentCloud**

~~https://www.documentcloud.org/~~

Platform for managing documents. Extracts text from an image using OCR software. Allows highlighting data, making annotations and organizing them in easily accessible links. Helps with searching by topic, embedding documents, and placing them in a public catalog. Accessible upon application.


**Visual Investigative Scenarios (VIS)**

~~https://vis.occrp.org/~~

A tool of special interest to investigative journalists. Allows establishing relationships between people and organizations and attaching documents that prove those relationships.


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


nies among their patients. The team took advantage of a law requiring laboratories to disclose information about money given to doctors for commissions, lunches and sponsorship of conventions, among other purposes. All the documents had been published on the pharmaceutical companies' websites but in formats that were difficult to handle. The _ProPublica_ programmers developed a script — a small

who had received money from the laboratories, how much and for what reason.

Klein often refers to his team of five people as "journalistic programmers who think like reporters." By this he means they have the skills to handle digital tools but at the same time have the instinct to detect a good story in a mountain of data. "Some have said that journalists with skills for developing _software_, or vice versa, are unicorns, rare to find. That is not true, you can develop

rigorous and related disciplines that expand the frontiers of knowledge. "Investigative journalism is the research and development department of the profession," wrote Brant Houston, co-founder of the _Global Investigative Journalism Network_. [15]

Perhaps the image that best reflects this moment is the one put forward by Evan Smith, co-founder of the Texas Tribune. Smith says that today's journalist must be like a Swiss Army knife. [16] The idea


14 FALLAS, Hassell. "Simplificar es clave para crear aplicaciones de noticias". Blog La Data Cuenta. At: http://
hasselfallas.com/2014/09/11/simplificar-es-clave-para-crear-aplicaciones-de-noticias/ [Viewed: November 25,
2015].
15 Cited in: KAPLAN, David. "Periodismo de Investigación Global: Estrategias para su Financiamiento".
Center for International Media Assistance, 2013.
16 "Journalists today have to be swiss army knives". Interview with Evan Smith in The future of news. At:


of keeping separate competencies is an anachronism comparable to those who in their time resisted swapping the typewriter for the computer. The editor illustrates this with a scene he still has to contend with despite his outlet's efforts to engage in multimedia projects. "People come to me and say: 'I want to be a writer.' What kind? 'I just want to write, nothing more than write.' Don't you want to shoot a video with your phone, edit it and post it? 'No.' Don't you want to record audio on your phone, edit it and post it? 'No.' Don't you want to do anything in basic HTML? 'No.' Don't you want to handle social networks? 'No.' Then here's what you're going to do: go to Home Depot, buy lots of wood, build a time machine and go back to _Esquire_ in 1964, because that was the last time someone had that job." The Swiss Army knife metaphor is not rhetorical: the reporter may not use all those tools every day, but the idea is that they are there when needed.


http://futureof.news/episodes/evan-smith-2/?utm_campaign=refdotfonesmithvideo2&utm_source=Twitter&utm_medium=esmith2_jrsch_hd_flw [Viewed: November 25, 2015].


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


**The dimension of what is investigated**


ince Wikileaks dynamited the global industry of secrets, investigative journalism has been caught up in a data fever. It is now possible to track corruption across several continents, detect companies and individuals S

seeking to evade taxes worldwide, or understand the international movements of organized crime. In September 2011, Australian journalist Gerard Ryle, of the International Consortium of Investigative Journalists (ICIJ), received a hard drive with 2.5 million files. Two computer engineers turned that flood into a reliable database. From there, intensive reporting was conducted that revealed the operations of more than 122,000 companies and 130,000 people in the shadows of the global financial system.

The finding drew praise but also warnings. "Investigative journalism must not be confused with what has been labeled 'leaks journalism'," says David Kaplan. This observation is a missile aimed at the heart of the debate about the encounter between journalism and technology. Are documents obtained by hacking valid? How do we make them tell us what we truly need to know? Spreadsheets must be seen as forensic records of reality: they offer details, but the truth requires work. "The basic skills of investigative journalists," Kaplan notes, "are similar to those of the most qualified prosecutors and police, field anthropologists and private investigators: the use of primary sources, verification of evidence, first-hand witness interviews, and following the trails of people, documents, and money."

The best examples of recent investigative journalism have also been generated by access to public information or the construction of new databases, with information compiled from different sources, to answer a question no one had asked before. Here are some notable examples.


~~**Lux Leaks**~~

~~_ICIJ_~~
~~**28,000**~~

~~files~~


~~**Swiss Leaks**~~

~~_ICIJ_~~
~~**60,000**~~

~~files~~


~~**Medicare**~~
~~**Unmasked**~~
~~_The Wall Street Journal_~~


~~**10,000,000**~~


~~files~~


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


The leak was 160 times larger than the diplomatic documents previously released by Wikileaks. The ICIJ had the help of computer experts including Sebastian Mondial from Germany; Duncan Campbell and Matthew Flower from England; Costa Rican Rigoberto Carvajal and Maltese Matthew Caruana. They performed data cleaning and organization using the OpenRefine tool. The program dtSearch helped them track names among 260 gigabytes of data. And with the Nuix software they obtained ~~**Impact**~~ connections of keywords included in email attachments from various individuals, The case shook Europe and provoked high-level resignations, without having to open the documents. They also used such as those of France's Economy Minister, the free software Talend Open Studio to integrate and or- Jérôme Cahuzac, and the deputy spokesperson of the Parliament ganize data in relationship graphs. of Mongolia, Bayartsogt Sangajav, for hiding Swiss bank accounts. The programmers managed to reconstruct the software Judicial investigations were opened against officials and businesspeople system of the companies providing offshore creation services. in the Philippines, India, Greece and South Korea. Various social movements This crucial task paved the way for journalists to begin their promoted campaigns against tax havens. In investigations, since they were able to navigate completely February 2015, the ICIJ was recognized with the structured files and find out who was behind the George Polk Award, one of the top awards in the US in companies created, who their partners, intermedi- the Business Reporting category. aries and beneficiaries were.
The hard drive analysis detected more than 100,000 com-

such as the Virgin Islands, Hong Kong, Cayman Islands, among http://offshoreleaks.icij.org/ others. The documents revealed the involvement of 12,000 intermediary agents and 130,000 people from 170 countries.
In June 2013, the ICIJ and the Investigative Unit of the Costa Rican newspaper La Nación, directed by Giannina Segnini, launched the Offshore Leaks Database application, which allows searching by name or by country. - The US Securities and Exchange Commission uses the Nuix program to monitor emails seized from corporations when it suspects illicit behavior.


**INVESTIGATIONS**


~~**Offshore Leaks**~~

~~**Outlet**~~

**International Consortium of**
**Investigative Journalists**
**(ICIJ)**

It was a global effort led by the International Consortium of Investigative Journalists (ICIJ) with the collaboration of The Guardian, BBC, Le Monde, The Washington Post and around thirty other outlets. It involved the work of 112 reporters from 56 countries.


~~Date: April 2013~~


~~**Revelation**~~


Politicians, aristocrats, bankers and criminals from various countries used tax havens to create companies and trusts to conceal their assets or capital, and in many cases to avoid paying taxes. The list includes the president of Azerbaijan, Ilham Aliyev, and his family; Jean-Jacques Augier, treasurer of French president François Hollande's electoral campaign; Spanish baroness Carmen Thyssen-Bornemisza, who used offshore channels to purchase works of art; and María Imelda Marcos, daughter of former Filipino dictator Ferdinand Marcos.


~~**Data analysis**~~


**WITH LEAKED**
**DATA**


few processes reveal the peculiarities of the era as starkly as

data leaks. To the new forms of interconnection with sources through specialized software programs, one must add the challenge of understanding

quantities of information that could bury any enthusiasm if we did not have the help of programmers. These cases demonstrate it.


The case shook Europe and provoked high-level resignations, such as those of France's Economy Minister, Jérôme Cahuzac, and the deputy spokesperson of the Parliament of Mongolia, Bayartsogt Sangajav, for hiding Swiss bank accounts. Judicial investigations were opened against officials and businesspeople in the Philippines, India, Greece and South Korea. Various social movements promoted campaigns against tax havens. In February 2015, the ICIJ was recognized with the George Polk Award, one of the top awards in the US in the Business Reporting category.


~~**Impact**~~


http://www.icij.org/offshore
http://offshoreleaks.icij.org/


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


~~**Lux Leaks**~~

~~**Outlet**~~

**International**
**Consortium of**
**Investigative**
**Journalists**
**(ICIJ)**

Another collaborative project led by the ICIJ. It involved 80 reporters from 26 countries.


~~Date: November 2014~~


~~**Revelation**~~


More than 340 companies, including Apple, JP Morgan, FedEx, Amazon and Pepsi, signed secret tax deals with Luxembourg to evade taxes. Those deals, approved between 2002 and 2010, represented billions of dollars in tax revenue lost for the countries where these companies obtained profits. The deals were signed when the current Prime Minister of Luxembourg, Jean-Claude Juncker, was Finance Minister of the duchy.


THE SWISS ARMY KNIFE


~~**Impact**~~


In February 2015, the Swiss Prosecutor's Office opened a criminal investigation against HSBC bank for aggravated money laundering. In the United Kingdom, the tax collection agency recovered 236 million dollars from some of the 3,600 British people identified as customers of HSBC's Geneva branch, but only opened proceedings against one person. France initiated 103 judicial actions against the same number of individuals.
In June 2015, the ICIJ received the Data Journalism Award in the Best Investigation of the Year category.


~~**Data analysis**~~


The ICIJ accessed a 4.4 gigabyte archive containing 28,000 pages of documents. For six months, 80 journalists joined a secure communication platform called Enterprise, implemented by the ICIJ to organize the analysis of the content. This tool allowed sharing everything from interview transcripts and photos to confidential material. "It was the closest thing to a global newsroom," said Marina Walker, deputy director of the consortium. Each reporter reviewed highly complex financial documents related to companies in their country. The ICIJ received advice from finance and taxation specialists. In parallel to the journalists' investigation, the ICIJ formed a team of reporters and computer engineers that developed a publicly searchable database.


~~**Impact**~~


The European Commission investigated whether Luxembourg's practices constituted a tax system tailored to large corporations in detriment of community law.
The ICIJ received the George Polk Award in the Business Reporting category, and the Data Journalism Award for Best Investigation of 2015, jointly with Swiss Leaks.


~~**Swiss Leaks**~~

~~**Outlet**~~

**ICIJ, The**
**Guardian, CBS,**
**Le Monde,**
**Süddeutsche**
**Zeitung and The**
**Washington Post**

Third international collaborative ICIJ project, in collaboration with The Guardian, CBS, Le Monde, Süddeutsche Zeitung and The Washington Post. It included 154 journalists from 47 countries.


~~Date: February 2015~~


~~**Revelation**~~


The Swiss branch of HSBC Bank established a tax evasion scheme that helped more than 100,000 wealthy clients from 203 countries worldwide conceal their money to avoid paying taxes between 2005 and 2007. Among the beneficiaries were members of royalty, politicians, celebrities, drug traffickers and businesspeople with accounts that, together, exceeded 100 billion dollars.


~~**Data analysis**~~


Based on secret bank account records of HSBC bank customers stolen by the computer technician and former employee of its Swiss branch, Hervé Falciani. The hard drive contained 2.5 million files. In early 2014, the French newspaper Le Monde gained access to the data and passed them to the ICIJ to design a way to investigate them. The first step was to reconstruct the HSBC customer database from the available flat Excel files. Next, relationships were drawn between names and countries. The Talend software was then used to transfer the original database to the Neo4j graph database, which allows organizing relationships. The Linkurious tool facilitated visualization and the analysis process. The participating reporters communicated through the Voyager platform — created with an open-source software called Oxwall — which allows everything from building thematic forums to sharing files. The database gave rise to a diagram of 275,000 nodes with 400,000 relationships among them.


http://www.icij.org/project/swiss-leaks


http://www.icij.org/project/luxembourg-leaks


OF THE REPORTER OF THE REPORTER


~~**Data analysis:**~~


In early 2014, American journalist Sasha Chavkin observed that the reports of the World Bank's Ombudsman, which oversees the organization's activities, contained dozens of complaints from communities displaced by projects financed by the bank in various developing countries. Chavkin downloaded more than 6,600 World Bank documents to build a record of projects, loan beneficiaries and complaints. The information on cases between 2004 and 2013 was incomplete. To verify it, sources within the organization, former officials and experts were sought. The data allowed identifying a pattern: the World Bank and the International Finance Corporation — its investment arm in the private sector — did not respect their policies to protect those who may be harmed by the projects it finances. It even gave loans to governments and companies accused of violating human rights. The reporters, who traveled to countries including South Sudan, Ethiopia, Guatemala and Peru, communicated via the Odyssey platform.


http://www.icij.org/project/world-bank


**INVESTIGATIONS**

**WITH PUBLIC**
**DATA**


seventy countries in the world — fourteen

in Latin America and
the Caribbean — have public information access laws, according to
the Regional Alliance for Free Expression and Information. This scenario represents an advantage

for investigative journalism:

it is possible to track the management of the State or how corporate power influences its decisions and how this impacts citizens' lives.


~~**Trapped by**~~
~~**Development**~~

_Evicted and Abandoned:_
_The World Bank's Broken Promise to the Poor_


~~**Outlet**~~

**The Huffington Post, The**
**Guardian, The Ground Truth**
**Project, The Investigative**
**Fund**

Joint work with outlets and organizations including the Huffington Post, The Guardian, the Ground Truth Project and the Investigative Fund. It involved 50 journalists from 21 countries.


~~Date: April 2015~~


~~**Revelation:**~~


More than three million vulnerable people were displaced from the areas where they lived by nearly one thousand projects financed by the World Bank in 124 countries between 2004 and 2013.


~~**Impact:**~~


The World Bank announced a plan to improve supervision of development projects and prevent bad practices that cause displacement.
The Online News Association recognized this investigation with the Online Journalism Award in the Innovative Investigative Journalism category.


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


~~**Congress members**~~
~~**back**~~
~~**legislation**~~
~~**that could**~~
~~**benefit**~~
~~**themselves**~~
~~**and their**~~
~~**relatives**~~

_Congress members back_
_legislation that could benefit_
_themselves, relatives_


~~**Outlet**~~

**The Washington**
**Post (USA)**


~~Date: October 2012~~


~~**Revelation**~~


Seventy-three American legislators approved rules that affected their investments or benefited their relatives because they were not required to disclose their potential conflicts of interest.


~~**Data analysis**~~


The team assembled a database in Excel using financial information forms and public records from all 535 members of the US Senate. It then compared lawmakers' personal investments with reports of their activities monitored by LegiStorm, a non-profit watchdog group. The information was also cross-referenced with reports from the White House Office of Management and Budget. Cases were detected such as that of a legislator who facilitated approval of tax exemptions for horse owners and then bought seven thoroughbred horses. Another sponsored a bill that benefited the natural gas company in which his wife was a shareholder.


~~**Impact**~~


Congress debated its code of ethical conduct and opened investigations into senators with clear conflicts of interest.


https://goo.gl/9WbZbT


~~**Missed signs,**~~
~~**fatal**~~
~~**consequences**~~


_Missed signs,_
_fatal consequences_


~~**Outlet**~~

**Austin American-**
**Statesman**
**(USA)**


~~Date: January 2015~~


~~**Revelation**~~


Between 2010 and 2014, the Texas Department of Family and Protective Services had a failed oversight system that allowed the deaths of 655 children at the hands of relatives

or caregivers. Officials did not take the necessary actions to protect them.


user-friendly database management tool based on Microsoft SQL Server. This tool established that child protective service employees had visited the victims several times but had not taken account of warning signs. The six-month project included reconstructing events through interviews, document cross-checking and home visits.


~~**Impact**~~


The Texas Department of Family and Protective Services reformulated its child abuse investigation system and opened an investigation into 50 employees for various offenses.
The Austin American-Statesman website won the Online Journalism Awards 2015 prize from the University of Florida in the Investigative Data Journalism category.


THE SWISS ARMY KNIFE


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER http://projects.statesman.com/news/cps-missed-signs/ OF THE REPORTER


http://projects.statesman.com/news/cps-missed-signs/


~~**In the**~~
~~**cobbler's**~~
~~**house,**~~
~~**wooden**~~
~~**knives**~~

~~**Outlet**~~

**La Nación**
**(Costa Rica)**


~~Date: April 2012~~


~~**Revelation**~~


Half of the ministers of Costa Rican president Laura Chinchilla undervalued their properties to pay less tax between 2009 and 2010.


~~**Data analysis**~~


The team, made up of two reporters and two computer engineers, organized an Excel database with information on the ministers' properties drawn from public records, the values they had declared in tax forms submitted to the municipalities where their properties are located, and the standardized values as calculated by the Ministry of Finance. The first two databases were downloaded by one of the engineers. The third was built using the arithmetic operations needed to calculate property values. When cross-referencing them, they identified the offending officials. The investigation extended to the ministers' family members, because in several cases properties were registered in the names of spouses. The series was published in the print edition of La Nación with an infographic of the revelations.


~~**Impact**~~


The property values of all implicated public officials were updated. In 2013, the Instituto de Prensa y Sociedad (IPYS) awarded the team the Latin American Investigative Journalism Prize for its skilled use of computing to boost accountability reporting.


# **6**


**INSTRUMENTS**
**FOR TELLING**
**BETTER STORIES**


_[How to enrich a narrative with graphics,_
_infographics and even audio]_


**3. Infogr.am:**


~~https://infogr.am/~~


Develops infographics online. Offers templates that allow displaying data in bars, circles and fever lines. You can enter information in its own format or import files in Excel or CSV. It has a free version and a paid Premium version. Graphs can be shared via Facebook, Twitter and Pinterest.


**4. Tableau Public:**


~~https://public.tableau.com/~~


Converts data from a spreadsheet into interactive graphics (maps, tables, bars) and creates filters so users can make queries and get personalized results. No programming knowledge is required to use this tool.


**5. StoryMapJS:**


~~http://storymap.knightlab.com/~~


Creates stories based on locations identified on a map. Allows inserting videos, tweets, texts or images to display them as a gallery associated with each selected location. Information is also entered in a Google spreadsheet.


**6. Soundcite:**


~~https://soundcite.knightlab.com/~~


Attaches sounds to a word or phrase in a text. The MP3 file is uploaded to SoundCloud, then selected through Soundcite and the desired segment is adjusted. A code will be generated for inserting it into the chosen phrase, enriching the reading experience with sound.


**1. Datawrapper:**


~~https://datawrapper.de/~~


Allows selecting data from a spreadsheet and converting it into explanatory charts and maps with customized color types and fonts. Offers options for pie charts, fever line charts and bar charts.


**2. TimelineJS:**


~~http://timeline.knightlab.com/~~


Used for creating interactive timelines with photos, videos and hyperlinks. No account is needed. Dates, texts and URLs are entered in a Google spreadsheet and the tool organizes them for display in a very attractive format.


http://goo.gl/16ndl8


THE SWISS ARMY KNIFE


OF THE REPORTER OF THE REPORTER


~~**Data analysis**~~


Data editor at the CPI, David Donald, began an analysis of 350 million mortgage applications approved from 1994 through 2007. The information had previously been collected from public documents of the Home Mortgage Disclosure Act and organized into spreadsheets by the National Institute for Computer-Assisted Reporting (NICAR). The analysis made it possible to identify that the majority of high-risk loans totaling more than one trillion dollars were granted between 2005 and 2007. This allowed establishing who the main lenders were. A team of reporters collaborated with profiles of the lenders and information was included about the campaign contributions of the companies involved to members of the US Congress. To visualize the location of each property subject to a subprime loan, heat maps were created using Palantir Government Software, which offers a powerful visual analysis tool used in both academic projects and disaster management and intelligence programs.


http://goo.gl/cVX1ee


**INVESTIGATIONS**

**WITH CONSTRUCTED**
**DATABASES**


In recent years, major cases were born from investigative projects with databases that the journalists themselves built. Here are thirteen experiences that may inspire the development of new topics.


~~**Who's Behind the**~~
~~**Financial Meltdown?**~~


_Who's Behind the Financial Meltdown?_


~~**Outlet or organization**~~

**The Center for Public**
**Integrity (USA)**


~~Date: May 2009~~


~~**Revelation**~~


American corporations Lehman Brothers, Merrill Lynch, JP Morgan & Co., Citigroup, Goldman Sachs & Co. and Swiss bank Credit Suisse First Boston were part of the business that generated the so-called real estate bubble that broke the financial system. Those corporations owned 21 of the 25 largest companies in the subprime industry that granted high-risk residential mortgage loans, which triggered the 2008 economic crisis, and then benefited from the financial bailout.


~~**Impact:**~~


The journalistic series contributed to the US Congress forming an investigative commission whose conclusions were that the disaster could have been avoided and that the crisis was the result of regulatory failures, poor corporate governance and Wall Street's irresponsible risk-taking.


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


~~**The Secret**~~
~~**Diaries of**~~
~~**Paraná**~~


_Diários Secretos_


~~**Outlet**~~

**Gazeta do Povo**
**in collaboration**
**with RPCTV**
**Paraná (Brazil)**


~~Date: March 2010~~


~~**Revelation**~~


Between 2006 and 2009, the Legislative Assembly of Paraná (Brazil) concealed a scheme of diverting public funds that included hiring ghost employees, inflated service costs, nepotism cases and other offenses. The embezzlement reportedly reached 400 million dollars.


~~**Data analysis**~~


Journalists James Alberti, Katia Brembatti, Karlos Kohlbach and Gabriel Tabatcheik compiled the legal gazettes of the Paraná Legislative Assembly published between 1998 and 2009, several of which were not available in the assembly's own archives. They manually digitized the contents of 724 official bulletins to build a database in Excel showing staff hiring and budget management detailed in the gazettes. This allowed them to identify around twenty ghost employees, including dead people and children. The journalistic team also detected that relatives of legislators and children of magistrates had been employed. The data analysis was completed with testimonies and documentary sources. They then made all the official gazettes — including those missing from the Assembly's archives — publicly searchable.


~~**Impact**~~


From publication through March 2015, fourteen officials and former employees of the Paraná Legislative Assembly were sentenced to prison for embezzlement and other offenses.
"The Secret Diaries of Paraná" won the Global Shining Light Award and the Latin American Prize for Investigative Journalism in 2011.


~~**Data analysis**~~


This investigative series began with the hypothesis that there might be abuses in the awarding of Avancemos scholarships, a subsidy program designed to encourage more than 167,000 young people to continue their studies. The team, led by Giannina Segnini, accessed the beneficiaries database, supplemented it with their parents' names, and cross-referenced it with family income and assets. An initial cross-reference revealed that 75 scholarship recipients had parents with salaries between two thousand and nine thousand dollars. However, the finding took a turn when reporters went in person to look for the beneficiaries: they turned out to be children of people with economic resources who had been abandoned and now lived in poverty with a relative. The investigation lasted three months and led to a new, more revealing story than the initial hypothesis: the State was subsidizing the education of young people abandoned by parents with assets. Three developers, three designers and 4 journalists worked on this project. It was accompanied by a multimedia special.


~~**Impact**~~


The investigation received a special mention in the Second Regional Prize for Journalism, Poverty and Human Rights in Central America in 2011.
The Mixed Social Aid Institute (IMAS) changed the criteria for awarding Avancemos program scholarships to selection by academic level.


~~**The faces of**~~
~~**abandonment**~~

~~**Outlet**~~

**La Nación**
**(Costa Rica)**


~~Date: February 2011~~


~~**Revelation**~~


The official Avancemos educational subsidy program covers the studies of young people abandoned by parents with high economic resources.


http://goo.gl/BfMkQC


THE SWISS ARMY KNIFE


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER http://goo.gl/0qXwNF OF THE REPORTER


http://goo.gl/0qXwNF


~~**Doctors without**~~
~~**oversight:**~~
~~**the owners**~~
~~**of public health**~~
~~**in Chile**~~

~~**Outlet**~~

**CIPER (Centro**
**de Investigación**
**Periodística)**


~~Date: September 2010~~


~~**Revelation**~~


A year-long follow-up of five Chilean hospitals demonstrated that they were not monitoring doctors' attendance or the use they made of health service infrastructure for personal gain and to the detriment of patients.


~~**Data analysis**~~


At the end of July 2009, CIPER requested attendance records for doctors at five hospitals in Santiago, Chile. To obtain them it had to overcome several obstacles, as some hospitals refused to provide the information and others provided it incompletely. The team managed to access more than 35,000 attendance records. After converting the information to a spreadsheet, it cross-referenced it with the schedules the professionals are required to keep in outpatient clinics and in their private practices or at private clinics. In parallel, it visited the selected hospitals to observe schedule compliance in the field. This confirmed that several doctors were using the infrastructure to see their private patients. It also showed that they were not fulfilling the hours stipulated in their contracts.


~~**Impact**~~


Seven months after this investigation was published, the Comptroller General of the Republic of Chile published a report confirming the violations by doctors at 13 hospitals across the country.
The investigative series received an honorable mention at the Latin American Prize for Investigative Journalism presented in 2011.


http://ciperchile.cl/multimedia/medicos-son-control/


~~**Dollars for**~~
~~**Doctors**~~


_Dollars for docs_


~~**Outlet**~~

**ProPublica in**
**partnership with**
**The Boston**
**Globe, Consumer**
**Reports,**
**NPR, Chicago**
**Tribune and Public**
**Broadcasting**
**Service (PBS).**


~~Date: October 2010~~


~~**Revelation**~~


Between 2009 and 2010, seven pharmaceutical companies made individual payments of more than one hundred thousand dollars to 17,000 doctors to promote and prescribe their medications in the USA.


~~**Data analysis**~~


The seven pharmaceutical companies had published this information on their websites, but in formats that were difficult to analyze (PDF and JPG). Two journalists and a developer downloaded and organized it in an Excel file that could be broken down into categories such as: consulting fees, meals, travel and gifts. For the first time a complete picture was obtained of payments to doctors by companies representing 36% of the pharmaceutical industry in the USA. The team used the Open Refine tool to clean and standardize the names of the doctors who received payments. Then it cross-referenced them with public databases of medical licenses and disciplinary records. ProPublica presented this investigation with a journalistic application in which anyone can search the name of their doctor to find out whether they received payments to promote a particular product. Three years later, the database was updated to document payments totaling four billion dollars to 681,432 doctors by 1,630 pharmaceutical companies or medical product manufacturers.


~~**Impact**~~


In 2012, a law was enacted making it mandatory to publish gifts and marketing payments to doctors in the USA.
More than 125 news organizations — such as the Boston Globe and the Chicago Tribune — conducted investigations based on the tool.


https://projects.propublica.org/docdollars/


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


~~**Terrorists**~~
~~**for the FBI**~~


_Terrorists for the FBI_


~~**Outlet**~~

**Mother Jones**
**(USA)**


~~Date: August 2011~~


~~**Revelation**~~


FBI informants fabricated evidence to incriminate suspects of threatening US security in order to claim rewards of 100,000 dollars as part of the counterterrorism campaign.


~~**Data analysis:**~~


Journalist Trevor Aaronson examined more than 500 cases of people accused of terrorism and found that nearly half had centered on the participation of an FBI informant. Aaronson combined data extracted from court records across different states, FBI documents, and interviews with agents and defense lawyers. He spent months working with an assistant to build a database. Initially he used Excel and the MySQL database manager, which helps build relational databases. Then the team used the Drupal language to build an online search tool.


~~**Impact:**~~


The FBI investigated agents accused of fabricating cases, while some of the involved informants were subjected to judicial proceedings.
The investigation won the Data Journalism Award 2012 in the Data-Driven Investigation category.


http://goo.gl/hKem0p


~~**Data analysis:**~~


Following alerts from several doctors, two journalists sought all available records in Washington to track the number and circumstances of deaths linked to this narcotic. Through freedom of information requests, they obtained four databases: death certificate records, the forensic notes of each doctor, clinical profiles of the patients and the costs of their methadone treatments at Washington hospitals. In parallel, they compiled additional data on the socioeconomic profile of the deceased. The files were reviewed and annotated with DocumentCloud. This information was transferred to Excel, then the Access software was used — which handles larger data volumes — along with ArcGIS software for mapping. To present the findings, Google Fusion Tables, Tableau, Final Cut Pro and Adobe were used.


~~**Impact:**~~


Washington authorities sent an alert to more than 1,000 pharmacists and 17,000 healthcare professionals about the risks of methadone.
In January 2012, they sponsored a program that instructed doctors to limit methadone to cases of last therapeutic resort.
The investigation received the 2012 Pulitzer Prize in the Investigative Journalism category. That same year it was awarded the Data Journalism Award.


~~**Methadone and**~~
~~**the politics of**~~
~~**pain**~~


_Methadone and the politics_
_of pain_


~~**Outlet**~~

**The Seattle**
**Times (USA)**


~~Date: December 2011~~


~~**Revelation:**~~


The Medicaid program, aimed at low-income people, dispensed the narcotic methadone to its patients to cut costs on medication purchases without taking into account the health risks caused by this painkiller. As a consequence, 2,173 people died between 2003 and 2011.


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER http://goo.gl/YoQcDs OF THE REPORTER


http://goo.gl/YoQcDs


THE SWISS ARMY KNIFE


~~**Senate**~~
~~**Expenses**~~

~~**Outlet**~~

**La Nación**
**(Argentina)**


~~Date: February 2013~~


~~**Revelation:**~~


The team discovered irregular contracting, travel and other expenses totaling more than one million dollars by the Argentine Senate between 2010 and 2012. The Senate's vice president, Amado Boudou, purchased luxury furniture for his office and filed per diem claims for overlapping trips.


~~**Data analysis:**~~


An anonymous informant sent La Nación an email containing a photograph of Argentine Senate vice president Amado Boudou's office with a luxurious Italian-imported table. This put the journalistic team to work downloading 33,000 documents from Senate contracting records available on its official website. The Omnipage 18 software was used to convert PDFs into searchable files. The information was transferred to an Excel file that included expenses on furniture, travel payments and security staff costs, among others. Tableau Public was used to explore the data and create interactive graphics. To handle some of the PDFs, the collaborative platform VozData was developed, which allowed volunteer participation to classify information in a pre-established format.


~~**Impact:**~~


The Prosecutor's Office opened an investigation into the Senate vice president's trips. The matter was covered on television, radio and other newspapers.
The work won the Data Journalism Award 2013 in the Data-Driven Investigation (Big Media) category, organized by the Global Editors Network (GEN).


http://www.lanacion.com.ar/gastos-en-el-senado-t49163


Mar Cabra, editor of the ICIJ's Research and Data Unit, **learned to use everything from spreadsheets**
**to sophisticated software** to follow the trail of fiscal and corporate corruption in millions of files that, on the surface, had no direct connection to each other. For the Swiss Leaks series she used a tool called Neo4j, which allows **identifying connections between large amounts of data and displaying them in graphs**. "The connections were crucial for identifying who was doing business with whom," Cabra said at the Global Investigative Journalism Conference held in October 2015 in Lillehammer, Norway.
**Instead of tables, this tool uses nodes and edges,** which **makes the reading of relationships between data more intuitive**.


This function allowed the **OjoPúblico** team to untangle the trail of party financing in Peru's 2016 electoral campaign, by cross-referencing 16 databases and analyzing 3 million records. "This system allowed us to understand, analyze and cross-reference the databases simultaneously," explains Nelly Luna, the journalist in charge of the investigation. **What would previously have taken several years took just six months with the tool.**


**THE POWERFUL**
**NEO4J**

_[Or how to uncover_
_a global fraud_
_with circles and_
_lines]_


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


~~**Foreclosed**~~
~~**Homes**~~


_Homes for the Taking. Liens,_
_losses and profiteers_


~~**Outlet**~~

**The Washington**
**Post**
**(USA)**


~~Date: September 2013~~


~~**Revelation**~~


About 200 people in Washington DC, mostly senior citizens, lost their homes in irregular foreclosures due to tax debts of less than one thousand dollars. These cases evidenced abuses in the district's tax lien program that allowed real estate companies to seize the properties.


http://goo.gl/ZGtrUP


~~**Data analysis**~~


The investigation was based on analysis of foreclosure documents between 2005 and 2013 available from the Office of Tax and Revenue, the Superior Court and the US Census Bureau. The team assembled a database of 200 senior citizen homeowners who lost their homes in auctions conducted by the district's tax lien program due to overdue payments of less than one thousand dollars. In the majority of cases, the properties were sold to real estate companies even though the original owners had finally paid their debts. When reporters sought out the victims they obtained more evidence of the abuses committed. One of those affected was dying of cancer and owed 1,025 dollars in taxes. Another was 95 years old and suffered from Alzheimer's disease, having forgotten to pay a balance of just 44 dollars. Documents were examined with DocumentCloud and data were analyzed with spreadsheets. The findings were processed using the Mapbox platform and the open-source code library Leaflet.js, which allows creating mobile-friendly maps.


~~**Impact**~~


A dozen senators requested that the government investigate tax programs with the aim of protecting vulnerable homeowners from losing their properties due to small tax debts.
The investigation won the Data Journalism Award 2014 in the Data-Driven Investigation category.


~~**Data analysis**~~


Reporter Chris Hamby set out to build a database with information from X-ray examinations performed on more than 1,500 miners at Johns Hopkins Hospital from 2000 to 2013. The coal companies had denied them healthcare and social benefit payments based on diagnoses signed by a single doctor, who ruled out that they had black lung disease. The miners took their cases to court. The journalist accessed those case files to build a second database on the mining companies' legal strategies, reports from other doctors, and judicial verdicts. Hamby spent months reading and processing the information in spreadsheets. In this way he was able to identify cases and patterns that evidenced a system designed to deny benefits to miners.


~~**Impact**~~


Johns Hopkins Hospital suspended and then dismissed the doctor responsible for the black lung detection program. In addition, US senators drafted bills to reform the benefits system for coal industry miners.
The investigation won the 2014 Pulitzer Prize in the Investigative Journalism category.


~~**Breathless and**~~
~~**Burdened**~~


_Breathless and Burdened_


~~**Outlet**~~

**Center for**
**Public Integrity (USA) and ABC News**
**Investigative Unit**


~~Date: October 2013~~


~~**Revelation**~~


Doctors and lawyers in the service of the coal industry have blocked aid to miners affected by black lung disease.


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER http://goo.gl/ZPZ9HE OF THE REPORTER


http://goo.gl/ZPZ9HE


THE SWISS ARMY KNIFE


~~**Data analysis:**~~


In May 2014, after a five-year legal battle, the WSJ obtained the release by the US Government of nearly 10 million records of Medicare contracts and disbursements to its medical service providers, kept secret since 1979. They then accessed a second database purchased from the CMS (Centers for Medicare and Medicaid Services) agency, which included payment claim records from providers over a 6-year period. Cross-referencing the information allowed building a database that served to detect cases of fraud, cost overruns and abuses in a program that spends more than 60 billion dollars annually. Journalists and data experts used the C# programming language to convert the records into relational tables and developed algorithms to make connections with the data. They then imported the information to the Microsoft SQL database manager. With that data they produced interactive graphics, rankings and a search platform for payments to each doctor.


~~**Impact:**~~


Winner of the 2015 Pulitzer Prize in the Investigative Journalism category.


~~**Medicare**~~
~~**Unmasked**~~


_Medicare Unmasked_


~~**Outlet**~~

**The Wall Street**
**Journal**
**(USA)**


~~Date: April 2014~~


~~**Revelation:**~~


Medicare, the healthcare assistance program for people over 65 and young people with serious illnesses, made annual payments of 60 billion dollars to more than 880,000 doctors, ambulance services and laboratories, several of which were cases of fraud, waste and abuse.


**DIGITAL**
**CARTOGRAPHY**

_[Resources for_
_locating events_
_and people in the_
_exact place]_


**OpenStreetMap**

~~http://www.openstreetmap.org/~~

Collaborative project to create free, editable maps. Geographic data captured with mobile GPS devices and other sources can be used.


**My Maps**

~~https://www.google.com/maps/d/u/0/~~

Tool for creating maps through Google Maps. Easy to use, share and embed thanks to the code it provides. The only requirement is having a Google account.


**MapBox**

~~http://mapbox.com/tour/~~

Website that allows creating customized maps simply. Uses free software.


**InfoAmazonia**

~~http://infoamazonia.org/~~

Website with environmental maps of the nine countries of the Amazon region.


**Geocommons**

~~http://geocommons.com/~~

Free program for creating maps with multiple layers. Allows using the geolocated information of other users and sharing it.


http://graphics.wsj.com/medicare-billing/


THE SWISS ARMY KNIFE


~~**Aresep**~~
~~**raises**~~
~~**gasoline and**~~
~~**diesel prices**~~
~~**to lower asphalt**~~
~~**and gas prices**~~

~~**Outlet**~~

**La Nación**
**(Costa Rica)**


~~Date: December 2014~~


~~**Revelation**~~


In 2008, Costa Rica's Public Services Regulatory Authority (Aresep) secretly approved a price calculation formula that made diesel and gasoline more expensive in order to lower gas and asphalt tariffs. This cross-subsidy benefited cement companies at the expense of thousands of consumers.


~~**Data analysis:**~~


Journalists Hassel Fallas and Mercedes Agüero manually created an Excel database with information extracted from 59 ordinary and extraordinary price resolutions issued by Aresep between June 2009 and September 2014. The components of the price formula were broken down to determine how the operating costs of Costa Rica's national oil refinery (Recope) were included in fuel tariffs. With the help of specialists, it was found that Aresep had established a cross-subsidy: it assigned a product a cost above the real one in order to reduce the price of another. In this case, the cost of diesel and gasoline was inflated to lower that of asphalt and gas. The team had to build five versions of the database before finding the correct one.


~~**Impact**~~


Aresep modified the formula for calculating fuel prices in order to eliminate the hidden costs in the methodology it had used since 2008.
The investigation was a finalist at the Data Journalism Awards 2015, organized by GEN, in the Investigation of the Year category.


http://goo.gl/aNriTd


~~**Data analysis**~~


Over a nine-month investigation, New York Times reporter Eric Lipton documented how corporate lobbying had penetrated attorneys general to twist their decisions in favor of the interests of 21 companies.
Lipton obtained, through legal requests, 8,000 pages of emails from the public accounts of the attorneys general and built a database in a spreadsheet with information extracted from this correspondence that evidenced the relationships between the officials and the companies.
He then documented the gifts and contributions that attorneys general receive from the corporations they investigate. That information was supplemented with photographs and trips the reporter made to academic conferences for attorneys general sponsored by those companies.
To complete his report, Lipton showed that company contributions to associations of Democratic and Republican attorneys general had quadrupled in four years.


~~**Impact**~~


The publications generated investigations in four states and the Senate proposed a bill prohibiting officials from receiving gifts or financial contributions.
Courting Favor was awarded the 2015 Pulitzer Prize in the Investigative Journalism category and the IRE Award in the Print/Online-Large category.


http://goo.gl/oKMMKg


~~**Courting**~~
~~**Favor**~~


_Courting Favor_


~~**Outlet**~~

**The New York**
**Times**
**(USA)**


~~Date: October 2014~~


~~**Revelation**~~


More than 20 corporations, including DirecTV, Pfizer, Coca-Cola, Google and Citigroup, made gifts and contributions to attorneys general in 12 states to influence their decisions.


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


**The data community in Peru**


~~**OjoPúblico**~~
~~Innovation laboratory~~
~~focused on investigative journalism~~


~~_http://odpe.org/_~~
~~**Convoca.pe**~~
~~Digital investigative journalism~~
~~site that brings together~~
~~reporters, data analysts~~

~~and developers.~~
~~_http:/convoca.pe/_~~


~~**HacksHackers**~~

~~**Lima**~~
~~Peruvian chapter of the~~


~~_http://hackspace.pe/_~~


efore journalism made friends with statistics, journalist Liz Mineo found a way to track corruption through numerical tables. At the end of B

1997, as Peru was shaken by frequent allegations about mismanagement by the government of the day, Mineo turned her attention to public works for prevention against the El Niño phenomenon, a cyclical process of climate disturbances that tends to trigger disasters at various points in the country. The reporter asked a basic question: How had the widely publicized public budget of one hundred million soles for those works been spent? The problem was that the regime of the time was not known for its transparency. Nor did the freedom of information law yet exist. In fact, the National Institute of Civil Defense (Indeci), the agency responsible for administering the money and making the contracts, was controlled by military officers linked to the feared presidential adviser, Vladimiro Montesinos, who had created an almost police-state atmosphere within the government. When she made her first inquiries, Mineo found that all information on public works had been declared classified. She then embarked on a pioneering experience of forensic information analysis for journalistic purposes: she built a database to look for patterns that would allow uncovering the hidden information.

In a first stage, the El Comercio reporter sought internal sources. After persistent persuasion, an Indeci official agreed to cooperate: he gave her an 80-page file with information on the works and contractors. It was the best raw material she could obtain. "I was afraid he would lose heart if I asked him for the


LA NAVAJA SUIZA LA NAVAJA SUIZA
OF THE REPORTER OF THE REPORTER


documents on a floppy disk," Mineo recalls. The second step was to transfer all the information to an Excel table, which included 293 works in 21 departments of Peru, totaling 100 million soles, carried out by 61 companies. "There were too many numbers to calculate by hand or with a calculator," she recalls. [1]

The result was a compendium of irregularities: the first filter revealed that many of the supposed prevention works were concentrated in departments that were not in the vulnerable area affected by the El Niño phenomenon. When she investigated who the shareholders were of the companies that received the contracts, Mineo identified that 12 of the 61 companies were owned by fellow officers of the Indeci chief, General Homero Nureña. Moreover, one of the companies was registered in the name of his private secretary and another in the name of his nephew. A third of them were companies created just months before receiving the contracts, and some even after having been awarded them.

The third stage was verification. Mineo, with the support of the newspaper's correspondents, visited the investment sites and discovered unfinished works and even some that had never existed. She thus confirmed that General Nureña had channeled funds to Cajamarca, his hometown, despite the fact that this department was not affected by El Niño, and that he had ordered the construction of a primary school there that he later named after his mother. Without having made that field visit in person, the findings might not have been as conclusive.

The experience marked a change in the journalist's operational capacities. At a time when the government reserved for itself the right to manage public information, Liz Mineo combined traditional journalistic techniques with the incipient use of data-thinking resources to conduct a compelling investigation. The case became a series of 15 articles in


1 Personal interview with Liz Mineo.


###### **8**

Latin American media outlets have
journalistic teams that include
hackers for mass data analysis.
In Peru, OjoPúblico and
Convoca work with programmers.


El Comercio. Some time later, General Nureña was convicted and sentenced to prison for embezzlement.

For a long time, this pioneering experience remained an isolated case in the Peruvian journalistic landscape. Replicating it was unlikely in a country with so little attachment to recording reality that some people even questioned the sitting president's date of birth. [2] At least until the late 20th century, Peruvian public archives suffered from amnesia and government agencies administered their budgets with something more akin to necromancy than accounting. Investigative reporters were focused on tracking drug trafficking, terrorism and corruption. They had to uncover those networks based on direct sources.

Only from 2001 onwards, with the publication of the Transparency and Access to Public Information Act, did the different State entities begin to digitize their data and publish it on their internet platforms. Even so, the informality of the data collection and update mechanisms generated unreliable data. A glaring example was detected in 2008 by journalists Gustavo Gorriti and Romina Mella of IDL Reporteros (IDL-R), while investigating crime records at police stations in Metropolitan Lima. [3] When they requested information on the number and type of crimes in different jurisdictions, they noticed that almost all of them showed very similar results. Digging a little deeper, they discovered that the reports were filled in with a simple copy/paste, under the premise that the situation was similar everywhere. The reporters had to find another approach to the criminality problem they were investigating.

Until the first decade of the 21st century, the use of databases in Peruvian journalism was due to individual efforts by investigative reporters to advance their inquiries. In


2 VALENZUELA, Cecilia. "Buscando la cuna de Fujimori". In Caretas magazine [Lima], See: http://www.caretas.
com.pe/1475/fujimori/fujimori.htm. [Viewed: November 25, 2015].
3 Taken from Romina Mella's presentation at the inauguration of Chicas Poderosas Peru, 20/11/15.


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


2010, journalist Milagros Salazar Herrera of IDL-Reporteros investigated Peru's powerful fishing industry using digital tools that allowed her to compile, verify and analyze in spreadsheets more than 47,000 anchovy landing reports — a species at constant risk of overexploitation. The documents corresponded to the volumes of catch declared by the companies and, on the other hand, to the weight records registered by State supervisors at terminals around the country between 2009 and 2010. The detailed cross-referencing allowed detecting a flawed audit system that benefited the world's second-largest fishing industry. An unreported catch volume representing 100 million dollars in taxes had gone undeclared.

Salazar's report for IDL-R was later expanded and incorporated into a global coverage coordinated by the International Consortium of Investigative Journalists (ICIJ). In 2012, that work was also one of the winners of the Latin American Prize for Investigative Journalism, awarded by the Instituto de Prensa y Sociedad (IPYS).

That same year, the Investigative Unit of El Comercio published a series of reports on the companies and family groups that most benefited from purchases by the State's massive Food Assistance Program (Pronaa) — which shortly afterward was shut down and replaced by the Qaliwarma program. A database of the program's contracting over the previous ten years was manually built based on reports from the Electronic System for State Contracting and Procurement (SEACE). This made it possible to identify the companies that obtained the most contracts, their owners and their backgrounds. Shortly afterward, the same method was applied to investigate government drug purchases, and it was found that a pharmaceutical monopoly was imposing excessive prices on the public health system. The star source was a spreadsheet.


**"Investigative journalism is**
**more alive than ever. Its**
**support from technology has**
**managed to increase the**
**quality and impact of**
**stories".**


**David Kaplan** _, director of the Global_
_Investigative Journalism Network_


A new stage was beginning in which journalists were exploring new tools to improve their analytical capacity and shift from reporting based on a particular lead to a general investigation based on mass evidence. The process would have implications beyond the results of individual investigations: from the approach to framing investigations to the professional metalanguage itself.


**JOURNALISM + TECHNOLOGY**

One morning in June 2014, on the premises of a Lima technology institute, more than fifty journalists and programmers came together for the first time to generate tools that would allow a leap forward in the ways of obtaining and processing information. The activity, a hackathon lasting twelve continuous hours, was named with the canonical expression that has always guided the best journalism: "Follow the money." It was an exercise in civic and journalistic oversight of the use of public funds. The gathering took place simultaneously with those of other groups in twelve Latin American cities, belonging to the HacksHackers community, which brings together journalists and programmers committed to reinventing media.

Expectations were fed by recent technology-backed journalistic revelations that were achieving high impact in the context of that year's municipal and regional elections. The clearest was an unprecedented alliance between the NGO Transparencia, a hacker and two journalists from the popular news website Utero.pe. The result was called Verita, software that cross-referenced the information in the curricula vitae of more than one hundred thousand candidates with several public databases, such as records of civil and criminal convictions. The findings were startling: 1,395 candidates for mayor and regional governor had criminal records; more than half for failing to meet their obligation to pay child support for their own children.


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


The project confirmed the defining new feature of Big Data era journalism: the collaborative spirit among experts from different fields of knowledge. What was particular about this project is that its protagonists — journalists Marco Sifuentes and Ernesto Cabral, and the director of the NGO Transparencia, Gerardo Távara — have never met in person with the hacker who helped them. The architect of the mass download and cross-referencing of all the information does not live in Lima. He is a young Peruvian biologist studying a doctorate in Europe who devotes his spare time to programming. He still prefers to identify himself under the pseudonym Aniversario Perú.

Shortly afterward, the Peruvian journalistic landscape was energized by the arrival of new independent media, with characteristics more akin to startups than to traditional outlets. These were small organizations with highly qualified teams of journalists and dynamic investigative methods. The essential feature — which set them apart even from similar experiences elsewhere in the world — was that their proposal focused from the outset on high-impact investigative content produced with digital resources.

The first of these outlets was **OjoPúblico**, created by reporters Óscar Castilla, David Hidalgo, Nelly Luna and Fabiola Torres, with long experience in the country's most important media outlets, in partnership with programmer Antonio Cucho, an open data activist and founder of the Open Data Peru community.

**OjoPúblico** shook public opinion with the launch of Cuentas Juradas, the first journalistic application to reveal the evolution of the assets of local authorities who sought re-election in the same 2014 electoral process. Through mass analysis of the information declared by these candidates in their sworn declarations and in their curricula vitae submitted to the electoral authority, the portal published a series of investigations on the inconsistencies, gaps and other irregular aspects related to their assets and income. The work was done in alliance with


**TWO**
**TECHNOLOGISTS**
**SUPPORT**
**JOURNALISM**


Behind the pseudonym **Aniversario Perú** is a 35-year-old biologist and father of two daughters who is studying a doctorate in Europe and who in his spare time becomes a civic hacker. He defines himself as: "A guy who knows some programming and wants to make information accessible to people." The architect of the "Verita" software — which serves to **explore candidates' curricula vitae in elections** — and "Manolo" — which **extracts information from records of official visits to State entities** — believes that **good journalism resembles science**. "In Biology or Physics you have to test an idea and you do so by searching for data and analyzing it to reach a conclusion. That is also what a good investigative reporter does," he notes.


A similar experience belongs to hacker **Antonio Cucho**, who in 2014 founded **Open Data Peru, one of the leading communities that promotes the release of information** of public interest and its conversion into information tools. His mission is not easy in a country with little transparency, but Cucho has already managed to enlist **870 young programmers** and professionals **interested in the State opening its data** over the past two years. The municipalities of Miraflores, San Isidro and Lima have got the message and already have portals with reusable information.


OF THE REPORTER OF THE REPORTER


the NGO Suma Ciudadana, which was responsible for a fundamental part of the public information requests through traditional channels, and had the support of members of the HackSpace at the National University of Engineering, who took on the downloading and processing of much of the information required for the data cross-referencing.

"If I hadn't allied with the journalists of **OjoPúblico**, a giant archive of ten years of sworn declarations from Lima's mayors would have ended up as a pile of useless paper," said Javier Casas, president of Suma Ciudadana, about Cuentas Juradas. His organization had gathered dozens of mayoral sworn declarations requested from the Comptroller General since 2012, but almost two years had to pass until they found a team of journalists willing to process and thoroughly investigate those documents to turn them into impactful stories.

Shortly afterward came the launch of the digital site Convoca, directed by journalist Milagros Salazar Herrera, who organized a team of five young reporters and two developers. Their first project was the construction of a comprehensive registry of more than twelve hundred sanction proceedings opened by the Agency for Environmental Assessment and Enforcement (OEFA) against companies in the mining, hydrocarbons, electricity and fishing sectors that committed malpractice between 2010 and 2014.

This database built by the journalists themselves, combined with six months of reporting work, produced the series "Excesses Without Punishment: the environmental trail of extractive industries." The analysis revealed that the mining and oil companies most fined by the Environment Ministry's supervisory body are also the most recidivous, and had established a legal scheme for appealing to the Judiciary, where they had managed to freeze more than 30 million dollars in penalties. It was another revelation born of multidisciplinary work in which journalists detect the potential of a story and organize the strategy and resources ad hoc to seek evidence.


**"We believe the future**
**of journalism will be**
**discovered through**
**piles and piles of**
**experiments".**


**Corey Ford** _, executive director of_
_Matter_


The result is a curious phenomenon in Peruvian journalism: in a context where several of the most important traditional media contracted resources to deal with a revenue crisis, the new digital outlets became a source of quality content, high impact and innovation. The reports developed by **OjoPúblico**, Convoca and Utero.pe crossed from online to offline thanks to agreements with nationally circulating newspapers interested both in the solidity of the investigations and in replicating the virality of the reports on social networks.

Although working with databases and the dynamics it requires is still a pending issue in the local journalism industry, newspapers such as El Comercio and La República have joined the trend using some free digital tools such as Tableau for visualizing sports or electoral results, and Thinglink for entertainment content. The curiosity about leveraging technology to do better journalism is already on the scene. The process, fortunately, is irreversible.


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


**CASE STUDY:**
**Intensive Care**

[News apps or the story that never
dies]


he encounter between journalism and technology offers a scalable range of possibilities for exposing findings to new audiences. It is an accepted idea that T

while visualizations allow understanding a story through a graphic, applications allow understanding several stories in a single journalistic piece and give the user the possibility of finding alternative paths to consume content. It is a process very distant from the traditional one-way nature of information — the difference between listening to a speech and having a conversation. Through applications we offer readers free access to specific data of their interest, a personal browsing experience and, consequently, the possibility of understanding a topic in the way that suits them best.

A clear example is Cuidados Intensivos (Intensive Care), a journalistic application created by **OjoPúblico** to investigate the private healthcare sector in Peru. At a primary journalistic level, the tool reveals the penetration of the country's large financial groups into the business of clinics and medical centers, which in previous years had expanded with scant State oversight. But its value for the reader-citizen-patient is that it is the first registry of clinics and doctors that have accumulated administrative sanctions and criminal proceedings for cases of medical negligence and malpractice in the treatment of users.


**The journalistic work**
**behind CI**


The investigation into the private health system in Peru and the construction of the journalistic application Cuidados Intensivos (Intensive Care) involved five journalists and one developer. The team of reporters worked the data in Excel and used the Open Refine program to clean it and cross-reference information from the different databases.


This application is the result of building proprietary databases to understand the dimensions of the sector. In a first stage, 52 requests were made under the Transparency and Access to Public Information Act. In addition, documentary archives were reviewed and mass data downloads were carried out from the websites of 44 clinics across the country. This volume allowed designing a search platform showing profiles of 61,372 licensed doctors, 9,920 healthcare establishments and 21 fund management companies (including Health Providing Entities, insurers and clinics that offer their own healthcare programs). In this way, the tool allows any user to investigate on their own whether the doctor or clinic to whom they entrust their health — and even their life — is authorized to provide services, what their specialty is, their effectiveness level, and whether they have received administrative sanctions or legal proceedings for malpractice.

The scale of the data collection work and its processing to obtain relevant conclusions allow establishing some clear lessons for any journalist wishing to tackle a challenge of this nature:


**1. The dimension of the data transforms**

The starting point of Cuidados Intensivos was the design of a fundamental database structure for understanding the sector and identifying all the State institutions that held necessary information. In this first phase, the team set out to compile four registries: the first, of corporate groups with investments in the healthcare sector; the second, of all private medical establishments registered in the country (from opticians and doctor's offices to specialist clinics); the third, of insurance companies and health fund administrators; and the fourth, of licensed doctors in Peru.

The main challenge was verifying the data update dates. When the **OjoPúblico** reporters first requested


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


the official registry of private medical establishments from the National Superintendent of Health (Susalud), they received the response that the information was published on the entity's website. There, they found a list of 2,500 private health services. However, a month later while processing that first download, they noticed that Susalud had created a new form for classifying information on private establishments. The new registry had more than 9,000 registered entities and included new terms. The initial work was incomplete and outdated. The team had to scrape all the online forms again to convert them into an Excel file.

A similar problem occurred with the registry of 60,000 licensed doctors. At a certain point, when taking random verification samples, they detected that the Medical Association was not regularly updating the accredited specialties of its members. In several cases, the data were incomplete. The problem had to be corrected by hand, with specific searches of specialists' records.


**2. Official information is contradictory**

The team carried out a second process of collecting more sensitive information to compile profiles of healthcare establishments, doctors, insurance companies and health fund administrators. We requested all penalty resolutions imposed by the National Institute for the Defense of Competition and Protection of Intellectual Property (Indecopi) against private healthcare service companies available from 1992 through mid-2015. During that period, Indecopi had been the only State body responsible for inspecting and penalizing malpractice in the private sector to the detriment of patients. However, it only had archived resolutions from 2011 onwards.

Indecopi's first response was that we download the PDF documents stored on its website, but we insisted


**The digital tools of the project**


The programming work was carried out in the Python language, chosen for its efficiency and performance. The structure was built with the Django framework, which has a powerful content management system in addition to being a modular system that allows the application to be scalable. PostgreSQL was chosen as the database management system for its capacity to store large amounts of data. And the search system was built with Elasticsearch, which has a powerful engine.


that they provide us the documents in physical form. Only then were we able to confirm that the body had more information that it had not processed. When we compared them, we found 30 penalty resolutions against clinics that did not appear on its website.

The Cuidados Intensivos application processed more resolutions than Indecopi itself to compile the ranking of clinics with the most administrative sanctions. Furthermore, with the complete list, journalists were able to verify that the majority of clinics had not paid the imposed fines and had appealed them in the Judiciary.


**3. Technical terms hide revelations**

During the investigation, we had to immerse ourselves in the technical terms used by the State to categorize healthcare establishments. Without mastery of this specialized jargon, we would have missed relevant data. A clear example appeared when we detected an indicator that the National Superintendent of Health (Susalud) calls: operational risk level. The corresponding datum was a percentage with no further explanation.

In official parlance, this concept refers to the result of Susalud's supervision of private services to measure their degree of compliance with patient care standards (conditions and equipment of emergency services, intensive care units, pharmacies, etc.). Susalud inspectors recorded as the risk level what in reality corresponded to the compliance percentage. Thus, when reports stated that a clinic had an "Operational risk level: 6%," what was actually being revealed was that the establishment was failing to comply with 94% of care standards. The impact of the data changed radically.

To understand the terminology, journalists turned to experts who helped them explain it in simple language for users, which was placed in the profiles of the evaluated healthcare establishments in a comprehensible form.


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


**4. If the database doesn't exist, there are always**

**ways to build it**
One of the greatest challenges was resolving the lack of information. Peru lacks an official record of sanctioned medical negligence. The information was requested from the Ministry of Health, the Medical Association, the Association of Private Clinics and the Judiciary. None of these institutions had any archive on the subject. We resolved to build an initial database from complaints reported in the media that had subsequently been formalized with the justice system.

To do this, part of the team immersed itself in the archives of three of the country's largest newspapers: El Comercio, La República and Ojo. We reviewed the period from 1991 through mid-2015 and then transferred the information to an Excel table with the following fields: name of the victim, clinic or hospital where the negligence occurred, doctor or health professional denounced, brief description of events, and year of occurrence. With this overview, we cross-referenced the names of the doctors and establishments involved with records from the Public Prosecutor's Office and the Judiciary. Only formalized cases (with a sentence or open proceeding) were included.


**5. If the information costs, treat yourself to**

**liberating it**
The profiles of companies that provide health services contain information that comes from the National Superintendency of Public Registries (Sunarp) and the Judiciary. The small detail is that both State entities charge a fee for each search. To consult each registered entry at Sunarp, four soles must be paid, and a single company can have several registered documents. At the Judiciary, one sol must be paid for each report to find out the status of a lawsuit. The team decided to bear the cost to access information on around 50 companies that were the focus of the investigation and released the data in Cuidados Intensivos.


**WORKSHOPS**
**FOR**
**REPORTERS**

_[Allied organizations_
_to combine_
_journalism and_
_technology]_


**Investigative Reporters & Editors, IRE**

~~http://www.ire.org/~~

Organizes conferences and training courses for journalists. Its headquarters is at the School of Journalism at the University of Missouri. It runs the NICAR program, which promotes the use of databases for investigative journalism.


**Global Investigative Journalism Network**

~~http://www.globalinvestigativejournalism.org/~~

The Global Investigative Journalism Network, created in 2003 in Copenhagen, organizes the Global Investigative Journalism Conference every two years. Its next


event will be in Johannesburg, South Africa, in 2017.


**Knight Center for Journalism in the Americas**

~~http://www.knightcenter.utexas.edu/~~

Permanently trains journalists from Latin America and the Caribbean in the latest digital tools through free online seminars. Its speakers include the leading journalists in the use of databases.


**International Center for Journalists, ICFJ**

~~http://www.ijnet.org/~~

This organization offers training in investigative journalism and digital tools. It has a program for developing innovative journalistic projects.


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


**Habemus**

**or not habemus data**

[Transparency Law _vs._ Personal Data Protection Law]


hirteen years after it came into force, the Transparency and Access to Public Information Act in Peru has become an indispensable tool, T

though not without setbacks in this area. The main stumbling block is the criterion some officials apply to personal information. In June 2015, lawyer Javier Casas requested from the Comptroller General of the Republic a copy of the sworn declaration of income, assets and liabilities of the President of the Republic, Ollanta Humala, arguing that this document is public and can be requested by law. After four months of insistent claims, Ca-

Personal Data since 2011.


had overlooked the constitutional precept that establishes it as a State obligation to disseminate the sworn declarations of officials for civic oversight. But the case evidenced something more: the frictions between the law that promotes the opening of public data and another that State bodies have begun to use at will to close access to it.


Months earlier, Casas had interviewed the head of the National Authority for Personal Data Protection (ANPDP), José Quiroga León, who stated the following: "The sworn declarations of public officials do not require the consent of the holders to be delivered, because they are not covered by the personal data protection regulation." The Comptroller's argument was therefore a particular interpretation to deny that information.

The paradox of this situation is that the State spends 11 million soles per year to maintain a Public Management Secretariat for promoting the opening of information while, at the same time, several of its ministries and agencies deny requests made by citizens and journalists.

A review of reports by Centro Liber, the Instituto de Prensa y Sociedad (IPYS) and the Defensoría del Pueblo allows identifying 17 public entities that between 2003 and 2015 refused to respond to public information requests, did so partially or outside the deadline. The majority of these information requests had journalistic purposes.


**Can we read a minister's emails?**

In mid-2014, the hacker groups Anonymous and Lulz Security were behind the largest leak of emails from a senior State official in Peru's history. Their members breached the account of the then Prime Minister, René Cornejo, and made public 6,482 messages. The press dubbed the case the 'Cornejoleaks.'

The volume of the leak had great political and media impact because it not only revealed the alleged secret lobbying by cabinet members in favor of various corporations, but also opened a legal debate on the public nature of officials' official communications.


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


Among the emails hacked from the then prime minister was a chain of messages between the Minister of Energy and Mining, Eleodoro Mayorga, and the Minister of the Environment, Manuel Pulgar Vidal, regarding a regulation approved to directly benefit companies in the hydrocarbons sector. When journalists began reporting this, Centro Liber, a non-profit organization that promotes transparency in the State, requested from Mayorga's office copies of "emails received by the minister at his official email account or any other account created for him at the ministry, with their respective replies, in which he communicated with any person to deal with matters related to the New National Hydrocarbons Regulation or similar." The request was made under the Transparency and Access to Public Information Act but was rejected. The ministry argued that the request violated the secrecy of the minister's communications.

The president of Centro Liber, former anti-corruption prosecutor Julio Arbizu, then decided to file a habeas data petition on the grounds that the content of the Energy and Mining Minister's conversation was a matter of public interest and did not in any way violate his privacy and the secrecy of his communications.

The case was placed in the hands of judge Hugo Velásquez Zavaleta of the Fifth Constitutional Court of Lima, who ruled in favor of the habeas data petition nearly a year later, when Mayorga had already left office. "The public information that may be requested and that the State administration is obliged to deliver may take any form of expression, whether graphic, audio, visual, electromagnetic or contained in any other material medium," the June 2015 ruling states. The decision held that "with the evolution of technology, communication is no longer conducted solely through paper, but through other means, such as electronic mail."

Judge Velásquez based his ruling on two principles: that of publicity and that of maximum disclosure. The first is regulated in


**"The reuse of data**
**made public by the State**
**allows citizens to exercise**
**the right of access to**
**information".**


**Miguel Morachimo** _, director of the_
_NGO Hiperderecho._


article 3 of the Transparency and Access to Public Information Act, which establishes that "all information held by the State is presumed public, except for provisions expressly provided for." The second principle was developed by the Inter-American Court of Human Rights and incorporated into the jurisprudence of the Constitutional Tribunal: "publicity in the actions of public authorities constitutes the general rule, and secrecy, when it has constitutional coverage, the exception."

The Ministry of Energy and Mining appealed the ruling even though Mayorga's successor, Minister Rosa Ortiz Ríos, said in a television interview that she would deliver the public information found in her predecessor's email.

Centro Liber also filed habeas data petitions to request emails from the Ministers of Agriculture, Milton Von Hesse, and of Economy, Luis Castilla, in which they had dealt with matters directly related to their management. At the time this manual went to press, both proceedings were still pending judicial ruling.

In the debate over these cases it became clear that the journalist has in the Transparency Act a powerful tool for accessing information on sensitive matters that relate both to the management of specific officials and to public policies. It is not an immediate key to evidence, but it should be one of the essential criteria in the mindset of the investigative journalist.


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


**The existential dilemma:**
**When is private data**
**a matter of public interest?**


n July 2011, the Presidency of the Council of Ministers (PCM) promulgated the Personal Data Protection Act with the aim of guaranteeing the proper treatment I

of any citizen's private information. In theory, it is a positive regulation, as it prevents the disclosure of sensitive data (about

The regulation does not regulate or restrict the use of public data, but admi-

public data that contain names and personal information.

A clear example is the case of the Datos Perú portal. In October 2014, the National Authority for Personal Data Protection (APDP) fined the site S/. 228,000 for replicating legal regulations, appointments and administrative sanctions against State officials and employees originally published in the legal norms bulletin attached to the official newspaper El Peruano — a

to review it.


to do so because the data had been collected from a public document. According to the APDP, Datos Perú violated the Personal Data Protection Act for not having the consent of the individuals to publish that information, even though the same content also appeared on the portals of El Peruano and the Ministry of Justice.


**"An autonomous authority**
**is needed to monitor**
**and oversee the delivery**
**of public information,**
**because the officials**
**in charge are**
**limited by orders**
**from their superiors".**


This was the first sanction carried out by the APDP and generated controversy, primarily because of the evident contradiction in criteria for determining what is public and what is private when the same information is disclosed on a State portal or on a private site. To that was added a greater concern: the possible repercussions of that criterion for journalistic practice and civic oversight. Can an official decree secrecy over what the State itself is obliged to report? And in a more fundamental sense: Where does public interest begin and where does it end?


In an era when the world is moving toward a culture of open data, investigative journalists have several

**Roberto Pereira** _, Centro Liber._ obstacles to overcome. The first step is knowing all the available tools for obtaining information and for then processing it in an innovative way. Until recently, this was a process closer to craftsmanship and intuition. The powerful union of journalism and technology has enriched the methods and standards of the profession. More than a set of new instruments, we have a strategic resource. It is, as stated, a diverse and practical toolkit —

**Roberto Pereira** _, Centro Liber._


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


**REQUEST FOR ACCESS TO**

**PUBLIC INFORMATION**


_Although_
_the law does not_
_specify an official_
_request format, this model_


_helps to request_


_information_


**THE FINE PRINT:**
**HOW TO MAKE**
**AN EFFECTIVE**
**INFORMATION**
**REQUEST**


The Transparency and Access to Public Information Act establishes that public bodies have a **deadline of seven working days**, after receiving a request, to issue a response. In case of delay, they have **five additional days** to deliver it, after prior notice to the applicant.
According to the Citizens' Manual for Access to Public Information, prepared by the Consejo de la Prensa Peruana, if a public body fails to comply with the law, as in several of the cases presented, **citizens have the right to file a habeas data petition**. This legal remedy applies not only when the public institution rejects an information request, but also when the information provided is ambiguous or when no response is issued within ten working days following receipt of the request. The reporter can also file a habeas data petition when the entity denied access to certain information after an appeal was submitted to the responsible official requesting that it be reviewed by their hierarchical superior. In these cases, without needing to be represented by a lawyer, **the journalist has 60 working days to file a habeas data petition** before the civil judge or mixed judge in the area where they live or where the public institution that denied their request is located.


|Name of Institution|Col2|Col3|
|---|---|---|
|**I. Official responsible for delivering the information:**|**I. Official responsible for delivering the information:**|**I. Official responsible for delivering the information:**|
||||
|**II. Applicant's details:**|**II. Applicant's details:**|**II. Applicant's details:**|
|Full name or company name:|Identity document and number:|Identity document and number:|
|Address:|Address:|Address:|
|Email address:|Phone number:|Phone number:|
|**III. Information requested:**|**III. Information requested:**|**III. Information requested:**|
||||
|**IV. Department to which the information is requested:**|**IV. Department to which the information is requested:**|**IV. Department to which the information is requested:**|
||||
|**V. Form of delivery of the information**|**V. Form of delivery of the information**|**V. Form of delivery of the information**|
||||
|Full name:|Full name:|Date:|
|Signature:|Signature:|Signature:|


**Observations:**


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER


~~**ABOUT THE AUTHORS**~~


**David Hidalgo**
_Editorial Director_
_of OjoPúblico_


He is the author of the book "Sombras de un rescate" (Shadows of a Rescue), about the last armed action of the MRTA terrorist group. In 2006 he won the national Human Rights and Journalism Prize. Fellow of the Edward R. Murrow Program for Journalists of the US Department of State. He was a member of the Peruvian team that won the Data Journalism Awards 2015.


**Fabiola Torres L.**
_Data Analysis Editor_
_of OjoPúblico_


Investigative journalist specializing in health, corporate power and public administration. Member of Investigative Reporters and Editors (IRE). She was a fellow of the Kiplinger Foundation at the University of Ohio, and of the Global Investigative Journalism Network (GIJN). She was a member of the Peruvian team that won the Data Journalism Awards 2015.


THE SWISS ARMY KNIFE THE SWISS ARMY KNIFE
OF THE REPORTER OF THE REPORTER
