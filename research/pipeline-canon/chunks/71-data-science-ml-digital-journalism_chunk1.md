<!-- chunk: 1/1 | source: 71-data-science-ml-digital-journalism.md | words: 14180 -->
<!-- headings: Expert Systems With Applications; ata Science, Machine learning and big data in Digital Journalism: A urvey of state-of-the-art, challenges and opportunities -->

Contents lists available at ScienceDirect
# Expert Systems With Applications


[journal homepage: www.elsevier.com/locate/eswa](https://www.elsevier.com/locate/eswa)


view
## ata Science, Machine learning and big data in Digital Journalism: A urvey of state-of-the-art, challenges and opportunities

zabeth Fernandes [a][,] [*], S´ergio Moro [b], Paulo Cortez [c ]

_CTE_ - _Instituto Universitario de Lisboa (ISCTE-IUL), ISTAR, Avenida das Forças Armadas, Edifício II, D615, 1649-026 LISBOA, Portugal_ ´

_tituto Universitario de Lisboa (ISCTE-IUL), ISTAR, Lisboa, Portugal_ ´
_GORITMI Research Centre, University of Minho, Guimaraes, Portugal_ ˜


T I C L E I N F O


_words:_
a science
tal journalism
mining
ematic literature review
ia analytics
hine Learning


**Introduction**


A B S T R A C T


Digital journalism has faced a dramatic change and media companies are challenged to use data science a
rithms to be more competitive in a Big Data era. While this is a relatively new area of study in the me
landscape, the use of machine learning and artificial intelligence has increased substantially over the last
years. In particular, the adoption of data science models for personalization and recommendation has attrac
the attention of several media publishers. Following this trend, this paper presents a research literature anal
on the role of Data Science (DS) in Digital Journalism (DJ). Specifically, the aim is to present a critical literat
review, synthetizing the main application areas of DS in DJ, highlighting research gaps, challenges, and
portunities for future studies. Through a systematic literature review integrating bibliometric search, text m
ing, and qualitative discussion, the relevant literature was identified and extensively analyzed. The rev
reveals an increasing use of DS methods in DJ, with almost 47% of the research being published in the last th
years. An hierarchical clustering highlighted six main research domains focused on text mining, event extract
online comment analysis, recommendation systems, automated journalism, and exploratory data analysis al
with some machine learning approaches. Future research directions comprise developing models to impr
personalization and engagement features, exploring recommendation algorithms, testing new automated jo
nalism solutions, and improving paywall mechanisms.


Digital innovation introduced a dramatic change in media com­
nies. The decline of print advertising revenue, the distribution of free
ital content and the change of reader’s behavior induced a need of
w sources of revenue (Arrese, 2016; Rußell et al., 2020). Subscription
iness models, usually in the form of paywall models (Pattabhir­
aiah et al., 2019; Rußell et al., 2020), become a solution to assure
mpanies’ sustainability (Davoudi & Edall, 2018; Simon & Graves,
19). Consequently, high level data-based Expert Systems models have
erged (Davoudi et al., 2018).
Currently, each second of time results in millions of readers inter­
ing on digital platforms, which provides huge volumes of data to be
lected and stored by media companies (Lewis, 2015). This new Big
a era in Journalism demanded the development of new technologies
d brought Data Science (DS) and Artificial Intelligence (AI) capabil­

s to the newsroom (Borges et al., 2021). Moreover, the adoption of


Machine Learning (ML) methods is mentioned in the Reuters Dig
Report as the new trend in media companies, especially for person
zation and content recommendation (Newman et al., 2019; Yeung
Yang, 2010; Zihayat et al., 2019). Comment analysis, event mining, a
journalism automation have attracted a great attention and nowad
continue being an outstanding research area. Currently, ML and D
Learning (DL) approaches have been sucessfully applied to dive
fields, such as Natural Language Processing, Social Network Analysis
business models development (Davoudi, 2018).
Motivated by the increase of interest in DS (including AI and ML
Digital Journalism (DJ), this study presents a systematic, transpar
and reproducible review process, through a Systematic Literature
view (SLR) (Abdelmageed & Zayed, 2020; Aria & Cuccurullo, 20
integrating bibliometric search, text mining, and qualitative discuss
of the literature. The time span time of study was 2010 and 2021. O
research literature about DS methods in DJ was considered. Our sur
methodology presents four stages: study design, data collection a


Corresponding author.
_E-mail addresses:_ [elisabeth.ferna@gmail.com, elizabeth.fernandes.data@gmail.com (E. Fernandes).](mailto:elisabeth.ferna@gmail.com)


[ps://doi.org/10.1016/j.eswa.2023.119795](https://doi.org/10.1016/j.eswa.2023.119795)


eived 14 September 2021; Received in revised form 2 March 2023; Accepted 2 March 2023


ilable online 5 March 2023
7-4174/© 2023 The Author(s). Published by Elsevier Ltd. [This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/](http://creativecommons.org/licenses/by-nc-nd/4.0/)
[nd/4.0/).](http://creativecommons.org/licenses/by-nc-nd/4.0/)


ection, data analysis and findings, and discussion and results. Hence,
contribution of our research is threefold: (i) to identify and describe
state-of-the-art of existing approaches; (ii) to identify gaps, chal­
ges, and opportunities on how to use DS to improve reader engage­
nt in DJ; (iii) based on the identified gaps, to generate future
ommendations and new research directions.
To summarize, the aim of this review is to present the most relevant
rks conducted in the field of DS in DJ by using a 4-step methodology.
e remainder of the paper is structured as follows. First, Section 2

sents the background of Data Science in Digital Journalism and an
roduction about literature analysis methods. Then, Section 3 de­


bes the review methodology by describing the study design and the
a collection steps. Followed by the descriptive analysis of the
lection at Section 4. Then, the SLR main results are discussed in


Cater, 2015). Thus, to examine the existing literature, this paper
sumes a Systematic Literature Review (SLR) (Abdelmageed & Zay
2020; Aria & Cuccurullo, 2017), which consists of a 4-step methodolo
As presented at Table 1, the presented approach combines three wid
known methodologies resulting in four steps that guided our resear
Firstly, the study design, then data collection and selection, followed
data analysis and findings, and finally, discussion and results presen
tion. This well-defined process allow us to identify, evaluate and in
pret the literature to answer relevant research questions (RQs) that
detailed at Section 3.


_2.3._ _Contribution_


Several studies present different techniques for gathering the state
the art on a research topic (Brous et al., 2020; Donthu et al., 202
Table 2 presents four literature review frameworks that were chosen
represent different and recent literature analysis on research ar
related to DJ. For each framework, the table mentions the keywor
selection criteria, the methodology followed, as well as, the tools us
The first two works (Engelke, 2019; O’Brien et al., 2020) presen
manual analysis, while the remaining two (Zhou & Liao, 2020; Zhou
Zhou, 2020) conducted a three-step bibliometric analysis by using
VOSviewer tool (Donthu et al., 2021; Van Eck & Waltman, 201
Finally, the last row presents the proposed approach. Our approach
the only literature review study that includes Text Mining (TM) au
mated methods and a clearly identified criteria for the keywords’
lection, followed by a Hierarchical Clustering to define exclus
criteria’s. Thus, this approach reduces the SLR manual effort, result
in a more easily replicable semi-automated methodology while sim
taneously avoiding human bias.
This study differs from others, firstly, because it presents a literat
review that investigates the relation between DS and DJ, a broa
theme than the research presented by (Zhou & Liao, 2020). Secondly
each step of the process the human intervention was minimized
reducing the subjectivity in the keywords’ selection or docum
exclusion criteria. Finally, the process combines TM methods develop
using the open source R statistical tool, thus benefiting from a co
munity of supporters contributing with packages for a myriad of d
analysis tasks (Cortez, 2014), as well as, science mapping analysis (SM
by using VOSviewer (Donthu et al., 2021; Van Eck & Waltman, 20
and _bibliometrix,_ the R-tool for comprehensive science mapping analy
(Aria & Cuccurullo, 2017). Moreover, the use of TM for synthesiz
existing literature enables to efficiently extract insights from a la
body of knowledge (Moro et al., 2015). Thus, the richness of the tex
published articles combined with TM enables deeper analysis beyo
keywords analysis. Resulting in an approach that, to the best of


**Table 1**
Comparison of distinct Literature review stages.

**SLR stages** **Standard Science** **Data Analytics** **Proposed**
**Mapping Workflow** **Approach in SLR** **approach**


tion 5. Finally, Section 6 presents the main conclusions and research
plications of this literature review.


**Related work**


_Context and Motivation_


Nowadays, media companies driven by economic pressures are
esting in data and technological solutions to achieve business results.
cording to the International News Media Association (INMA) report

ternational News Media Association, 2022), data is critical to create
der-centric products. Furthermore, the report argues that bringing
a to the centre of the decision-making process is a current and an
going process in media companies. Moreover, as discussed by Kotler
al. (2016), companies should map the customer path to purchase,
derstand customer touchpoints, and improve critical touchpoints.
nsequently, across the reader’s conversion funnel the goal it is to
ximize reader’s engagement (Lagun & Lalmas, 2016), retention and
sequently increase revenue (Sapian & Vyshnevska, 2019).
Despite the lack of a clear definition of reader engagement, authors
ee that engagement is a multidimensional phenomenon (Steensen
al., 2020) related to the level of attention and involvement
motional, cognitive and behavioral) with media (Attfield et al., 2011;
azek et al., 2016; Mersey et al., 2010). Furthermore, to measure
der engagement a range of engagement metrics are available on the
rature (Davoudi et al., 2019; Ksiazek et al., 2016; Lehmann et al.,
12; Peterson & Carrabis, 2008). However, to the best of our knowl­
ge, there is a lack of studies that analyze the large body of knowledge
how DS can improve reader engagement.
Publishers’ are using DS methods to understand media consumers
d their consumption patterns (Villi & Picard, 2019) to increase
gagement levels. Some examples can be listed: audience monitoring

yllylahti, 2017), recommendation algorithms (Gonzalez Camacho &
es-Souza, 2018; Yeung & Yang, 2010; Zihayat et al., 2019), news
formance or engagement prediction models (Fernandes et al., 2015;
skelainen et al., 2020; Zihayat et al., 2019¨ ), fake news detection
ntoun et al., 2020; Shim et al., 2021; Souza Freire et al., 2021) or,
orithms for paywall design (Davoudi et al., 2018; Rußell et al., 2020).
Zhou and Liou (2020) presented a bibliometric analysis of commu­
ation research on AI and Big Data, which proved an increase of
blications in since 2013 (Zhou & Liao, 2020). However, to the best of
knowledge, no intensive survey on the role of DS in DJ has been
ently published. Hence, by examining the existing research literature
the last decade, this paper surveys what has been done with DS
thods in media. Moreover, one of the main contributions of this paper
s to present research gaps in the current literature and opportunities
future research.


_Systematic literature review_


Synthesizing past research findings is a complex task that requires a
ailed methodological approach (Aria & Cuccurullo, 2017; Zupic &


Kitchenham and
Ebse (2007)


Zupic and Cater
(2015)


Haneem et al.
(2017)


Planning the Study Design Purpose of the Study Design
review Literature Review

Protocol and
Training
Data Collection Search the Data Collectio
literature and Selection
Practical
Screening
Quality
Assessment
Conducting the Data Analysis Analysis and Data Analysis
review Findings and Findings
Data Visualization
Reporting the Interpretation Writing the Results and
review review discussion


**le 2**
mples of relevant frameworks for literature analysis and the proposed approach.


**uthor** **Areas of Research** **Literature sources,**
**timespan and**
**number of articles**

ngelke, Online participatory **Data base:** Scopus
2019) jouralism **Timespan:** 1997 to
**Nr. Articles:** 378


**Keywords selection (query** **Methodology** **Approach and Tools**
**strings)**


Previous literature analysis to SLR based on (Cooper, 1998). Steps:
achieve content validity. problem formulation, data
collection, data evaluation, analysis
and interpretation, public
presentation.


O’Brien
et al.,
2020)


hou &
Liao,
2020)


Factors that contribute
to consumer’s pay
intentiont in DJ


Artificial Intelligence
and Big Data in
communication
research


**Data base:** Google
Scholar, EBSCOhost,
Web of Science and
ProQuest
**Timespan:** 2000 to
**Nr. Articles:** 37


**Data base:** Web of
science
**Timespan:** Until
February 2020
**Nr. Articles:** 685


Authors comprised
combinations of phrases
related to the field.


Authors defined the keywords Bibliometric analysis
without previous research. Steps: data collection, analysis and
intepretation, discussion and
conclusion.


SLR based on (Webster & Watson,
2002).
Steps: identify literature, structure
the review, theoretical development,
theory evaluation, discussion and
conclusion.


Manual selection and inspection
the articles.
Biblimetric analysis conducted
manually.


Manual selection and inspection
relevant Journals and articles.
Biblimetric analysis conducted
manually.


Data analysis conducted with
Pyhon.
Bibliometric analysis conducted b
using VOSviewer.


hou &
Zhou,
2020)


Human-Computer
interaction in
journalism


**Data base:** Web of
science
**Timespan:** Until 2020
**Nr. Articles:** 2156


Authors defined the keywords Bibliometric analysis
without previous research. Steps: data collection, analysis and
intepretation, discussion and
conclusion.


Combination of the top
keywords of two journals and
top terms in the Document
term matrix (TM method).


hou & Human-Computer **Data base:** Web of Authors defined the keywords Bibliometric analysis Data analysis conducted with
Zhou, interaction in science without previous research. Steps: data collection, analysis and Pyhon.
2020) journalism **Timespan:** Until 2020 intepretation, discussion and Bibliometric analysis conducted b

