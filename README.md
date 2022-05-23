# Task 1
## Evaluation
| |use BPE|vocabulary size|BLEU|
|---|---|---|---|
|(a)|no|2000|12.3|
|(b)|yes|2000|18.5|
|(c)|yes|4000|19.8|

all done with a beam size of 5
### Manual
The difference in BLEU is amazingly present when looking at the test output. Although for example bpe 2000 and 4000 weren't as far apart, the ouput reveals the system got a lot of details more correct: "Marshmallow" instead of "Marshmallos", "riesiger Erflog" instead of "riesiges Erfolg" and so on. As expected the word level looks and reads a lot worse than the two bpe level models, consisting of about one thir `<unk>` tags. Even though most of the rest of the words are correct or at least make some sense, as a whole they wouldn't be usable to convey any meaning because so much information is missing.
Surprisingly even this limited bpe system was able to translate some shorter and simpler senteces perfectly, even with grammatatical accord. Most of the senteces are quite disconnected though, semantically and grammatically, so I wouldn't call even the best model "good" per se. I'd like to add that the system basically spamming words in slight variations that it thinks are correct to brute force a reward is hilarious and very endearing, I had a blast skimming the hypothesis. Here one of my favorites:
- Hypothesis: Und die Idee ist ziemlich einfach: Teams von vier müssen die tödliche Struktur aus 20 Königin zu bauen, einer Tarte, eines Tarts, eines Tages, eines Tarts, eines Gards, und ein Marshmallow.
- Original: And the idea's pretty simple: Teams of four have to build the tallest free-standing structure out of 20 sticks of spaghetti, one yard of tape, one yard of string and a marshmallow.
- Ref: Die Idee ist ziemlich einfach. Vierer-teams müssen die größtmögliche freistehende Struktur mit 20 Spaghetti, ca. 1m Klebeband, ca. 1m Faden und einem Marshmallow bauen.
## Task 2 - Beam size
Note: I also took the liberty of adding plot for the time it took to evaluate with different beam sizes, as I thought this was interesting
![image of the line plot relating the beams size to BLEU-score and time in seconds](results/graph.png)
