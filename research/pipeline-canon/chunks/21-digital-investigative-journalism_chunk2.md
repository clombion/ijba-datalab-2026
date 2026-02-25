<!-- chunk: 2/3 | source: 21-digital-investigative-journalism.md | words: 39944 -->
<!-- headings: Visual Analysis: Verification via Geolocation and Photographs; eyeWitness to Atrocities: Verifying Images with Metadata; A Matter of Perspective: Truth, Evidence and the Role of Photography as an Investigative Tool; The Context Verification of Digital Photographs; Photo Manipulation: Software to Unmask Tampering; Authenticity, Identity and Transparency; Fact-Checking as Defence Against Propaganda in the Digital Age; Crowdsourced and Patriotic Digital Forensics in the Ukrainian Conflict; In-Depth Crisis Reporting; eJihad: Behind the Use of Social Media by ISIS; Truth Corrupted: The Role of Fact-Based Journalism in a Post-Truth Society; The Future of Investigative Journalism in an Era of Surveillance and Digital Privacy Erosion -->
<!-- sections: Interactive data visualization design and research; Image verification and geolocation forensics; Fact-checking, propaganda, and crisis reporting -->


© The Author(s) 2018
O Hahn and F Stalph (eds ) _Digital Investigative Journalism_


visual storytelling” at Malofiej, Infographic World Summit: “If you make
a tooltip or rollover assume that no one will ever see it” (Tse 2016).
You cannot expect the reader to interact with your graphic. All critical
information must be visible in the very first layer and not hidden behind
interactivity.
At first, this might sound like sad news for information visualisation
designers and journalists who are excited about the possibilities of interactivity in data visualisations. It allows for deeper stories, more context,
and, when compared to static print graphics where you often have to
drastically reduce the amount of data for the sake of formatting, a better medium for telling the full story. Interactive media allows us to show
readers the full spectrum of information with many different viewpoints
and perspectives, allowing the reader to go on their very own discovery
trip—so why are they not clicking?


What Science Says

First let us look at how we define interactivity in this context and what
studies have found about how interactive graphics can benefit engagement, recall, and memorability.


Definition: Interactivity

Interactivity is often defined as communication between sender and
receiver on the Internet. This “revolutionary new medium” (Hoffman
and Novak 1996)—the Internet—has transformed publishing from a
strictly centralised model with powerful gatekeepers (the publishers) to
a peer-to-peer based publishing model, where anyone can disseminate
information or participate in conversations far beyond what the old “letter to the editor” allowed for.
In the early stages of online journalism Deuze (1999) already foresaw a cultural change caused by interactivity as “the main discerning
characteristic of the online environment” (p. 378)—even though he was
primarily talking about the new interactive possibilities for quicker communication between the journalist and its audience. He elaborates on
this definition in his later work to three different types: “ **navigational**
**interactivity** ”, where the user has an influence on how they navigate the
content; “ **functional** **interactivity** ”, where the user can interact with
other users or even the producer; and “ **adaptive** **interactivity** ” where
the surfing behaviour is analysed to personalise the content according


to the users’ preferences (Deuze 2003). Now a decade later we can
add more interactive features such as sharing on social media (Hermida
2011), creating lists of most read or recommended stories to deal with
the “limitless volume of information” (Singer 2014), polls, or the ubiquitous comment sections (Stroud et al. 2016).
We are focusing on the “navigational interactivity” here. Common
ways in which a reader can interact with a visualisation are:


  - **Inspect** : get details about something specific, for example, hover or
click on an element to get more information

  - **Connect** : show related items, for example, by clicking on one

­element to highlight similar ones for comparison

  - **Select** : highlight element to keep track of it, for example, in an animated graph

  - **Filter** : show something conditionally, for example, select one country from a drop-down menu

  - **Abstract/elaborate** : show more or less detail by zooming in or out

  - **Explore** : input a query to see “something else”

  - **Narrate** : for example, a stepper-button that guides the reader to next
part of the story (Boy et al. 2015, p. 1451; Yi et al. 2007, p. 1226)


Studies

There are several disciplines that care about interactive data visualisation. Many of these are within Computer Science, namely Information
Visualisation (InfoVis) and Human Computer Interaction (HCI), which
includes the technical implementation in addition to the visual encoding, understandability, and usability. Additionally, the digital humanities,
communication studies, and journalism schools frequently investigate
their usage and benefits as well.
There are a few studies that in particular look at whether there is a
difference in engagement between static and interactive graphics. The
results, while not earth-shattering, give some ideas:


  - The Internet skill level plays a role in the use of interactive features
(Chung 2008)

  - When comparing an “interactive infographic, a static infographic
and a table condition” small advantages were found for the interactive condition and disadvantages for the table (Milatz 2013)


  - Interactivity (filter buttons in this case) can have a positive effect on
“reducing political misperceptions”. It can help in understanding a
topic more accurately and inspire more thoughts (Geidner et al. 2015)

  - Interactivity could lead to “more favourable attitudes towards an
article for users low in involvement”. For users that were engaged
already it did not seem to make much of a difference (Wojdynski
2015)

  - Self-paced animation control, where the user can decide when to
start or stop an animation—which is a low form of interactivity—
can reduce cognitive overload (Zhao and Huang 2013)


On the flip side, a 2010 study found that “interactive information
graphics tend to overwhelm users with too much information and disregard well-known principles and rules of the old media and web design”
(Burmester et al. 2010, p. 361). Further, unlike typographical style
standards, such as The Chicago Manual of Style or the AP Stylebook,
guidelines for interactive elements are inconsistent and vary widely across
individual newsrooms (Günther and Scharkow 2014; Stroud et al. 2016).
In 2016, Dada tested some of those assumptions about how interactivity can improve graphics and online news and found “engagement
benefits are restricted to participants who make use of interaction possibilities—and these are not in the majority” (Dada 2016, p. 52). She also
finds in her experiments that usability and skills and motivations were
responsible for more engagement and information recall.
What can we learn from this? It is advisable to know about the principles of user-based design, and in addition to maintaining the quality
and meaningfulness of the content, one should follow the current design
and usability standards and ensure that users know how to interact with
the content. This is often not the case. Boy et al. studied whether users
are naturally inclined to interact with visualisations and found that since
the majority of users were unaware of the interactivity of the charts, they
rarely used it (Boy et al. 2016).


What Practitioners Say

There is a lot of collaboration happening between Journalism schools,
research labs, and news outlets. Still, it can be hard for practitioners to
keep track of what science has found, and what new tools the research
labs have developed, and for scientists to always see what problems


practitioners are facing. So, let us have a look at the other side, from the
perspective of those who practice data visualisation every day in newsrooms and as reporters.


Interactives in the News

Data heavy reporting comes in many flavours, with terms like computational journalism, computer-assisted reporting, data-driven journalism,
and digital investigative journalism (Coddington 2015). Despite the
nuances distinguishing them, they are all very much intertwined with data
visualisation. Mirko Lorenz describes the workflow for such journalism as:


  - **Data Acquisition** : Scrape it, cleanse it, structure it, and start digging into it

  - **Data Filtering** : Mine it for nuggets of information

  - **Visualisation** : Create charts, graphics, or any kind of multimedia

  - **Storytelling** : Tell the story around it, to vamp up the dry statistics
and point out the interesting parts (Lorenz 2010).


The further along you move in that process, the more value you
create for the reader since the raw data is transformed into something
that is meaningful to the readers.
If you are using interactive data visualisations in the right way, they
can turn an objective, impersonal, fact-based article into something
much more personal and bi-directional. It could be “as if you were having a tête-à-tête with an expert on the data, patient enough to explain
you everything” (Baur 2017).
Scott McCloud, the famous cartoonist and comics theorist, has many
smart things to say about how to tell stories visually. The visualisation
creator’s job is to filter the information. In moving pictures, we use the
time to direct the viewer, in comics we use space. “In interaction we are
able to do it more explicitly, we’re able to say hover your mouse over
here or select this option and then you can see just this one trendline”—
the one that is most interesting to you (Bertini and Stefaner 2017, 7:19).
Some topics are more interesting for this kind of storytelling than
others. Murray Dick (2014) interviewed some interactives creators about
it: Bella Hurrel, editorial lead at the BBC Specials team, says those topics are “‘Big data’ stories, concerning stories buried in large data sets…
non-statistical process visualisations that help the audience understand


an issue… and personalised information generators, such as calculators”
(p. 499). Also “outliers often make for good stories, as do stories which
involve processes or personalisable information (such as school league
tables)” (p. 500).
Emily Cadman from the Financial Times interactives team says that
it is about “interactives that allow the user to explore something that
affects them directly, or that encourage the exploration of complicated
major topics” (p. 499).
Murray Dick concludes that whether interactives are used is less
dependent on the subject but “due in part to the availability of ‘newsworthy’ data, and in part to newsroom dynamics”. And since producing
those interactives takes a lot of resources, “‘important’ stories are more
likely to be selected for coverage” (p. 504).


Does Digital Journalism Need Interactives?

Visualisation is one essential part of this kind of digital journalism and
very often those visualisations are interactive ones. In a content analysis
about Canadian data journalistic projects we found that almost all (25
out of 26) projects were using some kind of interactivity in their stories
(Young et al. 2017). In general, the tenor seems to be that interactivity is
a core characteristic of digital journalism. Some of it is handcrafted, some
of it uses freely available tools, such as Tableau, Datawrapper, or Google
Maps (in fact Google Maps was by far the most used interactive technique in our Canadian content analysis). Since not all newsrooms have
dozens of people in an interactive lab, they often rely on the eagerness
of individuals willing to invest extra time in side projects, and in learning
to work with available tools on their own (Hermida and Young 2017).
Unfortunately, this can potentially lead to the journalistic output “to be
shaped less by what could be considered the best way of representing/
exploring the data and more by what can be done and is available for
free” (Young et al. 2017, p. 13). The study indicated one or both of two
things for newsrooms in Canada (and most likely over its borders)


1. There is a lack of knowledge about the principles of information
visualisation, of how to effectively represent data and/or
2. There is a lack of time/people/experience to create customised
solutions, so that freely available tools and platforms become shaping factors


Was there to be a better understanding of the principles and more
consideration going into the decision whether to use interactives at all,
we might see less unjustified interactives and more “good-old” static
visualisations, that deliver the message just as nicely (see also next part
“Rules of thumb”).
There already seems to be a trend away from interactives, and towards
creating expressive static graphics, where no information is “hidden”
behind tooltips. Priya Krishnakumar, a visual/data journalist at the
LA Times, says “lately I’m trying to hew more towards static if I can”
(Schwabish 2017, 7:40). Martin Stabe, the head of interactive news at
The Financial Times says that they too are trying “to avoid using interactivity where possible because it is more important to make something
responsive than adding that extra layer of complexity (Luyckx 2017).


Complex Visual Storytelling Needs Interactivity

**Data Visualisation is there to clarify—not to simplify** . Alberto
Cairo’s aims to get that misconception straight and says that while it is
necessary to remove unnecessary information and “simplify” the message, we must be extremely careful in ensuring that nothing essential
is removed. Sometimes, clarity can require additional data to provide
the appropriate context—a task extremely well suited for interactivity
(Rogers et al. 2017).
How does this argument hold up to the fact that only very few people will get to that additional information—because, remember? Nobody
clicks!
Simon Rogers (Guardian Datablog creator, now at Google) argues
that the number of people using interactive visualisations (10–15%), is
not much lower than the number of people reading the full article and
therefore, this should not be the main argument against using interactives. The small percentage of readers that actually click the buttons are
the ones you are creating it for—the interested ones (Aisch 2017; Rogers
et al. 2017).
Clearly, not every topic lends itself to this kind of time investment. In
many cases, readers visit news websites on their mobile phones to catch
up with the latest and hottest while riding the subway to work. But the
more complex, interesting, and data-heavy the topic, the more it does
lend itself to a deeper interactive investigation. Matt Daniels, member of
Polygraph (a visual storytelling incubator) and founder of The Pudding


(a journal for visual essays), says “I want the thing to be so deep, and
complex, and interesting that it is like a Lord of the Rings moment”
(Rogers et al. 2017, 24:30)—which is when you want to be alone with
your screen, getting fully emerged, digging in, understanding everything.


Rules of Thumb

Interactivity can greatly enhance data journalistic pieces. While there
is no need to despair just because not everybody engages with it, we
should preach caution in the way it is used. The decision to use interactivity has to be deliberate, conscious, and considered. A few rules of
thumb might help make the call.


Justify Interactivity

“Interactivity is an extra layer for visualisations, that will make [a data
visualisation] more complex and therefore more time-consuming” says
Martin Stabe from the Financial Times (Luyckx 2017). Think about what
the benefits of an interactive would be. In many cases, a well-curated static
graphic is way more useful and accessible than a blown-up interactive.

**Bottom line question** : Does this particular piece really need to show
more data than we can fit in a static graphic?


No Arbitrary Interactivity

The availability of easy-to-use data visualisation tools has led to their
widespread use, often by relatively novice users who stick to the default
settings. These settings are sometimes distracting: for instance, while
Google Maps understandably allows zooming and panning, sometimes
we want to show an explicit part of the map and prevent the user from
getting lost by accidentally scrolling over it. So, in this case a conscious
decision would be to disable the default zooming and panning and only
show the one area of interest.
Other chart libraries that enable the user to quickly create bar/line/
scatter/pie charts advertise themselves as having “easy interactivity”.
This is great, but also really unnecessary at times. Simple pie charts with
three pieces of clearly visible static information that change colour and
are highlighted when the user hovers over them—interactivity overkill
for no discernible extra information.


One might say: Well, it does not hurt, does it? But it is a misuse of
interactivity. Actually, it can hurt comprehension by forcing the reader to
search for meaning behind the interaction.
Every visual decision generates meaning. “Our eye assigns meaning to
every detail that is there. […] We assign significance to it at least subliminally. We’re going to think that that matters, that we are being told
something about that little nugget of data”, says Scott McCloud (Bertini
and Stefaner 2017, 30:30). So, be careful not to generate the wrong cues.

**Bottom line** : Disable interactivity if it does not have a purpose.


Lean Forward or Lean Back

Within interactive data visualisations the degree of interactivity can vary
a lot. There are “interactive” pieces that only have one “narrate” button, for example, to switch a visualisation from the current to the previous year. Segel and Heer call this an “author-driven” approach (2010,
p. 1145), as it uses linear storytelling and the author guides the reader
through the visualisations. In contrast to that there’s the “reader-driven”
approach, where the reader has many more options to interact and
explore.
Some topics lend themselves better to the reader-driven method than
others; for example, stories where the reader expects to get information quickly without having the time for exploration are a poor fit for
this model. Scott McCloud talks about a conflict between driving and
being driven. When considering the options of Virtual Reality, he says
“Either I’m in control, or the author is. Either I lean forward or I lean
back. I think that we tend to be a little uncomfortable when it’s flickering somewhere in the middle” (datastories, 28:10). Similarly, the BBC
Specials team found that when “taking a prescriptive narrative approach,
more readers are likely to complete all stages of the interactive—so this
approach is often preferred to experimental interactive graphics” (Dick
2014, p. 502).

**Bottom line** : Make the decision who is driving: author or reader.


Bart and Lisa Approach

In information design it is a good idea to create something that works
on different comprehension levels. Former New York Times graphics
editor Jennifer Daniel explains an idea that they called the “Bart and


Lisa approach” (in a reference to “The Simpsons” TV series). A graphic
should be attractive to Bart—with his rather low-attention span—as well
as to Lisa, who is interested in details and wants to understand the context and learn something new. So for interactive graphics: Bart should
be able to get the message without having to move the mouse at all;
whereas Lisa can dig way deeper to satisfy her curiosity (Miller 2016).

**Bottom line** : The important parts have to be there even without
interacting.


Have a Fallback Solution

The greatest interactive graphics sometimes use the latest web technologies, need the biggest space, or load a huge amount of data.
Unfortunately, we cannot assume that the readers always have the latest
browser, the biggest screens, or the fastest internet. So if we decide to go
for it anyway, there has to be a fallback solution.
This becomes harder the more complex the data and the visualisation is, and it is likely that information gets lost along the way (Aisch
2016, 10:30). But rather than showing a message like “Please go to your
desktop computer to enjoy the full experience”, or “Sorry but this only
works on the latest version of Browser XY”, it would be good to have a
static fallback image that shows as much as possible.
Often this will be the case for mobile devices because elaborate interactives tend not to work as well on them. Since mobile is becoming the
number one way how news is consumed, this brings up a whole new
abundance of challenges, such as screen size, internet speed, the fat finger problem, and an (even more) limited attention span. This is beyond
the scope of this chapter, but some interesting resources in this space are:
Julia Smith’s “Data Viz for All: Best practices for mobile, accessible interactives”, and more great examples, patterns, and best practices can be
found on the MobileVis website.

**Bottom line** : Consider all the platforms and devices and offer at least
a fallback solution.


Suggest Interactivity

As we have seen earlier, interactive features often remain undiscovered
by the audience (Boy et al. 2016). If you are deciding to use an interactive graphic, make it clear how this interactivity is supposed to work.
Alastair Dant, lead interactive technologist at the Guardian, mentions


the importance of providing “a clear journey through the data or
through whatever is in your interactive experience” (McAthy 2012).
Consequently, we should include annotations, instructions, directions,
or suggest the interactivity with visual means—Boy et al. formulated an
extensive table with visual cues that designers can use to suggest interactivity to users.
Martin Jefferies, the chief reporter at the KM Group, concurs: “You
need to tell them what they’ve got to click on” (McAthy 2012).

**Bottom line** : Do not assume the reader will intuitively know what to do


Conclusion

Interactives are a great way to present complex stories to the discerning
reader. As with every new technology, however, they have often been
overused. Designers sometimes opt for form over function and spend
too little time thinking about usability and the principles of data visualisation, which can lead to interactivity being hidden or unnecessary. This
chapter aims not to diminish the value of interactives, but to highlight
some of the pitfalls and real costs associated with it, and suggests some
rules of thumb for practitioners who are uncertain about whether it is
the right choice and what to consider when working with complex and
data-heavy topics.


References