**Nr. Articles:** 2156 conclusion. using VOSviewer.

oposed Data Science in digital **Data base:** Scopus Combination of the top SLR Data Analysis approach that Document’s agglomerative
approach journalism **Timespan:** 2010 to keywords of two journals and combines science mapping analysis hiearchical clustering to define
2021 top terms in the Document workflow and text minng. exclusion criterias (R statistical
**Nr. Articles:** 514 term matrix (TM method). tool) and reduce the size of searc


SLR Data Analysis approach that
combines science mapping analysis
workflow and text minng.


Document’s agglomerative
hiearchical clustering to define
exclusion criterias (R statistical
tool) and reduce the size of searc
space.
Bibliometric analysis conducted b
using bibliometrix and VOSviewe


owledge, is innovative on a DJ survey (Zhou & Zhou, 2020).


**Methodology**


This section presents the proposed 4-step systematic method for
iewing the literature presented at Table 1. The SLR process begins,
mprising study design, data collection and selection. Each stage en­
mpasses several activities, as outlined in Fig. 1. The following sub­

tion describes each stage of the SLR.


_Study design, data collection and selection_


This stage involves the preparation of the research work to conduct
review that includes the objective and research questions definition.
cording to the motivation of this paper, the following research
estions (RQs) and motivations are addressed to organize the study:
**RQ1 -** What are the main motivations and the major topics when
opting DS in DJ?
Motivation: Identify the most significant publications in the field.
**RQ2 -** What are the benefits or positive impacts of using DS in the DJ
main?
Motivation: Identify the DS approaches and applications domains in


**RQ3 -** What gaps exist in the current literature that provide new
earch paths?
Motivation: Identify challenges and research opportunities.
In the first step, the RQs were broken into thematic areas according
the bibliometric technique: co-citation, co-author, co-word and
liographic coupling (Cobo et al., 2011; Zupic & Cater, 2015). In the
rch process a database was chosen, in contrast to focusing on specific
rnals to not limit the review’s comprehensiveness. Data precessing and cleaning was performed (Jin et al., 2019). The digital


database considered was Scopus which is the largest abstract and c
tion database of peer-reviewed literature (Ballew, 2009) and it is used
multiple researches (Amado et al., 2018; Borges et al., 2021). As the S
is a semi-automated process, some human-led tasks (HLT) were p
formed. Thus, across the text we use the abbreviation HLT to signa
human-led task and ALT to signal an automated-led task. Therefore,
data collection and selection process followed the procedures describ
below:
The inclusion and exclusion criteria were applied. The first inclus
criteria consisted of terms that appeared in the titles, abstracts, a
keywords.
The initial keywords selection was based on filter the top keywo
of the Journals “Decision Support Systems” and “Digital Journalism
We selected the 20 most frequent keywords by year in the last 5 years
both Journals. Then, we saved the keywords that are in the top 20 m
than one year (ALT). This resulted in two lists of 26 and 24 keywor
Despite that we aimed to minimize human intervention, in both l
some keywords were still considered out of the scope of our resear
For example, the first list comprises some of the following keywor
**Information Systems**, Electronic Commerce, **Artificial Intelligen**
Commerce, Sales, **Decision Making**, Investments, Finance, **Big D**
and Costs. Thus, the authors saved those related to the scope of
research that are highlighted above in bold (HLT). The same ration
was applied to the second list, where for instance the keywords “fa
book” and “twitter” were excluded. Moreover, in the second list,
keyword “news” was considered often commonly used by other sci
tific branches, thus the term was replaced by “digital news”, “ne
media” and “news industry” (HLT). To reduce the subjectivity, the th
authors (a head of digital media and analytics office at a wide audie
journal; and two senior scholars in data science and analytics) analy
all HLT decisions until a consensus was reached. It should be mention
that one author is an analytics and audience insights manager i


**Fig. 1.** Framework of the systematic literature review process.


ional newspaper since 2015. Finally, the first query, with 25 key­
rds resulted in 1,689 documents, as presented at Fig. 1.
Then, after a preliminary analysis of the dataset, by using _bibliome­_
, some topics not related to our study appeared, for example, “health”
“security”, thus an enhancement of keywords was required.
The second keywords selection was improved by excluding the top


terms that are out of the research scope. As presented in the next secti
TM methods were used to find the top terms presented in the sam
(ALT). Then, non-related documents were removed from the collect
by adding an exclusion condition in the second search query as resul
a manual selection of top terms out of research scope (HLT).
Concerning the research literature type, only articles from journ


ferences and review papers were included.
The search focused only on articles published in English to avoid any
perception and efforts in translation.
Concerning the timeline, a period between 2010 and 2021 was
sen, as it contains the period of “Paywalls Popularization” (Arrese,
16), an adequate period to see the recent evolution of DS in DJ.


The bibliographic search resulted in 514 documents. For each p
lication, we retrieved the following data elements: title, authors,
stract, publication year, keywords, source title, document type a
language.
As result of a semi-automated process, we further note that the f
dataset can contain documents not directly related to the scope


**Fig. 2.** Framework of the text mining process to find the keywords to exclude in the second search query.


earch, nevertheless, we decided not to skim the article title and ab­
act to avoid a human bias.


_Keywords enhancement with text mining_


The selection of terms to exclude in the second research query en­
mpasses three steps. Firstly, we extracted the information from the
abase; then punctuation, numbers or stopwords were removed, as
l as, text was stemmed (Antonio et al., 2018; Welbers et al., 2017´ ).
e matrix with the frequency of each term by document (DTM) was
culated. Furthermore, to avoid non-informative terms, the matrix
M-tf-idf was also calculated. The term frequency-inverse document
quency (tf-idf) measures the relative importance of a word to a
ument (Silge & Robinson, 2019; Welbers et al., 2017). Finally,
lomerative hierarchical clustering (AHC) was performed to find the
in clusters in the sample. The AHC is an unsupervised algorithm that
rts by assigning each document to its own cluster and then the al­


**Table 3**
Main information about the collection (source: bibliometrix).

**Description** **Results**


Main information Timespan 2010:202
about data


ithm iteratively joins at each stage the most similar document until
re is only one cluster (Gordon, 1999). In order to obtain compact and
l-separated groups we calculate four measures: average distances
hin and between clusters, Dunn index and average Silhouette


Sources (Journals, Books, etc) 324.00
Documents 514.00
Average years from publication 4.44
Average citations per documents 8.35
Average citations per year per doc 1.24
Document types Article 228.00
Conference paper 278.00
Review 8.00
Document contents Author’s Keywords (DE) 1,476.00
Authors Authors 1,330.00
Author Appearances 1,777.00
Authors of single-authored documents 87.00
Authors of multi-authored documents 1,243.00
Authors Single-authored documents 90.00
collaboration


Documents per Author 0.39
Authors per Document 2.59
Co-Authors per Documents 3.07
Collaboration Index (the average number of 2.93
co-authors noted solely in multi-authored
publications (Gil et al., 2020))


2.93


ndon et al., 2011´ ). Thus, the number of clusters that optimizes the
r measures was nine (ALT). Then, we explored the clusters by
pecting the word clouds (HLT). As each cluster contains information
ated to the research scope, we cannot exclude any cluster. Thus, to i
ne the query, the 20 most frequent words by cluster were analysed to i
d non-related terms. As an example, the first cluster contains “social”,
edia”, “twitter and “tweet” on the most frequent words. By reading
abstracts, we found research on social media platforms content and
nds that were considered out of the scope (HTL). Hence, non-related
uments were excluded from the Scopus search query by removing
words highlighted in bold (see Fig. 2).


**Data analysis and findings**


The present section aims to explore the thematic areas presented in
. 1. Hence, by performing citation, co-citation, collaboration and cord analysis, complemented by a hierarchical clustering of the
lection, the RQ1 presented in Section 3.1 can be answered. Then, in

tion 5, a co-word analysis with keywords co-occurrences maps is also
sented, which enables to answer both RQ2 and RQ3.
The statistical analysis was performed by using two open-source
ls: _biblioshiny_ that is a shiny app providing a web-interface for bib­
metrix (Aria & Cuccurullo, 2017) and VOSviewer (Cobo et al., 2011;
n Eck & Waltman, 2010).
The sample comprises three types of documents: 228 articles/journal
pers (44%), 278 conference papers (54%) and 8 review papers (2%)
e Table 3). Furthermore, 47% of total sample was published between
18 and 2020 (see Fig. 3). In fact, in the last decade, there is an
reasing interest in DS along with the popularization of paywall
dels (Arrese, 2016; Rußell et al., 2020). Moreover, we have 1,161
hors (87%) with a single contribution, which indicates that a diverse
up of researchers is interested in this research field. Besides, that it is

- corroborated by the high number of sources (324) proving that
st editors consider the subject relevant.
The worldwide spreading of authors, obtained from _biblioshiny_ (see
. 4 a)), indicates that northern hemisphere is more representative, i.
researchers from North America, Asia and European Union (including
) published 25%, 34% and 35% of the total number of documents,
pectively. Furthermore, as presented at Fig. 4 b), the most cited
untries are USA, China and Singapore. However, the country with
her average article citations is Switzerland, followed by Singapore
d Portugal that have an average year of publication 2017 and 2018
pectively; while Switzerland has older publications. Fig. 4 c) illus­
tes a bibliometric VOSviewer network visualization map of cohorship (international collaboration) using country by average year


of publication and number of publications (Van Eck & Waltman, 20
Romero & Portillo-Salido, 2019). The distance between countr
approximately indicates the relatedness of the countries in terms of
authorship.
Citation analysis intends to identify the authors and journals t
most influenced the research (Donthu et al., 2021). It also provides
authors and journals that consequently contributed to the major top
of research on DS in DJ presented in the final reading list at Table 5 (t
answering to RQ1). In particular, Table 4 enables to identify the 20 m
productive authors. The vast majority contributed or started
contribution after 2015. Three authors present more than four pu
cations: firstly, Nicholas Belkin, affiliated with Rutgers University, p
sents contributions in 6 of the 10 years under analysis. Followed
Duen-Ren Liu affiliated with National Chiao Tung University and Ne
Cristianini affiliated with Bristol University, each one contributed wit
documents. Nicholas Belkin contributed with studies in the field of
formation retrieval, information search and user behavior, which app
in the first research domain shown at Table 5 (Cole et al., 2011, 20
Liu, Cole, et al., 2010). Liu D.-R. research focuses on recommendat
systems (D. R. Liu et al., 2018) while Cristianini focuses on news cont
analysis and readers preferences (Flaounas et al., 2013).
In terms of researcher’s impact measure, at Table 4 we present
index and G-index that are based on the number of publications and
number of citations of the bibliographic collection (Egghe, 2006; Hirs
2005). In the overall sample, the author’s with the highest H-index a
G-index are Nicholas Belkin and Nello Cristianini. Nicholas Bel
ranked top in the list where 6 of his articles have been cited at leas
times each.
In order to perform collaboration analysis, it was identified
clusters of collaboration network. Fig. 5 illustrates 11 of the 26 clust
and their main fields of research. Cluster 10, 2 and 16 present the high
network with 6, 5 and 4 researchers. Nicholas Belkin and Michael C
published documents together (cluster 10) (see Table 4) and two of th
are in the top most 20 cited articles of the sample (Cole et al., 2011; L
Cole, et al., 2010). Furthermore, Nello Cristianini, Ilias Flaounas, Om
Ali and Tijl De Bie (cluster 2) have one article in the top 20 most ci
(Flaounas et al., 2013), as presented at Table 5.
Seeking to investigate **RQ1** regards, the analysis of keywords all
us to understand the boundaries of the research domain, to find tre
and to identify some relationships (Abdelmageed & Zayed, 2020). Th
Fig. 6 presents the wordcloud of the top 50 author’s keywords a
highlights the most common keywords of the articles of the datab


**Fig. 3.** Year-wise distribution of publications.


