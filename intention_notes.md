
In order to gain a better knowledge on the role of MPs into the law creation process, we propose to focus on the amendments they propose.

Indeed the amendment procedure is the one which manages the law text modifications.

To gain a better knowledge on MPs role into the law (as a text) creation, we propose to establish a classification of amendments.

First, we aim at collecting a series of variables that could be used to characterize each amendment. The variable that we have collected are:

- resulting status (adopté, rejeté, retiré, etc)
- number of authors
- whether it is a duplicated amendment
- number of other amendments targeting the same law article at the same legislative step
- length of amendment's text
- length of motivations text
- main author's origin : (government, political group president, rapporteur, MP)

A more complex set of features can be produced by natural language processing on the "exposé des motifs" (motivations):

- TF/IDF of bigrams by political group
- categorisation by hand of the 1000 most frequent bigrams

We can then create categories based on the bigrams occurrences.

This approach allows to target the political motivations of an amendment's authors.

Features which we could work on:

- blurred duplicates: by defining a similarity measure on texts and motivations between each pair of amendments by article by lecture, we build the similarity network and cut the links on a similarity treshold (weight); we could then add to each amendment the number of blur duplicates
- the nature of the amended bill: loi de finances, EU directive application...
- the procedure type: accelerated, normal...
- whether the amendment was proposed during the committee step or plenary sessions
- number of references to existing laws the amendment contains

Based on those variables we propose to create groups of amendments which tend to aim at a common legislative usage.

More precisely, our intentions is first to interview french parliament specialists and browse the litterature on the known usage of amendment's right by MPs.

Then we propose to challenge our quantitative grouping methods with the qualitative definitions and vice-versa.

The law factory exploration tool will be of great help to check the quantitative groups of amendments back in the complexity of the law processing context. 

To illustrate our intentions we drafted our hypothetic types of amendment's usage by MPs. Each category is defined by a usage, a selection criteria based on a set of filters on the amendment variables, a set of quantitative profiles we expect the group of amendments to respect. 

- **"rédactionnel" / "coordination"**

  Amendments proposing small technical modifications which target more the form than the spirit of the law but making the law better in a juridical technic way. 

  Selection: short motivation (~<= 135 characters), containing one of this NLP markers: cohérence, rédactionnel, précision, coordination, précision rédactionnelle, etc.
  
  Expected quantitative profile: few authors, more likely to be adopted, large ratio of amendments proposed by the rapporteur.

- **"guerilla parlementaire"**

  Amendments which aims at protesting a strong opposition to a bill and to slow down the legislative process in order to mobilize opinion outside the parliament. 
  
  Selection: a high number of duplicates (ideally blurred ones, varying by a few characters), from the opposition, with a high level of concurrency, and short or similar motivations.
  
  Expected quantitative profile: all rejected, a large amount of those amendements starts with 'supprimer'

- **"lobbying"**

  Amendments written by a lobby and directly copy pasted by MPs.
  
  Selection: a small amount of blurred duplicates across various political groups, with nearly identical motivations.
  
  Expected quantitative profile: ?

- **"amendement d'appel" / "idéologique"**

  "Signaling amendments" formally tagged as 'appel' but also some not tagged as such but targeting the same usage. These are defined by the use of amendments to expose a political vision during the debates and invite the government to take public position on the matter but not necessarily to propose a text modification.
  
  Selection : contains bigrams categorizable as 'intention' and which contains the word 'rapport', thematic bigrams and no technical ones
  
  Expected quantitative profile: amendments more likely to be proposed by majority members and group presidents, long motivations text.

- **"consensus"**

  Selection: high number of blurred duplicates, unique motivations text
  
  Expected quantitative profile: high number of different number of groups, large amount of adopted amendments
  
  Beware: this category might overlap largely with lobyying.

- **"law making"**

  Selection: all the rest
  
  Expected quantitative profile: ?

Those categories are hypotheses to be tested.
Both quantitative and qualitative analysis might output a different set of categories.
Once the categories are set, we can analyse the profile of amendments usage by MPs, laws, time... 