Aisch, G. (2016, September 13). _Information+ Conference: Gregor Aisch_ [Video
[file]. Retrieved from https://vimeo.com/182590214.](https://vimeo.com/182590214)
Aisch, G. (2017, March 31). _In Defense of Interactive Graphics_ [Web log
post]. Retrieved from [https://www.vis4.net/blog/posts/in-defense-of-](https://www.vis4.net/blog/posts/in-defense-of-interactive-graphics/)
[interactive-graphics/.](https://www.vis4.net/blog/posts/in-defense-of-interactive-graphics/)
Baur, D. (2017, March 13). _The Death of Interactive Infographics?_ [Web log post].
Retrieved from [https://medium.com/@dominikus/the-end-of-interactive-](https://medium.com/%40dominikus/the-end-of-interactive-visualizations-52c585dcafcb)
[visualizations-52c585dcafcb.](https://medium.com/%40dominikus/the-end-of-interactive-visualizations-52c585dcafcb)
Bertini, E., & Stefaner, M. (Producers). (2017, July 17). _Datastories 102:_
_Understanding Comics and Visual Storytelling with Scott McCloud_ [Audio podcast]. Retrieved from [http://datastori.es/102-comics-and-visual-storytelling-](http://datastori.es/102-comics-and-visual-storytelling-with-scott-mccloud)
[with-scott-mccloud.](http://datastori.es/102-comics-and-visual-storytelling-with-scott-mccloud)
Boy, J., Detienne, F., & Fekete, J. D. (2015). Storytelling in Information
Visualizations: Does It Engage Users to Explore Data? In _Proceedings of the_
_33rd Annual ACM Conference on Human Factors in Computing Systems_ (pp.
1449–1458). New York, NY: ACM.


Boy, J., Eveillard, L., Detienne, F., & Fekete, J. D. (2016). Suggested
Interactivity: Seeking Perceived Affordances for Information Visualization.
_IEEE Transactions on Visualization and Computer Graphics,_ _22_ (1), 639–648.
[https://doi.org/10.1109/TVCG.2015.2467201.](http://dx.doi.org/10.1109/TVCG.2015.2467201)
Burmester, M., Mast, M., Tille, R., & Weber, W. (2010, July). How Users Perceive
and Use Interactive Information Graphics: An Exploratory Study. In _Information_
_Visualisation (IV), 2010 14th International Conference_ (pp. 361–368). London:
IEEE.
Chung, D. S. (2008). Interactive Features of Online Newspapers: Identifying
Patterns and Predicting Use of Engaged Readers. _Journal of Computer-_
_Mediated Communication, 13_ (3), 658–679.
Coddington, M. (2015). Clarifying Journalism’s Quantitative Turn: A Typology
for Evaluating Data Journalism, Computational Journalism, and Computerassisted Reporting. _Digital Journalism,_ _3_ [(3), 331–348. https://doi.org/10.1](http://dx.doi.org/10.1080/21670811.2014.976400)
[080/21670811.2014.976400.](http://dx.doi.org/10.1080/21670811.2014.976400)
Dada, J. (2016). _Engaging to Explore? An Online Experiment to Investigate the_
_Impact of Interactivity in Data Visualizations_ . Unpublished Master’s thesis,
University of Oxford.
Deuze, M. (1999). Journalism and the Web: An Analysis of Skills and Standards
in an Online Environment. _International Communication Gazette,_ _61_ (5),
[373–390. https://doi.org/10.1177/0016549299061005002.](http://dx.doi.org/10.1177/0016549299061005002)
Deuze, M. (2003). The Web and Its Journalisms: Considering the Consequences
of Different Types of Newsmedia Online. _New Media & Society,_ _5_ (2), 203–230.
[https://doi.org/10.1177/1461444803005002004.](http://dx.doi.org/10.1177/1461444803005002004)
Dick, M. (2014). Interactive Infographics and News Values. _Digital Journalism,_

_2_ [(4), 490–506. https://doi.org/10.1080/21670811.2013.841368.](http://dx.doi.org/10.1080/21670811.2013.841368)
Geidner, N., Pjesivac, I., Imre, I., Coman, I., & Yuran, D. (2015). The Role
of Interactive Graphics in Reducing Misperceptions in the Electorate. _Visual_
_Communication Quarterly,_ _22_ [(3), 133–145. https://doi.org/10.1080/1555](http://dx.doi.org/10.1080/15551393.2015.1069195)
[1393.2015.1069195.](http://dx.doi.org/10.1080/15551393.2015.1069195)
Günther, E., & Scharkow, M. (2014). Recycled Media: An Automated Evaluation of
News Outlets in the Twenty-First Century. _Digital Journalism, 2_ (4), 524–541.
Hermida, A. (2011). Mechanisms of Participation. In J. B. Singer (Ed.),

_Participatory Journalism: Guarding Open Gates at Online Newspapers_ (pp.
11–33). Malden, MA: Wiley.
Hermida, A., & Young, M. L. (2017). Finding the Data Unicorn: A Hierarchy
of Hybridity in Data and Computational Journalism. _Digital Journalism,_
_5_ [(2), 159–176. https://doi.org/10.1080/21670811.2016.1162663.](http://dx.doi.org/10.1080/21670811.2016.1162663)
Hoffman, D. L., & Novak, T. P. (1996). Marketing in Hypermedia Computermediated Environments: Conceptual Foundations. _Journal of Marketing,_
_60_ (July), 50–68.
Lorenz, M. (2010, June 29). _Data-Driven Journalism: What Is There to Learn?_
_(Stanford, June 2010)_ [Talk Slides]. Retrieved from [https://www.slideshare.](https://www.slideshare.net/mirkolorenz/datadriven-journalism-what-is-there-to-learn)
[net/mirkolorenz/datadriven-journalism-what-is-there-to-learn.](https://www.slideshare.net/mirkolorenz/datadriven-journalism-what-is-there-to-learn)


Luyckx, D. (2017, February 9). _3 Ways to Make Data Visualisations and_
_Interactives Work on Mobile_ . Retrieved from [https://www.journalism.co.uk/](https://www.journalism.co.uk/skills/3-ways-to-make-data-visualisations-and-interactives-work-on-mobile/s7/a699519/)
[skills/3-ways-to-make-data-visualisations-and-interactives-work-on-mobile/](https://www.journalism.co.uk/skills/3-ways-to-make-data-visualisations-and-interactives-work-on-mobile/s7/a699519/)
[s7/a699519/.](https://www.journalism.co.uk/skills/3-ways-to-make-data-visualisations-and-interactives-work-on-mobile/s7/a699519/)
McAthy, R. (2012, August 1). Visual Journalism: Advice on Building Interactives
[and Engaging the Audience. Retrieved from https://www.journalism.co.uk/](https://www.journalism.co.uk/news/tips-engage-the-audience-with-interactive-journalism/s2/a549988/)
[news/tips-engage-the-audience-with-interactive-journalism/s2/a549988/.](https://www.journalism.co.uk/news/tips-engage-the-audience-with-interactive-journalism/s2/a549988/)
Milatz, M. (2013). _Moving Graphics: The Effects of Interactive Infographics on_
_Media Users’ Recall Accuracy_ . Unpublished master’s thesis.
Miller, M. (2016, August 12). _The “Bart and Lisa” Theory of Information_
_Design_ . Retrieved from [https://www.fastcodesign.com/3066148/the-bart-](https://www.fastcodesign.com/3066148/the-bart-and-lisa-theory-of-information-design)
[and-lisa-theory-of-information-design.](https://www.fastcodesign.com/3066148/the-bart-and-lisa-theory-of-information-design)
Rogers, S., Cairo, A., & Daniels, M. (2017, March 31). _News Lab Data_
_Visualization Round Up: March 2017—With Special Guest, Matt Daniels_ [Video
[file]. Retrieved from https://www.youtube.com/watch?v=UqLAxpumENs.](https://www.youtube.com/watch?v=UqLAxpumENs)
Schwabish, J. (Producer). (2017, June 6). _PolicyViz Episode #89: Priya_
_Krishnakumar_ [Audio podcast]. Retrieved from [https://policyviz.com/](https://policyviz.com/podcast/episode-89-priya-krishnakumar/)
[podcast/episode-89-priya-krishnakumar/.](https://policyviz.com/podcast/episode-89-priya-krishnakumar/)
Segel, E., & Heer, J. (2010). Narrative Visualization: Telling Stories with Data.

_IEEE Transactions on Visualization and Computer Graphics, 16_ (6), 1139–1148.
Singer, J. B. (2014). User-generated Visibility: Secondary Gatekeeping in a
Shared Media Space. _New Media & Society,_ _16_ (1), 55–73. [https://doi.](http://dx.doi.org/10.1177/1461444813477833)
[org/10.1177/1461444813477833.](http://dx.doi.org/10.1177/1461444813477833)
Stroud, N. J., Scacco, J. M., & Curry, A. L. (2016). The Presence and Use of
Interactive Features on News Websites. _Digital Journalism,_ _4_ (3), 339–358.
[https://doi.org/10.1080/21670811.2015.104298.](http://dx.doi.org/10.1080/21670811.2015.104298)
Tse, A. (2016, March 21). _Why We Are Doing Fewer Interactives_ [talk slides].
Retrieved from [https://github.com/archietse/malofiej-2016/blob/master/](https://github.com/archietse/malofiej-2016/blob/master/tse-malofiej-2016-slides.pdf)
[tse-malofiej-2016-slides.pdf.](https://github.com/archietse/malofiej-2016/blob/master/tse-malofiej-2016-slides.pdf)
Wojdynski, B. W. (2015). Interactive Data Graphics and Information Processing.

_Journal of Media Psychology,_ _27_ (1), 11–21. [https://doi.org/10.1027/](http://dx.doi.org/10.1027/1864-1105/a000127)
[1864-1105/a000127.](http://dx.doi.org/10.1027/1864-1105/a000127)
Yi, J. S., ah Kang, Y., & Stasko, J. (2007). Toward a Deeper Understanding
of the Role of Interaction in Information Visualization. _IEEE Transactions_
_on Visualization and Computer Graphics, 13_ (6), 1224–1231. [https://doi.](http://dx.doi.org/10.1109/tvcg.2007.70515)
[org/10.1109/tvcg.2007.70515.](http://dx.doi.org/10.1109/tvcg.2007.70515)
Young, M. L., Hermida, A., & Fulda, J. (2017). What Makes for Great Data
Journalism? _Journalism Practice_ [. https://doi.org/10.1080/17512786.2016.](http://dx.doi.org/10.1080/17512786.2016.1270171)
[1270171.](http://dx.doi.org/10.1080/17512786.2016.1270171)
Zhao, L., & Huang, T. (2013). Experimental Research on the Effectiveness
of Animated Instruction. In _3rd International Conference on Multimedia_
_Technology (ICMT-13)_ (pp. 562–569). Amsterdam: Atlantis Press.


CHAPTER 13

#### Visual Analysis: Verification via Geolocation and Photographs


_Eliot Higgins_


With the wealth of photographic and video content now being
published the verification of this imagery has become increasingly
important. The basic question of where an image was captured has
become key to the process of verification, and through the technique of
geolocation it is often possible to find the exact position an image was
recorded.
Geolocation involves using all available material to confirm the location of an image. Often this involves satellite imagery available on a
range of services, such as Bing Maps, Google Earth, Google Maps, and
Terraserver. On the ground imagery, the location of which has already
been established, is also frequently used, and examples of this include
Panoramio and Google Street View.
However, the first challenge is, in a geographical sense, knowing
where to start looking. Images will often come with additional information, for example, the town or city the image was taken in, or they


E. Higgins (*)
Bellingcat, Leicester, UK


© The Author(s) 2018
O Hahn and F Stalph (eds ) _Digital Investigative Journalism_


will be posted on a social media profile belonging to an individual in a
specific location. What must first then be established is what the original
source of the image is. While in some circumstances you may be aware of
the original source, many images now shared online are often reposted
without the original source included. This can be for a variety of reasons,
but the need to establish the original source whenever possible is always
there.
In the case of photographs, it can be extremely simple. Reverse image
search functions on Google Image Search or TinEye, both freely available and easy to use, is the first tool to use in the search for the original
source of images. Browsers such as Chrome now allow users to simply
right-click an image and select reverse image search, so it could not
be easier. These searches will bring up a list of results, and often it will
be a simple matter of looking through those search results to establish
whether or not an image is new, or has been previously posted online.
One pitfall here is that dynamically generated pages can lead to misleading results. A YouTube page will list other videos related to the video
currently being viewed, with a dynamically generated list that includes
preview images which Google Image Search will find. This means that
when the search engine has crawled that site, it has resulted in a dynamically generated page being made, and the image search results are based
on when the search engine crawled that site, so it will include all the time
that image has appeared on the page as a related video on the page of
another video, and might not even appear at this point in time.
Another issue is that a page might be created on a date, but the
content is added to it at later dates, for example on an internet forum
thread. Often you will then see that the date given in the Google Image
Search result is the date when the webpage was created or when it was
first crawled by the search engine, not when the image was posted on
that page. In the case of the downing of Flight MH17 in Ukraine, it was
falsely claimed that one image showing a Buk missile launcher in Ukraine
and linked to the downing of the aircraft was published the day before
the attack, not on the day of the attack as many people had claimed,
because the reverse image search showed a search result that listed the
previous day. In fact, the page it was posted on had been created on a
previous day, but the update with the image was made later.
Videos can be harder to find. Unlike photographs, there is currently no reverse search platform for videos, but there is at least one
work-around. Amnesty International’s YouTube Dataviewer will


extract the preview frames from a YouTube video, allowing them to be
easily reversed image searched. This will find other versions of the video
in question, by searching for the preview frames in those versions of those
videos. However, there is a major limitation to this: It will not be accurate if the video is edited, shortened, or extended with additional footage.
If you are able to find the original source of the image, it then may
be possible to find more information about it. The simplest information
to find is whatever was posted along with the image. For example, an
Instagram image or Facebook post might have the location listed in the
description or discussed in the comments. The next step would be to
look at the profile it was posted on. Does it usually post about one location? Is the person who posted it talking about their movements?
This may, of course, not even be necessary depending on what the
image actually shows. A street sign or shop name might give a crucial
clue to where the image was recorded. These can be easily searched for
on Google along with the name of the locations it may be into see if
there are any results, which will often point to specific locations. In some
cases, Street View imagery may be available, at which point it should be
possible to verify the location in the image by comparing it to the Street
View imagery.
If you do not get lucky you then have to start thinking about how to
narrow down the possible locations it could be in. If you have the general location that can be useful, but finding the precise location requires
additional effort.
Begin first by identifying large features and distinct landmarks. During
the conflict in Libya in 2011, a video was posted online by rebels claiming to show them entering the town of Tiji, previously controlled by
Colonel Gaddafi’s forces. Establishing the exact location it was filmed
was possible, thanks to two major landmarks visible in the video. First,
the video was filmed outside a large mosque with a dome and minaret,
which would be clearly visible in satellite imagery. The major landmark
was the road next to the mosque, two wide lanes, with a slight bend in
the road clearly visible. By examining satellite imagery of Tiji on Google
Earth it was immediately apparent that a major road ran through the
centre of the town, and a closer look at the road was clear enough to
show individual cars on the road, with each lane being three car widths
wide, fitting with what was visible in the video. Also visible in the satellite
imagery was a slight bend in the road, and close to that was a mosque,
with a dome and minaret.


These two larger features had taken us to the same location the image
was recorded, but next, the video was re-examined to identify other,
smaller, features. The position of the curb, the location of utility poles
(visible by the shadows they cast), the position of buildings and trees.
While these features would not have led us to the location, they allowed
us to confirm the location, and precise position of the camera.
Sometimes it takes more than satellite imagery to find a location.
When investigating the downing of flight MH17 in Ukraine, a number
of videos and photographs of a Buk missile launcher being transported
through separatists’ territory had been posted online. With various claims
being made about what had happened, it was important to ensure all
images were verified, especially as the images appeared to show the missile
launcher on the way to the launch site from which it shot down MH17.
One image, a photograph taken from a garage forecourt, showed a
Buk missile launcher being transported by a low-loader truck. The photograph was being shared on various social media platforms, with claims
that it was either taken in the town of Torez, or in the town of Snizhne.
The first clue was a partially visible shop sign. Although the sign was
obscured, there were only reasonably few possibilities of words it could be,
and a Google search of those words and the town names resulted in only
a few viable leads, one of which was a Wiki listing streets in Ukraine with
the shops on them. This provided the street name, which was, along with
the shop name and town name, searched for on Google, resulting in a new
result. This was a court document detailing a fight that had taken place in
the shop, giving the full address. Searching for the address and shop name
led to a location visible on satellite imagery just across the road from a
garage forecourt, the same one the photograph had been taken from.
In addition, during the Google searches two videos were discovered, filmed by a local on a dashboard camera from his car as he drove
around the area, which he had uploaded to YouTube, listing the streets
he drove down in the description of each video. Now in addition to the
satellite imagery match, it was also possible to match imagery from the
videos to the location in the photograph. Because the videos showed an
entire journey through the area, it was possible to further verify where
the video was filmed by matching off various landmarks along the route
filmed on the dashboard camera, which in turn allowed the location of
the photograph to be more certain.
Understanding how information is organised and shared online can
also be useful. A bus visible in an image would suggest the location of


**Fig. 13.1** Crowdsourced geolocation via Twitter and Google Street View


the image is on a bus route. In many countries information like bus
routes, tramlines, etc. are available online, and often include maps. On
Google Earth and Yandex Maps tram and bus routes are sometimes visible, which can dramatically reduce the number of areas needing to be
looked at.
There is also less obvious information that has been organised online.
During an ISIS social media campaign, supporters of ISIS in Europe
were encouraged to take photographs of themselves holding a piece
of paper with a pro-ISIS hashtag on it, and the town or city they were
in. The location of one photograph in Paris was easily found because a
Suzuki logo was partially visible, and even though it was partly obscured
and out of focus, it was still easily identifiable. A Google search for
“Suzuki Paris” brought up the locations of Suzuki dealerships in Paris,
each of which was visible on Google Street View, and from there it was
easily possible to match other features in the background of the photograph (Fig. 13.1).
In another photograph from the ISIS social media campaign a photograph from Münster, Germany, was located because of an advertising
pole visible in the background. In Germany there is a website that lists


**Fig. 13.2** Crowdsourced geolocation of advertising sites via Twitter


the locations of advertising sites, intended to help buyers find ­advertising
positions across Germany. It was possible to search for all advertising poles in Münster, immediately giving a list of potential locations to
search, each visible on Google Maps satellite imagery, which could then
be systematically reviewed, until the location of the ISIS supporter who
had taken the photograph was established (Fig. 13.2).
Ultimately, the only way to develop geolocation skills is simply just
to do it. When I began verifying images, I found it extremely helpful to write out the steps I had taken to verify the image I was working on. This allowed me to really understand the process in my mind,
and to develop my own approaches to assessing and verifying material.
Geolocation is not a complicated discipline, so the best place to start
is just picking an image or video, and figure out exactly how to prove
where it was taken. Just going through the process, even with a simple geolocation, can build skill, and help you develop an eye for details
in images you might not have noticed before. It also pays to revisit old
cases, reviewing images you may have looked at months or years ago, as
often you will spot new details and other paths to geolocating the image
that you would not have seen before. Do this, and soon enough you will
develop the skill set and knowledge required to be an expert geolocator.


CHAPTER 14

#### eyeWitness to Atrocities: Verifying Images with Metadata


_Eleanor Farrow_


This case study looks at how the eyeWitness to Atrocities project
has collaborated with investigators to strengthen their reporting and
collect court-admissible evidence using the eyeWitness app. [1] eyeWitness to Atrocities (eyeWitness) is a free smartphone camera app
designed for individuals investigating human rights violations and international crimes. Developed under the auspices of the International Bar
Association, the app automatically collects basic information required
by courts to authenticate images. Metadata-enriched images taken with


1 In this chapter “eyeWitness to Atrocities” refers to the free android smartphone camera
app of that name. The eyeWitness to Atrocities project is also the name of the independent
registered UK charity comprised of a small team of lawyers funded by the International
Bar Association responsible for maintaining the app, collaborating with human rights
investigators for effective use of the app, and use of data collected using the app for ­justice
and accountability. The term “human rights investigators” is used in this chapter as an
umbrella term to describe investigative reporters, nongovernmental organisation (NGO)
journalists and human rights researchers documenting human rights violations and international crimes.


E. Farrow (*)
eyeWitness to Atrocities, London, UK


© The Author(s) 2018
O Hahn and F Stalph (eds ) _Digital Investigative Journalism_


the app can also support robust reports. The organisations that eyeWitness
works with collect information using a combination of technology tools
and traditional investigation methods. Despite the promise of new technologies for human rights investigations, their deployment comes with
challenges (Land et al. 2012; Tuckwood 2014; Raymond and Sandvik
2017; Aronson 2017). This case study also includes reflections on lessons
learned during the eyeWitness project and outlines some key considerations when adopting technology tools in human rights investigations.


Verification and Human Rights Reporting

Smartphones and social media platforms have increased the flow of information about human rights violations around the world. At the same
time, international news bureaux have closed, and the number of professional foreign correspondents has reduced due to economic pressures
(Constable 2007; Sambrook 2010). In addition to the lack of resources
needed to retain foreign correspondents, there are difficulties in accessing certain locations (Reporters Without Borders 2013; Allan 2017;
Koettl 2017). Non-governmental organisation (NGO) researchers often
step into the breach to provide information (Powers 2015). News ­editors
are increasingly reliant on user-generated content (UGC) and citizen
reporters, particularly in areas of armed conflict (Platt 2014; Mast and
Hanegreefs 2015).
One result of these trends is that media outlets are more dependent
on digital images from unknown sources that are easily manipulated.
News editors often have to judge whether to publish an image that they
have not been able to verify. Errors can occur with potentially serious
reputational or legal consequences (Shapiro et al. 2013, p. 664; Safran
2005). Yet, disclaimers that an image could not be verified potentially
weaken a report. Media organisations are actively seeking UGC, and
there is a flood of publicly available material posted on social media sites.
This has increased the need for image verification.
The verification of facts and sources is fundamental to both investigative journalism and human rights fact-finding. This is particularly the
case where official, organised, state-level denial of human rights violations and international crimes occurs (Cohen 2001, p. 10). News organisations and human rights organisations depend on their reputation for
credibility (Land 2016, p. 409; McPherson 2015b, 2016). With worldwide concerns about “fake news” and propaganda, and many images


appearing on social media out of context or edited, checking the authenticity of images remains crucial (Fabijanić et al. 2016). Koettl describes
this as “the ‘lemon problem’—the risk of using misinformation that can
discredit an entire research project” (Koettl 2017‚ p. 38).
Investigative journalists, in particular, have been said to adopt “a
distinctly quasi-scientific approach, setting out to prove or disprove a
hypothesis through triangulation of information from various sources”
(Cribb et al. 2006; Hunter 2011, as cited in Shapiro et al. 2013, p. 659).
Traditional methods of authentication include assessing the reliability
of individual sources and cross-checking with two or more independent
sources to corroborate facts (Golder and Reich 2017; Brandtzaeg et al.
2016; Shapiro et al. 2013; Hermida 2015; Wardle et al. 2014, p. 54).
More time-intensive techniques available to verify images include expert
analysis to detect edits, site visits to confirm the location, using satellite
images, weather reports, shadows and computer modelling (Goldsmiths
University “Forensic Architecture” 2011; Pantti and Sirén 2015, p. 496;
Bell 2015).
Many newsrooms now have verification processes and resources in
place, and it is hardly surprising that there are a growing range of image
authentication projects and tools (Silverman 2012). Indeed, some
have argued that “an image verification industry” now exists (Pantti
and Sirén 2015, p. 498). Resources and projects addressing this issue
include the Verification Handbook, Storyful, Verifeye Media, Checkdesk,
FourandSix, Citizenside, Amnesty International Citizen Lab, First Draft
News, Witness, StopFake and Bellingcat (Silverman 2012; Bell 2017;
Allan 2017; Witness, n.d.).
A growing range of new technology tools aim to facilitate and streamline image verification in response to constraints on time and resources.
Tools designed to verify images after they have been taken include
Amnesty International’s YouTube Data Viewer, Google reverse image
search, TinEye, Findexif and FotoForensics. When images are shared
via Facebook, Twitter, YouTube, or WhatsApp, key information about
the source and context are often stripped or misattributed. Smartphone
apps designed to collect key metadata information such as the time, date
and location at the point of capture include eyeWitness to Atrocities,
International Evidence Locker, Truepic, Whistler, the Guardian Project’s
Camera V and Proofmode. These tools are potentially useful in tackling
this “disembodiment of information” (McPherson and Probert 2017,
p. 267; McPherson 2015a, p. 21; 2015b, p. 198).


Legal “Reliability”

Human rights investigators often collect information with two purposes
in mind. In the short term, information can be used in reports to
bring issues to the attention of the public and key actors including
“gatekeeper” human rights organisations, governments, embassies, international and intergovernmental NGOs (Carpenter 2010, p. 205; Bob
2008, p. 6). [2] In the long term, this data can also be put forward to seek
social change, and if collected properly, to seek justice and accountability. For those collecting digital images for reporting on violations in the
near term, adhering to more rigorous verification standards can help to
increase their future impact (Lowe 2015).
The eyeWitness project focuses on justice for serious violations of
international law; the design of the eyeWitness camera app is therefore
founded on the core admissibility requirements for photo and video
evidence in international, regional and national courts. In particular,
the eyeWitness project reviewed the requirements of the International
Criminal Court (ICC), the International Criminal Tribunal for the
Former Yugoslavia (ICTY), the International Criminal Tribunal
for Rwanda (ICTR), the Extraordinary Chambers of the Courts
of Cambodia (ECCC), and the European Court of Human Rights
(ECtHR). [3] These courts draw on both national common law and civil
law traditions.
Even though the admissibility requirements of different courts vary,
there are some shared principles. Firstly, the images must be relevant,
or of probative value, meaning they help to prove or disprove a fact at


2 See Carpenter (2010, p. 205). Carpenter describes gatekeepers as “any global actor
densely connected to a particular issue network and thereby possessing particular influence over the issue agenda in that network” (Bob 2008, p. 6). Bob defines gatekeepers as
“entities at the core of the human rights movement, whose support for a claim can boost
it substantially. Typically these are organizations with the largest budgets, best staffs, and
greatest credibility in the rights movement. Among them…major NGOs such as Amnesty
International and Human Rights Watch; international organizations such as the UN’s
Office of the High Commissioner for Human Rights and other prominent international
bodies; and human rights intellectuals”.

3 See Ashouri et al. (2014) and Freeman (2018), for research on the use of digital evidence in international criminal courts. See also the International Criminal Court e-Court
Protocol from the Office of the Prosecutor Regulations ICC-BD/05-01-09 and Regulations
of the Court ICC-BD/01-01-04 (26 May 2004) as amended by Prosecutor v. Callixte
Mbarushimana, Case No. ICC-01/04-01/10, Decision amending the e-Court Protocol.


issue in the case. Secondly, the courts require the images to be “reliable”.
In assessing reliability, courts consider whether images are original and
unedited from the source, the chain of custody record, and information
about the time, date and location at the point of capture. The chain of
custody means information to establish the integrity of the image by tracing where it has been, who has had access and how susceptible to tampering it has been until offered in evidence (Umberg and Warden 2014;
The Engine Room 2016a, p. 36; Freeman 2018, p. 292). The eyeWitness
camera app was designed to address these authentication requirements.
At the international level, authorship of images is considered important in determining the weight given to the evidence, but the absence
of information about the author is not a bar to admissibility. There is a
need to balance protecting witness identity and establishing the source
(Ashouri et al. 2014, pp. 3–11). The eyeWitness app therefore provides
optional anonymity, and the project team consults those using the app
who chose to provide contact information before sharing their data
with a court. However, those who provide contact details may also be
called upon to testify in support of their images. Consultations with legal
professionals have confirmed that images captured with the app would be
more easily admissible. At the time of writing it is anticipated that information collected with the app will go to trial for the first time in 2018.


The eyeWitness to Atrocities App

This is a smartphone camera app that captures metadata to facilitate
the authentication of images for use in investigations or trials. It was
developed to help human rights investigators take verifiable images.
When an investigator uses the app in secure mode to take a photo or
video, the app automatically records the time, date and location using
the phone’s Global Positioning System (GPS) receivers to capture the
latitude, longitude, date and time. The app also collects information,
where available, about nearby Wi-Fi networks and cell towers, to corroborate the location. It generates a unique alphanumeric code called the
hash value for each image. This hash value is calculated using the pixel
value, which is based on the pixels’ colour, intensity and other factors.
If somebody challenges the authenticity of an image taken with the app,
the hash value of the original acts like a digital fingerprint that shows
that the image has not been edited since it was taken. The location, date
and time are stored encrypted with each image to ensure they cannot


be altered. Investigators can send the original image encrypted to the
eyeWitness server, where it is securely stored offline. This approach helps
to preserve the chain of custody. Those using the app can then save their
own copy of the image to use as they wish. The eyeWitness project can
certify the image metadata using the original to verify the copy. The app
includes a number of security features and is regularly reviewed using
feedback.


Collaborations with Investigators

In 2014, independent investigators field-tested the beta version of the
app in conflict zones and low infrastructure environments. The eyeWitness app was launched in 2015 as a free download for android devices
in the Google Play Store. Since then, the eyeWitness project has collaborated with investigators by providing this free tool for gathering and
storing evidence of international crimes for use in reports and litigation.
Despite the fact that the project arose out of the crowdsourcing movement, it was determined early on that targeted dissemination was more
appropriate. A small number of partnerships with human rights investigators were developed, and the eyeWitness project provided training and ongoing technical support to integrate the app into partners’
research methods. Today, the project has more than a dozen partner
organisations on four continents. Of the 3000 investigative images submitted to the eyeWitness server, the majority were submitted by partner
organisations.
The eyeWitness project leaves the content of investigations to each
partner’s mandate. While the eyeWitness project can verify the metadata
of images taken with the app, it does not investigate or verify the contents of the images or conduct its own advocacy. Instead, the eyeWitness
project collaborates with monitoring organisations already conducting
human rights investigations, mainly in areas of armed conflict. It aims to
support their work primarily by certifying the image metadata and the
app technology.
The approach of the eyeWitness project has been to agree to terms
on data sharing, security and confidentiality with its partners. Material
submitted from the app is securely stored and catalogued in the eyeWitness server, ensuring a protected chain of custody. The project assists its
partners’ efforts to produce stronger reports in the near term, and eventually to seek justice. Where the eyeWitness project team are not aware


of another group acting on the material to seek accountability and the
partner consents, they can seek out credible courts and accountability
mechanisms to investigate the images.


Case Study

The following is a case study of a partnership between the eyeWitness
project and investigators in Ukraine who agreed to make their use of
the eyeWitness app public. International Partnership for Human Rights
(IPHR) is an international NGO working with civil society groups
primarily in countries of the former Soviet Union, advocating for human
rights at the international level. IPHR agreed to use the eyeWitness app
as part of their documentation activities undertaken in collaboration
with Truth Hounds, a Ukrainian based NGO that aims to fight impunity by recording and monitoring human rights violations and international crimes. Prior to using the eyeWitness to Atrocities app, the Truth
Hounds team already collected photos and videos to document alleged
violations of international law.
The investigators used a combination of different investigative methods to collect information about the impact of shelling in Eastern
Ukraine for reports and submissions to courts. Their research methods include taking witness statements, notes, using Google Earth and
Google Maps and verifying information from other field researchers and
social media posts. Truth Hounds decided to use the eyeWitness app as
an additional tool to verify data collected by their monitors. They did
so as part of a “nine-step” model of data collection and verification that
aimed to strengthen evidence and reduce opportunities for data manipulation. Their main goal in using the app was to confirm shelling sites in
the Donbas region of Ukraine to help reveal whether objects protected
under international law such as schools, hospitals, churches and civilian houses may have been targeted and by whom. Truth Hounds took
photos and videos of shell casings, craters, property damage and the area
surrounding them. They then used metadata captured by the eyeWitness
app and other tools to help produce a visual map. The map accompanied the written report “Scorching Winter 2016-2017: Analysis of the
shelling of settlements in eastern Ukraine” (IPHR et al. 2017). Truth
Hounds did not use data from the app to collect standalone evidence,
but instead used it to corroborate and complement information using
multiple tools, methods and sources.


Challenges to Consider

Although technology tools have the potential to assist human rights
investigators, it is clear that they are not a panacea (Tuckwood 2014;
Raymond and Sandvik 2017; Aronson 2016, 2017). The organisations
that eyeWitness works with continue to use technology tools as part of
a combination of research methods. Our case study supports the view
that technology tools are best deployed through collaborative, reciprocal partnerships where assumptions and design are open to consultative
re-evaluation (Heinzelman and Meier 2013, pp. 125, 136; The Engine
Room 2016b, p. 16).
Technology tools designed for human rights investigations are not
suited to all contexts. When deciding on research methods and tools,
investigators should consider a number of important issues. What physical and digital security risks will the investigators face? For example, how
safe is it to have a smartphone? The availability of equipment, the level
of technology skills, access to Wi-Fi, mobile data and cell tower coverage are key factors. The storage and protection of sensitive data is also
important with options for paper archiving, electronic databases, encryption, onsite or remote repositories. Witness interviews and statements,
survey questions and written reports are used to document human rights
violations after events have taken place. Photos, videos, satellite images,
apps capturing or protecting metadata, election-monitoring apps, or hidden cameras may offer more flexibility for documenting events as they
happen or in the aftermath (The Engine Room 2016a, b; Carter Center
ELMO).
Informed consent is a matter of particular concern where technology tools are used as they can create distance between investigators,
victims and those acting on the data. Information about human rights
violations has serious security, confidentiality and legal privilege implications. However, smartphone technology has made it easy to capture and share images, often without the knowledge of the individuals
appearing in them. Human rights investigators should adhere to the
“do no harm” principle, which is the ethical obligation not to jeopardise the safety of victims and witnesses (Land et al. 2012; Land 2016,
p. 415; UNOHCHR 2011, p. 4). Investigative journalists similarly
protect the anonymity of sources in danger as a pillar of the right to
freedom of expression ( _Goodwin_ _v United Kingdom_ ECHR 1996-II).
In this context, “do no harm” implies that the person collecting the


data, the victims and bystanders appearing in images should have the
opportunity to consent to use of the data where possible and appropriate. The eyeWitness project has sought to navigate these issues by
seeking consent on use of the data from the partner organisations and
individuals submitting images to the eyeWitness server where they opt
to provide contact details.
The use of technology to document violations further complicates
informed consent by allowing anonymous data sharing. The human
rights investigators who receive information may not know the source
of the images to obtain informed consent. This challenge is particularly
acute when data collection is crowdsourced. In this situation, not
only may the sources be anonymous, they may also lack experience in
documenting human rights violations, and therefore may not recognise the risks to those they film or the need to obtain consent. A more
targeted approach to data collection like crowdseeding may ameliorate
these concerns to an extent as it allows for selection and training of the
documenters (Tuckwood 2014, p. 83; Van der Windt and Humphreys
2014, p. 3).


Conclusion

The need to authenticate images posted to social media when ordinary
bystanders and perpetrators take incriminating photographs is likely to
continue. [4] It is important that technology tools for human rights investigations complement, rather than replace, other documentation and
verification methods. Despite the challenges of new technologies, they
have the potential to help combat problems posed by “fake news”,
propaganda and misinformation by helping authenticated images to rise
above the noise. Where human rights investigators set out to collect
photographic evidence of international crimes for the dual purpose of
reporting and litigation, tools like the eyeWitness app can increase their
long-term impact for justice and accountability.


4 See Irving, E. (2017) on the use of social media videos as evidence in an ICC arrest
warrant for Mahmoud Mustafa Busayf Al-Werfalli, in the context of the Libya situation.


References


Allan, S. (Ed.). (2017). _Photojournalism and Citizen Journalism: Co-operation,_
_Collaboration and Connectivity_ . London: Routledge.
Aronson, J. D. (2016). Mobile Phones, Social Media and Big Data in Human
Rights Fact-Finding: Possibilities, Challenges and Limitations. In P. Alston
& S. Knuckey (Eds.), _The Transformation of Human Rights Fact-Finding_
[(pp. 441–462). Oxford: Oxford University Press. https://doi.org/10.1093/](http://dx.doi.org/10.1093/acprof:oso/9780190239480.003.0021)
[acprof:oso/9780190239480.003.0021.](http://dx.doi.org/10.1093/acprof:oso/9780190239480.003.0021)
Aronson, J. D. (2017). Preserving Human Rights Media for Justice,
Accountability, and Historical Clarification. _Genocide Studies and Prevention:_
_An International Journal, 11_ (1), 82–99. [https://doi.org/10.5038/1911-](http://dx.doi.org/10.5038/1911-9933.11.1.1441)
[9933.11.1.1441.](http://dx.doi.org/10.5038/1911-9933.11.1.1441)
Ashouri, A., Bowers, C., & Warden, C. (2014). The 2013 Salzburg Workshop
on Cyber Investigations: An Overview of the Use of Digital Evidence in
International Criminal Courts. _Digital Evidence and Electronic Signature Law_
_Review, 11,_ [115–127. https://doi.org/10.14296/deeslr.v11i0.2130.](http://dx.doi.org/10.14296/deeslr.v11i0.2130)
Bell, F. (2015, June 16). Verification: Source vs. Content. _First Draft_ . Retrieved from

[https://medium.com/1st-draft/verification-source-vs-content-b67d6eed3ad0.](https://medium.com/1st-draft/verification-source-vs-content-b67d6eed3ad0)
Bell, F. (2017, April 25). Here’s a List of Initiatives That Hope to Fix Trust
in Journalism and Tackle “Fake News”. _Medium_ . Retrieved from [https://](https://medium.com/%40ferg/heres-a-list-of-initiatives-that-hope-to-fix-trust-in-journalism-and-tackle-fake-news-30689feb402)
[medium.com/@ferg/heres-a-list-of-initiatives-that-hope-to-fix-trust-in-jour-](https://medium.com/%40ferg/heres-a-list-of-initiatives-that-hope-to-fix-trust-in-journalism-and-tackle-fake-news-30689feb402)
[nalism-and-tackle-fake-news-30689feb402.](https://medium.com/%40ferg/heres-a-list-of-initiatives-that-hope-to-fix-trust-in-journalism-and-tackle-fake-news-30689feb402)
Bob, C. (Ed.). (2008). _The International Struggle for New Human Rights_ .
Philadelphia: University of Pennsylvania Press.
Brandtzaeg, P. B., Lüders, M., Spangenberg, J., Rath-Wiggins, L., & Følstad, A.
(2016). Emerging Journalistic Verification Practices Concerning Social Media.
_Journalism Practice, 10_ [(3), 323–342. https://doi.org/10.1080/17512786.2](http://dx.doi.org/10.1080/17512786.2015.1020331)
[015.1020331.](http://dx.doi.org/10.1080/17512786.2015.1020331)
Carpenter, C. R. (2010). Governing the Global Agenda: Gate-Keeping and Issue
Adoption in Transnational Advocacy Networks. In D. Avant, M. Finnemore,
& S. Sell (Eds.), _Who Governs the Globe?_ (pp. 202–237). Cambridge:
Cambridge University Press.
Carter Center. (n.d.). _Election Monitoring App (ELMO)_ [. Retrieved from http://](http://electionstandards.cartercenter.org/tools/elmo/)
[electionstandards.cartercenter.org/tools/elmo/.](http://electionstandards.cartercenter.org/tools/elmo/)
Cohen, S. (2001). _States of Denial: Knowing About Atrocities and Suffering_ .
Cambridge: Polity Press.
Constable, P. (2007, February 18). Demise of the Foreign Correspondent.

_Washington Post_ [. Retrieved from http://www.washingtonpost.com/wp-dyn/](http://www.washingtonpost.com/wp-dyn/content/article/2007/02/16/AR2007021601713.html)
[content/article/2007/02/16/AR2007021601713.html.](http://www.washingtonpost.com/wp-dyn/content/article/2007/02/16/AR2007021601713.html)


Fabijanić, D., Spahr, C., & Zlatarsky, V. (Eds.). (2016). _Conflict Reporting in_
_The Smartphone Era: From Budget Constraints to Information Warfare._
Retrieved from Konrad-Adenauer-Stiftung website: [http://www.kas.de/wf/](http://www.kas.de/wf/doc/kas_47078-544-1-30.pdf%3f161128161223)
[doc/kas_47078-544-1-30.pdf?161128161223.](http://www.kas.de/wf/doc/kas_47078-544-1-30.pdf%3f161128161223)
Freeman, L. (2018). Digital Evidence and War Crimes Prosecutions: The Impact
of Digital Technologies on International Criminal Investigations and Trials.
_Fordham International Law Journal,_ _41_ (2), 283–355.
Golder, Y., & Reich, Z. (2017, May 1). Journalistic Evidence: Cross Verification
as a Constituent of Mediated Knowledge. _Journalism, 18_ (5), 558–574.
[https://doi.org/10.1177/1464884915620268.](http://dx.doi.org/10.1177/1464884915620268)
Goldsmiths University, London. (2011). _Forensic Architecture Project_ . Retrieved
[from http://www.forensic-architecture.org/.](http://www.forensic-architecture.org/)
_Goodwin v United Kingdom_ ECHR 1996-II.
Heinzelman, J., & Meier, P. (2013). Crowdsourcing for Human Rights
Monitoring: Challenges and Opportunities for Information Collection
and Verification. In J. Lannon & E. F. Halpin. (Eds.), _Human Rights and_
_Information Communication Technologies: Trends and Consequences of Use_
(pp. 123–138). Hershey, PA: IGI Global.
Hermida, A. (2015). Filtering Fact From Fiction: A Verification Framework for
Social Media. In L. Zion & D. Craig (Eds.), _Ethics for Digital Journalism_
(pp. 59–73). New York: Routledge.
International Criminal Court. (2004). _E-Court Protocol from ICC OTP_
_Regulations ICC-BD/05-01-09 Regulations of the Court ICC-BD/01-01-04_ .
Retrieved from [https://www.icc-cpi.int/NR/rdonlyres/B920AD62-DF49-](https://www.icc-cpi.int/NR/rdonlyres/B920AD62-DF49-4010-8907-E0D8CC61EBA4/277527/Regulations_of_the_Court_170604EN.pdf)
[4010-8907-E0D8CC61EBA4/277527/Regulations_of_the_](https://www.icc-cpi.int/NR/rdonlyres/B920AD62-DF49-4010-8907-E0D8CC61EBA4/277527/Regulations_of_the_Court_170604EN.pdf)
[Court_170604EN.pdf.](https://www.icc-cpi.int/NR/rdonlyres/B920AD62-DF49-4010-8907-E0D8CC61EBA4/277527/Regulations_of_the_Court_170604EN.pdf)
International Criminal Court. (2009). _E-Court Protocol from ICC OTP_
_Regulations ICC BD/05 01 09_ . Retrieved from [https://www.icc-cpi.int/](https://www.icc-cpi.int/NR/rdonlyres/%e2%80%a6/ICCBD050109ENG.pdf)
[NR/rdonlyres/…/ICCBD050109ENG.pdf as amended by Prosecutor v.](https://www.icc-cpi.int/NR/rdonlyres/%e2%80%a6/ICCBD050109ENG.pdf)
Callixte Mbarushimana, Case No. ICC-01/04-01/10, Decision amending
the e-Court Protocol, 4 (April 28, 2011). Retrieved from [https://www.icc-](https://www.icc-cpi.int/pages/record.aspx%3furi%3d1064629)
[cpi.int/pages/record.aspx?uri=1064629.](https://www.icc-cpi.int/pages/record.aspx%3furi%3d1064629)
International Partnership for Human Rights (IPHR), Truth Hounds, & Civic
Solidarity. (2017). _Scorching Winter 2016–2017: Analysis of the Shelling on_
_Settlements in Eastern Ukraine_ . Retrieved from [http://truth-hounds.org/](http://truth-hounds.org/wp-content/uploads/2017/09/last-UA-eng-20.09-web.compressed.pdf)
[wp-content/uploads/2017/09/last-UA-eng-20.09-web.compressed.pdf.](http://truth-hounds.org/wp-content/uploads/2017/09/last-UA-eng-20.09-web.compressed.pdf)
Irving, E. (2017, August 17). And So It Begins… Social Media Evidence in an ICC
Arrest Warrant. _Opinio Juris_ [. Retrieved from http://opiniojuris.org/2017/08/17/](http://opiniojuris.org/2017/08/17/and-so-it-begins-social-media-evidence-in-an-icc-arrest-warrant/)
[and-so-it-begins-social-media-evidence-in-an-icc-arrest-warrant/.](http://opiniojuris.org/2017/08/17/and-so-it-begins-social-media-evidence-in-an-icc-arrest-warrant/)
Koettl, C. (2017). Sensors Everywhere: Using Satellites and Mobile Phones to
Reduce Information Uncertainty in Human Rights Crisis Research. _Genocide_
_Studies and Prevention: An International Journal, 11_ [(1), 36–54. https://doi.](http://dx.doi.org/10.5038/1911-9933.11.1.1440)
[org/10.5038/1911-9933.11.1.1440.](http://dx.doi.org/10.5038/1911-9933.11.1.1440)


Land, M., Meier, P., Belinsky, M., & Jacobi, E. (2012, November). _#ICT4HR_
_Information and Communication Technologies for Human Rights_ . World Bank
Institute, Nordic Trust Fund, Open Development Technology Alliance &
ICT4Gov.
Land, M. K. (2016). Democratizing Human Rights Fact-Finding. In P. Alston
& S. Knuckey (Eds.), _The Transformation of Human Rights Fact-Finding_ (pp.
399–424). Oxford: Oxford University Press.
Lowe, R. (2015, June 11). _eyeWitness: Witnessing Atrocity_ . International Bar
[Association. https://www.ibanet.org/Article/NewDetail.aspx?ArticleUid=](https://www.ibanet.org/Article/NewDetail.aspx%3fArticleUid%3d11e76b66-d949-4738-9347-e67fbfbb9441)
[11e76b66-d949-4738-9347-e67fbfbb9441.](https://www.ibanet.org/Article/NewDetail.aspx%3fArticleUid%3d11e76b66-d949-4738-9347-e67fbfbb9441)
Mast, J., & Hanegreefs, S. (2015). When News Media Turn to Citizen
Generated Images of War: Transparency and Graphicness in Visual Coverage
of the Syria Conflict. _Digital Journalism, 3_ [(4), 594–614. https://doi.org/10.](http://dx.doi.org/10.1080/21670811.2015.1034527)
[1080/21670811.2015.1034527.](http://dx.doi.org/10.1080/21670811.2015.1034527)
McPherson, E. (2015a). _ICTs and Human Rights Practice: A Report Prepared_
_for the UN Special Rapporteur on Extrajudicial, Summary, or Arbitrary_
_Executions. Centre of Governance and Human Rights_ . Cambridge: University
of Cambridge.
McPherson, E. (2015b). Digital Human Rights Reporting by Civilian Witnesses:
Surmounting the Verification Barrier. In R. A. Lind (Ed.), _Producing Theory_
_in a Digital World 2.0: The Intersection of Audiences and Production in_
_Contemporary Theory_ ( _2)_ (pp. 193–209). New York: Peter Lang.
McPherson, E. (2016). Source Credibility as Information Subsidy: Strategies
for Successful NGO Journalism at Mexican Human Rights NGOs. _Journal of_
_Human Rights, 15_ [(3), 330–346. https://doi.org/10.1080/14754835.2016.](http://dx.doi.org/10.1080/14754835.2016.1176522)
[1176522.](http://dx.doi.org/10.1080/14754835.2016.1176522)
McPherson, E., & Probert, T. (2017). Special Procedures in the Digital Age.
In A. Nolan, R. Freedman, & T. Murphy (Eds.), _The United Nations Special_
_Procedures System_ (pp. 261–270). Leiden, Boston: Brill Nijhoff.
Pantti, M., & Sirén, S. (2015). The Fragility of Photo-Truth: Verification of
Amateur Images in Finnish Newsrooms. _Digital Journalism, 4_ (3), 495–512.
[https://doi.org/10.1080/21670811.2015.1034518.](http://dx.doi.org/10.1080/21670811.2015.1034518)
Platt, E. (2014, October 9). Citizen Journalists Playing a Crucial Role
in Syrian War. _Time_ . Retrieved from [http://time.com/3481790/](http://time.com/3481790/syria-journalism-kobani/)
[syria-journalism-kobani/.](http://time.com/3481790/syria-journalism-kobani/)
Powers, M. (2015). NGOs as Journalistic Entities: The Possibilities, Promises
and Limits of Boundary Crossing. In M. Carlson & S. C. Lewis (Eds.),
_Boundaries of Journalism: Professionalism, Practices and Participation_
(pp. 186–199). New York: Routledge.
Raymond, N. A., & Sandvik, K. B. (2017). Beyond the Protective Effect:
Towards a Theory of Harm for Information Communication Technologies in
Mass Atrocity Response. _Genocide Studies and Prevention: An International_
_Journal, 11_ [(1), 9–24. https://doi.org/10.5038/1911-9933.11.1.](http://dx.doi.org/10.5038/1911-9933.11.1)


Reporters Without Borders (2013, November). _Journalism in Syria,_
_Impossible Job?_ Retrieved from [https://rsf.org/en/reports/journalism-](https://rsf.org/en/reports/journalism-syria-impossible-job)
[syria-impossible-job.](https://rsf.org/en/reports/journalism-syria-impossible-job)
Safran, S. (2005, December 15). _How Participatory Journalism Works_
(Nieman Reports). Retrieved from [http://niemanreports.org/articles/](http://niemanreports.org/articles/how-participatory-journalism-works/)
[how-participatory-journalism-works/.](http://niemanreports.org/articles/how-participatory-journalism-works/)
Sambrook, R. (2010, December). _Are Foreign Correspondents Redundant? The_
_Changing Face of International News_ . Oxford: Reuters Institute for the Study
[of Journalism & Oxford University Press. Retrieved from http://reutersinsti-](http://reutersinstitute.politics.ox.ac.uk/publication/are-foreign-correspondents-redundant)
[tute.politics.ox.ac.uk/publication/are-foreign-correspondents-redundant.](http://reutersinstitute.politics.ox.ac.uk/publication/are-foreign-correspondents-redundant)
Shapiro, I., Brin, C., Bédard-Brûlé, I., & Mychajlowycz, K. (2013, December
1). Verification as a Strategic Ritual. _Journalism Practice, 7_ (6), 657–673.
[https://doi.org/10.1080/17512786.2013.765638.](http://dx.doi.org/10.1080/17512786.2013.765638)
Silverman, C. (2012). _A New Age for Truth_ (Nieman Reports). Retrieved from

[http://niemanreports.org/articles/a-new-age-for-truth/.](http://niemanreports.org/articles/a-new-age-for-truth/)
The Engine Room. (2016a). _Datnav: How to Navigate Digital Data for Human_
_Rights Research_ . Retrieved from [https://www.theengineroom.org/wp-con-](https://www.theengineroom.org/wp-content/uploads/2016/09/datnav.pdf)
[tent/uploads/2016/09/datnav.pdf.](https://www.theengineroom.org/wp-content/uploads/2016/09/datnav.pdf)
The Engine Room. (2016b). _Technology Tools in Human Rights_ . Retrieved from

[https://www.theengineroom.org/wp-content/uploads/2017/01/technolo-](https://www.theengineroom.org/wp-content/uploads/2017/01/technology-tools-in-human-rights_high-quality.pdf)
[gy-tools-in-human-rights_high-quality.pdf.](https://www.theengineroom.org/wp-content/uploads/2017/01/technology-tools-in-human-rights_high-quality.pdf)
Tuckwood, C. (2014). The State of the Field: Technology for Atrocity Response.

_Genocide Studies and Prevention: An International Journal, 8_ (3), 81–86.
[https://doi.org/10.5038/1911-9933.8.3.7.](http://dx.doi.org/10.5038/1911-9933.8.3.7)
Umberg, T., & Warden, C. (2014). The 2013 Salzburg Workshop on Cyber
Investigations: Digital Evidence and Investigatory Protocols. _Digital_
_Evidence and Electronic Signature Law Review, 11,_ 128–136. [https://doi.](http://dx.doi.org/10.14296/deeslr.v11i0.2131)
[org/10.14296/deeslr.v11i0.2131.](http://dx.doi.org/10.14296/deeslr.v11i0.2131)
United Nations Office of the High Commission for Human Rights
(UNOHCHR). (2011). _Basic Principles of Human Rights Monitoring_
_Manual on Human Right Monitoring_ . No. 7/Rev. 1, HR/P/PT/7/
Rev. 1. Retrieved from [http://www.ohchr.org/Documents/Publications/](http://www.ohchr.org/Documents/Publications/Chapter02-MHRM.pdf)
[Chapter02-MHRM.pdf.](http://www.ohchr.org/Documents/Publications/Chapter02-MHRM.pdf)
Van der Windt, P., & Humphreys, M. W. (2014). Crowdseeding in Eastern
Congo. _Journal of Conflict Resolution, 60_ (4), 748–781. [https://doi.](http://dx.doi.org/10.1177/0022002714553104)
[org/10.1177/0022002714553104.](http://dx.doi.org/10.1177/0022002714553104)
Wardle, C., Dubberley, S., & Brown, P. (2014). _Amateur Footage: A Global_
_Study of User-Generated Content in TV and Online News Output_ . Retrieved
[from the Tow Center for Digital Journalism website: http://towcenter.org/](http://towcenter.org/wp-content/uploads/2014/05/Tow-Center-Amateur-Footage-A-Global-Study-of-User-Generated-Content-in-TV-and-Online-News-Output.pdf)
[wp-content/uploads/2014/05/Tow-Center-Amateur-Footage-A-Global-](http://towcenter.org/wp-content/uploads/2014/05/Tow-Center-Amateur-Footage-A-Global-Study-of-User-Generated-Content-in-TV-and-Online-News-Output.pdf)
[Study-of-User-Generated-Content-in-TV-and-Online-News-Output.pdf.](http://towcenter.org/wp-content/uploads/2014/05/Tow-Center-Amateur-Footage-A-Global-Study-of-User-Generated-Content-in-TV-and-Online-News-Output.pdf)
Witness. (n.d.). _Video as Evidence Field Guide_ . Retrieved from [https://vae.wit-](https://vae.witness.org/video-as-evidence-field-guide/)
[ness.org/video-as-evidence-field-guide/.](https://vae.witness.org/video-as-evidence-field-guide/)


CHAPTER 15

#### A Matter of Perspective: Truth, Evidence and the Role of Photography as an Investigative Tool


_CJ Clarke_


“When I use a word,” Humpty Dumpty said in rather a scornful tone,
“it means just what I choose it to mean — neither more nor less.”

Lewis Caroll, Through the Looking Glass


It is said, the camera never lies. The camera always lies. Truth, evidence,
and the whole photographic tradition of bearing witness is really only a
matter of perspective. Whose truth, and whose pain, to paraphrase Susan
Sontag, do we choose to regard?
The role of photographer, image maker, or artist—all essentially interchangeable terms—is opaque: What they choose to frame, is dependent
on the process of exclusion. Stephen Mayes notes that “there is a vast
gulf between facts and truth, and history is strewn with factual images


CJ Clarke (*)
JAPC, London, UK


© The Author(s) 2018
O Hahn and F Stalph (eds ) _Digital Investigative Journalism_


that have been used to tell lies. So, in short, photography’s relationship
with truth is little more than ‘belief’ imposed by the viewer.” [1]

Further, we must also consider the media in which visual images
appear or are deemed fit to appear. Where and how images are used is
an important controlling factor in determining ‘whose’ truth is told, and
crucially, ‘how’ it is told. Traditionally, the individual practitioner does
not control the means of production, for instance, the headline associated with a particular image and perhaps not even the caption. All in all,
the narrative is shaped by editors far removed from the circumstances of
the images making. Without specific expertise, images are often viewed
through the prism of an editor’s own cultural understanding, which
invariably is an extension of their publications politics.
In this regard, we begin to understand the layers of framing taking
place in the photographic rendering of reality. First, there is the photographer’s own methodology, personal ethics and politics all leading to
the ‘actual’ act of framing—that is the taking of the photograph; and,
secondly, an act of framing occurs in how publications use and contextualise a particular image or set of images. It is not inconceivable that a
photographer’s own motivation or understanding of the situation is at
odds with the wider editorial position of a particular publication or the
contextual information provided by a particular publication to sit alongside their images.
So, how does all of this relate to investigative journalism? Unlike
other forms of investigative journalism—balance-sheet investigations,
for instance—the subjectivity of photographic representation makes this
a tricky question to answer. Indeed, within the confines of this article
it is, perhaps, an impossible question to answer. At its root is the inherent contradiction that photography _is_ the representation of reality and is
simultaneously _not_ the representation of reality. Such a duality keeps us
on the forked path.
For the purpose of this article I will, initially at least, focus on the
genre of photojournalism, as traditionally this is the area of photography that is most closely aligned with investigative journalism. Conceding
that I will be unable to provide any concrete ‘answers’ to the use of
photography within an investigative context, I will, instead, ruminate,


1 Stephen Mayes, interview with the author.


playfully and provocatively, on where we have been and how we might
move forward in the future.
For photojournalist Nic Dunlop, “of course, photography is the
truth,” [2] but he acknowledges its limitations, as it contains an inherent
“duality” that is not “widely understood or generally acknowledged by
practitioners, particularly in the world of photojournalism. There is still
the belief that a photograph ‘documents the truth’ which, on one level,
is true in and of itself. But the major flaw of this his view is that it implies
‘objectivity’, as though there is some nirvana of neutrality that can be
achieved.” [3]

Dunlop continues to note “the idea that a photograph can contain
many truths simultaneously is still hard for many to accept, especially if
they are contradictory truths.” He cites the example of the photographs
of those incarcerated in the infamous Khmer Rouge prison, S-21: “Many
of those incarcerated were Khmer Rouge themselves. Some were killers
who fell out of favour with the regime and found their roles reversed and
we are faced with images of victims who may have been perpetrators. It
complicates our view.” [4]

Dunlop contends that it is not “photography as a medium that is the
problem, but the way we choose to engage with a complex medium.
Photography can assist in helping us to understand on an emotional
level, but it can’t explain. Now, with smartphones even more stop to
think about the images and much fewer understand their power and why
some images arrest and others fail to engage.” [5] Similarly, filmmaker Peter
Greenaway has often commented on the inadequacies of visual imagery
in describing the representations of specific instances. Visual imagery
excels in the communication of atmosphere and mood—in all that is
non-verbal. Allied to the subjectivity inherent in the photographic gaze,
we can further glimpse the uneasy relationship between the photographic
object and notions of “evidence” or, indeed “truth.”
All of this is another way of saying that the photographic representation of the world is highly subjective. Whilst the camera can
record a moment and provide a ‘record’ of a particular event, situation


2 Nic Dunlop, interview with the author.

3 Nic Dunlop, interview with the author.

4 Nic Dunlop, interview with the author.

5 Nic Dunlop, interview with the author.


or person(s), the validity of this record as unadulterated reality is
questionable.
And yet, photography`s power to capture our imagination is unparalleled. It is a galvanising force, pulling together disparate arguments into
one readily understandable visual reference, shaping our view of events,
situations and people like no other. However, the ability of still images
to do so is dependent on its distribution through the mass media and it
would be possible to argue, perhaps cynically, that in this context, photography simply provides a visual accompaniment to the predominant
narratives that are ‘fit to print’ according to our mainstream news outlets. As Nic Dunlop notes, “We want our stories told back to us, to have
our prejudices confirmed. And we tell the same stories over and over
again to shore up our own values.” [6]

But who believes the news? Given the plurality of twenty-first century
media outlets and, especially in the ‘post-truth’ era and a steady flow of
disinformation, there is perhaps a wider, popular critique of what images
can and do (or do not) represent. Whilst scepticism is healthy, the trend
towards viewing images (or indeed any news) is worrying. One group
where belief in the power of images remains strong, however, is within
the photojournalistic industry itself. This belief, in many cases, is rigid
and built on foundations of a mythical set of values, located somewhere
in the industries mid-twentieth century heyday. (For ‘heyday’, read the
time when photojournalism was well funded and had access to a large
audience through photo-driven magazines such as _Life_ and _Picture Post_
and had not lost its audience to television news.)
From this time, the dominant form to emerge was the photographic
essay. This collection of twelve to twenty images published initially in
Life and similar publications and latterly in the glossy magazines found
in weekend newspapers probably represents the chief way in which most
people interacted with reportage and documentary visual content until
relatively recently. The leading proponent of the photo essay to emerge
in the 1950s was the photographer W. Eugene Smith. He is an iconic
figure within photojournalism, lionised for his dedication to both his
craft and the stories he chose to tell, most notably his long-term commitment to the story of the Minamata chemical disaster in Japan.


6 Nic Dunlop, interview with the author.


Smith’s much-quoted line—“With considerable soul searching, that
to the utmost of my ability, I have let truth be the prejudice” (Maddow
and Smith 1985)—has become something of a mantra for photojournalism, and his position is untouchable. Upon closer inspection, however,
Smith’s legacy rather more points towards the limitations of photojournalism and any rigid adherence to a singular ‘truth’ or proscribed ethical
standpoint. He is the proto ‘photographer-as-activist’ and his work does
rather more to advance the greater need for the subjective interpretation
than his champions would care to admit. In this sense Smith occupies a
more radical position that questions the role of mass media in the formation of dominant narratives and the relationship between said media and
individual practitioner contained therein. In such a context, the elevation
of his personal mantra to industry credo would rather seem to miss the
point.
The desire within photojournalism, to investigate by ‘bearing witness’,
with ‘truth’ on your side, would seem rather a naive standpoint; it emulates Smith’s enthusiasm without acknowledging the ambiguities highlighted through his work. As Paul Lowe (2014) identifies, “this role of
witness is more complex than at first sight” (p. 227) as it contains certain
limitations. He quotes the photographer Susan Meiselas:


[T]he other side of ‘witness’ is that we do intervene, and we intervene
by the fact of our presence in a particular place. We change how people
see themselves sometimes and how others may come to see them. I’m
also concerned about how we see ourselves in the process of our role as
witnesses. (as cited in Lowe 2014, p. 227)


Meiselas identifies photojournalism’s self-image problem, moulding
itself as a vanguard ‘truth-seeker,’ without acknowledging the problems
of such a position. Moreover, Meiselas’ comments acknowledge that the
presence of the photographer influences the scene that they are depicting
and, further, that the ‘evidence’ as gathered by a photojournalist bearing
witness is highly partisan. It is of no surprise that Meiselas’ principle concern is human rights violations and much of her work—photographic or
otherwise—embraces the partisan nature of this approach, very much in
the spirit of Smith, with the photographer occupying the role of activist
or, at very least, an active participant or visible presence within the story
they are trying to tell.


In further reference to the work of Smith we might choose to look at
his essay on Franco’s Spain—an extremely powerful set of pictures; they
are, however, something more than an impartial document of a moment
in time. In one memorable image, three Spanish soldiers are photographed looking into the sun. Their faces chiselled in harsh light and
shadow, they are ominous, and Smith’s own opinion of the dictatorship
is revealed. In another famous example, an image of a group mourning a
dead family member, Smith doctored the photograph because a woman
on the periphery was smiling—not in keeping with the overall tone of
the photograph. Smith is partisan and involved, shaping the images
based on his institution and opinion. Such involvement—and active doctoring of pictures—would fall foul of many modern ‘ethical’ standards;
nonetheless, few would argue that this work is not an ‘investigation’ into
a particular society, at a particular time. But his findings, his conclusions
are nuanced and non-verbal; they might not stand up to scrutiny as ‘evidence’ but I wonder if they tell us more about this society than a set of
images that attempts to be more impartial, distanced and objective?
Over the course of the twentieth century, the role of photography has
become intertwined with our ability to accept an event as significant. The
act of photographing, however subjective, is evidence not only of an act
actually occurring but is a signifier of importance: This event is important because it has been photographed. As Judith Butler notes, photography, with particular reference to conflict and pictures of atrocities, is
“built into the notion of atrocity, and photographic evidence establishes
the truth of the claim of atrocity in the sense that photographic evidence
has become all but obligatory to demonstrate the fact of atrocity” (as
cited in Lowe 2014, p. 227). Lowe (2014) further notes how this “is
the continual dilemma of the witness of atrocity, the more desperate and
debased the story, the more significant it becomes and the more necessary and likely it is to be reported” (p. 228).
This brings us back to the dualism of photography: A photograph is
evidence of the real, but that reality is only ‘real’ because it is photographed. And, as I enquired at the top of this essay, how does this fit
within media constructs of what is fit to print or, indeed, how is this
photographic evidence handled, understood and contextualised by the
largely western institutions that publish this material? What are their
roles and responsibilities in ‘decoding’ photographic evidence and presenting it to an audience?


Stephen Mayes notes how “impartiality and objectivity of news coverage were fantasies promoted by media proprietors as a means of bringing
credibility to their advertising platforms (AKA newspapers and magazines)”. [7] He continues to note that in the twenty-first century “photographers increasingly identify themselves as commentators, in which
capacity they bring judgment as well as supposedly fact-based observation.” Mayes’ interview with the Indian photographer Poulomi Basu
is instructive in this regard. Basu takes a “multidisciplinary” approach.
She “inhabit[s] the roles of human rights documentarian, journalist, artist and activist” noting that it is “often others who project limitations
or boundaries to an individual practitioner or, indeed, have an extreme
desire to impose constrictive labels” (Mayes 2017).
In a startling example of orientalism, Basu’s work on hidden and
normalised violence against women in sub-continental Asia in her project “ _Blood Speaks: A Ritual of Exile_ ” was censured after publication by
_The New York Times_ because it presented a more complex and nuanced
view of the ‘orient’. Basu notes how “the project tackles aspects of the
Brahmanical gaze, which is manifest throughout untouchability, gender
and caste. Such concepts might be less readily understandable to those
outside of the subcontinent. Even in the subcontinent, these issues are
considered taboo” (Mayes 2017). Highlighting the power imbalance
that exists between individual practitioners and media institutions, Basu
notes how, in her case, “the institutions of Western media have culturally
appropriated the issues to put themselves in a dominant position so that
they may cast judgement from a position of perceived cultural superiority” (Mayes 2017). In this case, Basu’s perception is rejected by “institutions that are unwittingly reinforcing the structures of patriarchy and
prejudice” (Mayes 2017) because of their inability to understand and
engage with a subject from beyond a western viewpoint. The intentions
and expertise of the practitioner are sidelined; the photograph as evidence
is censured because the western institution lacks the expertise and the
cultural humility to assess and understand the evidence as it is presented.
It is worth noting that, in Basu’s case, as with many of a new generation of photographic practitioners, the term photojournalist is assiduously avoided. Photojournalist has become a loaded term, associated
with a rigidity and sense of cultural superiority that is misplaced in


7 Stephen Mayes, interview with the author.


the multi-variant and multilayered media (and social) landscape of the
twenty-first century. As Fred Ritchin (2010) notes in his book _After_
_Photography_, in the digital age the “photograph may be seen as representing a point of view that is more synthetic and impressionist” (p. 57).
He continues to note how in “the digital arena one cannot with any certainty look at a photograph and say, ‘So that is how it was’” (p. 58).
A photograph becomes a “memory magnet” that “others can link to
… amplifying and contravening what its initial author claimed it represented” (p. 59). Thus, a photograph becomes a starting point in a wider
dialogue rather than an end, a static piece of ‘evidence’ as delineated and
asserted by ‘photojournalists’ working within what has become, particularly in the twenty-first century, an increasingly codified and reductive
framework.
For Ritchin, we certainly should not “abandon the documentary photograph as a credible recording device” because that would “handicap a
democracy’s capacity to function due to a dearth of credible evidence,”
but certainly the “growing inability of many governments and citizens
to assimilate and respond to nonlocal events, from global climate change
to the mass killings in Darfur, suggests that the kinds and amounts of
imagery available are already contributing to a cynical breakdown in
governance” (Ritchin 2010, p. 62).
First written in 2009, Ritchin’s words, in the context of ‘post-truth’,
are remarkably prescient. Despite the abundance of images to be found
in this new ‘digital’ world, the public are turning away—the value and
effectiveness of such work is in question. We may postulate that the
overuse of familiar tropes, narratives and an aesthetic associated with traditional photojournalism is, at least in part, contributing to such a situation. If this is the case then, where does this leave us? Where do we go
from here?
For Lowe (2014), one answer is to fully recognise the photograph as
an “independent artefact in and of itself as well as serving as the visual
testimony of the photographer.” The photograph is “a visual record of
the material world, yet it is also a thing in itself, with its own material
qualities” (p. 229). Lowe continues to note how “like shards of a tarnished old mirror that has been shattered, photographs reflect the past
into the present in a fragmentary, partial way” (p. 230) and that the
move towards photographing landscape and objects—what we might
call the secondary act of witnessing—positions modern photojournalism
into a more relevant and powerful space. The photographer no longer


needs to be photographing an event as it happened; rather allied to survivor testimony it “becomes an affirmation of the rights of the victim to
be known and heard,” and the “social act of witnessing” or re-witnessing to an audience “serves to re-suture the victim into the social fabric” (p. 235). Mayes notes how “photography has long been thought
to stand for truth simply because of the indexical quality which in the
analogue medium imprints fact-based information onto film; but even at
its most optimistic the medium is never truly factual when one considers the effects of blur, lens distortion and other physical phenomena.” [8]
Photography thus, assumes “a symbolic role” making full use of its qualities “to encompass both the referential and imaginative elements” (Lowe
2014, p. 235).
By way of example we may look at the work of photographer Gilles
Peress, whose work has progressed from a more classical style (albeit filtered through postmodernism and influenced by the fragmenting visual
techniques of Lee Friedlander) to something more akin to a crime scene
photographer with “close up images of the still lives of the aftermath of
atrocities, a visual trope that establishes this ‘legalistic’ approach and validates the more conventional photojournalist images in their projects,
giving them a deeper meaning than a conventional presentation might
obtain” (Lowe 2014, p. 237). Lowe (2014) argues that such a visual
strategy “builds up a more complete sense of a depth of coverage and
evidence” and the,


similarities between the role that the photograph plays in journalistic discourse and in the courtroom is [s _ic_ ] striking. In both arenas the photograph serves to help the audience grasp complex issues by simplifying them
and by giving a sense of place and orientation that textual descriptions
alone cannot deliver. (p. 237)


Embracing a more forensic approach is not, however, the only strategy for forging a new language beyond the historic conventions of photojournalism. As Basu earlier noted, her multidisciplinary practice not
only means that she inhabits many roles—artist, photographer, activist—but also that she utilises a variety of techniques, from conventional
photography and film through to virtual reality. Similar to Peress’ use
of forensic photography, Basu’s methodology expands the lexicon of


8 Stephen Mayes, interview with the author.


photography, allowing her work to contain a multiplicity of voices moving her work closer to “an oral tradition where divergent views of the
community are taken into account” (Ritchin 2010, p. 58). In embracing
such multiplicity, Basu’s visual strategies move us, the audience, towards
greater immersion and understanding of a situation in all its nuance and
complexity without the need for text-based linear explanation. Her work
is ‘evidence’ but rejects the binary—and power imbalance—that this has
traditionally meant within the strict limits of photojournalism.
The commonality between these two practitioners suggests that the
traditional lexicon of photography is inadequate for the purpose in which
it has been traditionally cast. Mayes notes that the “common anxiety is
that we need to find ways to shore up the investigative functions of the
press even as the rest of the institution moves into new territories. But
maybe the concern is misplaced, and we should instead be democratizing
investigation.” [9]

Mayes pursues this radical idea further to suggest that his “ideal
reporting team would comprise a psychologist to structure communications that get through people’s defences, a games engineer to create incentives for following stories, and an advertising creative director
because they’re the people who use imagery to really change people’s
behaviour”. [10] He continues, “In other words I’m not sure that we
should even want to sustain any credibility for twentieth century protocols … because these standards had less to do with truth-telling and
more to do with white, male capitalists trying to establish credibility for
the advertising platforms.”
We may even turn our attention away from photography altogether or, at least, photography as it is commonly understood. Threedimensional scanning, for example, is a rapidly developing technology
that has the power to record far more information than is possible with
any still or movie camera. In essence, it creates an enormous data set of
a particular environment which can be recreated as a three-dimensional
model or two-dimensional rendering, from whatever perspective the
‘author’ chooses. Beyond recording the shape of a certain environment,
it can also record data on its appearance. The UK company ScanLab


9 Stephen Mayes, interview with the author.

10 Stephen Mayes, interview with the author.


claims that it is “a form of machine vision that we argue is the future of
photography” (ScanLab, n.d.-a).
Scanning is already being utilised for forensic purposes. A collaboration with the London Fire Brigade has seen the scene of a fire scanned
and recreated so that the source of fire may be identified. Or, as in their
collaboration with _The Guardian_, “Crime Scene” (ScanLab, n.d.-b), the
technology is used to create a docu-fiction “interactive experience” that
“brings to life the fascinating world of forensic science, allowing you to
experience and understand the crucial role it plays during an investigation” (ScanLab, n.d.-b). Nevertheless, the technology’s ability to render
reality, in full 360 degrees, to a degree that allows it to be used for forensic purposes perhaps questions the role that photography holds as one of
the chief arbiters of visual ‘evidence.’
A further glimpse into the possibilities afforded by this technology is
demonstrated by an early experiment by a team led by Marc Levoy at
Stanford University. The team scanned a number of Michelangelo sculptures with such accuracy that it was possible to see Michelangelo’s chisel
marks (Levoy, n.d.).
This is ‘pure documentary’ where a data set is collected free from
the hindrance of any bias or perspective; free from the limitations of a
two-dimensional camera; free from the limitations of what an individual
is able to capture from one point within a location. Here, everything is
collected, and it is only later that this moment is recreated so that it can
be interrogated from multiple perspectives.
Similarly, Forensic Architecture (FA) “is a research agency, based at
Goldsmiths, University of London, that undertakes advanced architectural and media research on behalf of international prosecutors, human
rights organisations and political and environmental justice groups”
(Forensic Architecture, n.d.). Within this emergent field, 3D scanning
is a tool to be used alongside the collection of other data, notably film
and photos captured by those actually being affected by the event under
investigation. Unlike previous decades, the development of technology,
notably in the form of smartphones, has cast the ‘victims’ in the role of
their own documentarians. We no longer have to regard the pain of others, we can regard our own pain.


As Mayes notes, this is the “reading space to reconstruct behaviors,
or to validate people’s description of events.” [11] For FA “analysing IHL

[International Humanitarian Law] and HR [Human Rights] violations
must involve modelling dynamic events as they unfold in space and time
and creating navigable 3D models of environments undergoing conflict,
as well as the creation of filmic animations, and interactive cartographies
on the urban or architectural scale” (Forensic Architecture, n.d.).
A look at the history of arts tells us that the development of a new
technology, more suited to the portrayal of reality, liberates its antecedents to explore more abstract and nuanced territory. This was the case for
painting with the invention of photography, for instance. Such developments are, perhaps, the liberation of photography from a role in which
it was ill cast. As Nic Dunlop states, “We want the world simplified and
reduced to simple formulas of ‘good’ and ‘evil’ … we are fixated on this
interpretation in order to bring some kind of order to the messy and
grim realities of our world.” [12] Whilst understandable, this response can
be “dangerous as it shores up prejudices based on feeling alone rather
than contribute to a greater understanding.” [13]

Photography is the truth, in a sense, but it is also so much more.
Greater awareness, by both practitioners and audience, of its limitations
as ‘evidence’ is also an awareness of its strengths. At less than 200 years
old, photography is still a new art form, especially when compared with
the vast lineage of painting and literature. The photographic language
will continue to mutate. It will do so faster than those who make facile and arrogant attempts to codify its language and proscribe its ethical
standpoint. It will keep evolving and shifting; we must keep developing
and interrogating so that we can, to paraphrase T.S. Eliot, arrive where
we started and know that place for the first time.


References


Forensic Architecture. (n.d.). _Project_ [. Retrieved from http://www.forensic-archi-](http://www.forensic-architecture.org/project/)
[tecture.org/project/.](http://www.forensic-architecture.org/project/)
Levoy, M. (n.d.). _The Digital Michelangelo Project_ [. Retrieved from http://graph-](http://graphics.stanford.edu/projects/mich/)
[ics.stanford.edu/projects/mich/.](http://graphics.stanford.edu/projects/mich/)


11 Stephen Mayes, interview with the author.

12 Nic Dunlop, interview with the author.

13 Nic Dunlop, interview with the author.


Lowe, P. (2014). The Forensic Turn: Bearing Witness and Thingness of the
Photograph. In L. Kennedy & P. Caitlin (Eds.), _The Violence of the Image:_
_Photography and International Conflict_ (pp. 226–254). London: I.B. Tauris.
Maddow, B., & Smith, W. E. (1985). _Let Truth Be the Prejudice; W. Eugene_
_Smith, His Life and Photographs_ . New York, NY: Aperture.
Mayes, S. (2017, July 19). Poulomi Basu on Her Project “Ritual Of
Exile” ~ In Discussion with Stephen Mayes. _Tim Hetherington Trust_ .
[http://www.timhetheringtontrust.org/news-and-calendar/2017/07/](http://www.timhetheringtontrust.org/news-and-calendar/2017/07/poulomi-basu-her-project-ritual-exile-discussion-stephen-mayes)
[poulomi-basu-her-project-ritual-exile-discussion-stephen-mayes.](http://www.timhetheringtontrust.org/news-and-calendar/2017/07/poulomi-basu-her-project-ritual-exile-discussion-stephen-mayes)
Ritchin, F. (2010). _After Photography_ . New York, NY: W. W. Norton &
Company.
[ScanLab Projects. (n.d.-a). [Info page]. Retrieved from https://scanlabprojects.](https://scanlabprojects.co.uk/about/)
[co.uk/about/.](https://scanlabprojects.co.uk/about/)
ScanLab Projects. (n.d.-b). _Crime Scene_ [. Retrieved from https://scanlabprojects.](https://scanlabprojects.co.uk/work/crime-scene/)
[co.uk/work/crime-scene/.](https://scanlabprojects.co.uk/work/crime-scene/)


CHAPTER 16

#### The Context Verification of Digital Photographs


_Alexander Godulla_


Introduction

It is nearly impossible to determine the number of photographs taken
every day. As a direct result of the digitalisation of photography and the
rise of the smartphone, taking pictures has become an almost everyday
routine for billions of people. In a country like Germany alone, eleven
percent of all the photographs created this way enter social networking
sites within 60s (Godulla 2014, p. 402). Even without collecting comparable studies from other parts of the world, it is obvious that these
shared activities are increasing in strength. For journalists, this phenomenon is a blessing and a curse at the same time. A blessing, because it has
never been that easy to gather visual material of public interest. A curse,
because the material provided can often be the subject of manipulation.
As the essay of Tanasi in this volume shows, tampering can be identified
by using certain kinds of software. This technique of verification often
goes along with an ethic discussion. One of the most popular examples
is concerning the World Press Photo of 2013, which created its impact
on the audience by using an almost unreal use of shadow and light.


A. Godulla (*)
Institute of Communication and Media Studies, University of Leipzig,
Leipzig, Germany


© The Author(s) 2018
O Hahn and F Stalph (eds ) _Digital Investigative Journalism_


It was taken on November 20, 2012, showing dead children who are
carried through the streets of Gaza City after an Israeli attack carried
out as retaliation to Palestinian rocket fire. An extensive software analyses showed traces of intense postproduction (especially dodging, burning), but also proved that no pixels had been moved during this process
(Anthony 2013). The picture was taken by Paul Hansen, a photographer
of Danish origin. He remembers that he had to defend his image against
numerous attacks (Gailītis 2013):


Then the usual criticism came – it is too dark, too toned, too postprocessed and then again I defended and said what I did and did not.
The attacks have come from many different corners […] Finally enough
was enough and the World Press Photo sent the raw file to 3 different
experts – two in the US and one in the Netherlands. […] They went pixel
by pixel and I was cleared for any manipulation which was really good
because after that it stopped.


Hansen also explains the persistent discussion about his photograph
with the fact that its content is politically inconvenient: “Of course,
I realize that it is an uncomfortable picture for many people, it has a very
political context. Many people don’t like it, especially political players,
because it is a manifestation of a political failure” (Gailītis 2013). But
the discussion, where the enhancement of photography in general ends
and where fake photography begins could not be decided then and is still
open to debate. In contradiction to that, this essay focuses on aspects of
photography that can be described as “true” or “false”, leading to questions like:


  - Who or what is the subject of the picture?

  - Where has the photograph been taken?

  - When did the events pictured occur?

  - What is the context of the photograph, the bigger picture?


Although an important focus of the authors work lies on new formats
in journalism (Wolf and Godulla 2016), this contribution will not take
a theoretical perspective. Instead, it aims to give its reader a practical
description of the context verification of digital photographs. This technique is mainly based on journalistic research and fuelled by brainpower.
The strategy provided is the direct result of many practical courses
conducted by the author in journalism studies, where students were


confronted with similar questions. Another important inspiration can
be found in a Tipsheet based on a workshop by the German journalism
society Netzwerk Recherche (Bremer 2017). The combination of these
elements create the foundation for Fig. 16.1: Aspects like the source and
the seriality of a photograph, the quality of data, methods of external
validation, conspicuous features, the analyses of similar pictures and the
plausibility itself are combined in order to create a checklist consisting of
seven steps.
These steps will be described in detail in order to offer the reader an
easy and effective tool for the process of context verification.


_**Step 1: Source**_

In order to assess the credibility of a photograph, the quality of the
source should be taken into consideration first. Journalists should
always prefer sources of particularly high credibility. In addition to
relevant news agencies, these are also known and professional photographers, who are usually working for the editorial staff on a regular
basis. If the origin of a photograph cannot be clarified, it should not be
spread. This is particularly the case for images from social networking
sites. Frequently, it is not the images themselves, which are problematic. It is rather the caption, which is often deliberately (to manipulate
people) or mistakenly (in ignorance) falsified, changing the meaning
of a photograph by misinterpreting its context. Social networking sites
should therefore be regarded as a toxic environment for any form of
image research. Trolling, flaming and hate speech are the order of the
day, especially when dealing with controversial subjects, which makes the
assessment of the authenticity of the used imagery extremely difficult.


**Fig. 16.1** Aspects of context verification in press photography


_**Step 2: Seriality**_

In the analogous age, many popular cameras typically used 36 slides of
negative film per roll. Accordingly, it was costly and tedious in the past
to make picture serials. In any case, photographers are always looking for
the decisive moment, that is, the situation in which form and content
are in the best possible relationship. The photos taken before and after
this one shot are generally not published and are thus irrelevant to the
public. This has not changed in the digital age. However, it was common
then and is common now to create larger numbers of photographs when
being confronted with highly relevant motives. For example, a modern
professional photojournalist would take more than 1000 photographs
during an important soccer game (Godulla 2009, p. 50). Even with portrait photos, many photographers today use the serial mode of a camera
in order to capture the best possible facial expression of a person. When
assessing the authenticity of a possibly faked photograph, it is therefore a
good strategy to ask the source for further material from the same series.
Frequently, additional aspects of the situation become visible, which
allow a better assessment of the image. If the source cannot or will not
provide further material, the credibility of the justification is a further
hint for the authenticity of a photograph.


_**Step 3: Quality of Data**_

In the age of digital photography the use of film has been massively
pushed back. Instead, photos are stored in certain data formats, each
with certain properties. So-called JPEGs provide a lossy compression
for digital images. This format is used by nearly every amateur camera,
including smartphones. Even professionals often rely on JPEGs when
having to deliver photos to professional customers like editorial offices.
However, JPEGs provide only a little potential for shadow recovery
or highlight recovery. Legitimate and traditional techniques of image
optimization are thus made more difficult using them. Professional
photographers therefore often rely on the so-called RAW format,
which creates a kind of digital negative. This file requires much more
disk space, but also allows much better post-processing. Therefore, the
majority of professional photographers tend to use both formats in their
workflows. Digital manipulations are much more difficult to apply to
RAW-files than to JPEGs. For this reason, editorial teams should request


access to any RAW-file related to a photograph of questionable authenticity. In addition, the accompanying metadata should also be included in
the assessment. Although Metadata can easily be falsified, it is a possible
source of error for any counterfeiter. Metadata can, for example, list the
GPS coordinates of the location of the photograph, the focal length of
the lens used, or the shutter speed. These values should be compared
with the caption of the picture already provided. A programme being
able to read metadata (such as Adobe Lightroom) should be used for
this purpose. Metadata readers available only online should be avoided
in the meantime, since particularly sensitive image material should not be
uploaded to the World Wide Web without further need.


_**Step 4: External Validation**_

Whether this fourth step is necessary at all depends on the course of the
previous analysis steps. If the source is credible (step 1), if the photo
can be interpreted as part of a larger series (step 2) and if the data is of
high quality (step 3), a fair amount of journalistic care has already been
provided. If, on the other hand, the photo does not meet all or none of
the criteria, it must be regarded to be very questionable. In this case, an
editorial office must ask whether such a photo should be distributed at
all. If there is a compelling reason for this, the search radius should now
be extended to the World Wide Web. The use of monitoring pages such
as snopes.com, which deal with lies spread in cyberspace, may be ­helpful.
These sites allow searching for keywords or even URLs. However, this
requires that the relevant topic has already been exposed as a hoax.
Similarly, search engines like google.com can be used to find comparable
clues through a keyword search. If this is unsuccessful, the photo is far
from genuine: it can also only be an indication that you do not use the
adequate keywords.


_**Step 5: Conspicuous Features**_

If no suspicious fakes can be found elsewhere, it is worth taking a closer
look at the photograph on the actual image plane. When following this
strategy, it is important to free yourself from your own prejudices as a
viewer: how a refugee, a soldier or a passer-by can look like will be very
different, depending on the context. In the age of globalisation it is, for
example, completely normal that people wearing printed T-shirts appear


in tribal cultures. Nevertheless, it is worth taking a look at the attire of
people who are depicted: does it, for example, correspond to the ­cultural
context, religious traditions or climatic conditions? If the photo is
sufficiently important, experts with relevant knowledge can be consulted
here. Similarly, it is worth searching for everything that contains writing.
Road signs, number plates or advertisements are a good example. In this
case too, people with regional knowledge can be consulted in order to
identify the culture and the country. Strictly speaking, any element on
the picture can serve as an indication: Power sockets, for example, indicate which standard is used in a country. Floor coverings can massively
differ by country, making them correspondingly meaningful. The same
applies to shadows or the position of the sun in the sky, which can be
helpful when identifying the time of recording.


_**Step 6: Similar Pictures**_

This step is always effective when a photograph has been published
already in this form or a very similar form to the World Wide Web.
In this case, you can use the image search images.google.com to insert
the URL on which the image is to be found. Alternatively, you can also
upload the image directly to find it elsewhere. The context published
here can be very helpful in assessing the authenticity of the image and to
get further clues—also for the further external validation (step 4) or the
analysis of conspicuous features (step 5).


_**Step 7: Plausibility**_

A final step in the assessment of a photo can refer to the general plausibility. Visible phenomena (such as the weather) are compared with databases. The [wolframalpha.com search engine makes it possible to search](http://www.wolframalpha.com)
historical weather data in a very comfortable way. So if there is sunshine
on a photo and the database indicates heavy rain, you might be confronted with a fake.


Conclusion

With the help of the seven steps described, it is comparatively easy to obtain
a robust impression of the authenticity of a photograph. In ­journalism,
however, it is important to consider not only the search for truth


but also factors such as time and costs. In particular the search for
­conspicuous features (step 5) can devour a lot of time, if one would like to
proceed with the necessary thoroughness. If pictures are not even plausible
based on the review of their sources (step 1), they may not be worth this
particular effort. Visual communication is always accompanied by a great
risk: what people see with their own eyes, they automatically perceive as
true. At this moment, photographs become the object of interpretation and
possible further spreading. Perhaps the most sensible response to this problem may be the decision not to spread questionable picture material at all.


References


Anthony, S. (2013, May 13). _Was the 2013 World Press Photo of the Year Faked_
_with Photoshop, or Merely Manipulated?_ [Web log post]. Retrieved from
[http://www.extremetech.com/extreme/155617-how-the-2013-world-press-](http://www.extremetech.com/extreme/155617-how-the-2013-world-press-photo-of-the-yearwas-faked-with-photoshop)
[photo-of-the-yearwas-faked-with-photoshop.](http://www.extremetech.com/extreme/155617-how-the-2013-world-press-photo-of-the-yearwas-faked-with-photoshop)
Bremer, A. (2017). _Bilder verifizieren in 5 Schritten_ [How to Verify Pictures
in Five Steps]. Retrieved from Netzwerk Recherche website [https://net-](https://netzwerkrecherche.org/wp-content/uploads/2017/06/Tipsheet-Bilder-verifizieren-nr17.pdf)
[zwerkrecherche.org/wp-content/uploads/2017/06/Tipsheet-Bilder-](https://netzwerkrecherche.org/wp-content/uploads/2017/06/Tipsheet-Bilder-verifizieren-nr17.pdf)
[verifizieren-nr17.pdf.](https://netzwerkrecherche.org/wp-content/uploads/2017/06/Tipsheet-Bilder-verifizieren-nr17.pdf)
Gailītis, V. (2013, June 4). _Interview with Paul Hansen_ [Web log post]. Retrieved
[from http://fkmagazine.lv/2013/06/04/interview-with-paul-hansen/.](http://fkmagazine.lv/2013/06/04/interview-with-paul-hansen/)
Godulla, A. (2009). _Fokus World Press Photo. Eine Längsschnittstudie “aus-_
_gezeichneter” Pressefotografie von 1955–2009_ [Focus World Press Photo. A
Longitudinal Study of Exceptional Photography from 1955–2009]. [http://](http://d-nb.info/997407689/34)
[d-nb.info/997407689/34.](http://d-nb.info/997407689/34)
Godulla, A. (2014). Authentizität als Prämisse. Moralisch legitimiertes Handeln
in der Pressefotografie [Authenticity as a Premise? Morally Legitimized
Actions in Press Photography]. _Communicatio Socialis, 47_ (4), 402–410.
Wolf, C., & Godulla, A. (2016). Potentials of Digital Longforms in Journalism.
A Survey Among Mobile Internet Users About the Relevance of Online
Devices, Internet-Specific Qualities, and Modes of Payment. _The Journal of_
_Media Business Studies, 13_ [(4), 199–221. https://doi.org/10.1080/1652235](http://dx.doi.org/10.1080/16522354.2016.1184922)
[4.2016.1184922.](http://dx.doi.org/10.1080/16522354.2016.1184922)


CHAPTER 17

#### Photo Manipulation: Software to Unmask Tampering


_Alessandro Tanasi_


In the last 10 years, we noticed an unprecedented growth of multimedia
files usage, digital images and videos, shared across social networks and
other kind of communication technologies.
The access to more powerful and cheaper tools brought digital images
editing to everyone and, with easy-to-use software for computers and
mobile, made fraudulent image forgeries easier than ever.
The challenge of evaluating the trustworthiness of a digital photo has
become a common demand and a booming research area.
To detect digital image forgeries and rate an image’s fidelity, the science of digital image forensics comes to the rescue. In the last decades
researchers have developed many digital image forensic techniques and
tools.
A number of methods have been developed to detect image forgery;
however, the process of verifying an image is a laborious and a timeconsuming task. For example, the “Visual Verification Guide for
Photos”, provided by First Draft News (First Draft, n.d.), requires
­several steps involving human interactions.


A. Tanasi (*)
Ghiro Project, Milan, Italy


© The Author(s) 2018
O Hahn and F Stalph (eds ) _Digital Investigative Journalism_


Most techniques are based on the usage of footprints left on images.
These artefacts produced and left could help to reverse-engineer and
determine the history and authenticity of images.
Each device or process involved in image creation and manipulation
usually leaves some kind of trace that could provide clues about the file.
For example, camera and sensor noise, resizing, rotation, or filters leave
artefacts which are important evidences of image manipulation.
While tampering techniques have become more sophisticated, the
state-of-the-art image forensic tools and research in detection technologies against image forgery also keep up in an evolving and more sophisticated arms race.
Can image forensics always detect a forgery? It depends on who
is better at their job: the investigator or the person who modified the
image.
For the purpose of this chapter we are referencing only free tools—
there are many great commercial image forensics products, but they are
not affordable to all. For the following examples you are going to need
only a Linux distribution like Ubuntu (Ubuntu, n.d.) or Kali (Offensive,
Security n.d.) to run the software described.
First of all, it is important to understand how digital images are
created: in most cases they are built using a graphics editor or captured
with a digital photo camera.
In digital cameras, the light goes through an optical system, using
a lens with a variable diaphragm to focus light, and falls on the sensor
when the shutter is open. The sensor consists of a large number of photodiodes which act as light receptors and turns light into discrete signals.
Each receptor, dependent on the light intensity and colour, sends a
different signal to the processor.
It translates signals in a digital image, and saves it on the memory,
either in uncompressed format (RAW) or as compressed file (for example
JPG). The file is created using a defined format, usually applying algorithms to encode data.
If the image is created or manipulated with a photo editor, the
encoded data are decoded, processed as the user requested, encoded
again, and saved.
Data are saved to disk in one of the many image file types, standardized formats for storing digital images and related data.


An image file may store data in compressed, uncompressed, or in
vector format. A grid of pixels is composed by a number of bits; the size
of the file is correlated with the resolution and the colour depth.
Images can be compressed with an algorithm to store an exact
(lossless compression) or approximated (lossy compression) image
representation.
There are literally hundreds of image file types, some standards are
open and some proprietary.
The most often used image formats on the Internet are briefly
described below:


  - JPEG (Joint Photographic Experts Group) (JPEG, n.d.): Almost
every digital camera can save photos in the JPEG format, the file
extension used is .jpg or .jpeg. JPEG applies a lossy compression
algorithm, which results in a huge file size reduction. However,
when repeatedly edited and saved, the image becomes more and
more degraded.

  - GIF (Graphics Interchange Format) (World Wide Web Consortium
1987): It is a simple and aged format, created for storing graphics with few colours and using a lossy compression algorithm. Due
to its animation capabilities, it is still used today. The file extension
is .gif.

  - PNG (Portable Network Graphics) (Duce 2003): free and open
source format created as a successor of GIF. It excels with large
images and uses a lossless compression algorithm. It is designed
for online use and can be fully streamed with a progressive display
option; the file extension is .png.


If you need to understand the format of a file, you can use the Linux
“file” command (“file (command)” 2017): It looks to the header of the
file to identify it against a database of known headers:


$ file unknown_file.xxx
unknown: PNG image data, 1534 x 960, 8-bit/color RGBA,
non-interlace


Other tools to identify format for unknown files are TrID (Pontello
2018) and Apache Tika (The Apache Software Foundation, n.d.).
If you are dealing with a large number of images, you could be interested in quickly identify exact duplicates or search for a specific image.

_Image hashing_ is used to generate a hash value for an image. This hash
value is a unique identifier for the image, and it can be used to search for
that file, regardless of file name or extension.
Hash values can be used for image database indexing and for verifying
content integrity.
Many hashing algorithms can be used, as MD5 or SHA256; for example, you can calculate SHA1 hash for a photo as follows:


$ sha1sum photo.jpg
da39a3ee5e6b4b0e3255bfef15601892afd90709 photo.jpg


The main issue with classic hashing is that one minor change to a
file, and the hash (for example MD5) is completely different. A minor
change, which leaves the photo the same to human eyes, is an alteration
leading to a different hash.
Hash comparisons are either a yes or a no—either the hash matches,
or it does not. But that does not mean that the files are not the same, it
just means they are not exactly the same (in a bit-to-bit comparison).
A _fuzzy_ or _perceptual hash_ is a fingerprint of a file derived from ­various
features from its content. Unlike cryptographic hash functions, it can
efficiently and effectively help to identify images that contain a high percentage of similarities. An investigator can then take the files with the
highest percentage of similarities and manually review those individual
images.
SSDeep (Ssdeep Project 2017) and pHash (pHash, n.d.) are examples
of fuzzy hashes. We are going to calculate SSDeep for an image, slightly
modify it, and then compare it with the calculated hash, as follows:


$ ssdeep -b image.jpg
ssdeep,1.0–blocksize:hash:hash,filename
384:HEOV6N0/xFXSw0x2K+PFfNDOPK2TYWImaMsYLB3q60tL5DwpXe9hZ4ksJWaTNpyY:HEI9Xg7+P9yImaNk3qrDwpXe9gf5xkIZ,”image.jpg”


$ ssdeep -bm dez.hash altered.jpg
altered.jpg matches image.jpg (99)


The similarity between the two images is rated with a similarity of
99%.
Microsoft developed a technology dubbed PhotoDNA (Microsoft,
n.d.) that computes the hash of multimedia files to identify images in
order to prevent child pornography. Hashes for illegal images are computed and shared with trusted parties to search, block and, report these
contents.
When a digital camera captures an image, it usually appends a whole
set of additional information called metadata, which is stored within a
file.
This data includes basic photo settings, as well as information about
the device.
Photo editing software often adds its metadata including information
about the manipulation when saving a file.
In a computer forensic investigation metadata can be extremely useful
in answering some of the questions, such as when a photo was taken, or
which camera was used.
Metadata are in most cases text information stored in the image following one or usually more than one Photographic Metadata Standards.
Those have been developed by a number of organisations, the most common are:


  - Exif (Exchangeable image file format) (CIPA 2012)

  - XMP (Extensible Metadata Platform) (Adobe, n.d.)

  - IPTC (International Press Telecommunications Council) (IPTC,
n.d.)


Stored information following these standards can be found in most of
the image file types—JPEG, PNG, TIFF, and more as well as many RAW
images—and can be sorted in the following categories:


  - Image properties: resolution, dimensions, compression

  - Date and time: Most digital cameras and photo editing tools will
record one or more timestamps


  - Camera settings during capture: exposure time, shutter speed, focal
length, ISO, camera orientation, if flash was used

  - Camera hardware: model, serial number, lens information

  - Thumbnail: A preview of the original image in small size is stored
inside the metadata. It is used by file managers and camera’s LCD
screen when showing image’s preview

  - Descriptive text: keywords, description, copyright information


Some metadata tags can be a turning point in a forensic investigation.
For example when the image is manipulated with Adobe Photoshop,
it usually writes some tags in the XMP section describing the changes
made.
The amount and type of metadata tags written can be different
between camera models and vendors, and vendors sometimes also write
proprietary tags, like the tag “MakerNote”, containing custom or proprietary data.
This peculiarity can be used to fingerprint the camera, associate a
photo to a vendor or a camera used, just looking at the metadata tags
map.
Since metadata can contain relevant footprints, it is suggested to
examine all the tags and their contents—a correlation between metadata
and other evidence could quickly lead to close the investigation.
There are many tools available to read metadata, and many
online services like FotoForensics (Hacker Factor, n.d.) or
ImageForensic (ImageForensic, n.d.) are easy to use and require only a
web browser.
Command line tools are also available, for example you can use
ExifTool (Harvey, n.d.) to extract metadata (important data are
highlighted in bold):


Thanks to metadata we can see that the photo was taken with an
iPhone, powered up for one and a half hours, and that, when saved, the
file was downloaded using Photo app.
For performance reasons, cameras store a preview inside metadata;
this thumbnail can be extracted from one file to another with ExifTool,
with the following command (with img_003.jpg being the original
image and preview.jpg the extracted thumbnail):


$ exiftool -b -PreviewImage /tmp/img_003.jpg > /tmp/preview.
jpg


It is interesting how in rare cases, if the image is edited with a software that is able to save alteration to the image but misses to update
the preview inside metadata, by extracting the preview you can spot the
difference and discover the original image before manipulation.
The Exif format has standard tags for location information, and most
of the smartphones have a built-in GPS receiver enabled during capture
to include the location information in the metadata.
Geotagging is the process of adding geographical identification
metadata to media; this data usually consists of latitude and longitude
coordinates and the altitude.
The location is calculated using GPS, WiFi router locations, or cell
tower identification preferring the most accurate method available.
When stored in metadata, latitude and longitude are stored in units
of degrees with decimals. The location values can be read by many programs, such as ExifTool:


If further clues about the geolocation of the photo are needed, what
you see can be visually compared with other images that can be found
online.


Tools as Google Street View (Google, n.d.-a) offer valuable location
intelligence, as it can provide a virtually 360-degree view of any location
including buildings and landscaping.
Since metadata are really easy to read, write and delete, it is not possible to completely rely on them as they can be easily modified.
Images are a digital translation of a picture, using algorithms colours
and light written as bits. When an image is edited, the original mathematical properties are changed and could reveal anomalies.
The tampering localisation algorithms were created to detect the most
common types of tampering footprints that can be detected in an image,
just by looking at its properties.

_Error Level Analysis_ (ELA) (“Error level analysis” 2017) is one of the
dominant image tampering localisation methods currently used. It is
based on the idea that each re-saving of a JPEG file compresses it with
lower quality. An area that was edited would have a different compression level, so under ELA it would be brighter than other areas.
Other methods are established as standards in major image forensics platforms: Discrete Wavelet High Frequency Noise, Double JPEG
Quantization, Median Filtering Noise Residue, JPEG Blocking Artefact
Inconsistencies and JPEG Ghosts.
Each technique aims at detecting different tampering traces; there is
no silver bullet, and not all algorithms should be expected to work on all
images. Therefore, it is suggested to use different algorithms and correlate the traces found.
Light and shadows are an inseparable factor of an image. There are
several techniques to detect manipulated images based on light source
direction, light intensity, or shadow.
The brightness of a certain region of an image varies with the variations in the shape of the real object. One or many inconsistencies in
the lighting environment or light source direction on various parts of the
image can be used to detect tampered images.
An image can be manipulated to add more information (e.g., more
trees in a wood) or to remove some of it (e.g., fewer trees in a forest,
copy-moving the grass over real trees), using the _image splicing_ or
_copy-moving_ manipulation. The former refers to the practice of copying
a part of an image and inserting it into another, so as to give the impression that an additional element was present in a scene. The latter means
taking a part of an image and duplicating it in another area within the
same image.


These two practices have an important distinction as different
­techniques can be used to identify each one.
The detection of copy-move forgeries is based on finding internal replications of parts or blocks of the image. Splicing detection is more complex and is usually based on the assumption that the spliced region differs
from the rest of the image in some significant aspect.
The most frequent misuse of image duplication is ripping images, the
theft of intellectual properties. A person who intends to copy images
without permission creates a near duplication of the original images.
This is a growing phenomenon in eyewitness journalism, for example in breaking news: In case of a terrorist attack, Images from previous attacks are published on social media, duplicated or altered to seem
up-to-date.
In addition to image forgery detection, the detection of duplicates and near-duplicate images is emerging as an important forensic
challenge.
A variety of existing online services such as Google Images (Google,
n.d.-b) or TinEye (TinEye, n.d.) can aid in the process of duplicate
detection and social media content verification.
Their use is suggested as a best practice, to quickly check the uniqueness of an image or to search for similarities.
Sometimes images can be tampered in an extremely professional
way, using specific techniques to avoid tampering detection called
_anti-forensics_ .
Though many existing forensic techniques are capable of detecting
a variety of common image forgeries, usually they do not account for
the possibility that anti-forensic and ad-hoc custom operations may be
designed and used to hide manipulation footprints.
Anti-forensics require skilled professionals and expensive services;
in most cases, you can ignore the probability to deal with images of
this kind, except if your threat model is designed for high profile, well
financed, and skilled actors.
We live in a time where multimedia and digital images distributed
over social networks have widespread impact on people and societies.
The presence of metadata in an image is by no means guaranteed. In
fact, for several years, it has been observed that most social media platforms tend to strip metadata from uploaded multimedia to protect their
users’ privacy. Sometimes images from social networks or messaging
application are also resized or cropped.


Investigation on images coming from social media should take care of
this sanitisation and focus on forensic techniques not based on metadata.
Researchers have developed image forensics tools and frameworks,
some of them being on-premises tools, like Ghiro (Ghiro, n.d.),
Jpegsnoop (ImpulseAdventure 2017), or Phoenix (Fırat, n.d.), and others being online services, like ImageForensic or Reveal (Reveal, n.d.).
If you are evaluating an image forensic tool it is suggested it should
meet at least the following requirements:


  - Easy integration in your image verification workflows

  - Easy to use, also for non-skilled people with little training

  - Graphical interface and visual analysis

  - Summary and exhaustive results for a quick overview and deep analysis; clear indicators describing key image manipulations

  - Support of metadata extraction, image search, duplicate detection,
image classification

  - Access to the source code or at least an explanation of the techniques used under the hood. Never trust “black box” tools, as an
investigator you should understand the methods you are using.

  - Updated with the latest advances in image forensics techniques


Image forensics is not a matter of tools only, it is also about processes
and people. Workflows should take care of image validation, and people
should be trained to understand the problem of image authenticity and
to know how much trust to put in digital media.


References


Adobe. (n.d.). _Extensible Metadata Platform (XMP)_ . Retrieved from [https://](https://www.adobe.com/products/xmp.html)
[www.adobe.com/products/xmp.html.](https://www.adobe.com/products/xmp.html)
CIPA. (2012). _Exchangeable Image File Format for Digital Still Cameras: Exif_
_Version 2.3_ [. Retrieved from http://www.cipa.jp/std/documents/e/DC-008-](http://www.cipa.jp/std/documents/e/DC-008-2012_E.pdf)
[2012_E.pdf.](http://www.cipa.jp/std/documents/e/DC-008-2012_E.pdf)
Duce, D. (Ed.). (2003). _Portable Network Graphics (PNG) Specification_ (2nd
ed.). Retrieved from [http://www.libpng.org/pub/png/spec/iso/index-ob-](http://www.libpng.org/pub/png/spec/iso/index-object.html)
[ject.html.](http://www.libpng.org/pub/png/spec/iso/index-object.html)
Error Level Analysis. (n.d.). _In Wikipedia_ . Retrieved 2017, from [https://](https://en.wikipedia.org/wiki/Error_level_analysis)
[en.wikipedia.org/wiki/Error_level_analysis.](https://en.wikipedia.org/wiki/Error_level_analysis)


file (command). (n.d.). _In Wikipedia_ . Retrieved 2017, from [https://en.wikipe-](https://en.wikipedia.org/wiki/File_(command))
[dia.org/wiki/File_(command).](https://en.wikipedia.org/wiki/File_(command))
Fırat, B. (n.d.). _Phoenix—Image Forensics_ [. Retrieved from https://github.com/](https://github.com/ebemunk/phoenix)
[ebemunk/phoenix.](https://github.com/ebemunk/phoenix)
First Draft. (n.d.). _Visual Verification Guide—Photos_ [. Retrieved from https://firstdraft-](https://firstdraftnews.org/en/education/curriculum-resource/visual-verification-guide-photos/)
[news.org/en/education/curriculum-resource/visual-verification-guide-photos/.](https://firstdraftnews.org/en/education/curriculum-resource/visual-verification-guide-photos/)
[Ghiro. (n.d.). [Homepage]. Retrieved from http://www.getghiro.org/.](http://www.getghiro.org/)
Google. (n.d.-a). _Google Street View_ [. Retrieved from https://www.google.com/](https://www.google.com/streetview/)
[streetview/.](https://www.google.com/streetview/)
Google. (n.d.-b). _Google Images_ [. Retrieved from https://images.google.com/.](https://images.google.com/)
Hacker Factor. (n.d.). _FotoForensics_ [. Retrieved from https://fotoforensics.com.](https://fotoforensics.com)
Harvey, P. (n.d.). _ExifTool by Phil Harvey_ . Retrieved from [https://sno.phy.](https://sno.phy.queensu.ca/%7ephil/exiftool/)
[queensu.ca/~phil/exiftool/.](https://sno.phy.queensu.ca/%7ephil/exiftool/)
ImageForensic. (n.d.). [Homepage]. Retrieved from [https://www.imageforen-](https://www.imageforensic.org/)
[sic.org/.](https://www.imageforensic.org/)
ImpulseAdventure. (2017). _JPEGsnoop 1.8.0—JPEG File Decoding Utility_ .
[Retrieved from http://www.impulseadventure.com/photo/jpeg-snoop.html.](http://www.impulseadventure.com/photo/jpeg-snoop.html)
IPTC. (n.d.). _Photo Metadata_ . Retrieved from [https://iptc.org/standards/](https://iptc.org/standards/photo-metadata/)
[photo-metadata/.](https://iptc.org/standards/photo-metadata/)
[JPEG. (n.d.). [Homepage]. Retrieved from https://jpeg.org.](https://jpeg.org)
Microsoft. (n.d.). _Photo DNA Cloud Service_ . Retrieved from [https://www.](https://www.microsoft.com/en-us/photodna)
[microsoft.com/en-us/photodna.](https://www.microsoft.com/en-us/photodna)
Offensive Security. (n.d.). _Kali Linux_ [. Retrieved from https://www.kali.org.](https://www.kali.org)
pHash. (n.d.). pHash. _The Open Source Perceptual Hash Library_ . Retrieved from

[http://phash.org/.](http://phash.org/)
Pontello, M. (2018, April 8). _TrID—File Identifier_ . Retrieved from [http://](http://mark0.net/soft-trid-e.html)
[mark0.net/soft-trid-e.html.](http://mark0.net/soft-trid-e.html)
Reveal. (n.d.). _Reveal Image Verification Assistant_ [. Retrieved from http://reveal-](http://reveal-mklab.iti.gr/reveal/)
[mklab.iti.gr/reveal/.](http://reveal-mklab.iti.gr/reveal/)
Ssdeep Project. (2017, November 7). _Ssdeep—Fuzzy hashing Program_ . Retrieved
[from http://ssdeep.sourceforge.net.](http://ssdeep.sourceforge.net)
The Apache Software Foundation. (n.d.). _Apache Tika—a Content Analysis_
_Toolkit_ [. Retrieved from https://tika.apache.org/.](https://tika.apache.org/)
TinEye. (n.d.). _Reverse Image Search_ [. Retrieved from https://www.tineye.com/.](https://www.tineye.com/)
[Ubuntu. (n.d.). [Homepage]. Retrieved from https://www.ubuntu.com/.](https://www.ubuntu.com/)
World Wide Web Consortium. (1987). GIF. Graphics Interchange Format. _A_
_Standard Defining a Mechanism for the Storage and Transmission of Raster-_
_Based Graphics Information_ [. Retrieved from https://www.w3.org/Graphics/](https://www.w3.org/Graphics/GIF/spec-gif87.txt)
[GIF/spec-gif87.txt.](https://www.w3.org/Graphics/GIF/spec-gif87.txt)


PART III

#### Authenticity, Identity and Transparency


The previous chapters have shown emerging techniques that challenge
the status quo of journalism every day. A continuous datafication of
sources and information flows and accompanying requirements challenge not only practitioners, but in more general journalism as a pillar of
society. Innovative approaches, more than ever relying on technological
innovations, prompt producers and editors to incorporate new practices
into their repertoires; moreover, not only journalists, but also their readers and users who are a manifestation of the public sphere need to catch
up with these innovations.
Therefore, it is imperative to discuss previously introduced techniques
and projects from a societal and sociological viewpoint. Adducing current
incidents, the following chapters examine aspects and examples that are
both results from an ongoing digitalisation and evolution of journalism on
the one hand, and on the other hand reasons for the adaptation of innovative approaches. The dilemma here is a constantly widening gap between
technological advancements and deadlocked regulatory bodies and policies.
Authenticity, identity and transparency challenge journalism and other
societal institutions on several levels. Information warfare and propaganda try to undermine and destabilise established systems with the
objective to influence public opinion and to manipulate marginal groups.
As the political sector and the public sphere are evidently prone to
attacks from maleficent influencers, the journalistic system and its logic—
serving as a corrective in public communication and opinion building—
need to be discussed against this backdrop.


CHAPTER 18

#### Fact-Checking as Defence Against Propaganda in the Digital Age


_Anna Sarmina_


Globalisation, which covered all areas of human activity and became a
component of global integration processes, has led primarily to significant changes in the information space. The result of global changes
in almost all areas of human life and activity involved a transformation of society, therefore information gained a radically new meaning.
Information now has a global character; it means that the information
flows cannot be stopped by state borders or other barriers. Digitisation
promoted new ways for gathering, storing, and disseminating information, as a result information has become an important and even strategic resource that is produced and consumed in society. Furthermore, the
information space causes social changes.
All phenomena associated with the information belong to the field
of information policy that deals with the organisation of the processes
of origin, dissemination and storage of the information in social systems. Information reflects reality, and having control of information
facilitates the control of reality, in particular because each state strives to
control as many information streams as possible (either officially or unofficially). This caused the creation of different forms of influence on mass


A. Sarmina (*)
Taras Shevchenko National University of Kyiv, Kiev, Ukraine


© The Author(s) 2018
O Hahn and F Stalph (eds ) _Digital Investigative Journalism_


consciousness, for instance think tanks—information interventions that
aspire to transform the public information space by using own resources
(economic, political, military, and international).
In this context it is emphasised that the information space changes all
the time, producing ever new instruments for influencing the public. The
more invisible such instruments are, the more powerful they are. First of
all, propaganda is one of those instruments. Propaganda can be successful only if it is inconspicuous, in which case it has a destabilising effect.
Thus, since the role of the information space is really important, it is to
be kept and defended, which is one of the main tasks of the information
policy of each state.
The radical realisation of information policy takes the form of an
information war. This means that information mechanisms are used to
solve non-informative tasks. As a result, non-informative objectives are
achieved through the use of information tools, and thus the mass consciousness is transformed. It is to be underlined that the objectives of
modern information wars cover a wide range of areas, for example economics, politics, culture, military, and other spheres.
Information war is to be seen as intervention in the information space
of another state. Such intervention can pursue two main objectives—
to integrate information or to steal information. So, the information
that belongs to the opponent must either be destroyed or controlled,
while own information must be protected. Information infrastructure,
therefore, has already become an official object of attack and defence.
The Prussian theorist Carl von Clausewitz maintained in his work “On
war” that “war is a mere continuation of politics by other means” (von
Clausewitz 2010). Generally, “by other means” describes armed violence
that is nowadays understood in the form of combat. Four generations of
wars are known in the newer history, which began after the Westphalian
peace. At the moment, we are experiencing the fourth and the most
modern generation of war: information warfare.
But what is of decisive importance for this kind of war is the fact
that the information warfare is no longer a complementary but a decisive one. The clash of information and disinformation, various types of
counterfeits (fakes)—all this is undoubtedly part of the information war.
Furthermore, the crucial role of information in the war of the fourth
generation is that the information thereby gives the possibility to conquer without armed struggle. This also implies the tendency to distance
oneself from the armed struggle; many states, as well as Ukraine, have


become demilitarised zones. Therefore, there is a need to use special
weapons, mainly cyber weaponry and information weaponry. One of
the main features of the 4th generation war is mediatisation because this
war is running under the eye of the camera and transmitted in media.
Marshall McLuhan defined this type of war very accurately. He described
it as the third war and claimed that “World War III is a guerrilla information war with no division between military and civil participation”
(McLuhan 2015).
It is clear that information campaigns are primarily targeted at informative resources, but they nevertheless produce physical consequences.
The modern type of information war is the so-called “hybrid war” or
“non-linear war”. Hybrid war is a revolution in the form of terrorism. It
is the mixture of subversive activity, ideological influences, informational
influences, and ordinary military operations. It is therefore a societyspecific warfare, in which irregular and regular tactics are combined with
modern information.
The goal of this hybrid war is to change the character of power and to
influence the opinion of the civilian population of the opponent. It is the
war of external influences and it includes a wide range of different warfare operations, including conventional and irregular combat, terrorist
attacks, information operations, or espionage. Information plays a significant role in hybrid wars because its main task is to camouflage physical violence. Glenn Russel clarified this phenomenon by talking about a
simultaneous combination of political, military, social, and media means
with conventional and irregular methods of terrorism and of subversive-criminal warfare (Russel 2009).
Thus, in every type of information war all possible means are used as
weapons, in addition to conventional methods. An important part of any
information war is information weaponry, which distinguishes it from
other wars. Information weaponry comprises complex technologies of
destructive influence on information resources and information systems
of the opponent, on the consciousness and on the area of the unconscious of the opponent. The information weapon is universal, accessible,
and massive, has non-lethal character, destroys network systems (with
viruses), controls information resources, and influences radically.
The use of information weapons in wars is closely linked to the art
of propaganda. Propaganda is as old as the hills. The origin of the
word is neutral: It comes from the ecclesiastical sphere and used to be
an honourable word. The term has received negative shading only later,


primarily because it was compromised by political regimes. Under propaganda one understands intensive communicative processes which are
aimed at changing the behaviour of the audience. Theoretically, propaganda is a special form of systematically planned mass communication, which does not want to inform or argue, but wants to persuade or
convince (Bussemer 2015). It intends to persuade to take a specific position on a specific issue and to act according to that conviction.
Disinformation is also an influential weapon of the information war. It
is the targeted distribution of false or misleading information, therefore
it is to be seen as fraud or one of its forms—lie, deception and others.
Disinformation and propaganda have much in common—both are tampering with information, misleading people by producing and presenting
untrue information, creating fakes and spreading them mainly by mass
media. In contrast to propaganda, which appeals to “emotion”, disinformation manipulates with “ratio”. But the main aim of both techniques
is that truths should be distorted, lose their value, and become useless.
That is, the first strangled victim of the information war is the truth.
The modern period is indicated as “Post-Truth Era”, which could
be explained as “relating to or denoting circumstances in which objective facts are less influential in shaping public opinion that appeals to
emotion and personal belief” (Oxford English Dictionary). It means
that the contributed information is inaccurate, skewed, biased, or fabricated. This Post-Truth Era generates some new phenomena, for example
“fake news”. Fake news are distorted signals uncorrelated with the truth
(Allcott and Gentzkow 2017). Reporting mistakes, rumours, conspiracy
theories, satire, false statements, or slanted reports are disseminated with
special intentions (Allcott and Gentzkow 2017).
Fake news, propaganda and disinformation are powerful weapons in
the modern world, as they play a significant role during the information
war, and all over the world they are changing the media landscape step
by step. The development of social media has not only made a great contribution to global changes, it has also affected democracy. Social media
is seen as a special mechanism of disseminating fake news as the information can be posted without prior approval and an increasing number
of users are getting their news from social media. The spreading of fake
information through social media is the best way because most of the
social groups accept information without checking or verifying it. In this
way society pollutes the information environment by itself. A lot of people are sceptical of the information spread by state, but they express a


greater degree of confidence in what their friends are sharing. Actually,
fictitious messages such as fake news exploit the functional logic of social
networks.
At first blush, it is difficult to realise the gravity of consequences
that fake news are able to cause. But a deeper approach to this problem
makes it clear that fakes can be really dangerous insofar as they can damage the reputation of a person as fake producer as well as fake consumer.
Moreover, fakes create distrust in all types of media, and in this way they
damage democracy. False information can ruin lives and politics, and
construct new reality by threatening through lie. The aim of spreading fakes is to create chaos in civil society. A wide range of examples
of the negative consequences of fake news is well known; among them
“Pizzagate” or the US election result in 2016 are worth mentioning.
Various types of fake news are known from media sources, for instance
“100% False”, “Slanted and Biased”, “Pure Propaganda”, “Misusing the
Data”, “Imprecise and Sloppy”, “Misinformation”, and “Shitposting”
(Johnson 2016). The verification agency First Draft News describes
seven types of Mis- and Disinformation. Among them are “False
Connection”, “False Context”, “Manipulated Content”, “Satire or
Parody”, “Misleading Content”, “Imposter Content”, and “Fabricated
Content” (Wardle 2017). Nevertheless, propaganda still has the leading
role.
Nowadays, at the time of Russian interventions in democratic processes in Ukraine, reliable sources are significant. The actual events in
Ukraine are a mixture of propaganda, subversive activity and, of course,
military actions. So the Ukraine conflict is the obvious pattern of a
hybrid war that consists of two inalienable components—information
attacks and military actions. Russia’s policy of destabilisation in Ukraine
has attracted the attention of experts to the phenomenon of the information war and its tools. “Russia had to make a big propagandistic effort

- to change the situation in the physical domain, it had to change it in
information and virtual domains” (Pocheptsov 2017).
In Russia, information campaigns are closely linked to propaganda—
perhaps because Russia has inherited from the USSR a certain experience
of using propaganda for the purpose of psychological influence on individuals. The Cold War was based on propaganda mechanisms. The information war between Ukraine and Russia has a whole series of examples
of “twisting facts” and manipulation with information. The annexation
of the Crimea was accompanied by the massive use of propaganda and


disinformation being spread through different channels: by TV broadcasters, by radio, by newspapers, through the Internet. The Maidan revolution was portrayed as fascist and extremely russophobic. According
to the main types of propaganda (Lee and Lee 1979) all of them were
used as weapon in Ukraine conflict. For example, during the annexation of the peninsula, explicit names for Russian soldiers were avoided in
Russian reports and instead replaced by such euphemisms as “little green
men” or “polite people”. This is a brilliant example of the _card stacking_
technique.
The _glittering generalities_ technique was aimed at the destruction of
characteristics of illegality; negative labels were neutralised by using positively connoted components (for example “people’s governor”) and by
replacing illegal components with positive concepts, for example “reunification of Crimea” instead of “annexation” or “self-defence” instead of
“occupation”.
The _name calling_ technique was presented by the reinforcement of
negative characteristics of the opponent. By introducing the Maidan revolution, the protesters were called “radicals”, “fascists”, “extremists”,
“nationalists”, and “junta”. In opposition to this, the typical name for
pro-Russian elements was “patriots”.
As a brilliant example of the _plain folks_ technique could be considered the (false) information that a woman assured she witnessed the
Ukrainian soldiers crucifying a small boy and then tying his mother to
tank and dragging her.
The utmost importance has the fact that during the annexation of
the Crimea, telephone and Internet connections were cut by intentional
cables damage. In order to create a media vacuum, television was taken
under control, the Ukrainian channels were taken off the air, and Russian
programmes were broadcast. So this approach came with a special focus
on broadcast media.
Fakes have become crucial elements of this hybrid war. Aggressive
propaganda activity is aimed at domination in the information sector.
In order to achieve this goal, all possible means are applied—activity of
information services, special services, international terrorist groups. All
of them strive for information dominance, by using terror, propaganda,
diversion, and sabotage holding attacks on information, on rights, and
on liberties of the state as well as of humans. These methods demoralise society, and lead to confrontation in the society and to anarchy as a
result.


As a matter of fact, fighting propaganda is a real challenge. Certainly,
in order to defend yourself, it is important to become critical and to prevent negative consequences of fake news. It is necessary to debunk and
disable them.
There is a wide range of special organisations that keep debunking
false information. Nevertheless, common Internet users are included to
do debunking by comments (first of all in social networks).
Fact-checking is the most popular method of debunking, and in this
way it is an important tool for protecting the truth. Fact-checking is
relevant in all spheres of everyday life, but primarily it is important for
journalism, so that people could trust media. It helps to keep the media
climate healthy. “If journalism is a cornerstone of democracy, then
fact-checking is its building inspector, ensuring that the structure of a
piece of writing is sound” (Borel 2016). Journalism plays a crucial role
in the process of formation of democracy. Moreover, it is so important
to maintain public trust and to become an anchor of truth in the ocean
of propaganda. We became witnesses of a new Digital Era that causes
global changes across the world and has changed the role of information.
Earlier, the message was important, now interpretation, which is the reason why information wars evolve. Due to the digitisation, the boundaries
of what can be said and perceived have been moved. Furthermore, digitisation facilitated the creation as well as the debunking of fakes.
The aim of fact-checking as a democratic institution is promoting
truth in public discourse. Primarily it has become the task of NGOs,
think tanks, civil society, and other organisations to counter blatant propaganda. During the last years a significant rise of fact-checking websites
has been fixed. The statistics say that nowadays there are 104 active websites (the total number is 169 according to Duke Lab) whose activity
is aimed at debunking fakes. To compare, in 2014 there were only 44
web pages. This indicates the growing need for debunking fakes, and at
the same time it is the signal of an increasing number of fakes. Almost
every country of the world has at its disposal at least one web resource.
For example FactCheck.org in the USA, Faktomat in Germany, Les
Decodeurs in France, Factcheckni.org in Great Britain, Pagella Politica in
Italy, Faktabaari in Finland, Factchecker in India, the Conversation Fact
Check in Australia, Aos Fatos in Brazil, and Trudeau Meter in Canada.
In Ukraine there are at least four active web resources that evaluate the truth in news reports. The most reputed is StopFake that was
founded by alumni and volunteers at the Mohyla Journalism School in


Kiev. This website was created in 2014 for debunking Russian propaganda in Ukraine and during the last years it has grown spectacularly.
Now, this resource provides information in ten languages not only about
debunked fakes, but it also serves as an educational resource for civil
society. Ukraine is still living under fake news bombardment that contributes to the manipulation of public opinion. In our society the media
informs people primarily. As a rule, this way of informing involves huge
audience. So StopFake was launched to check facts, verify information,
refute false news about Ukraine, and this challenge was faced first of all
to restore public trust in the media. Furthermore, they keep protecting
journalism standards and draw public attention to these standards.
They analyse thousands of reports about Ukraine and in case they
establish the fact of a submission of fake information they start to investigate it. Herewith they check the sources of fakes and give conclusions
about unreliable information. It is not always possible to trace the tracks
of the origin of rumours. Nevertheless, the strategy becomes apparent.
Actually, the common techniques and methods for debunking are
used, for example checking the source (or even double-checking), checking geolocation, and verification of the information. In some cases it
is possible to investigate the origin of the rumour. In order to debunk
fakes, the possibilities of Google are widely used, as well as tools for
checking pictures in order to authenticate user-generated photos. The
most common methods are verifying information about a website and
its owner, geolocation verification, using metadata, and asking witnesses.
In this way StopFake as well as other organisations whose activity is
devoted to debunking has become a real power in an information war,
being able to disprove fakes. StopFake is a first line defence against propaganda in Ukraine.
For example, at the beginning of May 2017 Russian media reported
about a peak of tourism from Ukraine in annexed Crimea. But later on,
the Border Service Advisor of Ukraine refuted this information. On 2
May 2017 it was reported that after a meeting with Russian President
Vladimir Putin, German Chancellor Angela Merkel supports the suspension of sanctions against Russia. However, the statement of Merkel was
reduced and quoted out of the context, and in this way “twisted”. The
Chancellor noted that sanctions would be lifted only after the elimination of the reasons for which they were imposed.
A wide discussion was prompted by the topic of a beginning famine
in Ukraine. Russian media published a post from Facebook with a photo


and comment that Ukrainians are on the verge of starvation. Other
media added the false information about introduction of food cards in
Ukraine. This story was based on a video about the introduction of a
programme similar to the US food stamp programme in order to control
the prices of some food.
The fact that fighting against fake news is a top priority for Ukraine is
confirmed by the premiere of the documentary film “Nothing but Lies:
Fighting Fake News” (by Tim White), presented in Kiev in March 2017.
The film shows the history of fake news as well as actual methods and
ways for spreading them in the societies.
In order to draw conclusions, it is necessary to point out that the
Digital Age has brought significant changes that have spread over all
spheres of life. Primarily, these changes have an impact on the information domain. Globalisation has brought in addition to a number of
advantages new ways for the inflow of foreign information products,
which propagate foreign values. Due to the development of new media,
the prohibitions that existed earlier were removed; moreover, new
opportunities for terrorism have appeared.
Since 2014, we have been witnessing in Ukraine the advanced form
of hybrid warfare run according to atypical patterns that consists of
armed conflict, violence and propaganda as invisible power in this war.
Actually, non-military means play a more significant role than weapon.
Nevertheless, the strategy has become apparent; the rising fact-checking
and debunking activities have become the reaction on the propaganda
machine and disinformation company. Independent fact-checkers are
fighters in an information war.
Information campaigns are by no means a new phenomenon because
information has always been a part of conflict; such campaigns have
already evolved in the twenty-first century. They are characterised by the
use of communication technologies as well as by cyber attacks, and by
the growing importance of civil domains. In different countries they take
different forms, and different tactics are used. Nowadays, we are among
numerous information flows and that is why every information, every
fact, every event must be subject to critical analysis.


References


Allcott, H., & Gentzkow, M. (2017). Social Media and Fake News in the 2016
Election. _Journal of Economic Perspectives,_ _31_ (2), 211–236. [https://doi.](http://dx.doi.org/10.1257/jep.31.2.211)
[org/10.1257/jep.31.2.211.](http://dx.doi.org/10.1257/jep.31.2.211)


Borel, B. (2016). _The Chicago Guide to Fact-Checking_ . Chicago: The University
of Chicago Press.
Bussemer, T. (2015). _Propaganda: Konzepte und Theorien_ . Wiesbaden: VS Verlag
für Sozialwissenschaften.
Duke Reporters Lab (Cartographer). (n.d.). Global Fact-Checking Sites.

[[Interactive Map]. Retrieved from https://reporterslab.org/fact-checking/.](https://reporterslab.org/fact-checking/)
Johnson, D. J. (2016, December 13). The Five Types of Fake News. _Huffington_
_Post_ . Retrieved May 15, 2017, from [http://www.huffingtonpost.com/](http://www.huffingtonpost.com/dr-john-johnson/the-five-types-of-fake-ne_b_13609562.html)
[dr-john-johnson/the-five-types-of-fake-ne_b_13609562.html.](http://www.huffingtonpost.com/dr-john-johnson/the-five-types-of-fake-ne_b_13609562.html)
Lee, A. M., & Lee, E. B. (1979). _The Fine Art of Propaganda: Prepared for the_
_Institute for Propaganda Analysis_ . New York: Octagon Books.
McLuhan, M. (2015). _Culture Is Our Business_ . Eugene, Oregon: Wipf & Stock
Publishers.
Pocheptsov, G. (2017). The Origins of Fake and Alternative Facts Can Help Us
Understand the Concept of Post-truth. _Russian Journal of Communication,_
_9_ [(2), 210–212. https://doi.org/10.1080/19409419.2017.1323180.](http://dx.doi.org/10.1080/19409419.2017.1323180)
Post-Truth Era. (n.d.). _In Oxford English Dictionary_ . Retrieved May 15, 2017,
[from http://www.oed.com/.](http://www.oed.com/)
Russel, W. G. (2009). _Thoughts on “Hybrid” Conflict_ . Retrieved from [http://](http://smallwarsjournal.com/blog/journal/docs-temp/188-glenn.pdf%253Fq%253Dmag/docs-temp/188-glenn.pdf)
[smallwarsjournal.com/blog/journal/docs-temp/188-glenn.pdf%3Fq%3D-](http://smallwarsjournal.com/blog/journal/docs-temp/188-glenn.pdf%253Fq%253Dmag/docs-temp/188-glenn.pdf)
[mag/docs-temp/188-glenn.pdf.](http://smallwarsjournal.com/blog/journal/docs-temp/188-glenn.pdf%253Fq%253Dmag/docs-temp/188-glenn.pdf)
von Clausewitz, C. (2010). _On War: Volume I_ (n.p.). Floating Press.
Wardle, C. (2017, February 16). Fake News. It’s Complicated. _First Draft_ .
Retrieved June 15, 2017, from, [https://firstdraftnews.com/fake-news-](https://firstdraftnews.com/fake-news-complicated/)
[complicated/.](https://firstdraftnews.com/fake-news-complicated/)


CHAPTER 19

#### Crowdsourced and Patriotic Digital Forensics in the Ukrainian Conflict


_Aric Toler_


The Ukrainian Conflict is the first European war to be fought with
the ubiquitous presence of the internet, producing thousands of hours
of video and over three years’ worth of online witness accounts relaying information about the ongoing war. While this wealth of materials
allows analysis of the war in ways that would be a pipedream for journalists and historians a century ago, there is a gap between the amount
of materials compared to the capabilities and available time for professional journalists to review them. While the Syrian Civil War has lasted
for over two years longer than the Ukrainian Conflict, a similar problem
exists there, where, according to Kosslyn and Green (2016), “there are
more hours of footage online than there have been hours of actual conflict.” Just as with the Syrian Civil War, there are years of footage online
concerning the war—more than professional journalists alone are able to
handle, especially with the recent downsizing of newsrooms.
From the start of the Ukrainian Conflict in 2014, this vacuum was
filled by crowdsourcing, with amateur enthusiasts finding, verifying, and
analyzing online materials related to the war. The individuals and groups
that became active in this sphere had different motivations and expertise,


A. Toler (*)
Bellingcat, Kansas City, MO, USA


© The Author(s) 2018
O Hahn and F Stalph (eds ) _Digital Investigative Journalism_


with some choosing to maintain an anonymous internet persona and
others who use developing methodologies and practices of crowdsourced
online research to spur real-world action. But what makes these research
groups different than other types of investigators? For one, there is a
decentralized nature to them, with contributors flung across the world
and no central newsroom, as you would see with most newspapers and
even online publications. There is also the distinction of the types of
materials they use to build investigations, which are openly available to
anyone with an internet connection, as opposed to research conducted
on the ground and through local sources. While some research collectives use some non-digital research in their investigations, the vast majority of the research is built off of open source materials, which bring a
number of challenges in verification and contextualization.


What Materials Are Being Investigated?

Videos are often the most important element of open source analysis
related to the Ukrainian Conflict. The sources of the majority of these
videos are:


1. Professional media outlets, including both domestic (Hromadske,
TSN, 112 Ukraine…) and foreign outlets (BBC, RT, CNN…).
Also included are semi-professional media outlets that often veer
into propaganda, such as News-Front and DONi News.
2. Governments, including information ministries. Some of these
include Ukrainian Military TV and the so-called Donetsk People’s
Republic (DNR) Ministry of Information.
3. Participants of the conflict, including both enlisted soldiers from
Ukraine, Russia, and separatist forces, and members of volunteer
battalions.
4. Citizens, including those living in the conflict zone, and others
who record footage relevant to the on-going war, such as military
convoys en route to the Russia-Ukraine border or conflict zone.


We can see a nearly full range of these types of sources in tracking a
single BMP-2, a Soviet amphibious infantry fighting vehicle, with the
word Lavina (“Avalanche”) written across it in Russian. In August
2014, a Russian woman named Anna Bocharova uploaded a photograph (Bocharova 2014) onto the Russian social network Vkontakte


of “Lavina,” as it was being hauled through the Russian city of Staraya
Stanitsa, near the Ukrainian border. She left a geotag on the photograph,
making it easy to discover the location, along with other geographical
details that can be found on satellite imagery. At about the same time,
a Russian filmed (Action Tube 2014) as a convoy of military vehicles
passed by in the same city. “Lavina” can be seen passing by, along with
other vehicles, including one with the phrase “For the Donbas!” written
on the side. This video was uploaded to YouTube, among other social
networks.
This was not the last we would see of Lavina. A month after the
Russian citizens filmed Lavina in their country, September 2014, an
Associated Press reporter in Ukraine photographed (Vojinovic 2014)
Lavina in the city of Zhdanivka in the Donetsk Oblast. In October, a
Ukrainian citizen filmed a video (Roman iNapalm 2014) of Lavina travelling through separatist-controlled Yenakiieve, Ukraine. Later, a man
named Sergey who fought alongside separatist forces in Donetsk posted
a picture of himself on Vkontakte posing with Lavina ([Digital photo],
n.d.), while holding a rifle. Finally, in 2015, Lavina reached Vuhlehirsk,
where it participated in the February 2015 Battle of Debaltseve, which led
directly to the second Minsk ceasefire agreement. Videos from the propaganda news outlet News-Front (2015) along with the major Russian news
publication Komsomolskaya Pravda (Bellingcat Vehicle Tracking Project
2015) show Lavina in the winter battlefield where Russian and separatist
forces drove Ukraine out of the key rail hub of Debaltseve.
Together, all of these photographs and videos provide us with a
timeline of one Russian military vehicle travelling from a border city in
Russia, to Ukraine, and finally to a major battle that tipped the scale
of the Ukrainian Conflict. Most journalists do not have the time or
resources to look for all of these sources—while some are easy to find,
such as the battle footage from a major media outlet, others are not,
such as the photographs shared by normal Russian and Ukrainian citizens, or participants of the conflict. However, a number of groups did
have the collective time and expertise to gather all of these data points.


Open Source Research Groups

The three largest investigative groups that emerged during the Ukrainian
Conflict are Bellingcat, InformNapalm, and the Conflict Intelligence
Team (CIT). Each of these groups operates with different methodologies


and structures, but they are united in their near-simultaneous rises and
their focus on the Ukrainian Conflict, and later with Russia’s involvement in the Syrian Civil War. In particular, the groups differ in how
political ideology is expressed in their research, their levels of cooperation with larger media outlets and independent groups, and their efforts
to include reader engagement with research.


_**Conflict Intelligence Team (CIT)**_

The Russia-based CIT was founded under the name “War in Ukraine,”
and then rebranded to its current name in September 2015 after Russia
began its military operations in Syria. Over the past two years, this
group led by the Muscovite Ruslan Leviev has published a number of
investigations that have garnered international recognition on the presence and activities of the Russian military in Ukraine and Syria. Notably,
CIT has uncovered information regarding the deaths of Russian soldiers deployed to Syria and Ukraine, along with uncovering information regarding the Russian Armed Forces’ use of cluster munitions in
Syria. An example of one of their most successful investigations was
researching photographs and video footage from Russian state-­operated
news outlets from the Russian air base in Syria’s Latakia province.
After intense analysis of these photographs, there was clear evidence of
cluster munitions being deployed by the Russian Air Force in bombing
runs throughout the country. Combined with photographs shared from
Syrian civilians, this research showed—entirely through open source
materials—that Russia was employing these munitions, despite denials
from officials.
CIT is unique among open source-focused investigative groups in
that they are a very small team, with only six members, and all of their
researchers are Russian. The fact that this group is made up entirely of
Russian citizens and primarily operates in Russia has brought them, and
especially founder Leviev, unwanted attention from Russian authorities.
Leviev was targeted in a hack perpetrated by the Kremlin-linked hacker
group CyberBerkut (n.d.). Leviev has not just been targeted online,
but he has also been harassed with “phone calls, death threats” due to
the nature of his investigations (D’Agata 2016). Since he began probing the hidden activity of the Russian Armed Forces, Russian authorities
have twice attempted to open a criminal case against him, including in an


instance where he was interrogated by a military prosecutor. [1] As of yet,
the charges have not stuck, but the threat remains due to a 2015 decree
that makes military deaths during peacetime a state secret (Luhn 2015).
Kirill Mikhailov, a Russian anti-Kremlin activist who now lives in
Ukraine, joined the CIT in 2015 during an investigation into the
death of three GRU agents in Luhansk, Ukraine. He joined in order to
“uncover the truth about Putin’s war in Ukraine,” and does not hide
that the team has a degree of political activism built into its investigations. Dating back before the annexation of Crimea and the war in the
Donbas, Leviev has closely cooperated with Russian oppositionist and
anti-corruption activist Aleksey Navalny. Leviev still runs the Newscaster.
TV group and works as a producer there to air live streams. Navalny has
worked with Newscaster.TV to live stream protests, such as nationwide
anti-corruption demonstrations on March 26, 2017. But Leviev and
Mikhailov’s political activism does not necessarily taint their investigations, as they stress that “our goal is not to show the true face of wars
waged by the regime [Putin’s government] in Syria and Ukraine,” and
even seeing their work as a patriotic service to Russia, allowing greater
transparency into the deadly wars that Russia has participated in since
2014. “We believe soldiers’ relatives and the Russian public in general
deserve accountability from military officials,” Mykhailov explains. “This
accountability is lacking in Russia, even when compared with the United
States’ less-than-ideal track record when it comes to these issues.” [2]

The CIT has seen its greatest success through cooperative efforts with
major news outlets, namely with Reuters (Tsvetkova 2017), SkyNews
(Sparks 2016), the BBC, and Spiegel Online (2016). Leviev says that
cooperating with these major media outlets is not only beneficial in
increasing the quality of the investigation, but also through generating exposure throughout the Russian media landscape. “If you work
together with a large publication,” Leviev says, “this means that all
Russian publications will write about your work – they always monitor
what is being written by these major outlets, and also about what they
do not cover.” When a work does not come with the cooperation of a
major media outlet, CIT investigations receive less attention, and have “a
much weaker effect and smaller audience,” as Leviev explains. However,


1 Personal correspondence (May 14, 2017).

2 Personal correspondence (May 14, 2017).


these cooperative efforts are not entirely without their issues. While
online-based investigative outlets are able to be comparably agile in when
and where they share their work, there are more stringent standards and
time limits at larger news outlets, or as Leviev puts it, “The staffs at these
outlets often have hard deadlines for publication, and are not able to wait
around while you gather facts and continue on with investigations. They
need everything _now_ .” While the investigations published on the CIT
website or Facebook page do not receive nearly the number of eyeballs as
when a report is in a Reuters article, there is more flexibility with updating an investigation with newly discovered facts.


_**InformNapalm**_

The pseudonymous Ukrainian “Roman Burko” formed the investigative collective InformNapalm following a successful period of operat[ing his own investigative news site, BurkoNews.info. Burko, a native to](http://BurkoNews.info)
the Donbas of eastern Ukraine and resident of Crimea until the Russian
annexation, began writing on the Russian takeover of Crimea as it
occurred, thrusting him into a new role that he had no part of in his life
before war began (Nikitenko 2015). The Georgian Irakli Komakhidze
co-founded the project alongside Burko in 2014 (Holub et al. 2017),
with the two co-founders sharing a history of war with Russia in their
home countries. Komakhidze joined Burko in the early days of investigation by helping “identify units and equipment of the Russian terrorist forces,” as he described in a 2015 interview (Nikitenko 2015). Soon,
InformNapalm gathered volunteers from around the world, but with a
plurality of contributors from Ukraine who were concerned with Russia’s
involvement in the Ukrainian Conflict. There may also be some degree
of familiarity or cooperation with some members of InformNapalm and
the Ukrainian Security Service, judging by a report in which Roman
Burko wrote that materials in an investigation were “handed over exclusively to InformNapalm from officials of the SBU [Ukrainian Security
Service]” (Burko 2016).
Like the CIT, InformNapalm is almost exclusively concerned with
investigating events surrounding war, including tracking military units,
equipment, and sharing information on violations of the Minsk ceasefire
agreement between Ukraine and separatist forces. Some of their most
popular investigations have concerned Russian involvement in eastern
Ukraine and alleged violations of the Minsk ceasefire agreements from


separatist forces. Materials sourced from social networks and satellite images serve as the basis for these investigations, such as “Russian
cockroaches: identification of an occupier from the Russian 137th
Reconnaissance Battalion in Donetsk” (Krm 2017) and “Avdiivka on
fire: BM-21 GRAD MLRS position identified” (Kuznetsov 2017b). A
frequent type of investigation will be to uncover the social network profiles of Russian and separatist soldiers, and cross-referencing the materials
on these pages to establish which Russian military units have had active
participation in the Donbas. InformNapalm also receives photographs
and videos of drones launched by volunteer battalions and other organizations near the front-lines, allowing their analysts to identify types of
military equipment used by the Russian-separatist forces and determine
their location (Velichko 2016a).
However, in a departure from other open source research outlets,
InformNapalm has embraced a number of Ukrainian hacker groups
who have targeted Russian and separatist officials, providing a wealth
of pilfered documents and emails concerning Russian activities in the
Donbas. The most well-known of these releases were the Surkov Leaks,
for which InformNapalm provided the first analysis (Velichko 2016b) after
being granted exclusive access to the materials by the Ukrainian Cyber
Alliance, consisting of the hacker groups Cyber Hunta, FalconsFlame,
RUH8, and Trinity. These leaks received international news attention,
including widespread coverage in major American news outlets (Associated
Press 2016) at a time when news surrounding Ukraine was firmly on hold.
Similar to the CIT, InformNapalm has cooperated with large media
companies, but its greatest successes seem to come from their cooperation with Ukrainian patriotic hacker groups. The exact extent to which
InformNapalm cooperates with these groups is unclear, but it is evident
that they have been able to provide detailed analysis of the information
contained in the leaks, and drawn connections between data points in
hacked inboxes and servers. For example, a January 2017 hack from the
Ukrainian Cyber Alliance revealed documents from “the desktop computer of the reconnaissance commander” of separatist forces in Luhansk
(Kuznetsov 2017a). These documents detailed the use of the Russian
Orlan-10 drone in the Donbas, with direct cooperation between Russian
servicemen and separatist forces. InformNapalm was able to provide
analysis that further corroborated these hacks by sharing information
about previous sightings of crashed Orlan-10 drones, with serial numbers
and locations matching leaked documents.


_**Bellingcat**_ _**[3]**_

Following years of successful blogging on the “Brown Moses Blog,”
UK-based Eliot Higgins launched Bellingcat on 14 July 2014 following a crowdfunding campaign that raised over £50,000. While Higgins
mostly focused on the civil wars in Syria and Libya, the downing of
Malaysian Airlines Flight 17 (MH17) three days after his site’s launch
led to the site’s most well-known investigation. In the three years since
the site’s launch, Bellingcat has published dozens of reports investigating
the open source evidence surrounding MH17, along with other topics
related to the Ukrainian Conflict.
Similar to InformNapalm, Bellingcat hosts contributors from around
the world with roughly equal focus on Ukraine/Russia and Syria. While
the two previously discussed open source collectives focus almost exclusively on conflict-related investigations, Bellingcat uses open source
research to investigate other topics, including corruption, environmental issues, and information security. With contributors spread out across
the globe more diversely than with InformNapalm or the CIT, there is a
greater plurality of ideologies, but the majority of published investigations
take similar stances opposing the military activities of Russia and Syria,
with less of a focus towards Ukraine and the West, with some exceptions.
A difference in research methodology between Bellingcat and other
investigative collectives is the use of crowdsourcing the collection and
analysis of information. Crowdsourcing research involves a call for readers to share the burden of data collection and verification, in hopes of
increasing the quantity and quality of analysis for large amounts of information. Bellingcat’s Ukraine Conflict Vehicle Tracking Project (Kivimäki
2015) produced the most success in its crowdsourcing projects, where
the free platform Check (previously CheckDesk) was used to verify photographs and videos of military equipment in Russia and Ukraine. In this
project, Bellingcat volunteers gathered over 350 pieces of evidence surrounding military equipment in Russia and Ukraine, with the exact times
and locations established for most of these materials. Each photograph
or video was collected and verified jointly between Bellingcat staff and
online volunteers, establishing the veracity of the materials. For example,
a video showing a tank being transported would be verified as truly in
Ukraine or Russia during the time of the Ukrainian Conflict, and not


3 Note: The Author Is a Long-Time Contributor and Staff at Bellingcat.


a recycled video from the Russia-Georgia War or the Syrian Civil War.
With such a large collection of information, trends and relationships
between military convoys and individual pieces of equipment could
clearly emerge, such as the previously discussed example of the Lavina
BMP-2.
Along with its investigations, Bellingcat has focused on providing instructional materials related to open source research to readers
(Bellingcat, n.d.). Additionally, it has made efforts to establish relationships with larger media outlets through digital research training workshops. Many of the most widely-read and watched investigations into
the Ukrainian Conflict include materials from open sources, making a
working familiarity with the specialized skills surrounding their collection
and verification essentials for journalists working in the region. In 2016
alone, Bellingcat volunteers and staff members held seventeen training
workshops in seven countries, with over 200 participants representing about sixty media organizations. Among these workshops are several self-organized training sessions targeted for Russian and Ukrainian
journalists, with a focus on how to successfully implement research from
open source materials into their reporting.


Anonymous Sleuths and Citizen Activism

A number of anonymous digital sleuths work mostly on social media or
blogging platforms, where they collect and analyse information. One of
these anonymous researchers goes by the handle “Necro Mancer,” or
[@666_mancer on Twitter, and operates a blog (donetsksite.wordpress.](http://donetsksite.wordpress.com)
[com). “Mancer,” who lives in Donetsk, started writing in April 2014](http://donetsksite.wordpress.com)
after his home city was occupied by pro-Russian separatists. The Donetsk
native’s research is wide-ranging, but has two main focuses: collecting and
disseminating information regarding the daily fighting throughout the
Donbas from local witnesses, and collecting information on the local and
foreign fighters who joined the Russia-sparked war in eastern Ukraine.
Though his research methods and sources are transparent and replicable
by anyone with an internet connection, he does not pretend to be neutral in how he presents his information—“Neutral truth is good,” he says,
“but I’d like to see Donetsk Ukrainian again, and that is my target.” [4]


4 Personal correspondence (May 14, 2017).


Askai, who also uses the pseudonyms of Askai707 and sled_vzayt, is
known for his exhaustive research into Russian military equipment and
units that have made their way into eastern Ukraine since 2014. The
majority of his investigative work is rooted in the summer of 2014, when
the largest surge of Russian resources made its way into the Donbas.
The only known biographical detail about Askai is that he is a Ukrainian
man, with his name, location, and background unknown to the public.
Over three years after the outbreak of the Ukrainian Conflict, Askai still
researches the activities of Russian forces in the hot summer of 2014,
where the war turned in the favour of the self-proclaimed separatist
republics over the Ukrainian Armed Forces. Unlike the three previously
discussed research collectives, Askai runs a solo operation, with his personal Twitter account and a LiveJournal blog (sled_vzayt, n.d.).
Along with specialized anonymous investigators, there have also been
grassroots efforts enabling locals in the Donbas to share information
with Ukrainian intelligence and military officials. This trend can be seen
most clearly in the use of the hashtag #StopTerror (#CтoпTeppop) on
Twitter in 2014, in which Ukrainians would share first-hand accounts,
either through witness reports or photographic/video materials, regarding the movements of Russian/separatist military equipment and troops.
Spokesperson for the Ukrainian Anti-Terrorist Operation (ATO) Press
Center, Vladislav Sleeznev, praised these efforts in a July 2014 interview:


A lot of patriotic Ukrainians are helping us by reporting on militant positions. The help of such people is invaluable. With some other people, there
is also feedback—after the destruction of a firing position, these people will
report to us how effective we were. If, for example, information appears
in social networks, then our intelligence officials will verify this information. There have been many cases when information from local residents
has been confirmed by our intelligence officials and really helped the ATO
forces. (Serov 2014)


Challenges and Successes

While open source investigations into the Syrian and Libyan Civil Wars
existed before the Ukrainian Conflict, the rise of open source collectives
has launched the methodology to a new level of exposure and gained
a degree of public trust. In particular, Bellingcat’s investigation into
MH17 has drawn responses from high-level officials in Ukraine and


Russia, including Russian Minister of Foreign Affairs Sergey Lavrov.
Investigations from InformNapalm and the CIT have received similar
attention from government officials, granting them greater clout with
the public—even if the Russian officials only provide criticism of their
findings.
With user-generated content and internet access expanding globally,
the practices of open source research and verification will only become
more important over time, both to specialized online research groups
and traditional investigative journalists. The most common criticism levelled against open source investigations is the supposedly lesser value of
online materials as the basis of investigations, as opposed to more traditional sources such as interviews, documents acquired from anonymous
sources, and so on. However, as shown by the popularity and success
of open source-based investigations into the Ukrainian Conflict, digital
research can be just as trustworthy and appealing to audiences as shoe
leather journalism if it is properly presented and contextualized.


References


Action Tube. (2014, August 29). _Из Poccии_ _и_ д _yт_ _тaнки c_ _нa_ д _пиcью “Зa_


Action Tube. (2014, August 29). _Из Poccии_ _и_ _yт_ _тaнки c_ _нa_ _пиcью “Зa_

_Дoнбacc”, “Зa po_ д _инy”_ [From Russia There Are Tanks With the Inscription
“For Donbass”, “For Motherland”] [Video file]. Retrieved from [https://](https://www.youtube.com/watch?v=CJm5bjM3Z5c&feature=youtu.be&t=1m27s)
[www.youtube.com/watch?v=CJm5bjM3Z5c&feature=youtu.be&t=1m27s.](https://www.youtube.com/watch?v=CJm5bjM3Z5c&feature=youtu.be&t=1m27s)
Associated Press. (2016, October 26). Hackers: Emails Show Ties Between
Kremlin, Ukraine rebels. _Fox News_ . Retrieved from [http://www.foxnews.](http://www.foxnews.com/world/2016/10/26/hackers-emails-show-ties-between-kremlin-ukraine-rebels.html)
[com/world/2016/10/26/hackers-emails-show-ties-between-kremlin-](http://www.foxnews.com/world/2016/10/26/hackers-emails-show-ties-between-kremlin-ukraine-rebels.html)
[ukraine-rebels.html.](http://www.foxnews.com/world/2016/10/26/hackers-emails-show-ties-between-kremlin-ukraine-rebels.html)
Bellingcat. (n.d.). Category:Guides. _Bellingcat_ . Retrieved from [https://www.](https://www.bellingcat.com/category/resources/how-tos/)
[bellingcat.com/category/resources/how-tos/.](https://www.bellingcat.com/category/resources/how-tos/)
Bellingcat Vehicle Tracking Project. (2015, February 10). _[1140] Donbass_ ★
_8,000 soldados ucranianos rodeados en Debaltsevo 31.01.15_ [[1140] Donbass ★
8,000 Ukrainian soldiers surrounded on Debaltsevo 31.01.15] [Video file].
[Retrieved from https://www.youtube.com/watch?v=-0DBVrKi_4k.](https://www.youtube.com/watch%3fv%3d-0DBVrKi_4k)
Bocharova, A. (2014, August 22). [Photograph]. Retrieved from [https://](https://archive.is/xSUka)
[archive.is/xSUka.](https://archive.is/xSUka)
Burko, R. (2016, August 25). Doveli do psikhushki i razvalili brigadu – primery
uspeshnykh informatsionnykh operatsiy [How to Drive Someone Crazy
and Ruin a Brigade—Examples of Successful Information Operations].
_InformNapalm_ [. https://informnapalm.org/26400-doveli-do-psihushki-i-raz-](https://informnapalm.org/26400-doveli-do-psihushki-i-razvalili-brigadu-primery-uspeshnyh-informatsionnyh-operatsij/)
[valili-brigadu-primery-uspeshnyh-informatsionnyh-operatsij/.](https://informnapalm.org/26400-doveli-do-psihushki-i-razvalili-brigadu-primery-uspeshnyh-informatsionnyh-operatsij/)


CyberBerkut. (n.d.). [Website]. Retrieved from [https://cyber-berkut.org/en/](https://cyber-berkut.org/en/olden/index8.php)
[olden/index8.php.](https://cyber-berkut.org/en/olden/index8.php)
D’Agata, C. (2016, October 26). Hacking Techniques Used Against DNC,
Podesta Also Targeted Journalists Covering Russia. _CBS News_ [. http://www.](http://www.cbsnews.com/news/hacking-techniques-used-against-dnc-podesta-also-targeted-russian-journalists/)
[cbsnews.com/news/hacking-techniques-used-against-dnc-podesta-also-tar-](http://www.cbsnews.com/news/hacking-techniques-used-against-dnc-podesta-also-targeted-russian-journalists/)
[geted-russian-journalists/.](http://www.cbsnews.com/news/hacking-techniques-used-against-dnc-podesta-also-targeted-russian-journalists/)

[[Digital photo]. (n.d.). Retrieved from https://017qndpynh-flywheel.netdna-ssl.](https://017qndpynh-flywheel.netdna-ssl.com/wp-content/uploads/2015/05/lavina_10.jpg)
[com/wp-content/uploads/2015/05/lavina_10.jpg.](https://017qndpynh-flywheel.netdna-ssl.com/wp-content/uploads/2015/05/lavina_10.jpg)
Holub, A., Yelyzavetta, H., Kozlikuk, S., Malko, R., & Tynchenko, Y. (2017,
January). Information Napalm. _The Ukrainian Week. International_
_Edition, 107_ (1). Retrieved from [http://i.tyzhden.ua/content/photoal-](http://i.tyzhden.ua/content/photoalbum/2017/01_2017/23/12/book1.pdf)
[bum/2017/01_2017/23/12/book1.pdf.](http://i.tyzhden.ua/content/photoalbum/2017/01_2017/23/12/book1.pdf)
Kivimäki, V. (2015, February 3). Bellingcat Launches the Ukraine Conflict
Vehicle Tracking Project. _Bellingcat_ . [https://www.bellingcat.com/resources/](https://www.bellingcat.com/resources/2015/02/03/ukraine-conflict-vehicle-tracking-launch/)
[2015/02/03/ukraine-conflict-vehicle-tracking-launch/.](https://www.bellingcat.com/resources/2015/02/03/ukraine-conflict-vehicle-tracking-launch/)
Kosslyn, J., & Green, Y. (2016, April 20). Montage—The Next Generation
of War Reporting. _Jigsaw (Medium)_ . [https://medium.com/jigsaw/](https://medium.com/jigsaw/montage-the-next-generation-of-war-reporting-a04f4176aff)
[montage-the-next-generation-of-war-reporting-a04f4176aff.](https://medium.com/jigsaw/montage-the-next-generation-of-war-reporting-a04f4176aff)
Krm, V. (2017, March 16). Identification of an Occupier from the Russian
137th Reconnaissance Battalion in Donetsk. _InformNapalm._ Retrieved from
[https://informnapalm.org/en/russian-cockroaches-identification-occupi-](https://informnapalm.org/en/russian-cockroaches-identification-occupier-russian-137th-reconnaissance-battalion-donetsk/)
[er-russian-137th-reconnaissance-battalion-donetsk/.](https://informnapalm.org/en/russian-cockroaches-identification-occupier-russian-137th-reconnaissance-battalion-donetsk/)
Kuznetsov, M. (2017a, January 17). Reconnaissance Commander in the
2nd Army Corps in the Focus of the UCA. Part 1. Orlan-10 drone.
_InformNapalm_ . [https://informnapalm.org/en/reconnaissance-commander-](https://informnapalm.org/en/reconnaissance-commander-of-the-2nd-army-corps-in-the-focus-of-the-uca-part-1-orlan-10-drone/)
[of-the-2nd-army-corps-in-the-focus-of-the-uca-part-1-orlan-10-drone/.](https://informnapalm.org/en/reconnaissance-commander-of-the-2nd-army-corps-in-the-focus-of-the-uca-part-1-orlan-10-drone/)
Kuznetsov, M. (2017b, February 1). Avdiivka on Fire: BM-21 GRAD MLRS
Position Identified. _InformNapalm_ . Retrieved from [https://informnapalm.](https://informnapalm.org/en/avdiivka-bm21)
[org/en/avdiivka-bm21.](https://informnapalm.org/en/avdiivka-bm21)
Luhn, A. (2015, May 28). Vladimir Putin Declares All Russian Military Deaths
State Secrets. _The Guardian_ . [https://www.theguardian.com/world/2015/](https://www.theguardian.com/world/2015/may/28/vladimir-putin-declares-all-russian-military-deaths-state-secrets)
[may/28/vladimir-putin-declares-all-russian-military-deaths-state-secrets.](https://www.theguardian.com/world/2015/may/28/vladimir-putin-declares-all-russian-military-deaths-state-secrets)
News-Front. (2015, February 3). _Полная_ _зачистка_ _Углегорска._ _Спецоперация_

_ополчения. Эксклюзив. 18+_ [Complete Sweep of Uglegorsk. Special Operation
[of the Militia. Exclusive. 18+] [Video file]. Retrieved from https://www.you-](https://www.youtube.com/watch?v=7g05kXeULis)
[tube.com/watch?v=7g05kXeULis.](https://www.youtube.com/watch?v=7g05kXeULis)
Nikitenko, T. (2015, August 17). Vyzhigat napalmom. Sozdatel InformNapalm

  - Gosdepe, informatsionnom ugare i recepte dlya gosudarstva [Burned
with Napalm. The Creator of InformNapalm on the State Department,
Information Waste, and the Prescription for the State]. _Farwater_ . [https://](https://farwater.net/farwater/vyzhigat-napalmom-sozdatel-informnapalm-o-gosdepe-informacionnom-ugare-i-recepte-dlya-gosudarstva/)
[farwater.net/farwater/vyzhigat-napalmom-sozdatel-informnapalm-o-gos-](https://farwater.net/farwater/vyzhigat-napalmom-sozdatel-informnapalm-o-gosdepe-informacionnom-ugare-i-recepte-dlya-gosudarstva/)
[depe-informacionnom-ugare-i-recepte-dlya-gosudarstva/.](https://farwater.net/farwater/vyzhigat-napalmom-sozdatel-informnapalm-o-gosdepe-informacionnom-ugare-i-recepte-dlya-gosudarstva/)


Roman iNapalm. (2014, December 6). _#tanks2 Eнaкиeвo 2_ [#tanks2
Yenakiieve 2] [Video file]. Retrieved from [https://www.youtube.com/](https://www.youtube.com/watch?v=OQ4qbPQf0YU)
[watch?v=OQ4qbPQf0YU.](https://www.youtube.com/watch?v=OQ4qbPQf0YU)
Serov, I. (2014, July 15). Mirnyye geroi Donbassa: Kak zhiteli Vostoka pomogayut armii [Peaceful Heroes of the Donbass: How the People of the East
Help the Army]. _Segodnya_ . [http://www.segodnya.ua/regions/donetsk/](http://www.segodnya.ua/regions/donetsk/mirnye-geroi-donbassa-kak-zhiteli-vostoka-pomogayut-armii-536742.html)
[mirnye-geroi-donbassa-kak-zhiteli-vostoka-pomogayut-armii-536742.html.](http://www.segodnya.ua/regions/donetsk/mirnye-geroi-donbassa-kak-zhiteli-vostoka-pomogayut-armii-536742.html)
sled_vzayt. (n.d.). [Web log]. Retrieved from [http://sled-vzayt.livejournal.](http://sled-vzayt.livejournal.com/)
[com/.](http://sled-vzayt.livejournal.com/)
Sparks, J. (2016, August 10). Revealed: Russia’s ‘Secret Syria Mercenaries’. _SkyNews_ .
Retrieved from [http://news.sky.com/story/revealed-russias-secret-syria-](http://news.sky.com/story/revealed-russias-secret-syria-mercenaries-10529248)
[mercenaries-10529248.](http://news.sky.com/story/revealed-russias-secret-syria-mercenaries-10529248)
Spiegel Online. (2016, February 12). Russische Bodentruppen unterstützen
Assad-Offensive. _Spiegel Online._ Retrieved from [http://www.spiegel.de/](http://www.spiegel.de/politik/ausland/syrien-russische-bodentruppen-unterstuetzen-assad-offensive-a-1077054.html)
[politik/ausland/syrien-russische-bodentruppen-unterstuetzen-assad-offen-](http://www.spiegel.de/politik/ausland/syrien-russische-bodentruppen-unterstuetzen-assad-offensive-a-1077054.html)
[sive-a-1077054.html.](http://www.spiegel.de/politik/ausland/syrien-russische-bodentruppen-unterstuetzen-assad-offensive-a-1077054.html)
Tsvetkova, M. (2017, March 22). Russia Underplayed Losses in Recapture of
Syria’s Palmyra. _Reuters_ . Retrieved from [http://www.reuters.com/article/](http://www.reuters.com/article/us-mideast-crisis-syria-russia-casualtie-idUSKBN16T0S4)
[us-mideast-crisis-syria-russia-casualtie-idUSKBN16T0S4.](http://www.reuters.com/article/us-mideast-crisis-syria-russia-casualtie-idUSKBN16T0S4)
Velichko, A. (2016a, October 17). Drones Spot Another Large Concentration of
Russian Weaponry in Donbas (Aerial photos, video). _InformNapalm_ . Retrieved
from [https://informnapalm.org/en/concentration-russian-weaponry-](https://informnapalm.org/en/concentration-russian-weaponry-donbas-aerial/)
[donbas-aerial/.](https://informnapalm.org/en/concentration-russian-weaponry-donbas-aerial/)
Velichko, A. (2016b, October 25). SurkovLeaks: 1 GB Mail Cache Retrieved
by Ukrainian Hacktivists. _InformNapalm_ . Retrieved from [https://informna-](https://informnapalm.org/en/surkovleaks/)
[palm.org/en/surkovleaks/.](https://informnapalm.org/en/surkovleaks/)
Vojinovic, D. (2014, September 2013). _Pro-Russian Gunmen Sit Atop Armored_
_Personal Carrier as They Pass Through the Checkpoint Near the Town of_
_Zhdanivka, Eastern Ukraine, Tuesday, Sept. 23, 2014_ [Digital image].
Retrieved from [http://www.apimages.com/metadata/Index/Ukraine/](http://www.apimages.com/metadata/Index/Ukraine/76ac286a94864a32867e324de4bcbd50/7/0)
[76ac286a94864a32867e324de4bcbd50/7/0.](http://www.apimages.com/metadata/Index/Ukraine/76ac286a94864a32867e324de4bcbd50/7/0)


CHAPTER 20

#### In-Depth Crisis Reporting


_Natalia Antelava_


The boy’s name was Ziosu and he was 13 years old. I watched him as he
stood in the middle of a giant pile of debris, staring at what was, only ten
days ago, his family home.
It was May 2008. Ten days earlier, a massive cyclone had hit Burma’s
Irrawaddy Delta. We will never know for sure how many lives Cyclone
Nargis claimed, but estimated hundred thousand people had died
and tens of thousands went missing. In his village, Ziosu was the only
survivor. When the cyclone hit, he managed to climb a tree and cling on
to it for fourteen long hours as he waited for the storm to calm. From
the safety of his height he watched as the dark water swallow up his
mother, his father, his two brothers and his baby sister. No one came to
his rescue.
The illogical cruelty of any natural disaster is difficult, perhaps even
impossible to comprehend. But in Burma in 2008, a cruelty of a different sort was even more disturbing.
More than a week since the cyclone first hit, hundreds of thousands of
people like Ziosu all across the Irrawady Delta were still waiting for help.
They were hungry, desperate and isolated—not because of the weather,


N. Antelava (*)
Coda Media Inc, New York, USA


© The Author(s) 2018
O Hahn and F Stalph (eds ) _Digital Investigative Journalism_


but, as I discovered while covering it for the BBC, because their government was not interested in rescuing them.
Burma’s military rulers had spared no effort on bringing order to
the former capital Rangoon. On almost every corner of the capital there
were soldiers in dark green uniforms: sweeping, fixing and cleaning. The
state-controlled newspapers had been full of praise for the way the government has handled the crisis. The generals had made sure that no one
was in a position to challenge their view. Army checkpoints blocked all
roads to the Irrawaddy Delta. No aid workers, no foreign journalists
were allowed into the country. A few who managed to get into Rangoon
were deported.
I got lucky. I had an unused Myanmar visa in my passport when the
cyclone hit, and I flew in pretending to be a tourist. Once in the country, I eventually met up with a BBC cameraman from Bangkok who was
there under pretext of being a Thai businessman. Lying down under a
back seat in a van of one very brave Burmese man, we smuggled ourselves into the depth of Irrawaddy Delta.
It was there that I met Ziosu. A lonely boy sleeping on a floor of a
house of a local fisherman who gave shelter to a few survivors. When
the fishermen offered to take us to the worst hit villages, Ziosu said he
wanted to come along. Before dawn the following morning, we got into
a small fishing boat. Shouting to each other over the rumble of an old
engine, fishermen steered the boat through the heavy curtain of rain.
The trail of bodies and destruction stretched along the two sides of the
river. The air stunk. I counted one hundred and seven bodies before
I finally gave up. They were everywhere: lining the muddy banks of
the river, pushed into sludge and rubble—white, swollen figures of the
countless victims of cyclone Nargis.
Across the deck from me Ziosu sat quietly, his dark eyes focused on
the distance. He did not look at the bodies and paid no attention to the
heavy drops of rain that fell on his face. I tried to imagine what he had
just lived through and what was ahead of him: a thirteen-year-old in one
of the world’s most isolated countries, left without a single family member or a safety net of any sort.
As we docked, Ziosu confronted a pile of rubble that was now his
home village. For a second he stared, and then, as if he had just remembered something, he jumped off and hurriedly stretched out his hand to
help me off the boat.


And that is all I know about him. Not because his story ends there
but because a few days later I flew out of Burma, tapes hidden in a box
of tampax and I never found out what happened to him next. Because
there was always a next disaster, revolution or war to cover. Because
truth is, we journalists are terrible at following up.
In the news business, we always descend on places when big events
happen and then leave just as suddenly, pulled out by our own circumstances rather than because the story has come to an end. The result?
Gaping holes in public understanding of the crises that are shaping our
world.
Had I been able to tell you what happened to Ziosu next, had I been
able to tell the story of his community in the aftermath of the cyclone
then I would also be in a much better position to explain to you the next
big story in Burma, and the next one, too.
A few years after Cyclone Nargiz made headlines, the next time
Myanmar got into news in a big way was when it suddenly opened up.
It was a bizarre transformation from one of the world’s worst dictatorships
into a democracy. Watching it from the outside it made no sense; countries normally do not metamorphose from dictatorships overnight. But
this seems to have happened with Burma, and no one could quite explain
why. I got my explanation a couple of years later when I happened to be
seated next to a high-ranking Burmese official at a formal dinner. I asked
the man, whom I cannot name, what was behind Myanmar’s incredible
transformation. His answer shocked me: Cyclone Nargis.
The damage of the cyclone and the way it was handled made the generals realise that something in the system had to change, he explained.
I was surprised. This simple and apparently crucial bit of information was
missing entirely from a narrative that media had built around Myanmar’s
political transformation. What are we missing from the narrative of the
following big story: the horrific persecution of tens of thousands of
Rohingyas?
It is not just Burma. Did ISIS come out of nowhere? What has happened in Haiti, Syria, Libya, or Ukraine, all these places that dominate
our headlines for a while and then disappear only to burst back into our
living rooms with puzzling events that we struggle to understand.
The earthquake in Haiti killed hundreds of thousands in January
2010, precipitating a massive humanitarian and political crisis. Yet by
October only a single foreign correspondent was based in the country to
report on how the United Nations had introduced a decimating cholera


epidemic. The assassination of the US ambassador in Benghazi occurred
in an on-the-ground reporting vacuum. The conflict in Eastern Ukraine
erupted after most journalists had left the country following the referendum in Crimea.
We all know that context is key to understanding anything that happens in our life, be it a dispute with a neighbour, a success of a local
politician, or an international conflict. Events which feed news cycles
do not happen in a vacuum and crises do not end when television crews
leave. In fact, the most important things often happen once journalists
are gone and at times precisely because they have gone.
So why is it, then, that we journalists keep covering events as if they
happen in a vacuum?
The answer is multi-layered, but it is not very complex. One reason is,
of course, the decline in revenue at newsgathering organisations that has
caused a well-publicised contraction in high-quality international news
reporting—for many journalism outlets foreign reporting has reached
a point of abdication. The reduction in foreign coverage is now a twodecade trend: Back in 1998 _The American Journalism Review_ identified
18 newspapers and two chains which had shuttered every one of their
overseas bureaus during the previous twelve years (Arnett 1998). Since
then, the retreat from overseas coverage has only worsened even if media
companies like to pretend otherwise. By 2012 _The Los Angeles Times_
claimed 10 overseas “bureaux,” but eight of those bureaus consisted
only of a single reporter (Martin 2012).
Another, often sighted reason behind journalism’s lack of follow up is
the modern-day panacea of short attention spans. There are, of course,
plenty of fantastically dedicated reporters covering all sorts of issues,
and most of them know how hard it is to get editors’ attention once the
story they are covering has lost its place in the global running order.
And yet it is not the attention span or even lack of resources that
really prevents us journalists from following up. The reason why we are
so bad at giving our audiences a meaningful follow up is because journalism, as we know it, is simply not designed for staying on a story.
Traditionally, journalism has always been housed on disposable platforms: Think of newspapers that go into a dusty pile or television or
radio pieces that vanish after being aired. All traditional journalism
formats that we know are disposable, which, for decades, has made it
nearly impossible for reporters to create a meaningful follow up.


Take the story of Ziosu as an example. If I had spent ten months
reporting on Ziosu’s story for a conventional newspaper, I would have
needed to make sure that my readers had access to every preceding story
that I had written. But because they would not, as a reporter I would
have needed to tell the story from scratch each time, with basic facts and
background repeated each time and only limited space left for an actual
update. Essentially, traditional formats force journalists into dumbing
down stories as we can never assume that our readers or viewers have the
background needed to understand the update.
Structure is at the heart of any good storytelling; journalists know the
value of constructing narratives that keep people reading, listening and
viewing. However, the digital age has rendered our ability to tell a good
individual story insufficient. The traditional news story is a self-contained
item with a headline, picture and text, which is repeated every time
there is a development just in case the reader missed previous edition.
When published online, this format creates an overload of information,
with millions of fragmented versions of the same story and an absence of
cohesive narrative.
Internet, however, has fundamentally changed the disposable nature
of journalism platforms. It gave us an opportunity to create digital scrapbooks, where each individual story can be told in wider context, allowing
us to follow characters, events and trends over a period of time. Digital
formats now allow us to show how stories relate to each other; they
empower journalists to place intimate, engaging, on-the-ground storytelling into a much wider context of crises and events.
It is a revolutionary change, but one that the industry has been very
slow to embrace. When newspapers and broadcasters created their new
homes for themselves online, they essentially copy pasted the format that
they were familiar with. Internet became a digital pit for endless updates,
a virtual equivalent of a pile of newspapers that we used to see in our
parents’ hallway: full of invaluable information, lessons of the past, and
clues to the future, all hidden away in a plain site.
In fact, internet amplified the inherent superficiality of a news cycle by
introducing a rolling deadline. For most journalists, there was no longer
an evening broadcast or a morning paper to aim for; instead, there are
constant updates to be filed anytime day or night. The constant pressure to file not only increases a reporter’s workload, it also interferes with
a journalist’s ability to report. The more time we spend filing, the less
time we have left to make phone calls, to travel, to talk to people directly


affected by a crisis. The more we file, the more locked in we become in
an echo chamber, repeating and regurgitating what has already been said.
I remember landing in Sanaa, Yemen, in 2013 as the country was
being shaken by massive and increasingly violent anti-government protests. My phone rang just as I cleared security. An editor in London
wanted me to send a dispatch as soon as possible. “But I just arrived,”
I tried to argue. It did not matter—the beast had to be fed and the fact
that the beast was now digital made its appetite insatiable.
Six weeks later, in the departures lounge in the same airport in Sanaa,
I wondered whether there was another, better way of covering events in
digital age. Walking towards my gate, I thought of Yemen’s uncertain
future, the people I was leaving behind and their stories that would
now go untold. I had another assignment waiting, and it is not that my
editors did not care about Yemen; but with resources scarce and other
stories fighting for their attention, the decision had been made not to
send in another reporter. I knew that without a journalist pushing
the story from the ground, Yemen would disappear from the editorial
agenda, just like Burma or so many other stories I had covered have
slipped down newsroom’s running orders in the past. I thought of Ziosu
and wondered what had happened to him.
After my trip to Yemen I reached out to several colleagues who
I knew shared my frustration with the way media covers big ­crises.
Together with the American journalist and fellow veteran foreign
correspondent Ilan Greenberg we embarked on a mission to figure out
a model that would allow journalists to take stories out of an erratic
news cycle and cover crises in a way that creates a meaningful, cohesive
narrative.
Coda, the journalism start-up that we co-founded, was born out of a
three-year long conversation that we initiated with a group of young and
veteran reporters, designers, technologists and editors with whom we
skyped, met and corresponded between deadlines and assignments.
Coda is a musical term—and in music it is a passage, usually at the
end of a piece, that helps define the whole work. In journalism, we
decided, Coda Story would be a stand-alone voice that helps define a
whole crisis.
We set our goals: to investigate crises that shape our world, to challenge conventional narratives, to make important, complex stories accessible to general public, and to promote in-depth journalism through
partnerships, collaborations and mentorship schemes. As a non-profit,


Coda would also support freedom of the press, without which consequential journalism cannot exist.
We quickly realised that in order for us to achieve any of the above,
to stay on the story, and to keep our audience on the story with us, we
could not simply continue to produce coverage when others had left. We
had to do something more fundamental: to move away from news as a
constant stream of incrementally-updated articles and to stop using the
internet as a bottomless pit for updates. We had to re-imagine journalistic storytelling in digital age by moving away from the mentality of a
disposable platform.
A successful Coda, we thought, could not be a news dashboard, aggregation site, user-generated platform, or hyper-specialist watering hole.
It would need to produce high-quality, original narrative storytelling that
attracts a wide readership via traditional text, features and video, as well as
distinct, innovative and inventive digital formats. Coda’s success would lie
in its ability to yield a complex, nuanced, and contextual understanding
of specific storylines fuelling contemporary global issues.
The operational formula we created to achieve this was simple: Coda,
a non-profit newsroom, would deploy like everyone else after a crisis,
but go in with a long-lens view and commit to a story for an extended
period. The core editorial team would then define trends or “currents”
that run through the crisis and works with a network of international and
local journalists to report on different aspects of the issue. Each individual piece of content, regardless of its format, would be placed in one of
the trends or “currents” allowing our audience to follow a narrative line
and see the wider context. Currents, in other words, would be the heart
of Coda’s storytelling; a fusion of editorial and design enabling connection and context to work as hard as the individual pieces of content.
To test Coda’s editorial concept, in 2016, we ran a successful crowdfunding campaign, matched it with a small foundation grant and
launched an MVP, a minimal viable product.
For our pilot project, we picked the subject of gay rights in the former
Soviet Union. Media widely reported on gay rights abuses around the
time of the Sochi Olympics in 2014 but then moved on, largely abandoning the subject. However, by 2016, from the Baltics to Central Asia
the letters LGBT were no longer just an expression of identity. They had
instead turned into a rallying cry, either as a fundamental benchmark of
tolerance or as a hate phrase defining a threat to tradition.


Our aim with the pilot was not just to follow up on individual stories
of homophobic abuse and violence but place them into wider context of
geopolitical developments. We did not just want to show that gay men
and women were victims, we wanted to understand why they were victims, and what the reasons were the Kremlin had chosen to wage its war
on gays. Through dispatches, video web-series and photography we told
the story not only of individuals affected by this crisis but of how the
crisis of gay rights pit the Kremlin against the West, both reflecting and
feeding the wider geopolitical story, whether in Syria, Ukraine or among
the right-wing politicians in the United States.
The pilot edition explored the crisis by following five currents, or
trends, that ran through it: In the _Rights Abuses_ current we tracked the
human cost of cultural and state-sanctioned homophobia and reported
on individual cases of violence and abuse. In the _Kremlin Influence_
current we examined Moscow’s role in turning sexual orientation into
a matter of political ideology not only in Russia but across the former
Soviet Union, while in the _Orthodox Church_ current we told stories of
the central role the Church has played in framing this new “traditionalist” ideology. The stories in the _East_ - _West_ current tracked the growing
divide between two schools of thought as Moscow’s definition of ­values
and tradition clashed with the Western emphasis on individual rights
and, finally, stories in the _Information Wars_ current followed coverage
patterns and decoded agendas behind them. The content was disseminated through Coda’s own social media and published by a number of
editorial partners, including _The Guardian_, World Policy Journal and
Reveal, a podcast from the Centre for Investigative Reporting.
There were three main key takeaways from our test pilot edition.
The first was that such editorial framing of a crisis and thematic rather
than chronological curation of the content did not just allow us to follow trends and individual characters as their stories developed, but crucially it generated stories that had an infinitely longer shelf life than those
reported in reaction to news events.
The second lesson was that when selected carefully, currents could
greatly aid the process of journalistic discovery. For example, a current
that unexpectedly emerged as most popular and hence most ­populated
in our pilot edition was the one tracking Information Wars. As the
editorial team dug into the crisis, commissioning freelancers from
across the region and following the news, we realised that the role of


disinformation and propaganda against gays was not just key to understanding the issue, but it had also been severely underreported.
Disinformation soon ballooned into its own Coda edition, which we
in turn broke up into individual themes. It led us to covering another
crisis connected to Disinformation: that of migration in Europe. We continue to develop editorial offshoots of our initial subjects, linking crises
and big themes, creating a cohesive narrative of the modern world where
each individual story works as a building block of a wider, overarching
narrative.
The third lesson of our pilot edition was just as consequential. While
design and editorial architecture has allowed us to create a system
in which journalists can stay on the story, there is only one thing, we
learned, that will keep our audiences on the story with us: outstanding
storytelling.
Innovative storytelling is one of the buzzwords of the media industry, but we have learned to be cautious about using the term because
at Coda, we, in fact, aspire to what some would call “old fashioned”
journalism, in which reporters are free from filing constant updates and
instead are encouraged to dig deep, look beyond social media to find
voices that are not being heard and help audiences connect the dots
often obscured by the drama of breaking news. The new formats such as
360° video or animation, we learned, can be empowered when coupled
with traditional values of journalism: accuracy, fairness and powerful,
character-driven narrative storytelling.
In 2013, Pew Research published a study that offers insight into a
journalism gap—the unaddressed desire among news consumers for
quality storytelling predicated on deep reporting in the field (Mitchell
et al. 2013). The study found that longform journalism stories which
contain deeper reporting or analysis and tend to be more than 1000
words long appeared infrequently in the start-up media that Pew evaluated. In a two-week period, about two-thirds of the outlets did not produce a single longform piece and most of the remainder only produced
between one and five longform pieces.
News consumers are not monolithic, and many are indeed the peripatetic readers of nugget-sized news flashes and RSS headlines. But there
are also legions of readers interested in better, slower, more detailed storytelling that offers meaningful insight into the issues and events that go
into invisible remission in the major media only to suddenly re-emerge


like multiplying cells, an unexamined tumour affecting their economies,
their national security, their place in the world.
There is an emerging recognition of a strong appetite for journalism
predicated on sustained, longform storytelling. New feature departments
at legacy media organisations like _The Guardian_ and initiatives from
newcomers like _Buzzfeed, Politico,_ and _Medium_ reflect how investment in
the longform genre is on the uptick. [1] Their efforts at deeper excavation,
however, are spread across topics, regions, everything and everywhere;
their individual stories illuminate a subject for a moment. There are also
other news start-ups, like Coda, which chose one topic to focus on.
In fact, the 2013 Pew Research study also found most of the 73
recently founded journalism non-profits it surveyed have niche orientations—they focus on one topic or type of reporting. Only 26% of the
172 non-profits cover general interest news (Mitchell et al. 2013). The
bulk of them focus on narrower topics to fill one gap or another. Other
niche areas include government, health, education, and the environment,
with foreign affairs occupying a focus of only 13%. While “nichification”
seeks to fill a hole in newsgathering, media start-ups focusing on international stories remain few.
The growth of single-issue media start-ups and the efforts of many
media organisations to build better topics pages as well as explore deeper
forms of storytelling are indicators of the demand for deep, specialist
information. Coda’s single-subject agenda can uniquely lash the power
of longform journalism to a topic over time, creating a unique digital
record of an issue or a major event, and eventually scaling up by deploying on several crises at the same time, creating a niche audience with
each deployment.
Will it work? There will be plenty of sceptics who would argue that in
the age of short attention spans, people would never want to stay on a
story of a faraway place. We believe it depends how it is told. Would you
not want to hear what happened next to Ziosu, a boy who had lost his
entire family and yet thought of jumping off a boat first in order to help
a stranger?


1 For an analysis on key drivers of the resurgence in longform journalism, see: [http://](http://pando.com/2013/08/12/epic-launches-politico-goes-deeper-why-longform-is-flavor-of-the-month/)
[pando.com/2013/08/12/epic-launches-politico-goes-deeper-why-longform-is-flavor-of-](http://pando.com/2013/08/12/epic-launches-politico-goes-deeper-why-longform-is-flavor-of-the-month/)
[the-month/.](http://pando.com/2013/08/12/epic-launches-politico-goes-deeper-why-longform-is-flavor-of-the-month/)


References


Arnett, P. (1998, November). State of the American Newspaper. Goodbye, World.

_American Journalism Review_ [. http://ajrarchive.org/Article.asp?id=3288.](http://ajrarchive.org/Article.asp?id=3288)
Martin, J. D. (2012, April 23). Loneliness at the Foreign ‘Bureau’. _Columbia_
_Journalism Review._ [http://archives.cjr.org/behind_the_news/loneliness_at_](http://archives.cjr.org/behind_the_news/loneliness_at_the_foreign_bureau.php)
[the_foreign_bureau.php.](http://archives.cjr.org/behind_the_news/loneliness_at_the_foreign_bureau.php)
Mitchell, A., Jurkowitz, M., Holcomb, J., Enda, J., & Anderson, M. (2013,
June 10). The Landscape. _Pew Research Center_ . [http://www.journalism.](http://www.journalism.org/2013/06/10/landscape/)
[org/2013/06/10/landscape/.](http://www.journalism.org/2013/06/10/landscape/)


CHAPTER 21

#### eJihad: Behind the Use of Social Media by ISIS


_Asiem El Difraoui with Oliver Hahn_


Introduction

Today’s so-called eJihad is a worldwide phenomenon and the cross-media propaganda toolbox of the global Jihadist movement. Without
the audio-visual propaganda to unite sympathisers by creating a
shared identity, the global Jihadist movement might no longer exist
(El Difraoui 2015, p. 127). Jihadism can generally be understood as the
most radical interpretation and distortion of Islam and its concepts as
well as the most extremist current and movement of Islamism within
Sunni Islam. In classical Sunni thought, the concept of Jihad has many
different meanings—such as the struggle within oneself to become a
better human being. Jihadists, however, reduce the concept to armed
struggle and violently attempt to impose their political and societal
worldview on others. Fighting is not only considered the most important instrument for solving the problems of the Muslim world, but
also for personal salvation including the supposed martyrdom through


A. El Difraoui (*)
Institut für Medien- und Kommunikationspolitik, Cologne, Germany

O. Hahn
Centre for Media and Communication, University of Passau, Passau, Germany


© The Author(s) 2018
O Hahn and F Stalph (eds ) _Digital Investigative Journalism_


suicide attacks. It is important to stress that—within Sunni Islam—three
different forms and groups of Islamism: political Islam(ism), Salafism
(this current is strongly influenced by the long-time Saudi Arabian
state doctrine of Wahhabism) and finally the Jihadism, have to be differentiated. All forms of Islamism also have a very strong transnational
component. The diversity of these different groups is reflected in the
extreme variety of the Islamist media landscape. It is equally important
to stress that a large part of Muslims all over the world are not Islamists
(El Difraoui 2015, pp. 117–118).
The emergence of the ‘Arab Spring’ in late 2010 and early 2011
allowed numerous actors, groups and parties of especially political
Islam(ism) and Salafism to operate media for the first time or more and
more officially (El Difraoui and Hahn 2013; El Difraoui 2015, p. 122).
The phenomenon of eJihad is part of the rapid development of Islamist
media. Also, eJihad remains a key recruitment tool for attracting young
people to pseudo-religious terror on a global scale (El Difraoui 2015,
p. 128).
This chapter focuses on how eJihad has developed since the late
1970s and specifically traces how it has expanded in reach and diversity since the rise of social media. The history and proliferation of
Jihadist propaganda can be roughly divided into four phases: its prehistory in the Afghan war against the Soviet Union (1979–1989), the
spread of propaganda efforts to the Western world and the appearance of the first Jihadi websites (1990–2001), the globalisation of the
Jihadist internet (2002–2006) and finally the Jihadists’ use of social
media (2006 to the present). The fourth and current phase of eJihad
is characterised by its use of cross-media elements and has grown into
a flood of Jihadist propaganda since 2014 through the activities of the
so-called Islamic State (ISIS or ISIL or Daesh). The propaganda campaign has peaked in 2015 and 2016, and it has somehow receded in
2018 after military defeats of ISIS, but it could anytime and anywhere
in the world gain again in strength due to the large number of global
sympathisers and affiliated organisations. The propaganda generally
merges Jihadist symbolism with the language and imagery of global
youth culture and the extreme brutality of some video games to create
a Jihadist subculture that is increasingly attractive to Europe’s youth
(El Difraoui 2015, p. 123).


Phase One: Prehistory in the Afghan War against the

Soviet Union (1979–1989)

During the first phase, the war in Afghanistan, Jihadist propaganda
was disseminated primarily through traditional print media, audiocassettes and the first (and back then expensive) VHS videotapes. Abdallah
Azzam (who is often viewed as the ideological founder of Jihadism) published a magazine called _Jihad_ to report on the ‘glorious’ deeds of the
Afghan Mujahedin and the brutal acts of the ‘Russians’ to successfully
recruit followers and solicit donations. The first videos about ‘martyrs’
also began to appear around this time. The fact that Jihadist cameramen who lost their lives were considered ‘martyrs’ just as the fighters
were, shows that propaganda was already then thought to play a decisive
role. Influential theoreticians such as Abu Musab Al-Suri later criticised
these propaganda efforts as insufficient because they were only reaching
Jihadi circles and not the ‘Umma’, the Muslim community in general
(El Difraoui 2015, pp. 123–124).


Phase Two: The Spread of Propaganda Efforts to the
Western World and the Appearance of the First Jihadi
Websites (1990–2001)

In the second phase, when propaganda was spreading globally, the
first elements of a Jihadist communications strategy began to emerge.
The propaganda became more professional and took hold in Europe.
These developments began in the early 1990s in what is referred to as
“Londonistan” (Thomas 2003). At the time, the United Kingdom’s
renown freedom of press and opinion provided Islamists of all kind,
including former Afghan fighters who had sought refuge in Britain,
a unique platform for their propaganda−including calls for Jihad. The
Bosnian War, which began in 1992, served as a catalyst for their efforts.
The suffering of the Bosnian Muslims generated a huge wave of sympathy among the Muslim diaspora in Europe, which the propagandists used
to their advantage. Influential texts in terms of Jihadi propaganda strategy appeared. Abu Musab Al-Suri called for a diversified propaganda tailored to the various target audiences. Using the motto ‘system, not an
organisation’, he called for a decentralised form of information warfare
in which independent organisational groups use leading technology to


promote a Jihadist ideology and serve as a blueprint for future propaganda. In 1996, shortly after the Bosnian War ended, the first Jihadist
website, Azzam(dot)com, appeared. This website was developed by a
24-year old computer science student at London’s Imperial College by
using the college’s server and served as a prototype (El Difraoui 2013a;
2015, p. 124).


Phase Three: The Globalisation of the Jihadist Internet

(2002–2006)

In the third phase commencing after September 11, 2001, the subsequent intervention in Afghanistan and especially the start of the Iraq War
in 2003 provided the Jihadists with numerous new sympathisers, and eJihad became a global phenomenon. The unpopularity of the American
invasion of Iraq among Muslims allowed the Jihad propagandists to
attract thousands of new recruits, and to achieve important successes in
their media war. Four key developments have spread the Jihad propaganda globally. First, a considerable amount of the propaganda material
no longer stems directly from the strict hierarchy of the Jihadist organisations and their media committees, but is rather disseminated directly
to interested persons by decentralised so-called independent media companies. Secondly, traditional websites (in which interaction between the
producers and consumers of information was rarely possible) have been
replaced by dynamic, interactive online forums. As a third factor, technological advances (such as inexpensive digital cameras and video-editing
software for laptops) led to an exponential growth in video production.
The fourth factor was the emergence of propaganda products directly
targeted at the youth influenced by global pop culture in Muslim countries and Europe (El Difraoui 2012). In online forums, Jihadist sympathisers posted materials (and especially existing materials from Jihadist
organisations) for worldwide dissemination. Among these media companies, one in particular played a key role: the ‘Global Islamic Media
Front (GIMF)’. Generally, the Jihad’s communication platforms were
characterised by, among other things, a very rapid expansion throughout other languages. Nearly every European language, from Swedish to
Spanish, can be found in the Jihad’s online presence. This has enabled
the Jihad’s media staff to address local issues and alleged discrimination against Muslims in the local language and context. Examples can


be found in texts addressing the Mohammed caricatures in Denmark
or the ­banning of headscarves in France. Through the use of online
forums, the Jihadist internet has metamorphosed into an essentially
non-­hierarchical yet widely interconnected propaganda network. This
has enabled a much broader dissemination of information and laid the
foundation for the production of the videos that have played such a key
role in the emergence of a Jihadist subculture or anti-culture in Western
nations. Jihadist symbols and content have been adapted to the global
youth pop culture in an attempt to appeal to the youth in the West. A
so-called ‘Al-Qaeda Rap’ began to appear as early as 2005 in the music
video “Dirty Infidels”. These productions were the starting point of the
fourth phase as well as the on-going propaganda campaign launched by
ISIS in 2013 (El Difraoui 2013b; 2015, pp. 124–125).


Phase Four: The Jihadists’ Use of Social Media (2006

to the Present)

The fourth phase of eJihad, introduced by the emergence of the Web
2.0, continues until today. It has been characterised by three key developments. First, the Jihad propagandists began to expand their activities into social networks and the ubiquitous smartphones. This allowed
a form of Jihadi youth subculture and anti-culture (“Jihadi Cool”), to
expand into the Western world. Secondly, the Jihadists tried to hijack
the Islamic world’s mainstream forums for their purposes. Thirdly, the
Jihadists strengthened their activities in the ‘deep dark net’, the hidden internet. Social networks such as Facebook, together with video
portals such as YouTube and message services such as Twitter, have
evolved into important propaganda tools and a stronger interconnection of the group’s cross-media activities emerged: a Twitter tweet mentions a new YouTube video or a Facebook page, and vice versa. The
content of social media platforms is furthermore often re-used in traditional media or propaganda tools such as Jihadist print publications or
flyers. The rapid, direct and global communication via various channels
and the emotion-laden multimedia content consisting of personal narratives, text, music and videos are designed to give users the feeling of
belonging to an international Jihadi community or Jihadist subculture
which has a status equal to other communities and cultures in the digital
media (El Difraoui 2015, pp. 125–126). The Jihadist have since 2016


increasingly shifted to encrypted social networks and messaging services
like Telegram and WhatsApp to avoid detection and censorship.
A German-Ghanaian former rapper Deso Dogg (born Denis Cuspert)
who began calling himself Abu Maleeq after his conversion to Islam,
is considered to be one of the most prominent propagandists of the
Jihadist subculture. While he is assumed dead, he still has a strong presence on YouTube and Facebook through his videos. Digital natives who
rap (such as Deso Dogg) and thousands of other radicalised Europeans
use the codes, gestures and aesthetics of European and US subcultures
to promote the eJihad’s propaganda and symbolism to influence a new
generation of powerful propagandists and spread global terror. For
example, a universally recognisable symbol in the Jihadist community is
the raised index finger, whether in a selfie showing the subject posing in
front of a tank or in their own living room. The gesture originated in the
Web 2.0 repertoire of members of this community and can be seen on
hundreds of photos and videos from the so-called Islamic State. The gesture is intended to remind Salafists and Jihadists of the important concept of ‘tawhid’, the unity of God and the ‘Umma’. In reality it is a new
symbol, the Jihadist version of the thumbs-up ‘Like’ on Facebook and
symbol of group identification not unlike certain gestures of street gangs
(El Difraoui 2015, p. 126).
Whole legions of ‘lolcats’ are also part of Jihad 2.0’s new repertoire.
The cat was purportedly one of the Prophet Mohammed’s favourite animals. According to historical sources, anyone mistreating a cat is condemned to the torment of purgatory. In Islamic history, however, the
symbolism of the cat is completely new. The images of cat-caressing
fighters flooding the social networks seem intended to portray the fighters as ‘the nice guys next door’ and present them in a sympathetic light.
The Jihadists are thereby part of the global trend flooding the web with
cat selfies and videos (El Difraoui 2015, p. 126).
ISIS’s ‘virtual Jihadistan’ is simultaneously a world filled with unbridled horror and new levels of barbaric violence. The ‘death sentence’ and
brutal beheading of the American Nicholas Berg in 2004 by the mythical founder of the ISIS movement and ‘Butcher of Bagdad’, Abu Musab
Al-Zarqawi, was still filmed using a stationary camera similar to Iraqi TV
broadcasts of communiqués during the reign of Saddam Hussein. More
recently in a general trend and professionalised way, more and more
Hollywood-style audio-visual codes are to be found in ISIS’s Jihadist
propaganda. The perverse video of the murder of US journalists, Steven


Sotloff and James Foley, in 2014, dressed in orange prison garb, is reminiscent of the final scenes of Brad Pitt in the movie thriller “Seven”. The
threatening speech by the British ex-rapper Jihadi John after the beheading was filmed with a handheld steady-cam using imagery similar to that
found in music videos (El Difraoui 2015, p. 126).
The decision taken in this context by some Western media outlets to
no longer report and by doing so, to no longer further distribute ISIS’s
Jihadist propaganda, but instead to simply show the black-and-white
flag and logo of Daesh, has become a controversy. In a way, showing the
logo endorses the theft of an Islamic symbol by Daesh: in fact, the logo
itself resembles the seal of the prophet.


Conclusions and Perspectives

Jihadists have managed to reinterpret and hijack Islamic concepts and
symbols to create their own imagery and ultimately a Jihadi subculture. The elimination of language barriers has greatly expanded the
propaganda’s reach. Today’s youth now finds it easier than ever to identify with the Jihadists as role models, making it even simpler for them to
overcome their inhibitions and join a Jihadist organisation. All Jihadist
propaganda products reduce complex theological content to the level of
rhetorical dichotomies consisting of ‘us’ (the ‘true’ Muslims) vs. ‘them’
(everyone else) in which there can be no compromises. The goals of
Jihadist propaganda are complex and multifaceted. At the base level, the
goal is to attract a maximum amount of media attention and thereby
recruit young Muslims and to obtain financial, material and physical support to the Jihadist cause. At the second level, the Jihadist movement
tries to create a closed worldview and to convince the Muslim community that it (the Jihadist movement) alone represents the true faith.
It thereby strives to portray itself as the sole authority on key Islamic
concepts and symbols, an attempt which has been successful to a certain extent. On the third level, the Jihadists attempt to manipulate these
concepts and symbols to establish their own mythology and doctrine
of salvation. This eschatology encompasses a cosmology in which the
Jihadists are the only true believers and in which only they ascend to
paradise. The leaders of these Jihadist groups are portrayed as the only
ones authorised to preach divine revelation and become self-proclaimed
prophets through the promise of salvation accorded to simple combatants through their martyrdom. Representatives from all Islamist


currents—political Islam(ism), Salafism and finally the Jihadism—will
continue to try to expand their media presence and use all technologies available to them to their own advantage. In light of these factors, it
becomes clear that the Jihadist media is an inflammatory propaganda tool.
Global education and prevention campaigns as well as counter-­narratives
have been launched already with varied success (El Difraoui 2015,
pp. 127–128).
Western and European countries in particular but also several Arab
nations still face the challenge to offer their own ‘grand-narratives’ to
counter the Jihadists’ one via digital media. Innovations in digital investigative journalism on an international level can provide fact-checked
information and data that make propaganda and information warfare
more transparent to audiences, and that, at the same time, challenge the
Jihadi narrative.


References


El Difraoui, A. (2012). _jihad.de. Jihadistische Online-Propaganda: Empfehlungen_
_für Gegenmaßnahmen in Deutschland_ . SWP-Studien S 05, February.
El Difraoui, A. (2013a). _Al Quaida par l’image. La prophétie du martyre_ . Paris:
Presses Universitaires de France.
El Difraoui, A. (2013b). Propaganda und Märtyrertum: Drei Jahrzehnte
Videodschihad. _Blätter für deutsche und internationale Politik,_ _6,_ 43–51.
El Difraoui, A. (2015). Islamistische Medien: Vom Wahhabismus über die
Muslimbrüder zum Cyber-Dschihad. In C. Richter & A. El Difraoui (Eds.),
_Arabische Medien_ (pp. 117–128). Constance: UVK.
El Difraoui, A., & Hahn, O. (2013). Der arabische Schwarm im Netz des
Medienwandels. Ein Salon-Streitgespräch zur Protestkommunikation ziviler
Bewegungen in mehr als 140 Zeichen. In E. Bettermann & R. Grätz (Eds.),
_Digitale Herausforderung. Internationale Beziehungen in Zeiten von Web 2.0_
(pp. 111–118). Göttingen: Steidl.
Thomas, D. (2003). _Le Londonistan. La voix du djihad_ . Paris: Editions Michalon.


CHAPTER 22

#### Truth Corrupted: The Role of Fact-Based Journalism in a Post-Truth Society


_Florian Stalph_


The Pulitzer Prize winning fact-checking website PolitiFact found that
out of 489 statements made by the 45th president of the United States
during his presidential campaign and while he has been in office, 34%
are false and another 15% are “pants on fire” false (as of 08/01/2018),
meaning that the accounts are not only wrong but also add untenable
assertions. [1] While this might not come as a surprise and false claims have
been swiftly corrected by legacy media outlets over the last years, we
must acknowledge that almost half of all statements by Donald Trump
are mostly true, half true, or mostly false. Having a factual core, therefore portraying at least some ‘truth’ or providing an accurate piece of
information, calling out these statements is more difficult than such
being completely made up. On April 7, 2017 the US president claimed
a 64% reduction on illegal immigration on the southern border of the


[1 For a current overview see http://www.politifact.com/personalities/donald-trump/.](http://www.politifact.com/personalities/donald-trump/)


F. Stalph (*)
Centre for Media and Communication, University of Passau, Passau,
Germany


© The Author(s) 2018
O Hahn and F Stalph (eds ) _Digital Investigative Journalism_


US in the previous month. In the months before, he cited other statistics, highlighting previous decreases on a sequential monthly basis. This
time, however, he did not choose to quote month over month measurements but year over year measurements—without declaring it. Monthly
numbers would have suggested a 35% decrease and while these numbers
were apparently too low they would have at least shown measurements
comparable to those announced through previous statements (Valverde
2017). Not only did the president deliberately change the measurement
category without indication—he chose statistics that fit his narrative
while completely breaking with his previously established use of statistical
comparisons. As a result, this inconsistent use of data reveals a systematic use of numbers that favour a certain agenda. Furthermore, through
focusing on the southern border, the fact that illegal immigration via the
northern border has been on a rise was neglected. A prime example that
“politicians have leaned heavily on statistics to buttress their authority.
Often, they lean too heavily, stretching evidence too far, interpreting
data too loosely, to serve their cause” (Davies 2017).
Just as PolitiFact tries to evaluate statements made by American political actors, the collaborative effort CrossCheck has been debunking dubious (social) media claims by bundling the power of 37 newsrooms in
order to call out political meddling in the French presidential election
by correcting disinformation and misinformation. During that time they
could identify 10 misleading and 19 manufactured stories and dozens
of other misreported, manipulated or misattributed stories (CrossCheck
2017). Most of these indicted reports stem from news websites or blogs
and are shared via Twitter or disseminated through Facebook sites, and
most of these sources can clearly be affiliated with certain political movements as they clearly propagate disinformation aimed at harming political enemies through establishing toxic narratives. These platforms are
only two examples for fact-checking organisations that set out to defend
objectivity and transparency. Voters and societies in general are in dire
need of such institutions around the globe. The US and French election,
Brexit, the Russian insurgency on Ukrainian soil and preceding information war during the Euromaidan, the Four Day War between Armenia
and Azerbaijan—recent years are stacked with episodes of disinformation
and misleading reporting putting a spotlight on media organisations and
social media being subject to manipulation and exploitation as means of
propaganda.


The Duke Reporter’s Lab has been observing fact-checking projects
around the world since 2014. Whereas they counted 44 active sites in
2014 (Adair 2014), they report 126 active organisations in 49 countries
three years later (Stencel 2017). More interestingly, fact-checking appears
to become a global movement: Africa, Asia, Australia, Europe, North
America and South America all have agencies “driven by concerns about
a global epidemic of misinformation, viral hoaxes and official lying”
(Stencel 2017). The Duke Reporter’s Lab further determines that more
than half of these projects have ties to media organisations while others
are affiliated to journalism research institutes, universities or non-governmental organisations. When analysing the roots of the global fact-checking movement, Graves (2018, p. 618) proposes a model in order to map
the international landscape of fact-checkers by locating them in a triad
composed of journalism, academia, and politics and civil society according to values the organisations represent and affiliations they have. He
concludes that fact-checking is a highly diversified system being a “forceful example of non-news organisations adopting an emerging journalistic
genre in order to pursue a civic agenda” (Graves 2018, p. 624). Despite
persistent differences between projects—differing organisational and
methodological approaches or varying values and institutional affiliations—transnational collaboration flourishes (Graves 2018, p. 627).
The rise of fact-checking movements around the world is symptomatic
of shifting paradigms in post-truth societies: Information dissemination
and information consumption have fundamentally changed.
Disruptive technologies provide new means of communication that
circumvent traditional communication models and turn established
media logics upside down. By providing new channels and platforms that
allow spreading information without verification and without institutionalised ministration, such technologies evade correctives that advocate
truthful and accurate information flow, predominantly journalistic institutions such as TV and radio broadcasters, newspapers, news magazines
and internet-based news media. As information now flows more freely
than ever before, new players appear, filling gaps created by innovative
disruptions. Disrupted information dissemination offers a wide array of
options to political and societal influences from all sides of the political
and social spectrum, having manifold implications for the circulation
of news and messages. For instance, these new logics allow breaking
through institutionalised barriers set up by autocratic regimes in order to
impede public communication and to diminish alternative voices; at the


same time, political actors, interest groups or subversive powers can use
certain channels and platforms to undermine the authority of political
elites and leaders as well as renowned media organisations. In the end,
gate keeping mechanisms seem to be overridden.
Kurt Lewin was the first to coin the term “gate keeper”. Focusing
on group dynamics, the psychologist analysed food habits of Americans
after the Second World War. Lewin (1947) was looking into the question
of who is responsible for dishes on American families’ tables. He found
that food components pass through several sections which are affected
by certain powers. Certain areas in each channel constitute gates which
serve as partitions of forces and can completely alter them, even reverse
them. While he found that housewives—who Lewin identified as the
most likely gate keepers of buying food—determine what food is served,
what ingredients are bought, how much money is spent on them and
ultimately what the members of a group, that is a family, eat, he also
claimed that this concept “holds not only for food channels but also for
the travelling of a news item through certain communication channels in
a group” (p. 145). White (1950) put this to test and transferred Lewin’s
theory into a journalistic context. He observed a wire editor as the gate
keeper who determines which news items lastly appear on the pages of
a newspaper. White stated that the news selection is highly dependent
on the editor aka the gate keeper, his own experiences and mind-set, his
own evaluation of the newsworthiness of a story, and his estimation of
the paper’s audience. At last, White concludes that the process of gate
keeping is highly subjective:


It is a well known fact in individual psychology that people tend to perceive as true only those happenings which fit into their own beliefs concerning what is likely to happen …. in his position as ‘gate keeper’ the
newspaper editor sees to it (even though he may never be consciously
aware of it) that the community shall hear as a fact only those events which
the newsman, as the representative of his culture, believes to be true.
(White 1950, p. 390)


White describes a phenomenon comprehensively discussed by
the social psychology community. The cognitive dissonance theory
was put forward by Festinger (1957). When he analysed the interplay between human actions and underlying beliefs and attitudes, he
established that people adapt their set of beliefs and ultimately act


accordingly when a situation arises that causes dissonance with pre-existing attitudes. As a premise, individuals are perceptive to inconsistencies
that are caused by a conflict between current beliefs and new, contradictory information. Now, in order to act in harmony with one’s attitudes,
eliminating a discomforting situation, the individual seeks to resolve or
reduce the dissonance by choosing to change behavioural or environmental elements by avoiding certain situations and information that are
likely to cause cognitive dissonance, thus, selecting information that
matches one’s beliefs or behavioural elements. This concept—selective
exposure—describes the subjectivity of a gate keeper’s actions. Building
on cognitive dissonance and substantiating selective exposure, Klapper
(1960) determines that media do not change recipients’ behaviours or
beliefs rather than strengthening them. Within a series of experiments,
Brock and Balloun (1967, pp. 424–425) found that there are “relationships between behavioral commitment and behavioral self-exposure to
pertinent propaganda”. Participants had to press a button to remove a
static from spoken messages in order to improve reception. Their studies
show that smokers were found to be more interested in messages refuting a connection between smoking and lung cancer while being disinterested in messages that uphold cancer is caused by smoking. Moreover,
the amount of button presses positively correlated with the amount of
cigarettes smoked. More recent studies have shown similar effects. A
pilot study by the YouGov-Cambridge Programme explored how British
citizens are affected by conspiracy theories. One noteworthy result is that
conservative UKIP voters are more likely to believe that Brussels and the
EU are plotting to take power away from the United Kingdom. Liberal
Labour voters, however, are less likely to believe that climate change is a
hoax (Rogers 2015). Another poll shows that almost half of Trump supporters completely distrust economic data provided by the government
whereas only 5% of Clinton supporters do so (Ryssdal 2016). These
examples show that beliefs of citizens oftentimes align with ideologies
promoted by affiliated political parties.
The early psychological experiments have shown that information
consumption is selective: Supporting information is more likely to be
sought out, while information that is not congruent with one’s views is
avoided. As a result, the shaping of public opinion appears to be subject
to the combination of (a) disruptive technologies that circumvent established logics and redefine information flows by debilitating force fields
around gates, (b) recipients’ behavioural patterns explaining deliberate


devotion to self-affirming information and negligence of deviating information, and (c) political powers that seek to benefit from new communication patterns and information flows, promoted by political campaigns
that systematically utilise this new environment—an interplay of these
factors, rather than regarding them as well-defined effects.
Former US President Barack Obama spearheaded the use of social
media tools to directly address citizens, promote himself or raise donations for his election campaign. His internet strategy turned out to
be highly successful—according to Arianna Huffington: “Were it not
for the Internet, Barack Obama would not be president. Were it not
for the Internet, Barack Obama would not have been the nominee”
(Miller 2008). History has shown that new technologies provide effective tools for aspiring politicians: Roosevelt used the radio, John F.
Kennedy the TV, Obama the Internet, and Trump heavily relied on
social media, primarily Twitter, to promote his messages directly without any intervention by established gate keepers. [2] What all of these
presidents did was using disruptive technologies (a) and developed
strategies to benefit from these new communication patterns (b) in
order to influence citizens. To further utilise behavioural phenomena
(c), creating a diversified, fractured media landscape is highly advantageous. A fractured media system composed of binary subsystems that
either support or oppose political and societal movements is prone
to manipulation and tampering. Adducting Luhmann’s logic of binary-coded systems, such subsystems would work according to partisan/
non-partisan, liberal/non-liberal, mainstream media/non-mainstream
media et cetera, thereby showing true colours and facilitating political leverage and influence. In addition, these subsystems in a fractured
media landscape are perfect breeding grounds for alternative views, lies
and propaganda; on top of that, surrounding communities are easily
manipulable.
Analysing the 1988, 1992 and 1996 US presidential elections, Watts
et al. (1999) suggest:


[C]riticisms of media coverage–driven by conservative elites, and reported
and discussed in new stories during these campaigns–have been a substantial influence behind the rising public perception of liberal media bias.


2 This direct wire to the people lead to the surge of fact-checking projects as described
initially.


Indeed, analysis of a wide range of news content indicates that discourse
on media bias in the past three presidential campaigns has focused overwhelmingly on allegations of liberal bias; has emanated increasingly from
political elites (particularly if the claim is of liberal bias); and has predominantly conceived of the bias as existing across the entire media industry.
(Watts et al. 1999, p. 166)


In a similar way Ladd (2010, p. 42) concludes that his study on
antipathy towards news media “indicates that elite rhetoric can also
powerfully influence the public’s attitudes toward the institutional news
media.” When discussing the role of elites within this field of political
communication, Stroud (2014) addresses “ _selective production_ ”, a phenomenon where elites are more open to giving interviews to agnate
media. Recent incidents after the White House allegedly excluded
certain members of the White House press corps due to their affiliation
with critical or liberal news outlets (Mullin 2017), certainly substantiate this claim. Sykes (2016), who quit hosting a conservative political talk show, stated that the “conservative media is broken” and after
years of efforts the conservative media “had succeeded in persuading
our audiences to ignore and discount _any_ information from the mainstream media. Over time, we’d succeeded in delegitimizing the media
altogether – all the normal guideposts were down, the referees discredited”. Before this op-ed for _The New York Times_ he gave an interview
to the _Business Insider_ considering the conservative media who “basically eliminated any of the referees, the gatekeepers” (Darcy 2016) as
responsible for disinformation, misinformation and propaganda proclaimed by Trump—partisan news outlets basically serve as mouthpieces
for political elites.
Within this context, times for journalism seem dire. Besides these
external influences as described above, factual journalism and in particular data-driven journalism has feared for its integrity during recent
years. While fact-checking sites have been correcting claims or debunking lies, many legacy media outlets chose partisanship over objectivity,
giving the floor to political fights, undermining their own impartiality.
Data-driven journalism, seeking objectivity through forecasting based on
statistical models and deriving facts from numbers, has been trying to
evade this vicious circle of being instrumentalised and subsumed. In theory, journalism based on statistics, data collected by governmental bodies, academia or other research institutions and reported by professional


journalists trained in data analysis and conveying numbers in the form
of widely comprehensible journalistic products, sounds like salvation for
skewed media systems. It is not. Kayser-Bril (2016) states that “Truth
is a niche market” as news outlets would rather bow to interests of
donors, advertisers or readers’ interests without regard to quality and
fact-based journalism. He continues that some US outlets such as Vox or
FiveThirtyEight would very successfully serve this niche market. During
2016, however, fact-based journalism had to suffer massive setbacks.
After most analytical and explanatory outlets misinterpreted—or at least
reported their findings rather ingenuously—and ultimately wrongfully
forecasted the results of US elections and Brexit referendum, they saw
themselves confronted with accusations: Their methodology would be
flawed, even impractical as a journalistic practice. Data journalists and
statisticians were accused of blindly applying statistical models while
losing touch with reality; at last, due to their painfully wrong forecasts,
Gabler (2017), among others, concluded that “[n]o one will ever believe
Nate Silver or Nate Cohn or The Huffington Post aggregator or any
other polling data ever again. Political Moneyball failed spectacularly”.
Leading poll analyst Nate Silver repeatedly warned that chances of a
different outcome of the US election than expected are not that small
(Silver 2016a, b; Milbank 2016)—in fact, his team gave Trump the
highest chances of winning across all forecasts. Even if certain results are
more unlikely than others, this does not mean that they are impossible.
After Trump’s nomination, that analysts—again—did not see coming,
_The New York Times_ ’s Rutenberg (2016) called out data journalism and
his ex-colleague Silver and demanded a return to shoe-leather reporting, “to get a good night’s sleep, and then talk to some voters”. At
this point we need to paint a more nuanced picture of data journalism:
Forecasts based on advanced statistical modelling and likelihoods have a
margin of error. Such projections have been enjoying enormous popularity over the past years, particularly as they claim to predict results of
elections or referenda. After these failing predictions, negative repercussions do not only harm predictive data journalism but data journalism in
general. Descriptive, explanatory and analytical data-driven journalism,
that reports demographic or economic data, portrays communities and
societies, and presents correlations of factors by connecting indicators,
applies more basic statistical calculations. Clearly, we need to distinguish
these two streams—predictive and descriptive data journalism.


Unfortunately, infighting will lead to a further disrupted media system. Instead of working together, trying to right the wrongs and developing better statistical models or even bundling forces of traditional
reporters and data journalists, different journalistic streams appear to
resort to pointing fingers. These frictions hurt the integrity of quality
journalism as well as damage the reputation of data journalism—and data
journalism is an integral part of objective reporting in the fight against
disinformation: “The declining authority of statistics – and the experts
who analyse them – is at the heart of the crisis that has become known as
‘post-truth’ politics” (Davies 2017). It is important to acknowledge the
value data-driven practices bear for journalism. A return to shoe-leather
reporting would have journalists to rely on old-established sources such
as press releases and official statements. In a post-truth era, these sources
are likely to be peppered with malinformation and disinformation. Data
sources—be it that they are provided by official governmental bodies,
non-governmental organisations or whistleblowers—allow citizens and
journalists to compare claims and statements with actual underlying
data, ultimately holding elites and governments accountable. As Segnini
(2017) puts it: “Data can help a reporter fill in the missing pieces, and it
also allows journalists to expose a universe beyond the one sources are
willing to share.” In that sense, citizens should look to journalists rather
than state officials when it comes to constructing models of reality.
Certainly, aspects of shoe-leather reporting need to be inherent
to data journalism. _The New York Times_ alumni Sarah Cohen says that
“if a data reporter doesn’t go out into the field and report, they are
only doing a third of their job” (Pierce 2015). Data journalism could
greatly benefit from enhancing stories and findings drawn from quantitative data with a qualitative narrative. This would mean appending personal accounts with rows of data. Giving these numbers—that
once were abstracted from individual cases—voices and faces would
make data journalism more tangible and relatable. A combination
of quantitative and qualitative approaches would also invalidate the
argument that data journalism exclusively targets data-savvy elites,
requiring knowledge of statistics, the willingness to read numbers and
digest complex data visualisations. Dickinson (2013) asks if data journalism is not “just creating a small, equally uncountable, data elite?
Is it really just a good way to reposition (consolidate) journalism as
gatekeepers?” Indeed, data journalism might run the risk of building
an elitist circle of journalists who know statistics and computational


techniques as well as appealing to an audience that is already dataoriented while neglecting the majority of readers. To attract a wider
audience, data journalism needs to fulfil two tasks: First, educating their readers. Just as the many journalists who got into data,
they need to pass their knowledge on to their audience. By explaining their calculations, their modelling, used statistical indicators et
cetera, journalists do not only create transparency regarding their
employed methods, but they could also dispel fears of seemingly
over-complicated stories. In this regard, data journalists need to be
more than data reporters: They have to become educators. Secondly,
within a holistic approach, data journalism needs to develop appealing and intelligible storytelling formats. Translating data and statistics
into comprehensible journalistic products does not equal long reads
packed with numbers and dozens of interactives. Accessible storytelling means keeping in mind the reader’s habits and socialisation. Alvin
Chang of Vox considers a lack of context, particularly when covering complex topics, as problematic when trying to connect with the
reader: Laying out the context not only makes a story more comprehensible by describing the background, the underlying mechanics of a
problem, but he also regards it as a means to fight disinformation. On
another note, Chang argues that a more visual journalism can create
empathy and lead to more inclusivity in contrast to fabricating exclusivity through the use of jargon (Adams 2017).
If data journalism wants to constitute itself as an objective corrective in
mainstream media and play a major role in today’s news dissemination and
news consumption, it needs to continue developing its profile as a datadriven and evidence-based form of journalism. Whether or not it succeeds
in doing so, depends on many interfering variables as laid out in this essay.
An objective and scientific analysis and interpretation of data can promote
a journalism culture that combats disinformation and misinformation, and
also holds accountable authorities within digital public spheres.


References


Adair, B. (2014, April 4). _Duke Study Finds Fact-Checking Growing Around the_
_World_ [. Retrieved from https://reporterslab.org/duke-study-finds-fact-checking-](https://reporterslab.org/duke-study-finds-fact-checking-growing-around-the-world/)
[growing-around-the-world/.](https://reporterslab.org/duke-study-finds-fact-checking-growing-around-the-world/)
Adams, J. (2017, November 14). Q&A: Vox Data Guru on How Cartoons Can
Help Simplify Complex Issues. _Columbia Journalism Review_ . Retrieved from
[http://www.cjr.com.](http://www.cjr.com)


Brock, T. C., & Balloun, J. L. (1967). Behavioral Receptivity to Dissonant
Information. _Journal of Personality and Social Psychology,_ _6,_ 413–428.
[https://doi.org/10.1037/h0021225.](http://dx.doi.org/10.1037/h0021225)
CrossCheck. (2017). CrossCheck _. A Collaborative Journalism Project_ . Retrieved
[from https://crosscheck.firstdraftnews.org/france-en/.](https://crosscheck.firstdraftnews.org/france-en/)
Darcy, O. (2016, August 26). Donald Trump Broke the Conservative Media.

_Business Insider_ [. Retrieved from http://www.businessinsider.com.](http://www.businessinsider.com)
Davies, W. (2017, January 19). How Statistics Lost Their Power—And Why We
Should Fear What Comes Next. _The Guardian_ [. Retrieved from http://www.](http://www.theguardian.com)
[theguardian.com.](http://www.theguardian.com)
Dickinson, A. (2013, August 13). _Does Data Journalism Help Democracy?_
[Retrieved from http://digidickinson.net/2013/08/13/does-data-journalism-](http://digidickinson.net/2013/08/13/does-data-journalism-help-democracy/)
[help-democracy/.](http://digidickinson.net/2013/08/13/does-data-journalism-help-democracy/)
Festinger, L. (1957). _A Theory of Cognitive Dissonance_ . Evanston, IL: Row,
Peterson.
Gabler, N. (2017, January 24). Five Ways the Media Bungled the Election.

_Columbia Journalism Review_ [. Retrieved from http://www.cjr.org.](http://www.cjr.org)
Graves, L. (2018). Boundaries Not Drawn: Mapping the Institutional Roots of
the Global Fact-Checking Movement. _Journalism Studies, 19_ [(5). https://doi.](http://dx.doi.org/10.1080/1461670x.2016.1196602)
[org/10.1080/1461670x.2016.1196602.](http://dx.doi.org/10.1080/1461670x.2016.1196602)
Kayser-Bril, N. (2016, September 26). _Data-Driven Journalism in the Post-truth_
_Public Sphere_ . Retrieved from [http://blog.nkb.fr/datajournalism-in-the-](http://blog.nkb.fr/datajournalism-in-the-posth-truth-public-sphere)
[posth-truth-public-sphere.](http://blog.nkb.fr/datajournalism-in-the-posth-truth-public-sphere)
Klapper, J. T. (1960). _The Effects of Mass Communication_ . Glencoe: Free Press.
Ladd, J. M. (2010). The Neglected Power of Elite Opinion Leadership to
Produce Antipathy Toward the News Media: Evidence from a Survey
Experiment. _Political Behavior_, _32_ (1), 29–50. [https://doi.org/10.1007/](http://dx.doi.org/10.1007/s11109-009-9097-x)
[s11109-009-9097-x.](http://dx.doi.org/10.1007/s11109-009-9097-x)
Lewin, K. (1947). Frontiers in Group Dynamics: II. Channels of Group Life;
Social Planning and Action Research. _Human Relations_, _1_ (2), 143–153.
[https://doi.org/10.1177/001872674700100201.](http://dx.doi.org/10.1177/001872674700100201)
Milbank, D. (2016, November 8). No Matter Who Wins the Presidential
Election, Nate Silver Was Right. _The Washington Post_ [. Retrieved from http://](http://www.washingtonpost.com)
[www.washingtonpost.com.](http://www.washingtonpost.com)
Miller, C. C. (2008, November 7). How Obama’s Internet Campaign Changed
Politics. _Bits/The New York Times_ [. Retrieved from http://bits.blogs.nytimes.](http://bits.blogs.nytimes.com)
[com.](http://bits.blogs.nytimes.com)
Mullin, B. (2017, February 24). White House Press Corps Rebels as Colleagues
Are Excluded from Gaggle. _Poynter_ [. Retrieved from http://www.poynter.org.](http://www.poynter.org)
Pierce, E. (2015, September 29). New York Times Editor: Data Journalism
Starts with People. _Downtown Devil_ [. Retrieved from http://www.downtown-](http://www.downtowndevil.com)
[devil.com.](http://www.downtowndevil.com)


Rogers, J. F. (2015, February 13). _Are Conspiracy Theories for (Political) Losers?_
Retrieved from [https://yougov.co.uk/news/2015/02/13/are-conspiracy-](https://yougov.co.uk/news/2015/02/13/are-conspiracy-theories-political-losers/)
[theories-political-losers/.](https://yougov.co.uk/news/2015/02/13/are-conspiracy-theories-political-losers/)
Rutenberg, J. (2016, May 5). The Republican Horse Race Is Over, and
Journalism Lost. _The New York Times_ . Retrieved from [http://www.nytimes.](http://www.nytimes.com)
[com.](http://www.nytimes.com)
Ryssdal, K. (2016, October 13). _Poll Finds Americans’ Economic Anxiety Reaches_
_New High_ . Retrieved from [https://www.marketplace.org/2016/10/13/](https://www.marketplace.org/2016/10/13/economy/americans-economic-anxiety-has-reached-new-high)
[economy/americans-economic-anxiety-has-reached-new-high.](https://www.marketplace.org/2016/10/13/economy/americans-economic-anxiety-has-reached-new-high)
Segnini, G. (2017, August 3). Data Empowers Journalism Independence in
Trump’s Era. _Columbia Journalism Review_ . Retrieved from [http://www.cjr.](http://www.cjr.com)
[com.](http://www.cjr.com)
Silver, N. (2016a, November 1). Election Update: Yes, Donald Trump Has a
Path to Victory. _FiveThirtyEight_ [. Retrieved from http://www.fivethirtyeight.](http://www.fivethirtyeight.com)
[com.](http://www.fivethirtyeight.com)
Silver, N. (2016b, November 11). Why FiveThirtyEight Gave Trump a Better
Chance Than Almost Anyone Else. _FiveThirtyEight_ . Retrieved from [http://](http://www.fivethirtyeight.com)
[www.fivethirtyeight.com.](http://www.fivethirtyeight.com)
Stencel, M. (2017, June 30). _Fact-Checking Booms as Numbers Grow by 20_
_Percent_ . Retrieved from [https://reporterslab.org/fact-checking-booms-as-](https://reporterslab.org/fact-checking-booms-as-numbers-grow-by-20-percent/)
[numbers-grow-by-20-percent/.](https://reporterslab.org/fact-checking-booms-as-numbers-grow-by-20-percent/)
Stroud, N. J. (2014). Selective Exposure Theories. In K. Kenski & K.
H. Jameson (Eds.), _Oxford Handbook of Political Communication_ .
Oxford: Oxford University Press. [https://doi.org/10.1093/oxfordhb/](http://dx.doi.org/10.1093/oxfordhb/9780199793471.013.009)
[9780199793471.013.009.](http://dx.doi.org/10.1093/oxfordhb/9780199793471.013.009)
Sykes, C. J. (2016, December 15). Charlie Sykes in Where the Right Went
Wrong. _The New York Times_ [. Retrieved from http://www.nytimes.com.](http://www.nytimes.com)
Valverde, M. (2017, April 10). _Donald Trump Changes Yardstick in Claim_
_About Southern Border Apprehensions_ . Retrieved from [http://www.politi-](http://www.politifact.com/truth-o-meter/statements/2017/apr/10/donald-trump/trump-illegal-immigration-down-64-percent-march-tr/)
[fact.com/truth-o-meter/statements/2017/apr/10/donald-trump/](http://www.politifact.com/truth-o-meter/statements/2017/apr/10/donald-trump/trump-illegal-immigration-down-64-percent-march-tr/)
[trump-illegal-immigration-down-64-percent-march-tr/.](http://www.politifact.com/truth-o-meter/statements/2017/apr/10/donald-trump/trump-illegal-immigration-down-64-percent-march-tr/)
Watts, M. D., Domke, D., Shah, D. V., & Fan, D. P. (1999). Elite Cues and
Media Bias in Presidential Campaigns: Explaining Public Perceptions of a
Liberal Press. _Communication Research,_ _26_ (2), 144–175.
White, D. M. (1950). The “Gate Keeper”: A Case Study in the Selection of
News. _Journalism & Mass Communication Quarterly_, _27_ (4), 383–390.
[https://doi.org/10.1177/107769905002700403.](http://dx.doi.org/10.1177/107769905002700403)


CHAPTER 23

#### The Future of Investigative Journalism in an Era of Surveillance and Digital Privacy Erosion


_Julie Posetti_


Introduction