onthu et al., 2021). In the most frequent keywords we find “text
ning” that occurs 31 times in our collection, followed by “machine
rning”, “big data” and “sentiment analysis”, which appears 26, 23
d 22 times respectively. Next, the words “artificial intelligence”, “data
ning”, “news recommendation” and “natural language processing”
ur between 18 and 13 times.
Moreover, Fig. 7 illustrates the overlay visualization mode of author
words, the full-counting method was applied to calculate keyword
ghts. We considered the minimum number of occurrences of a
word of 5. The distance between keywords approximately indicates
relatedness of the keywords in terms of co-citation links, and each
or represents a moment in the timespan. Accordingly, to the diagram
ours, from blue to yellow, during the period of study (from 2010 to
21), keywords such as “text mining”, or “information extraction”
re more frequent at the beginning of the period. Followed by “news
ommendation” or “sentiment analysis” (at green colour) and,
ently, “artificial intelligence”, “big data” or “automated journalism”.
Furthermore, by exploring the thematic evolution map (see Fig. 8) to
mplement the data presented at Fig. 7, we can note that “text mining”,
m” (which stands for support vector machines, a supervised learning
hnique) and “computational journalism” are important keywords
ween 2010 and 2017. Moreover, both stages have little connection,
he number of common keywords is low. The focus between the first
d second stages evolved to other DS domains such as, audience
gagement, machine learning or artificial intelligence, which is also
roborated by Fig. 7. As an example, “text mining” evolved into “on­
e news”, “machine learning” or “sentiment analysis”.
In addition, a clustering of our collection help us to explore the main
mains of research. By repeating the previous AHC algorithm, the
lection was partitioned into six groups (see Fig. 9). Each cluster al­
ws us to identify the major research domains to adopt DS in DJ (RQ1),
t are: exploratory studies and detached ML approaches, text mining
alysis, recommendation systems, event extraction, opinion mining,
d automated journalism. In accordance to previous network analysis,
period between 2018 and 2020 presented an increase on exploratory
dies and detached ML studies as well as, as increase on research on
t mining, recommendation systems and artificial intelligence.
In order to define the final reading list, which presents the major
ics of DS adoption in DJ (RQ1), this paper ranks the most cited ar­
es by cluster (as presented in Table 5). Due to the number of docu­
nts, and to guarantee the quality of the selected publications, Table 5
s limited to the top 10 most cited articles related to the field under
dy by cluster. A content analysis was carried out by a meticulous


abstracts’ reading to guarantee that we selected contributions c
cerning the topic studied (HLT). Each document contains the numbe
total citations (TC), the TC per year and the normalized TC together w
two journal’s quality measures: SCImago Journal Rank (SJR) is a m
sure of the journal prestige calculated by considering the number
journal citations (Colledge et al., 2010); and the known Journal Citat
Report (JCR) ISI impact factor quartiles, which reflect the quotient o
journal’s rank in a scientific category and the total number of journal
the category (Garfield, 2006).
The top cited paper, which presents a news recommendation syste
was published by (J. Liu, Dolan, et al., 2010) and it is also the top ci
per year (32.9). Followed by, (Tandoc Jr, 2014) with 21 citations
year, that studies the impact of web analytics in the gatekeeping proc
And, the third most cited per year, (Carlson, 2014) presents a case stu
analysis about automated journalism. These studies indicate the m
significant research domains (RQ1) of the collection that contain so
of the most important keywords between 2018 and 2020 (see Fig.
such as, “recommender systems” or “artificial intelligence”.
In the collection, only 23 articles (4.4%) have more than five TC
year as the interest on DS in DJ is recent. As result, the comparison
older articles with newer only based in citations could exclude in
ential documents. Furthermore, _bibliometrix_ presents the normali
citation score of a document (NCS) calculated by dividing the act
count of citing items by the expected citation rate for documents w
the same year of publication (Aria & Cuccurullo, 2017). In our col
tion, 45 documents (8.6%) present value higher than 3 and 360 do
ments (70%) less than one. Thus, the top three highest NCS (13.8, 1
and 11.1) were published by (Haim et al., 2018; Lewis et al., 20
Schonlau & Zou, 2020), related to “personalization”, “journalism au
mation” and “statistical learning”. However, the last two are not
Table 5, as their TC is lower than the top ten articles of their clus
Nevertheless, both are mentioned in the literature map (see Fig. 12)
they present promising future research trends in journalism.


**5.** **Discussion and challenges**


In this section, the analysis conducted is based on the outcome fr
the procedure illustrated at Fig. 1. To answer the RQs, a deeper analy
across each cluster (see Fig. 9) allows to summarize the major top
(RQ1), benefits (RQ2) and gaps (RQ3) of DS applications in
Furthermore, we summarize the research by presenting a literature m
(see Fig. 12) that contains different levels of interactions, which are:
main domains found in the six clusters, DS topics of research in DJ a


**4.** (a) Geographic distribution of published articles by country-based scientific production (b) total citations (left y-axis at grey colour), country scieni
duction (blue) and average article citations (right y-axis at orange) in the 20th most cited countries (c) VOSviewer network visualization map of country
horship by average year of publication and number of publications (documents weights). (For interpretation of the references to color in this figure lege
reader is referred to the web version of this article.)


**le 4**
hors’ production over time from the top 20 authors that contributed with 73 documents.

**uthors’ Production** **2010** **2011** **2012** **2013** **2014** **2015** **2016** **2017** **2018** **2019** **2020** **Total** **H-** **G-** **Cluster of**
**ver time (Top 20)** **(#)** **index** **index** **collaboration**

cholas Belkin 1 1 1 1 1 1 6 6 6 10
uen-Ren Liu 1 1 3 5 2 2 9
ello Cristianini 1 2 1 1 5 4 5 2
bhijnan Chakraborty 1 1 1 1 4 2 3 14
ron Harambam 1 3 4 3 4 7
ndreas Lommatzsch 1 1 2 4 1 2 17
mon Fong 1 1 1 1 4 3 4 3
alf Steinberger 1 2 1 4 3 4 4
as Flaounas 1 2 1 4 3 4 2
eidar Davoudi 1 1 1 3 2 2 11
mitrios Bountouridis 3 3 3 3 7
cholas Diakopoulos 1 2 3 2 2 12
un-Cheng Chou 1 1 1 3 2 2 9
aptarshi Ghosh 1 1 1 3 2 3 14
arcel Broersma 1 2 3 2 3 8
iriam Boon 1 1 1 3 1 1 6
ch-Liˆen Doan 2 1 3 1 2 16
ichael J. Cole 1 1 1 3 3 3 10
mar Ali 1 1 1 3 3 3 2
jl De Bie 1 1 1 3 3 3 2
**otal (#)** 6 8 2 8 4 6 4 10 9 14 2 73
62%


me of the most relevant studies found in the SLR. The characteristics of
detected clusters are summarized as follows (across the text we use
abbreviations RQ1, RQ2 and RQ3 to signal each RQ answer):
Cluster 1 (“ **Exploratory studies and ML approaches** ”) contains 234
cles (46%), with the top author keywords being “online news”, “big
a”, “machine learning”, “opinion mining”, “personalization” and
dience engagement”. This cluster presents approaches for personal­
tion on information retrieval that include user behaviour analysis

le et al., 2011, 2015) (RQ1). Those studies use engagement metrics,
h as dwell time (Liu, et al., 2010) to analyze reader preferences and
sfaction (Lu et al., 2018), or to measure live events engagement
nz-Narrillos et al., 2020). Moreover, articles proposing new engage­
nt metrics are presented in this cluster, such as _viewport_ time (Lagun
Lalmas, 2016). On the other hand, approaches based on ML algo­
hms include linear log prediction model (Tatar et al., 2014) or random
ests to predict news popularity (Fernandes et al., 2015; Obiedat,
20) and to predict news’ shares (Schonlau & Zou, 2020) (RQ2).
wever, other engagement metrics could be used in predictive models,
h as the number of comments that could be an opportunity for future
earch (Davoudi et al., 2018) (RQ3).
Furthermore, this cluster contains the only sample article about an
ective function for optimal paywall decision making that shows the
evance of user engagement to increase subscription possibility (RQ2).
h result indicates that low research has been done about paywall
ution’s and their optimal design (Olsen et al., 2020; Rußell et al.,
20). Thus, improve digital business models in DJ is an opportunity for
ure research (Rußell et al., 2020) (RQ3).
The thematic evolution map (see Fig. 8) shows that, the most
quent keyword in the first cluster, “online news” evolved to “big
a”. In fact, big data technologies make the management of online
ws big data feasible (RQ2). However, the exponential increase of data
d the changes of reader behavior (Rußell et al., 2020) make some of
presented approaches limited with regard to their input. When
ling with real data, the future can be completely different from the
t. Indeed, one of the three types of uncertainties when dealing with
l forecasting situations is data uncertainty (Makridakis et al., 2020).
us, research on data sources and data quality in DJ can help to
prove DS models and results (RQ3).
This group contains 10 of the 20 articles with highest Normalized TC.
ey are not at Table 5, as they are recent, TC is less than the minimum
he top 10 in the cluster. Personalization (Haim et al., 2018), auto­
tion (S. Lewis et al., 2019), predict news shares (Schonlau & Zou,


2020), topic analysis in news (Canito et al., 2018), content analy
(Burggraaff & Trilling, 2017) are the main topics in the articles to
considered in the literature map presented at Fig. 12.
From the remaining five clusters, three are related to text analy
the third main domain on the literature map (Fig. 12).
Cluster 2 (“ **text mining - sentiment analysis** ”) contains 51 artic
with the top author keywords being “text mining”, “sentiment analy
and “natural language processing”. Those keywords are presented
blue, green and yellow at Fig. 10 indicating a line of research in
across the timespan (RQ1). Furthermore, 82% of the articles w
published since 2015 (see Fig. 9) proving the increasing interest on
approaches in the last five years. Approaches include topic model
methods to build emotional dictionaries (Rao et al., 2014), classificat
algorithms (Li et al., 2016; Manjesh et al., 2017; Rivera et al., 2014)
predictive models (Bai, 2011) (RQ2). Besides, this cluster contains t
articles that show the increasing interest on ML methods for automa
fact-checking (Azevedo, 2018; Indurthi et al., 2018) (RQ2). Both auth
agree that in the big data era there is an imperative need and a resea
opportunity on fake news detection to build reader confidence (RQ3
Clusters 4 and 5 (“Orange” and “Grey” at Fig. 12), defined as “ev
extraction” and “opinion mining” (see Fig. 9), contain 22 and 14 d
uments, respectively. Each cluster present less than four publications
year. Two of the top 20 most cited articles belong to these clusters, o
about event extraction (Hogenboom et al., 2011) and the other o
about news comments modeling (Tsagkias et al., 2010) (as presented
Table 5). Approaches for event mining include the use spatiotempo
features to provide localized future suggestions to the reader (Ho et
2012), the development of semantic information extraction to tr
occurrences and evolution of event dynamics (W. Wang & Stew
2015), and research on methods for event semantic extraction to reli
information overrun (Wang, 2012; Wang et al., 2010) (RQ2). Furth
more, approaches for opinion mining include multiple classif
(Haring et al., 2018; Lee ¨ & Ryu, 2019), _meta_ -comments or ERI
(engaging, respectful, and informative conversations) identificat
(Balali et al., 2013) (RQ2). Those studies prove the increasing imp
tance to better understand reader comments to improve rea
engagement (H¨aring et al., 2018) (RQ3). In fact, co-occurrences m
(see Fig. 11) present a clear line of research related to text mining fie
machine learning algorithms, natural language processing and big da
Clusters 3 and 6 (“Green” and “Yellow”) mainly focused on ne
recommendation and automated journalism, respectively (RQ1). Bo
present a slight increase of publications since 2016 that demonstra


**le 5**
ten most cited articles related to the feld under study by cluster.

**uster** **Authors, Year** **Title** **TC**
(rank
number)


**TC**
**per**
**Year**


**Normalized**
**TC**
(rank
number)


**Source** **IF** **SJR**
(highlighted top 10 sources) **201**


**- Exploratory**
**research and**
**detached ML**
**approaches N ¼ 234**


(Tandoc Jr, Journalism is twerking? How
2014) web analytics is changing the
process of gatekeeping


(Liu et al., Search behaviors in different task 82 (6th) **6.8** 2.3 (69th) Proceedings of the ACM
2010) types International Conference on
Digital Libraries


168 **21.0** **10.7 (6th)** New Media and Society 4.577 2.96
**(2nd)**


- 


(Fernandes A proactive intelligent decision
et al., 2015) support system for predicting the
popularity of online news

(Leetaru, 2011) Culturomics 2.0: Forecasting
Large-Scale human behavior
using global news media tone in
time and space


73 (7th) **10.4** 4.7 (22nd) **Lecture Notes in Computer** **—** 0.43
**Science**


63 **5.7** 3.1 (44th) First Monday - 0.7
(11th)


(Tatar et al., From popularity prediction to 61 **7.6** 3.9 (30th) Social Network Analysis and 0.398 0.4
2014) ranking online news (12th) Mining


(Haim et al., Burst of the Filter Bubble?:
2018) Effects of personalization on the
diversity of Google News


60 **15** **13.8 (1st)** **Digital Journalism** 4.476 2.69
(14th)


(Cole et al., Task and user effects on reading 50 4.5 2.5 (62th) Interacting with Computers 1.036 0.42
2011) patterns in information search (17th)


(Reis et al., Breaking the news: First
2015) impressions matter on online
news


- 


(Flaounas Research methods in the age of
et al., 2013) digital journalism: Massive-scale
automated analysis of
newscontent—topics, style and
gender

(Lagun and Understanding and measuring
Lalmas, 2016) user engagement and attention in
online news reading


48 **6.9** 3.1 (45th) Proceedings of the 9th
(18th) International Conference on Web
and Social Media, ICWSM 2015


48 **5.3** 2.8 (51st) **Digital Journalism** 4.476 2.69
(19th)


45 **7.5** 5.2 (16th) WSDM 2016 - Proceedings of the
(20th) 9th ACM International Conference
on Web Search and Data Mining


- 0.78


**- Text mining N ¼ 51** (Bai, 2011) Predicting consumer sentiments 141 **12.8** **7.1 (9th)** Decision Support Systems 4.721 1.92
from online text **(3rd)**


(Rao et al., Building emotional dictionary for 96 **(5th)** **12.0** 6.1 (15th) World Wide Web 2.892 0.53
2014) sentiment analysis of online news


(Christin, Algorithms in practice:
2017) Comparing web journalism and
criminal justice

(Du et al., Dirichlet-hawkes processes with
2015) applications to clustering
continuous-time document
streams


64 **12.8** **10.8 (5th)** Big Data and Society 4.577 3.25
(10th)


57 8.1 3.7 (31st) **Proceedings of the ACM SIGKDD**
(15th) **International Conference on**
**Knowledge Discovery and Data**
**Mining**


**—** 


(Burrows et al., Paraphrase acquisition via
2013) crowdsourcing and machine
learning


(Li et al., 2016) Hierarchical classification in text
mining for sentiment analysis of
online news

(Steinberger, A survey of methods to ease the
2012) development of highly
multilingual text mining
applications


41 4.6 2.4 (64th) ACM Transactions on Intelligent - 1.05
(24th) Systems and Technology


25 (41st) 4.1 2.9 (46th) Soft Computing 3.050 0.71


23 2.3 2.6 (57th) Language Resources and 1.014 0.44
(46th) Evaluation


(I. Flaounas The structure of the EU 23 (47 1.9 0.6 (197th) PLoS ONE - 1.02
et al., 2010) mediasphere th)


(Rivera et al., A text mining framework for
2014) advancing sustainability
indicators


19 (57 2.4 1.2 (129th) Environmental Modelling and 4.807 1.9
th) Software


(Zhu et al., Tracking the Evolution of Social
2014) Emotions: A Time-Aware Topic
Modeling Perspective


18 (60 2.3 1.1 (146th) **Proceedings - IEEE International**
th) **Conference on Data Mining,**
**ICDM**


395 (1st) **32.9** **11.1 (4th)** International Conference on
Intelligent User Interfaces,
Proceedings IUI


**- Recommendation** (Liu et al., Personalized news
**systems N ¼ 60** 2010) recommendation based on click
behavior


61 6.8 3.6 (35th) RecSys 2013 - Proceedings of the
(13th) 7th ACM Conference on
Recommender Systems

42 4.7 2.4 (63th) Journal of the American Society
(23rd) for Information Science and
Technology


(Garcin et al., Personalized news
2013) recommendation with context
trees

(O’Brien & Mixed-methods approach to
Lebow, 2013) measuring user experience in
online news interactions


**—** 0.79


- 0.59


- 

2.410 


(Montes-García 32 3.6 1.9 (85th) Expert Systems with Applications 5.452 1.49
et al., 2013) (30th)


( _continued on next pag_


**le 5** ( _continued_ )

**uster** **Authors, Year** **Title** **TC**
(rank
number)


**TC**
**per**
**Year**


**Normalized**
**TC**
(rank
number)


**Source** **IF** **SJR**
(highlighted top 10 sources) **201**


Towards a journalist-based news
recommendation system: The
Wesomender approach
(Yang, 2016) Effects of popularity-based news
recommendations (“mostviewed”) on users’ exposure to
online news

(Tang et al., An empirical study on
2016) recommendation with multiple
types of feedback


(Wang et al., Hybrid recommendation model
2017) based on incremental
collaborative filtering and
content-based algorithms


(Mizgajski & Affective recommender systems
Morzy, 2019) in online news industry: how
emotions influence reading
choices


10 3.3 3.9 (29th) IJCAI International Joint
(100th) Conference on Artificial
Intelligence


31 5.2 3.6 (34th) Media Psychology 2.397 1.86
(32nd)


20 3.3 2.3 (68th) **Proceedings of the ACM SIGKDD**
(55th) **International Conference on**
**Knowledge Discovery and Data**
**Mining**


**—** **—**


**—** **—**


15 (71st) 3.0 2.5 (59th) **Proceedings of the 2017 IEEE**
**21st International Conference**
**on Computer Supported**
**Cooperative Work in Design,**
**CSCWD 2017**


11 3.7 4.3 (25th) User Modeling and User-Adapted 4.682 1.57
(93rd) Interaction


(Wu et al., Neural news recommendation
2019) with attentive multi-view
learning


9 1.8 1.5 (114th) 26th International World Wide - (108th) Web Conference, WWW 2017


- 1.21


(Chakraborty Optimizing the recencyet al., 2019) relevancy trade-off in online
news recommendations


**- Event extraction N** (Hogenboom An overview of event extraction 66 (9th) 6.0 3.3 (38th) **CEUR Workshop Proceedings** **—** 0.18
**¼** **22** et al., 2011) from text


(Wang & Spatiotemporal and semantic
Stewart, 2015). information extraction from Web
news reports about natural
hazards

(Ho et al., Mining future spatiotemporal
2012) events and their sentiment from
online news articles for locationaware recommendation system


30 4.2 1.9 (81st) Computers, Environment and 4.655 1.36
(35th) Urban Systems


(Wang, 2012) Chinese news event 5W1H
semantic elements extraction for
event ontology population

(Wang et al., Extracting 5W1H event semantic
2010) elements from Chinese online
news


28 2.8 3.2 (40th) Proc. of the 1st ACM SIGSPATIAL
(36th) Int. Workshop on Mobile
Geographic Inf. Systems, MobiGIS
2012 - In Conjunction with the
20th ACM SIGSPATIAL Int. Conf.
on Advances in Geographic Inf.
Systems, GIS 2012

17 1.7 1.9 (82nd) WWW’12 - Proceedings of the 21st
(63rd) Annual Conference on World Wide
Web Companion

14 1.2 0.4 (237th) Lecture Notes in Computer Science
(79th) (including subseries Lecture Notes
in Artificial Intelligence and
Lecture Notes in Bioinformatics)


(Wang et al., Chinese news event 5W1H
2012) elements extraction using
semantic role labeling


7 (131st) 0.6 0.2 (280th) Proceedings − 3rd International
Symposium on Information
Processing, ISIP 2010


(Tessem & Supporting journalistic news 5 1.7 1.9 (80th) Proceedings - International
Opdahl, 2019) angles with models and analogies (150th) Conference on Research
Challenges in Information Science


(Zhang et al., RCFGED: Retrospective Coarse
2015) and Fine-Grained Event
Detection from Online News


(Fu et al., Mining Newsworthy Events in
2019) the Traffic Accident Domain from
Chinese Microblog

(Alashri et al., Snowball: Extracting Causal
2018) Chains from Climate Change Text
Corpora


5 0.6 0.3 (200th) Proceedings − 2015 IEEE
(159th) International Conference on
Systems, Man, and Cybernetics,
SMC 2015


3 1 1.2 (136th) International Journal of
(210th) Information Technology and
Decision Making


2 0.5 0.5 (217th) Proceedings − 2018 1st
(250th) International Conference on Data
Intelligence and Security


**—** **—**


**—** **—**


**—** 0.43


**—** 0.58


**—** **—**


**—** 0.00


1.894 0.41


**—** 0.21


**—** 0.43


**– Opinion mining N** (Tsagkias et al., News comments: Exploring, 73 (8th) 6.1 2.0 (75th) Lecture Notes in Computer Science
**¼** **14** 2010) modeling, and online prediction (including subseries Lecture Notes
in Artificial Intelligence and
Lecture Notes in Bioinformatics)


(Chung et al., Triggering participation:
2015) Exploring the effects of thirdperson and hostile media
perceptions on online
participation


24 3.4 1.6 (113th) **Computers in Human Behavior** 5.003 2.17
(44th)


(Chen & Ng, 23 1.9 2.7 (197th) **Computers in Human Behavior** 5.003 2.17
2016) (45th)


( _continued on next pag_


**le 5** ( _continued_ )

**uster** **Authors, Year** **Title** **TC**
(rank
number)


**TC**
**per**
**Year**


**Normalized**
**TC**
(rank
number)


**Source** **IF** **SJR**
(highlighted top 10 sources) **201**


Third-person perception of
online comments: Civil ones
persuade you more than me
(Chen & Ng, Nasty online comments anger
2017) you more than me, but nice ones
make me as happy as you

(Napoles et al., Automatically identifying good
2017) conversations online (yes, they
do exist!)

(Balali et al., A supervised approach for
2013) reconstructing thread structure
in comments on blogs and online
news agencies


13 2.6 2.2 (72nd) **Computers in Human Behavior** 5.003 2.17
(80th)


9 1.8 1.5 (115th) Proceedings of the 11th
(109th) International Conference on Web
and Social Media, ICWSM 2017


- 0.55


5 0.6 0.3 (257th) Computacion y Sistemas 0.620 0.19
(164th)


(Haring et al., ¨ Who is addressed in this
2018) comment? Automatically
classifying _meta_ -comments in
news comments


(Meguebli Towards better news article
et al., 2017) recommendation: With the help
of user comments

(Riedl et al., The downsides of digital labor:
2020) Exploring the toll incivility takes
on online comment moderators


3 0.8 0.7 (187th) Proceedings of the ACM on 5.120 0.54
(205th) Human-Computer Interaction


3 0.6 0.5 (206th) World Wide Web 2.892 0.46
(212th)


2 1 3.1 (42nd) **Computers in Human Behavior** 5.003 2.17
(235th)


2 0.7 0.8 (174th) Telematics and Informatics 4.139 1.44
(237th)


137 19.6 8.9 (8th) **Digital Journalism** 4.476 3.69
(4th)


(Lee & Ryu, Exploring characteristics of
2019) online news comments and
commenters with machine
learning approaches


**- Automated** (Carlson, 2014) The Robotic Reporter:
**journalism N ¼** **51** Automated journalism and the
redefinition of labor,
compositional forms, and
journalistic authority


22 2.8 1.4 (121st) **Journal of Mass Media Ethics:**
(50th) **Exploring Questions of Media**
**Morality**


(García-Avil´es, Online Newsrooms as
2014). Communities of Practice:
Exploring Digital Journalists’
Applied Ethics


0.867 0.54


(Melki & Block Her Entry, Keep Her Down
Mallat, 2016) and Push Her Out: Gender
discrimination and women
journalists in the Arab world

(Lehmkuhl & Constructing (un-)certainty: An
Peters, 2016) exploration of journalistic
decision-making in the reporting
of neuroscience


15 2.5 1.7 (93rd) **Journalism Studies** 2.345 1.51
(74th)


13 2.2 1.5 (116th) Public Understanding of Science 2.338 1.14
(81th)


12 (91st) 1.2 1.4 (125th) **Journalism Practice** 1.542 1.26


(Gravengaard
& Rimestad,
2012)


Elimination of ideas and
professional socialization:
Lessons learned at newsroom
meetings


(Yang et al., Perceived emotional intelligence 11 2.2 1.9 (86th) Conference on Human Factors in 5.23 0.67
2017) in virtual agents (94th) Computing Systems - Proceedings


(Lewis et al., Libel by Algorithm? Automated
2019) Journalism and the Threat of
Legal Liability

(Wu et al., When Journalism and
2019) Automation Intersect: Assessing
the Influence of the
Technological Field on
Contemporary Newsrooms

(Zheng et al., When algorithms meet
2018) journalism: The user perception
to automated news in a crosscultural context

(Galily, 2018) Artificial intelligence and sports
journalism: Is it a sweeping
change?


10 3.3 3.9 (27th) Journalism and Mass 1.706 1.66
(98th) Communication Quarterly


9 3.0 3.5 (36th) **Journalism Practice** 1.542 1.26
(106th)


9 2.3 2.1 (74th) **Computers in Human Behavior** 5.003 2.17
(107th)


7 1.8 1.6 (95th) Technology in Society 2.414 0.56
(123th)


increasing interest in simplify the content discovery (RQ2) and
vanced analytics approaches (Gonzalez Camacho & Alves-Souza,
18; Mizgajski & Morzy, 2019). Furthermore, there is an increasing
erest in understanding how AI can help to improve DJ (Carlson, 2014;
hmkuhl & Peters, 2016; Wu et al., 2019) (RQ3).
**News recommendation systems** development is a line of research


that evolved from algorithms based on click behaviour (Liu, et al., 20
to more advanced methods (Babanejad et al., 2020; Hazrati & Ela
2021). Approaches that use temporal features (Muralidhar et al., 201
movie and mobile solutions (Tewari et al., 2016; Viana & Soares, 201
collaborative filtering applications (Saranya & Sadasivam, 2017; Wa
et al., 2017) or neural networks to solve the cold-start problem (Misz


**Fig. 5.** _Bibliometrix_ collaboration network map between authors from 11 of the 26 clusters of authors.


**6.** Wordcloud of top 50 author’s keywords (the word size depends on
d occurrence).


decka et al., 2021) (RQ2). However, to explore other features such as,
article cost, the author level of engagement or the content propensity
nduce subscription, can be relevant in future research (RQ3).
In what **automated journalism** concerns, the most part of the ar­
es focus on exploratory studies (RQ1). Approaches focus on under­
nding ethical issues and the impact on the working practices of
rnalists in digital newsrooms (Carlson, 2014; García-Avil´es, 2014),
the potentialities and pitfalls for news organizations (S. C. Lewis
al., 2019), as well as analyze the user perception to automated news

eng et al., 2018). Finally, there are other studies related with specific
ics, such as: AI techniques to improve the organization, management
d distribution of content (Barriuso et al., 2016); or intelligent news
ots (Yang, 2020) to reduce routine tasks to prove the positive impact


of AI in DJ (RQ2). Moreover, there seems to exist a low emphasis on
use of AI to increase levels of reader engagement (RQ3). This is
interesting finding, revelling a gap on the research on how AI can aff
readers’ engagement (RQ3).
Across the SLR, we have demonstrated the main motivations a
positive impacts of DS use in DJ to improve reader engagement (R
and RQ2). For instance, exploratory web analytics studies and pract
ML applications improve reader experience and simplify content
covery, consequently, increases engagement metrics, such as tim
interactivity or _viewport_ time. Furthermore, applications on ne
popularity (Yang et al., 2020) forecast helps media companies to o
mize homepage decisions and maximize content distribution to acqu
and retain more readers. Moreover, TM applications by using sentim
analysis methods (Greco & Polli, 2020), event mining or opinion min
allow in understanding reader’s interests, helps to provide be
recommendation according to readers’ opinions and consequen
media platforms provide more content increasing recirculation and ti
per visit. We further note the increasing relevance of recommendat
systems to improve personalization (Gonzalez Camacho & Alves-Sou
2018). As well as the use of automated journalism to reduce rout
tasks and improve truly journalism.


**6.** **Potential research opportunities**


While there is an increasing need for data-driven approaches
journalism, the translation into ML approaches is still a complex t
(Davoudi, 2018). Our findings rise in the form of a list of key topics w
enhancements areas and future research opportunities (RQ3) listed


**7.** VOSviewer co-occurrences map of keywords based on the full-counting method with a minimum number of occurrences of a keyword 5. The size of the no
resent the relevance of the terms in the papers. The thickness of the lines means the bonding force between them. Finally, the colours indicate the average yea
cles publication that mention those keywords.


**Fig. 8.** _Bibliometrix_ thematic evolution map that demonstrates the evolution of keywords in two different stages (2010–2017, 2018–2020).


ows:
Big data: the establishment of new datasets sources in DJ is required
most of the research is being done with limited datasets (Von Bloh


et al., 2020). External data, like weather data or financial informati
can help to better understand readers’ patterns and behaviours, as w
as, to improve DS models that consequently improve reade


**Fig. 9.** Scientific Production by year and by cluster.


**10.** VOSviewer keywords co-occurrences map based on the full-counting method (cluster 2 - **“** text mining **”** ). The weight being visualized is the occurrence, t
en a keyword has a greater weight the label and bubble are bigger (Van Eck & Waltman, 2013).


gagement (Reno ´ & Reno, 2015´ ; Z. Yang, 2020).
Recommend Systems: most of the existing approaches focuses on
r’s clicks as the indicator to understand users’ interests either in, for


example, engagement business indicators. Therefore, further researc
required to explore innovative solutions, for example, to handle c
start problems, for multimedia content recommendations or to impr


**Fig. 11.** VOSviewer keywords co-occurrences map based on the full-counting method (cluster 4 - **“** event extraction **”** ).


l-time recommendations (Ficel et al., 2021; Hazrati & Elahi, 2021;
ayat et al., 2019).
Personalization: as users present a wide range of reader behaviours
Liu, Dolan, et al., 2010), the development of innovative DS algo­
hms to better personalize user experience by website page, by device,
channel or by content type, will improve engagement levels (Haim
al., 2018; Omar et al., 2020). Furthermore, AI can be a solution to
rease content engagement optimization (Kulkarni et al., 2019; Lim &
ang, 2022).
Content automation: one of the issues in the journalism ethics
alysis is to explore the advantages of content automation (Danzonambaud, 2021; S. C. Lewis et al., 2019; S. Wu et al., 2019). However,
invest in content automation can reduce routine tasks to improve
rnalism to the full potential (Carlson, 2014; Zheng et al., 2018).
thermore, further research is required to automate content in other
guages such as Spanish or Portuguese (Campos et al., 2020).
Fact-checking: as the information increases, the information credi­
ty and readers’ trustworthiness become a matter of concern. Thus,
lore new models on fake news detection is an opportunity of research
evedo, 2018; Meel & Vishwakarma, 2020; Shim et al., 2021).
Engagement metrics: further research is required to bridge the gap
ween reader engagement metrics and business goals (Davoudi et al.,
19). Thus, to explore others metrics, such as, sentiment perceived in
comments to develop better predictive models (chum prediction or
pensity to subscribe) can have a positive impact in the business
del (Davoudi, 2018; Lehmann et al., 2012; Seale, 2021).
Paywall mechanism/business model: as to the best of our scrutiny,
y (Davoudi, 2018) investigate an adaptive paywall mechanism by
ng advanced analytics. ML and AI can help to design and improve
re efficient paywall mechanisms. Furthermore, our study has shown
t there is still a research gap concerning to the use of more advanced
methods (e.g., Deep Learning (Goldani et al., 2021)). In fact, these i
dings are consisted with the work of (Davoudi, 2018), which argued
t that there is a gap between journalism and ML communities.


**7.** **Conclusion**


In this paper, we present a SLR analysis focused on the interact
between journalism, technology and data through the use of DS meth
(including AI and ML) to improve reader engagement, attempt
identify trends, knowledge gaps and to indicate propositions to fut
researches. A total of 541 articles gathered from the Scopus datab
and published from 2010 to 2021 were scrutinized. The large numbe
articles makes the usage of TM convenient for a better selection a
analysis of the literature. Bibliometric research and HTC were combin
to answer the RQs.
Generally, the findings show the hype of DS in DJ research, es
cially in the last three years, due to its potential to extract valuable
formation from big data. The SLR suggests that the literature about DS
DJ puts more emphasis on studying TM methods followed by reco
mendation systems. Furthermore, exploratory studies, web analy
and the impact of analytics in newsrooms are popular in the resear
Finally, we note there is still a research gap concerning to the use
more advanced DS methods (RQ3), e.g., Deep Learning (Goldani et
2021). In fact, these findings are consisted with the work of (Davou
2018), which argued that that there is a gap between journalism and
communities.
Currently, big data challenges (Yang, 2020), reader retent
(Suarez, 2020´ ), personalization and paywall models (Rußell et al., 20
are some of the major points of concern in the industry. Furthermo
more research is required to improve data sources, to explore enga
ment metrics, to develop models for fake news detection (Goldani et
2021), and to investigate innovative paywall models.
In terms of theoretical contributions, this paper presents an intens
literature review on the state of the art of DS in DJ, something that
the best of our knowledge, none intensive SLR in this field of resea
has been published before. Nevertheless, this SLR has some limitati
that also provides future research opportunities. Firstly, the literat
search was carried out only on documents published at Scop
Furthermore, non-English papers and book chapters were neglect


**Fig. 12.** Literature map.


us, future research can consider other scientific databases. Moreover,
s study proposes three research questions, other researchers may add
er questions. Then the final reading list can exclude important recent
earch papers as DS is a recent research field in DJ. Finally, nonentific literature published by respectful entities in the area, such as
MA could be included in future research to explore recent successful
use cases.
Hopefully, the results of this SLR can guide researchers in their
laboration with media companies in order to help publishers to
prove readers’ engagement through DS.


**claration of Competing Interest**


The authors declare that they have no known competing financial
erests or personal relationships that could have appeared to influence
work reported in this paper.


**ta availability**


Data will be made available on request.


_knowledgements_


This work was supported by the FCT - Fundaçao para a Ci˜ ˆencia e
nologia, under the Projects: UIDB/04466/2020, UIDP/04466/2020,
d UIDB/00319/2020.


**References**


Abdelmageed, S., & Zayed, T. (2020). A study of literature in modular integrated
construction - Critical review and future directions. _Journal of Cleaner Productio_
_277_ [, Article 124044. https://doi.org/10.1016/j.jclepro.2020.124044](https://doi.org/10.1016/j.jclepro.2020.124044)
Alashri, S., Tsai, J. Y., Koppela, A. R., & Davulcu, H. (2018). Snowball: Extracting cau
chains from climate change text corpora. _Proceedings - 2018 1st International_
_Conference on Data Intelligence and Security, ICDIS 2018_, 234–241. 10.1109/
ICDIS.2018.00045.
Amado, A., Cortez, P., Rita, P., & Moro, S. (2018). Research trends on Big Data in
Marketing: A text mining and topic modeling based literature analysis. _European_
_Research on Management and Business Economics, 24_ [(1), 1–7. https://doi.org/](https://doi.org/10.1016/j.iedeen.2017.06.002)
[10.1016/j.iedeen.2017.06.002](https://doi.org/10.1016/j.iedeen.2017.06.002)
Antonio, N., Almeida, A. de, ´ & Nunes, L. (2018). Predictive models for hotel bookin
cancellation: A semiautomated analysis of the literature. _Tourism & Management_
_Studies International Conference TMS Algarve_ .
Antoun, W., Baly, F., Achour, R., Hussein, A., & Hajj, H. (2020). State of the Art Mod
for Fake News Detection Tasks. _2020 IEEE International Conference on Informatic_
_IoT, and Enabling Technologies (ICIoT)_, 519–524.
Aria, M., & Cuccurullo, C. (2017). bibliometrix: An R-tool for comprehensive scienc
mapping analysis. _Journal of Informetrics, 11_ [(4), 959–975. https://doi.org/10.10](https://doi.org/10.1016/j.joi.2017.08.007)
[j.joi.2017.08.007](https://doi.org/10.1016/j.joi.2017.08.007)
Arrese, A. (2016). From Gratis to Paywalls: A brief history of a retro-innovation in t [´]
press’ s business. _Journalism Studies, 17_ [(8), 1051–1067. https://doi.org/10.1080](https://doi.org/10.1080/1461670X.2015.1027788)
[1461670X.2015.1027788](https://doi.org/10.1080/1461670X.2015.1027788)
Attfield, S., Kazai, G., & Lalmas, M. (2011). Towards a science of user engagement
(Position Paper). _WSDM Workshop on User Modelling for Web Applications._ [http:/](http://www.dcs.gla.ac.uk/%7emounia/Papers/engagement.pdf)
[www.dcs.gla.ac.uk/~mounia/Papers/engagement.pdf.](http://www.dcs.gla.ac.uk/%7emounia/Papers/engagement.pdf)
Azevedo, L. (2018). Truth or Lie: Automatically Fact Checking News. _The Web Confere_
_2018 - Companion of the World Wide Web Conference_ . _WWW, 2018_ [, 807–811. http](https://doi.org/10.1145/3184558.3186567)
[doi.org/10.1145/3184558.3186567](https://doi.org/10.1145/3184558.3186567)
[Babanejad, N., Agrawal, A., Davoudi, H., An, A., & Papagelis, M. (2020). Leveraging](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0050)
[emotion features in news recommendations.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0050) _INRA@ RecSys, 2554_, 70–78.
Bai, X. (2011). Predicting consumer sentiments from online text. _Decision Support_
_Systems, 50_ [(4), 732–742. https://doi.org/10.1016/j.dss.2010.08.024](https://doi.org/10.1016/j.dss.2010.08.024)


[li, A., Faili, H., Asadpour, M., & Dehghani, M. (2013). A supervised approach for](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0060)
[reconstructing thread structure in comments on blogs and online news agencies.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0060)
_[Computacion y Sistemas, 17](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0060)_ ´ (2), 207–217.
[ew, B. (2009). Elsevier’s Scopus® Database.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0065) _Journal of Electronic Resources in Medical_
_Libraries, 6_ [(3), 245–252.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0065)
[iuso, A. L., de La Prieta, F., Murciego, A. L., Hern](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0070) [´] ´andez, D., & Herrero, J. R. (2016).
[An Intelligent Agent-Based Journalism Platform.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0070) _International Conference on Practical_
_[Applications of Agents and Multi-Agent System](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0070)_, 322–332.
ges, A. F. S., Laurindo, F. J. B., Spínola, M. M., Gonçalves, R. F., & Mattos, C. A.
(2021). The strategic use of artificial intelligence in the digital era : Systematic
literature review and future research directions. _International Journal of Information_
_Management, 57_ [(September 2020), Article 102225. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.ijinfomgt.2020.102225)
[ijinfomgt.2020.102225](https://doi.org/10.1016/j.ijinfomgt.2020.102225)
us, P., Janssen, M., & Herder, P. (2020). The dual effects of the Internet of Things
(IoT): A systematic review of the benefits and risks of IoT adoption by organizations.
_International Journal of Information Management, 51_ (September 2018), Article
[101952. https://doi.org/10.1016/j.ijinfomgt.2019.05.008](https://doi.org/10.1016/j.ijinfomgt.2019.05.008)
[ggraaff, C., & Trilling, D. (2017). Through a different gate: An automated content](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0085)
[analysis of how online news and print news differ.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0085) _Journalism, 21_ (1), 112–129.

[ows, S., Potthast, M., & Stein, B. (2013). Paraphrase Acquisition via Crowdsourcing](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0090)
and Machine Learning. _[ACM Transactions on Intelligent Systems and Technology](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0090)_
_(TIST), 4_ [(3), 1–21.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0090)
mpos, J., Teixeira, A., Ferreira, T., Cozman, F., & Pagano, A. (2020). Towards Fully
Automated News Reporting in Brazilian Portuguese. _Anais Do XVII Encontro Nacional_
_de Intelig_ ˆ _encia Artificial e Computacional, 543_  - _554_ [. https://doi.org/10.5753/](https://doi.org/10.5753/eniac.2020.12158)
[eniac.2020.12158](https://doi.org/10.5753/eniac.2020.12158)
[ito, J., Ramos, P., Moro, S., & Rita, P. (2018). Unfolding the relations between](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0100)
[companies and technologies under the Big Data umbrella.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0100) _Computers in Industry, 99_,
[1–8.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0100)
[son, M. (2014). The Robotic Reporter Automated journalism and the redefinition of](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0105)
[labor, compositional forms, and journalistic authority.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0105) _Diital Journalism, 3_ (3),
[416–431.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0105)
kraborty, A., Ghosh, S., Ganguly, N., & Gummadi, K. P. (2019). Optimizing the
recency - relevance - diversity trade - offs in non - personalized news
recommendations. _Information Retrieval Journal, 22_ [(5), 447–475. https://doi.org/](https://doi.org/10.1007/s10791-019-09351-2)
[10.1007/s10791-019-09351-2](https://doi.org/10.1007/s10791-019-09351-2)
[n, G. M., & Ng, Y. M. M. (2016). Third-person perception of online comments: Civil](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0115)
ones persuade you more than me. _[Computers in Human Behavior, 55](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0115)_, 736–742.
[n, G. M., & Ng, Y. M. M. (2017). Nasty online comments anger you more than me, but](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0120)
nice ones make me as happy as you. _[Computers in Human Behavior, 71](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0120)_, 181–188.
stin, A. (2017). Algorithms in practice: Comparing web journalism and criminal
justice. _Big Data & Society_, _4_ (2), 2053951717718855.
[ng, M., Munno, G. J., & Moritz, B. (2015). Triggering participation: Exploring the](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0130)
[effects of third-person and hostile media perceptions on online participation.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0130)
_[Computers in Human Behavior, 53](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0130)_, 452–461.
o, M. J., Lopez-Herrera, A. G., Herrera-Viedma, E., & Herrera, F. (2011). Science ´
mapping software tools: Review, analysis, and cooperative study among tools.
_Journal of the American Society for Information Science and Technology, 62_ (7),
[1382–1402. https://doi.org/10.1002/asi.21525](https://doi.org/10.1002/asi.21525)

, M. J., Gwizdka, J., Liu, C., Bierig, R., Belkin, N. J., & Zhang, X. (2011). Task and
user effects on reading patterns in information search. _Interacting with Computers, 23_
[(4), 346–362. https://doi.org/10.1016/j.intcom.2011.04.007](https://doi.org/10.1016/j.intcom.2011.04.007)

, M. J., Hendahewa, C., Belkin, N. J., & Shah, C. (2015). User activity patterns during
information search. _ACM Transactions on Information Systems, 33_ [(1). https://doi.org/](https://doi.org/10.1145/2699656)
[10.1145/2699656](https://doi.org/10.1145/2699656)
edge, L., Moya-Anegon, Guerrero-Bote, V., L´ opez-illescas, C., Aisati, M., ´ & Moed, H.
(2010). SJR and SNIP : two new journal metrics in Elsevier ’ s Scopus. _Insights_, _23_ (3),
215–221.
per, H. (1998). _[Synthesizing research](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0155)_ . SAGE.

ez, P. (2014). _[Modern optimization with R](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0160)_ . Springer.
zon-Chambaud, S. (2021). A systematic review of automated journalism scholarship:
guidelines and suggestions for future research. _Open Research Europe_, _1_ (May), 4.
10.12688/openreseurope.13096.1.
oudi, H. (2018). _User Acquisition and engagement in digital News Media_ (Issue
December).
[oudi, H., An, A., & Edall, G. (2019). Content-based Dwell Time Engagement](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0175)
Prediction Model for News Articles. _[Conference of the North American Chapter of the](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0175)_
_[Association for Computational Linguistics: Human Language Technologies, 2](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0175)_, 226–233.
[oudi, H., An, A., Zihayat, M., & Edall, G. (2018). Adaptive Paywall Mechanism for](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0180)
Digital News Media Heidar. _[Proceedings of the ACM SIGKDD International Conference](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0180)_
_[on Knowledge Discovery and Data Mining, 2018](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0180)_ (205–214), 205–214.
oudi, H., & Edall, G. (2018). _Adaptive Paywall Mechanism for Digital News Media_ .
205–214.
thu, N., Kumar, S., Pandey, N., & Gupta, P. (2021). Forty years of the International
Journal of Information Management: A bibliometric analysis. _International Journal of_
_Information Management, 57_ [(December 2020), Article 102307. https://doi.org/](https://doi.org/10.1016/j.ijinfomgt.2020.102307)
[10.1016/j.ijinfomgt.2020.102307](https://doi.org/10.1016/j.ijinfomgt.2020.102307)
N., Farajtabar, M., Ahmed, A., Smola, A. J., & Song, L. (2015). Dirichlet-Hawkes
Processes with Applications to Clustering Continuous-Time Document Streams
Categories and Subject Descriptors. _21th ACM SIGKDD International Conference on_
_Knowledge Discovery and Data Mining_, 219–228.
[he, L. (2006). Theory and practise of the g-index.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0205) _Scientometrics, 69_, 131–152.
elke, K. M. (2019). Online participatory journalism: A systematic literature review.
_Media and Communication, 7_ [(4), 31–44. https://doi.org/10.17645/mac.v7i4.2250](https://doi.org/10.17645/mac.v7i4.2250)


[Fernandes, K., Vinagre, P., & Cortez, P. (2015). A Proactive Intelligent Decision Supp](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0220)
[System for Predicting the Popularity of Online News.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0220) _Portuguese Conference on_
_[Artificial Intelligence](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0220)_, 535–546.
Ficel, H., Haddad, M. R., & Baazaoui Zghal, H. (2021). A graph-based recommendat
approach for highly interactive platforms. _Expert Systems with Applications, 185_
[(May), Article 115555. https://doi.org/10.1016/j.eswa.2021.115555](https://doi.org/10.1016/j.eswa.2021.115555)
[Flaounas, I., Turchi, M., Ali, O., Fyson, N., De Bie, T., Mosdell, N., & Cristianini, N.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0230)
[(2010). The structure of the EU mediasphere.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0230) _PloS One, 5_ (12), 14243.
Flaounas, I., Ali, O., Lansdall-welfare, T., Bie, T. D., Lewis, J., Cristianini, N., … Bie, T
(2013). Research methods in the age of digital journalism: Massive-scale automa
analysis of news-content—topics, style and gender. _Digital Journalism, 1_ (1), 102–1
[https://doi.org/10.1080/21670811.2012.714928](https://doi.org/10.1080/21670811.2012.714928)
[Fu, X., Lee, J., Yan, C., & Gao, L. (2019). Mining newsworthy events in the traffic](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0240)
[accident domain from Chinese microblog.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0240) _International Journal of Information_
_[Technology & Decision Making](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0240)_, 717–742.
[Galily, Y. (2018). Artificial intelligence and sports journalism: Is it a sweeping chan](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0245)
_[Technology in Society, 54](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0245)_, 47–51.
[García-Avil´es, J. A. (2014). Online Newsrooms as Communities of Practice: Explorin](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0250)
Digital Journalists’ Applied Ethics. _[Journal of Mass Media Ethics, 29](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0250)_ (4), 258–272
Garcin, F., Dimitrakakis, C., & Faltings, B. (2013). Personalized News Recommendat
with Context Trees. _Proceedings of the 7th ACM Conference on Recommender Syste_
105–112.
[Garfield, E. (2006). The history and meaning of the journal impact factor.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0260)
_JAMA_  - _[Journal of the American Medical Association, 295](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0260)_ (1), 90–93.
Gil, M., Wrobel, K., Montewka, J., & Goerlandt, F. (2020). A bibliometric analysis a´
systematic review of shipboard Decision Support Systems for accident preventio
_Safety Science, 128_ [(March), Article 104717. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.ssci.2020.104717)
[ssci.2020.104717](https://doi.org/10.1016/j.ssci.2020.104717)
Goldani, M. H., Safabakhsh, R., & Momtazi, S. (2021). Convolutional neural networ
with margin loss for fake news detection. _Information Processing and Management,_
[(1), Article 102418. https://doi.org/10.1016/j.ipm.2020.102418](https://doi.org/10.1016/j.ipm.2020.102418)
Gonzalez Camacho, L. A., & Alves-Souza, S. N. (2018). Social network data to allevi
cold-start in recommender system: A systematic review. _Information Processing a_
_Management, 54_ [(4), 529–544. https://doi.org/10.1016/j.ipm.2018.03.004](https://doi.org/10.1016/j.ipm.2018.03.004)
Gordon, A. D. (1999). _Cassification_ [(2nd Edition). Chapman & Hall/CRC.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0280)
[Gravengaard, G., & Rimestad, L. (2012). Elimination of ideas and professional](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0285)
[socialisation: Lessons learned at newsroom meetings.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0285) _Journalism Practice, 6_ (4),
[465–481.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0285)
Greco, F., & Polli, A. (2020). Emotional Text Mining: Customer profiling in brand
management. _International Journal of Information Management, 51_ (April 2019),
[Article 101934. https://doi.org/10.1016/j.ijinfomgt.2019.04.007](https://doi.org/10.1016/j.ijinfomgt.2019.04.007)
Haim, M., Graefe, A., Brosius, H., Haim, M., Graefe, A., & Brosius, H. (2018). Burst of
Filter Bubble ? Effects of personalization on the diversity of Google News. _Digita_
_Journalism, 6_ [(3), 330–343. https://doi.org/10.1080/21670811.2017.1338145](https://doi.org/10.1080/21670811.2017.1338145)
H¨aring, M., Loosen, W., & Maalej, W. (2018). Who is addressed in this comment?
Automatically classifying meta-comments in news comments. _Proceedings of the A_
_on Human-Computer Interaction_, 1–20.
Hazrati, N., & Elahi, M. (2021). Addressing the New Item problem in video recommen
systems by incorporation of visual features with restricted Boltzmann machines
_Expert Systems, 38_ [(3), 1–20. https://doi.org/10.1111/exsy.12645](https://doi.org/10.1111/exsy.12645)
[Hirsch, J. E. (2005). An index to quantify an individual’s scientific research output.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0310)
_[Proceedings of the National Academy of Sciences, 102](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0310)_ (46), 16569–16572.
Ho, S. S., Lieberman, M., Wang, P., & Samet, H. (2012). Mining future spatiotempo
events and their sentiment from online news articles for location-aware
recommendation system. _Proceedings of the First ACM SIGSPATIAL International_
_Workshop on Mobile Geographic Information Systems_, 25–32.
Hogenboom, F., Frasincar, F., Kaymak, U., & De Jong, F. (2011). An overview of ev
extraction from text. _DeRiVE@ ISWC_, 48–57.
Indurthi, V., Oota, S. R., Gupta, M., & Varma, V. (2018). Believe it or not! Identifyin
bizarre news in online news media. _ACM International Conference Proceeding Ser_
_257_  - _264_ [. https://doi.org/10.1145/3152494.3152524](https://doi.org/10.1145/3152494.3152524)
International News Media Association, I. (2022). _The Benefits and Risks of Media Dat_
_Democratisation_ (Issue January).
J¨a¨askelainen, A., Taimela, E., ¨ & Heiskanen, T. (2020). Predicting the success of new
Using an ML-based language model in predicting the performance of news artic
before publishing. _Proceedings of the 23rd International Conference on Academic_
_Mindtrek_, 27–36. 10.1145/3377290.3377299.
Jin, R., Gao, S., Cheshmehzangi, A., & Aboagye-Nimo, E. (2019). A holistic review o
public-private partnership literature published between 2008 and 2018. _Journal_
_Cleaner Production, 202_ [, 1202–1219. https://doi.org/10.1155/2019/7094653](https://doi.org/10.1155/2019/7094653)
Ksiazek, T. B., Peer, L., & Lessard, K. (2016). User engagement with online news:
Conceptualizing interactivity and exploring the relationship between online new
videos and user comments. _New Media and Society, 18_ [(3), 502–520. https://doi.o](https://doi.org/10.1177/1461444814545073)
[10.1177/1461444814545073](https://doi.org/10.1177/1461444814545073)
Kulkarni, H., Joshi, T., Sanap, N., Kalyanpur, R., & Marathe, M. (2019). Personalize
newspaper based on emotional traits using machine learning. _Proceedings - 2019_
_International Conference on Computing, Communication Control and Automation,_
_ICCUBEA 2019_ . 10.1109/ICCUBEA47591.2019.9128691.
Lagun, D., & Lalmas, M. (2016). Understanding and measuring user engagement an
attention in online news reading. _WSDM 2016 - Proceedings of the 9th ACM_
_International Conference on Web Search and Data Mining_, _22_   - _25_, 113–122. 10.114
2835776.2835833.
[Lee, S. Y., & Ryu, M. H. (2019). Exploring characteristics of online news comments](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0360)
[commenters with machine learning approaches.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0360) _Telematics and Informatics, 43_
[(101249).](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0360)


aru, K. (2011). _[Culturomics 2.0: Forecasting Large-Scale human behavior using global](http://refhub.elsevier.com/S0957-4174(23)00296-8/optur4xEWQC6q)_
_[news media tone in time and space](http://refhub.elsevier.com/S0957-4174(23)00296-8/optur4xEWQC6q)_ . First Monday.
mann, J., Lalmas, M., Yom-Tov, E., & Dupret, G. (2012). Models of user engagement.
In _Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial_
_Intelligence and Lecture Notes in Bioinformatics)_ [(pp. 164–175). Springer. https://doi.](https://doi.org/10.1007/978-3-642-31454-4_14)
[org/10.1007/978-3-642-31454-4_14.](https://doi.org/10.1007/978-3-642-31454-4_14)
[mkuhl, M., & Peters, H. P. (2016). Constructing (un-) certainty: An exploration of](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0370)
[journalistic decision-making in the reporting of neuroscience.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0370) _Public Understanding of_
_Science, 25_ [(8), 909–926.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0370)
is. (2015). Journalism In An Era Of Big Data Cases, concepts, and critiques. _Digital_
_Journalism_, _3_ (3), 321–330. 10.1080/21670811.2014.976399.
[is, S. C., Sanders, A. K., & Carmody, C. (2019). Libel by Algorithm? Automated](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0380)
[Journalism and the Threat of Legal Liability.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0380) _Journalism & Mass Communication_
_[Quarterly, 96](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0380)_ (1), 60–81.
[is, S., Guzman, A., & Schmidt, T. (2019). Automation, Journalism, and Human-](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0385)
[Machine Communication: Rethinking Roles and Relationships of Humans and](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0385)
Machines in News. _[Digital Journalism, 7](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0385)_ (4), 409–427.
[., Fong, S., Zhuang, Y., & Khoury, R. (2016). Hierarchical classification in text mining](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0390)
[for sentiment analysis of online news.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0390) _Soft Computing, 20_ (9), 3411–3420.
J. S., & Zhang, J. (2022). Adoption of AI-driven personalization in digital news
platforms: An integrative model of technology acceptance and perceived
contingency. _Technology in Society, 69_ [(February), Article 101965. https://doi.org/](https://doi.org/10.1016/j.techsoc.2022.101965)
[10.1016/j.techsoc.2022.101965](https://doi.org/10.1016/j.techsoc.2022.101965)

Cole, M., Liu, C., Bierig, R., Gwizdka, J., & Belkin, N. (2010). Search Behaviors in
Different Task Types. _Proceedings of the 10th Annual Joint Conference on Digital_
_Libraries._, 69–78.
D. R., Chen, K. Y., Chou, Y. C., & Lee, J. H. (2018). Online recommendations based
on dynamic adjustment of recommendation lists. _Knowledge-Based Systems, 161_,
[375–389. https://doi.org/10.1016/j.knosys.2018.07.038](https://doi.org/10.1016/j.knosys.2018.07.038)
J., Dolan, P., & Pedersen, E. R. (2010). Personalized news recommendation based on
click behavior. _Proceedings of the 15th International Conference on Intelligent User_
_Interfaces_, 31–40.
H., Zhang, M., & Ma, S. (2018). Between clicks and satisfaction: Study on multi-phase
user preferences and satisfaction for online news reading. _41st International ACM_
_SIGIR Conference on Research and Development in Information Retrieval, SIGIR 2018_,
435–444. 10.1145/3209978.3210007.
ridakis, S., Hyndman, R. J., & Petropoulos, F. (2020). Forecasting in social settings:
The state of the art. _International Journal of Forecasting, 36_ [(1), 15–28. https://doi.](https://doi.org/10.1016/j.ijforecast.2019.05.011)
[org/10.1016/j.ijforecast.2019.05.011](https://doi.org/10.1016/j.ijforecast.2019.05.011)
jesh, S., Kanakagiri, T., Vaishak, P., Chettiar, V., & Shobha, G. . (2017). Clickbait
pattern detection and classification of news headlines using natural language
processing. _2nd International Conference on Computational Systems and Information_
_Technology for Sustainable Solution (CSITSS)_ .
l, P., & Vishwakarma, D. K. (2020). Fake news, rumor, information pollution in social
media and web: A contemporary survey of state-of-the-arts, challenges and
opportunities. _Expert Systems with Applications, 153_ [, Article 112986. https://doi.org/](https://doi.org/10.1016/j.eswa.2019.112986)
[10.1016/j.eswa.2019.112986](https://doi.org/10.1016/j.eswa.2019.112986)
[uebli, Y., Kacimi, M., Doan, B. L., & Popineau, F. (2017). Towards better news article](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0435)
recommendation. _[World Wide Web, 20](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0435)_ (6), 1293–1312.
[ki, J. P., & Mallat, S. E. (2016). Block Her Entry, Keep Her Down and Push Her Out:](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0440)
[Gender discrimination and women journalists in the Arab world.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0440) _Journalism Studies,_
_17_ [(1), 57–79.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0440)
sey, R. D., Malthouse, E. C., & Calder, B. J. (2010). Engagement with online media.
_Journal of Media Business Studies, 7_ [(2), 39–56. https://doi.org/10.1080/](https://doi.org/10.1080/16522354.2010.11073506)
[16522354.2010.11073506](https://doi.org/10.1080/16522354.2010.11073506)
[ztal-Radecka, J., Indurkhya, B., & Smywinski-Pohl, A. (2021). Meta-User2Vec model ´](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0450)
[for addressing the user and item cold-start problem in recommender systems.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0450) _User_
_[Modeling and User-Adapted Interaction, 31](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0450)_ (2), 261–286.
gajski, J., & Morzy, M. (2019). Affective recommender systems in online news
industry : How emotions influence reading choices. _User Modeling and User-Adapted_
_Interaction, 29_ [(2), 345–379. https://doi.org/10.1007/s11257-018-9213-x](https://doi.org/10.1007/s11257-018-9213-x)
ntes-García, A., Alvarez-Rodríguez, J. M., Labra-Gayo, J. E., & Martínez-Merino, M. [´]
(2013). Towards a journalist-based news recommendation system: The Wesomender
approach. _Expert Systems with Applications, 40_ [(17), 6735–6741. https://doi.org/](https://doi.org/10.1016/j.eswa.2013.06.032)
[10.1016/j.eswa.2013.06.032](https://doi.org/10.1016/j.eswa.2013.06.032)
o, S., Cortez, P., & Rita, P. (2015). Business intelligence in banking: A literature
analysis from 2002 to 2013 using text mining and latent Dirichlet allocation. _Expert_
_Systems with Applications, 42_ [(3), 1314–1324. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.eswa.2014.09.024)
[eswa.2014.09.024](https://doi.org/10.1016/j.eswa.2014.09.024)
alidhar, N., Rangwala, H., & Han, E.-H. S. (2015). Recommending Temporally
Relevant News Content from Implicit Feedback Data. _2015 IEEE 27th International_
_Conference on Tools with Artificial Intelligence (ICTAI)_, 689–696. 10.1109/
ICTAI.2015.104.
[lylahti, M. (2017). We need to talk about metrics. In](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0475) _Themes and debates in_
_contemporary journalism_ [(pp. 87–103). Cambridge: Cambridge Scholar Publishing.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0475)
oles, C., Pappu, A., & Tetreault, J. (2017). Automatically identifying good
conversations online (yes, they do exist!). _Proceedings of the International AAAI_
_Conference on Web and Social Media_, _11_ (1).
wman, N., Fletcher, R., Kalogeropoulos, A., & Nielsen, R. K. (2019). _Reuters Institute_
_Digital News Report 2019_ .
rien, D., Wellbrock, C. M., & Kleer, N. (2020). Content for Free? Drivers of Past
Payment, Paying Intent and Willingness to Pay for Digital Journalism–A Systematic
Literature Review. _Digital Journalism, 8_ [(5), 643–672. https://doi.org/10.1080/](https://doi.org/10.1080/21670811.2020.1770112)
[21670811.2020.1770112](https://doi.org/10.1080/21670811.2020.1770112)


O’Brien, H. L., & Lebow, M. (2013). Mixed-Methods Approach to Measuring User
Experience in Online News Interactions. _Journal of the American Society for_
_Information Science and Technology, 64_ [(8), 1543–1556. https://doi.org/10.1002/](https://doi.org/10.1002/asi)
[Obiedat, R. (2020). Predicting the popularity of online news using classification meth](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0500)
with feature filtering techniques. _[Journal of Theoretical and Applied Information](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0500)_
_Technology, 98_ [(8), 1163–1172.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0500)
Olsen, R. K., Kammer, A., Solvoll, M. K., & Olsen, R. K. (2020). Paywalls ’ Impact o
Local News Websites ’. _Traffic and Their Civic and Business Implications., 9699_ .
[https://doi.org/10.1080/1461670X.2019.1633946](https://doi.org/10.1080/1461670X.2019.1633946)
Omar, N., Omar, Y. M. K., & Maghraby, F. A. (2020). Machine Learning Model for
Personalizing Online Arabic Journalism. _Machine Learning_, _11_ (4). 10.14569/
IJACSA.2020.0110484.
Pattabhiramaiah, A., Sriram, S., & Manchanda, P. (2019). Paywalls: Monetizing onli
content. _Journal of Marketing, 83_ [(2), 19–36. https://doi.org/10.1177/](https://doi.org/10.1177/0022242918815163)
[0022242918815163](https://doi.org/10.1177/0022242918815163)
[Peterson, E. T., & Carrabis, J. (2008). Measuring the Immeasurable: Visitor Engageme](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0520)
_[Web Analytics Demystified, 14](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0520)_ (16).
[Rao, Y., Lei, J., Wenyin, L., Li, Q., & Chen, M. (2014). Building emotional dictionary](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0525)
[sentiment analysis of online news.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0525) _World Wide Web, 17_ (4), 723–742.
[Reis, J., Olmo, P., Prates, R., Kwak, H., & An, J. (2015). Breaking the News : First](http://refhub.elsevier.com/S0957-4174(23)00296-8/optfsbNLpwScj)
Impressions Matter on Online News. _[Proceedings of the International AAAI Confere](http://refhub.elsevier.com/S0957-4174(23)00296-8/optfsbNLpwScj)_
_[on Web and Social Media, 9](http://refhub.elsevier.com/S0957-4174(23)00296-8/optfsbNLpwScj)_ (1), 357–366.
[Rendon, E., Abundez, I. M., Gutierrez, C., Díaz, S., Arizmendi, A., Quiroz, E. M., & H´](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0530)
[a.. (2011). A comparison of internal and external cluster validation indexes. In](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0530)
_[Proceedings of the 5th WSEAS International Conference on Computer Engineering an](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0530)_
_Applications_ [(pp. 158–163).](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0530)
Reno, D., & Ren´ o, L. (2015). The newsroom, Big Data and social media as informati´
sources. _Estudios Sobre El Mensaje Periodistico, 21_ [(21), 131–142. https://doi.org/](https://doi.org/10.5209/rev_ESMP.2015.v21.51135)
[10.5209/rev_ESMP.2015.v21.51135](https://doi.org/10.5209/rev_ESMP.2015.v21.51135)
[Riedl, M. J., Masullo, G. M., & Whipple, K. N. (2020). The downsides of digital labo](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0540)
[Exploring the toll incivility takes on online comment moderators.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0540) _Computers in_
_[Human Behavior, 107](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0540)_ (106262).
Rivera, S. J., Minsker, B. S., Work, D. B., & Roth, D. (2014). A text mining framework
advancing sustainability indicators. _Environmental Modelling and Software, 62_,
[128–138. https://doi.org/10.1016/j.envsoft.2014.08.016](https://doi.org/10.1016/j.envsoft.2014.08.016)
Romero, L., & Portillo-Salido, E. (2019). Trends in sigma-1 receptor research: A 25-y
bibliometric analysis. _Frontiers in Pharmacology, 10_ [(MAY). https://doi.org/10.33](https://doi.org/10.3389/fphar.2019.00564)
[fphar.2019.00564](https://doi.org/10.3389/fphar.2019.00564)
Rußell, R., Berger, B., Stich, L., Hess, T., & Spann, M. (2020). Monetizing Online Conte
Digital Paywall Design and Configuration. _Business & Information Systems Engineer_
_1_  - _8_ [. https://doi.org/10.1007/s12599-020-00632-5](https://doi.org/10.1007/s12599-020-00632-5)
[Sanz-Narrillos, M., Masneri, S., & Zorrilla, M. (2020). Combining video and wireless](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0560)
[signals for enhanced audience analysis.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0560) _International Conference on Agents and_
_[Artificial Intelligence](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0560)_, 151–161.
[Sapian, A., & Vyshnevska, M. (2019). The marketing funnel as an effective way of a](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0565)
business strategy. _Λ_ Ό _[ГOΣ. The Art of Scientific Mind, 4](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0565)_, 16–18.
[Saranya, K. G., & Sadasivam, G. S. (2017). Personalized news article recommendatio](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0570)
[with novelty using collaborative filtering based rough set theory.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0570) _Mobile Networ_
_[and Applications, 22](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0570)_ (4), 719–729.
[Schonlau, M., & Zou, R. Y. (2020). The random forest algorithm for statistical learni](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0575)
_[The Stata Journal, 20](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0575)_ (1), 3–29.
Seale, S. (2021). How Wall Street Journal uses metrics and engagement to drive dig
subscriptions. _INMA International News Media Association._ [https://www.inma.org](https://www.inma.org/blogs/conference/post.cfm/how-wall-street-journal-uses-metrics-and-enagagement-to-drive-digital-subscriptions)
[blogs/conference/post.cfm/how-wall-street-journal-uses-metrics-and-enagageme](https://www.inma.org/blogs/conference/post.cfm/how-wall-street-journal-uses-metrics-and-enagagement-to-drive-digital-subscriptions)
[nt-to-drive-digital-subscriptions.](https://www.inma.org/blogs/conference/post.cfm/how-wall-street-journal-uses-metrics-and-enagagement-to-drive-digital-subscriptions)
Shim, J. S., Lee, Y., & Ahn, H. (2021). A link2vec-based fake news detection model us
web search results. _Expert Systems with Applications, 184_ (June), Article 115491.
[https://doi.org/10.1016/j.eswa.2021.115491](https://doi.org/10.1016/j.eswa.2021.115491)
Silge, J., & Robinson, D. (2019). _Text Mining with R - A Tidy Approach_ . O’Reilly.
Simon, A. F. M., & Graves, L. (2019). _Pay Models for Online News in the US and Euro_
_2019 Update_ . _May_, 1–16.
Souza Freire, P. M., Matias da Silva, F. R., & Goldschmidt, R. R. (2021). Fake news
detection based on explicit and implicit signals of a hybrid crowd: An approach
inspired in meta-learning. _Expert Systems with Applications, 183_ [(February). https](https://doi.org/10.1016/j.eswa.2021.115414)
[doi.org/10.1016/j.eswa.2021.115414](https://doi.org/10.1016/j.eswa.2021.115414)
Steensen, S., Ferrer-Conill, R., & Peters, C. (2020). (Against a) Theory of Audience
Engagement with News. _Journalism Studies, 20_ [, 1–19. https://doi.org/10.1080/](https://doi.org/10.1080/1461670X.2020.1788414)
[1461670X.2020.1788414](https://doi.org/10.1080/1461670X.2020.1788414)
Steinberger, R. (2012). A survey of methods to ease the development of highly
multilingual text mining applications. _Language Resources and Evaluation, 46_ (2),
[155–176. https://doi.org/10.1007/s10579-011-9165-9](https://doi.org/10.1007/s10579-011-9165-9)
[Su´arez, E. (2020). How to build a successful subscription news business.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0615) _lessons from_
_[Britain and Spain (Issue February)](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0615)_ .
Tandoc, E. C., Jr (2014). Journalism is twerking ? How web analytics is changing th
process of gatekeeping. _New Media & Society, 16_ [(4), 559–575. https://doi.org/](https://doi.org/10.1177/1461444814530541)
[10.1177/1461444814530541](https://doi.org/10.1177/1461444814530541)
[Tang, L., Long, B., Chen, B. C., & Agarwal, D. (2016). An empirical study on](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0625)
[recommendation with multiple types of feedback. In](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0625) _22nd ACM SIGKDD Internatio_
_[Conference on Knowledge Discovery and Data Mining](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0625)_ (pp. 283–292).
Tatar, A., Antoniadis, P., De Amorim, M. D., & Fdida, S. (2014). From popularity
prediction to ranking online news. _Social Network Analysis and Mining, 4_ (1), 174
[https://doi.org/10.1007/s13278-014-0174-8](https://doi.org/10.1007/s13278-014-0174-8)
Tessem, B., & Opdahl, A. L. (2019). Supporting journalistic news angles with models
analogies. _Proceedings - International Conference on Research Challenges in Informa_
_Science, 1_   - _7_ [. https://doi.org/10.1109/RCIS.2019.8877058](https://doi.org/10.1109/RCIS.2019.8877058)


[ari, A. S., Yadav, N., & Barman, A. G. (2016). Efficient tag based personalised](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0640)
[collaborative movie reccommendation system. In](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0640) _2016 2nd International Conference_
_[on Contemporary Computing and Informatics (IC3I)](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0640)_ (pp. 95–98).
[gkias, M., Weerkamp, W., & De Rijke, M. (2010). News comments: Exploring,](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0645)
modeling, and online prediction. _[European Conference on Information Retrieval](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0645)_,
[191–203.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0645)
Eck, N. J., & Waltman, L. (2010). Software survey: VOSviewer, a computer program
for bibliometric mapping. _Scientometrics, 84_ [(2), 523–538. https://doi.org/10.1007/](https://doi.org/10.1007/s11192-009-0146-3)
[s11192-009-0146-3](https://doi.org/10.1007/s11192-009-0146-3)

Eck, N. J., & Waltman, L. (2013). VOSviewer manual. In Univeristeit Leiden (Issue
[February). http://www.vosviewer.com/documentation/Manual_VOSviewer_1.6.1.](http://www.vosviewer.com/documentation/Manual_VOSviewer_1.6.1.pdf)
[pdf.](http://www.vosviewer.com/documentation/Manual_VOSviewer_1.6.1.pdf)
[na, P., & Soares, M. (2016). A hybrid recommendation system for news in a mobile](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0655)
environment. In _[6th International Conference on Web Intelligence, Mining and Semantics](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0655)_
[(pp. 1–9).](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0655)
, M., & Picard, R. G. (2019). Transformation and Innovation of Media Business
Models. In _Making Media: production, Practices, and Professions_ (pp. 121–132).
Bloh, J., Broekel, T., Ozgun, B., & Sternberg, R. (2020). New(s) data for [¨]
entrepreneurship research? An innovative approach to use Big Data on media
coverage. _Small Business Economics, 55_ [(3), 673–694. https://doi.org/10.1007/](https://doi.org/10.1007/s11187-019-00209-x)
[s11187-019-00209-x](https://doi.org/10.1007/s11187-019-00209-x)
[ng, H., Zhang, P., Lu, T., Gu, H., & Gu, N. (2017). Hybrid Recommendation Model](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0670)
[Based on Incremental Collaborative Filtering and Content- based Algorithms. In](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0670)
_[2017 IEEE 21st International Conference on Computer Supported Cooperative Work in](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0670)_
_[Design (CSCWD)](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0670)_ (pp. 337–342).
[ng, W. (2012). Chinese news event 5W1H semantic elements extraction for event](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0675)
ontology population. In _[Proceedings of the 21st International Conference on World Wide](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0675)_
_Web_ [(pp. 197–202).](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0675)
[ng, W., & Stewart, K. (2015). Spatiotemporal and semantic information extraction](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0680)
[from Web news reports about natural hazards.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0680) _Computers, Environment and Urban_
_[Systems, 50](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0680)_, 30–40.
[ng, W., Zhao, D., Zou, L., Wang, D., & Zheng, W. E. (2010). Extracting 5W1H event](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0685)
[semantic elements from Chinese online news.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0685) _International Conference on Web-Age_
_[Information Management](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0685)_, 644–655.
ng, Wei, Zhao, D., & Wang., D. (2012). Chinese news event 5W1H elements extraction
using semantic role labeling. _2010 Third International Symposium on Information_
_Processing_, 484–489. 10.1145/2187980.2188008.
ster, J., & Watson, R. (2002). Analyzing the past to prepare for the future: writing a
literature review. _MIS Quarterly_, _2_, xiii–xxiii. 10.1016/j.freeradbiomed.2005.02.032.
bers, K., Amsterdam, V. U., Atteveldt, W. V., Amsterdam, V. U., & Benoit, K. (2017).
Text Analysis in R. _Communication Methods and Measures, 11_ [(4), 245–265. https://](https://doi.org/10.1080/19312458.2017.1387238)
[doi.org/10.1080/19312458.2017.1387238](https://doi.org/10.1080/19312458.2017.1387238)
[C., Wu, F., An, M., Huang, J., Huang, Y., & Xie, X. (2019). Neural News](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0705)
[Recommendation with Attentive Multi-View Learning.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0705) _IJCAI International Joint_
_[Conference on Artificial Intelligence, 1907](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0705)_, 05576.


[Wu, S., Tandoc, E. C., Jr, & Salmon, C. T. (2019). When journalism and automation](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0710)
[intersect: Assessing the influence of the technological field on contemporary](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0710)
newsrooms. _[Journalism Practice, 13](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0710)_ (10), 1238–1254.
Yang, J. A. (2016). Effects of popularity-based news recommendations (“most-viewe
on users’ exposure to online news. _Media Psychology, 19_ [(2), 243–271. https://d](https://doi.org/10.1080/15213269.2015.1006333)
[org/10.1080/15213269.2015.1006333](https://doi.org/10.1080/15213269.2015.1006333)
[Yang, W. (2020). Ux Design of Artificial Intelligence News Robot.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0720) _IOP Conference Ser_
_[Materials Science and Engineering, 740](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0720)_ (1), Article 012135.
[Yang, Y., Ma, X., & Fung, P. (2017). Perceived emotional intelligence in virtual agents](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0725)
_[Proceedings of the 2017 CHI Conference Extended Abstracts on Human Factors in](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0725)_
_[Computing Systems](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0725)_ (pp. 2255–2262).
Yang, Y., Liu, Y., Lu, X., Xu, J., & Wang, F. (2020). A named entity topic model for ne
popularity prediction. _Knowledge-Based Systems, 208_ [, Article 106430. https://do](https://doi.org/10.1016/j.knosys.2020.106430)
[org/10.1016/j.knosys.2020.106430](https://doi.org/10.1016/j.knosys.2020.106430)
Yang, Z. (2020). Analysis of the Impact of Big Data Technology on News Ecology. _Jour_
_of Physics: Conference Series, 1682_ [(1), Article 012084. https://doi.org/10.1088/](https://doi.org/10.1088/1742-6596/1682/1/012084)
[1742-6596/1682/1/012084](https://doi.org/10.1088/1742-6596/1682/1/012084)
Yeung, K. F., & Yang, Y. (2010). A proactive personalized mobile news recommendat
system. In _Proceedings - 3rd International Conference on Developments in ESystems_
_Engineering_ [. https://doi.org/10.1109/DeSE.2010.40](https://doi.org/10.1109/DeSE.2010.40)
Zhang, C., Wang, H., Wang, W., & Xu, F. (2015). RCFGED: Retrospective Coarse an
Fine-Grained Event Detection from Online News. _Proceedings - 2015 IEEE_
_International Conference on Systems, Man, and Cybernetics, SMC 2015_, 139–144.
10.1109/SMC.2015.37.
[Zheng, Y., Zhong, B., & Yang, F. (2018). When algorithms meet journalism: The use](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0750)
[perception to automated news in a cross-cultural context.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0750) _Computers in Human_
_[Behavior, 86](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0750)_, 266–275.
Zhou, Y., & Liao, H.-T. (2020). A Bibliometric Analysis of Communication Research
Artificial Intelligence and Big Data. _6th International Conference on Humanities an_
_Social Science Research_, _435_, 456–459. 10.2991/assehr.k.200428.097.
[Zhou, Y., & Zhou, Z. (2020). Towards a Responsible Intelligent HCI for Journalism:](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0760)
[Systematic Review of Digital Journalism.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0760) _International Conference on Intelligent_
_[Human Computer Interaction](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0760)_, 488–498.
[Zhu, C., Zhu, H., Ge, Y., Chen, E., & Liu, Q. (2014). Tracking the evolution of social](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0765)
[emotions: A time-aware topic modeling perspective.](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0765) _IEEE International Conference_
_[Data Mining, 2014](http://refhub.elsevier.com/S0957-4174(23)00296-8/h0765)_, 697–706.
Zihayat, M., Ayanso, A., Zhao, X., Davoudi, H., An, A., Rogers, T., & Technology, I.
(2019). A utility-based news recommendation system. _Decision Support Systems_,
(December 2018), 14–27. 10.1016/j.dss.2018.12.001.
Zupic, I., & Cater, T. (2015). Bibliometric Methods in Management and Organizatio
_Organizational Research Methods, 18_ [(3), 429–472. https://doi.org/10.1177/](https://doi.org/10.1177/1094428114562629)
[1094428114562629](https://doi.org/10.1177/1094428114562629)
