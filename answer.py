# from openai import OpenAI
# client = OpenAI()

# def getAnswers(name):
#     response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {
#             "role": "system",
#             "content": [
#                 {
#                 "type": "text",
#                 "text": "Given a biblical character (for instance, Adam (gen)) consider each of the following questions. Discuss before coming to answer. One you've answered every question, put the answers in a comma separated list, as in: ```Adam (gen), No, Not bad, No, eh, ``` and so on. Here are the questions:\n\n1. Would you call yourself a gigachad? Yes/No\n2. How immoral is your sexual activity? Not bad/little bad/very bad\n3. Do you have rizz? Yes/No\n4. How down-bad are you? I’m not/eh/it’s bad\n5. How big is your brain? small/not of note/big\n6. How do you feel about killing people? Yeah/Nah\n7. Would you say you’re good with animals? Yes/No\n8. You ever had 1–1 chats with God? Yes/No\n9. Do you feel like an active and valued part of your community? Yes/No\n10. Are you on the piss? Yes/No\n11. Are you a fundamentally sad and angry kind of a person? Yes/No\n12. Do you have any redeeming qualities? Yes/No\n13. Would you call yourself an out of the box thinker? Yes/No\n14. How much blood is on your hands? None/a bit/many have been struck down\n15. Have you ever written something which is now wrongfully included in the canon? Yes/No\n16. Are you loaded? Yes/No\n17. You ever feel like murdering any of your children? Yes/No\n18. Do you work in the food industry? Yes/No\n19. Do you work in construction? Yes/No\n20. Do you work in governance? Yes/No\n21. Have you lost a spouse? Yes/No\n22. Do you have a cool stick? Yes/No\n23. Do you keep your word? Yes/No\n24. Are you straight? Yes/No\n25. Would you call yourself an artistic person? Yes/No\n26. Do you have two nuts? Yes/No\n27. Do you have magical weirdo vibes? Yes/No\n28. Have you ever experienced divine judgement? Yes/No\n29. Are you a bit of a whinger? Yes/No\n30. Are you a quick runner? Yes/No\n31. Are you a fan of persia? Yes\n32. Do you travel often? Yes/No"
#                 }
#             ]
#             },
#             {
#             "role": "user",
#             "content": [
#                 {
#                 "type": "text",
#                 "text": "Eve (gen)"
#                 }
#             ]
#             },
#             {
#             "role": "assistant",
#             "content": [
#                 {
#                 "type": "text",
#                 "text": "Eve (gen) is the first woman created by God in the Book of Genesis, made from Adam's rib to be his companion, and is central to the narrative of the Fall of Man.\n\n1. Eve has some powerful qualities but does ultimately to fit the gigachad image. No\n2. Eve's sexual activity is not of moral note. Not bad\n3. Eve was able to convince adam to eat the fruit, this one could go either way, this time we'll say yes. Yes\n4. Eve is not single for the sake of the lord, but she's not note-worthily downbad. eh\n5. Eve seems to do some thinking, but is ultimately tricked by the snake. not of note\n6. Eve doesn't kill anyone. Nah\n7. Eve doesn't display affinity for animals. No\n8. Eve hangs out in the garden with God, and speaks with him during the fall. Yes\n9. Eve is an integral part of the first human community, even though her actions lead to the fall. Yes\n10. There's no indication Eve is \"on the piss.\" No\n11. Eve is definitely immature, but she doesn't seem *fundamentally* sad or angry. No\n12. Eve played a role in the Fall, but she is still a mother and companion, which can be seen as redeeming qualities. Yes\n13. Eve's decision to eat the fruit, and her quickness to blame afterwards, could be seen as \"thinking outside the box,\" albeit with severe consequences. Yes\n14. Eve does not directly shed any blood, though in some sense she is responsible for the fall and therefore all human death. many have been struck down\n15. Eve is part of the biblical canon, but she didn’t write anything. No\n16. Eve is not \"loaded\" in the material sense. No\n17. There's no indication that Eve wanted to harm her children. No\n18. Eve does not, in any sense, work in the food industry. No\n19. Eve does not, in any sense, work in construction. No\n20. Eve does not, in any sense, work in governance. No\n21. Eve does not lose a spouse in the narrative. No\n22. Eve does not have a cool stick. No\n23. Eve doesn't renege on any promises, though she does disobey gods command. No\n24. Eve is depicted in a heterosexual relationship with Adam. Yes\n25. There's no indication Eve is particularly artistic. No\n26. Eve is a woman. She does not have any nuts. No\n27. Eve definitely interacts with some \"magical weirdos\", but she herself is pretty normal. No\n28. Eve experiences massive divine judgement after eating the fruit. Yes\n29. Eve does not seem to be a whinger in the narrative. No\n30. There's no mention of Eve being a quick runner. No\n31. Everybody loves Persia. Yes\n32. Eve does not travel often in the narrative. No\n\nFinal answers:\n\n```Eve (gen), No, Not bad, Yes, eh, not of note, Nah, No, Yes, Yes, No, No, Yes, Yes, many have been struck down, No, No, No, No, No, No, No, No, No, Yes, No, No, No, Yes, No, No, Yes, No```"
#                 }
#             ]
#             },
#             {
#             "role": "user",
#             "content": [
#                 {
#                 "type": "text",
#                 "text": "Serpent (gen)"
#                 }
#             ]
#             },
#             {
#             "role": "assistant",
#             "content": [
#                 {
#                 "type": "text",
#                 "text": "The Serpent in the Book of Genesis is traditionally understood as the tempter who persuades Eve to eat from the Tree of the Knowledge of Good and Evil.\n\n1. The Serpent is often seen as cunning rather than a gigachad. No\n2. The Serpent's role isn’t about sexual activity, but leading others into sin. Not bad\n3. The Serpent is very persuasive, which could be considered having \"rizz.\" Yes\n4. The Serpent doesn't show any kind of romantic desperation. I'm not\n5. The Serpent showcases intelligence and cunning. big\n6. The Serpent leads mankind to the fall and death, and will bite the sons of eve in the heel. It's reasonable to say it would endorse murder. Nah\n7. The Serpent is itself an animal. Yes\n8. God talks to the serpent after the fall when cursing it and its offspring. Yes\n9. The Serpent does not seem to be part of any community. No\n10. The Serpent does not engage in drinking alcohol. No\n11. There's no strong indication the Serpent is fundamentally sad or angry, but rather rebellious or deceptive. No\n12. The Serpent's redeeming qualities are hard to identify. No\n13. The Serpent could be considered an out-of-the-box thinker for persuading Eve. Yes\n14. The Serpent doesn’t directly kill anyone but causes events that lead to the suffering and ultimate death of mankind. many have been struck down\n15. The Serpent doesn't write anything in the biblical narrative. No\n16. The Serpent isn’t depicted as wealthy. No\n17. The Serpent does not have children in the narrative. No\n18. The Serpent does not work in the food industry. No\n19. The Serpent does not work in construction. No\n20. The Serpent does not work in governance. No\n21. The Serpent does not have a spouse. No\n22. The Serpent doesn’t possess any kind of cool stick. No\n23. The Serpent tells eve she won't die, then she does. It does not keep its word. No\n24. The Serpent’s sexuality isn’t discussed. Yes\n25. There’s no indication of the Serpent being artistic. No\n26. The Serpent doesn’t have nuts. No\n27. The Serpent has a sinister and tempting presence, which could be seen as \"magical weirdo vibes.\" Yes\n28. The Serpent faces divine judgment, being cursed by God. Yes\n29. The Serpent is more deceptive than a whinger. No\n30. There’s no mention of the Serpent’s speed in the narrative. No\n31. Everybody loves Persia. Yes\n32. The Serpent does not travel often. No\n\nFinal answers:\n\n```Serpent (gen), No, Not bad, Yes, I'm not, big, Nah, Yes, Yes, No, No, No, No, Yes, many have been struck down, No, No, No, No, No, No, No, No, No, Yes, No, No, Yes, Yes, No, No, Yes, No```"
#                 }
#             ]
#             },
#             {
#             "role": "user",
#             "content": [
#                 {
#                 "type": "text",
#                 "text": "Adam (gen)"
#                 }
#             ]
#             },
#             {
#             "role": "assistant",
#             "content": [
#                 {
#                 "type": "text",
#                 "text": "Adam in the Book of Genesis is the first human created by God, placed in the Garden of Eden, and a central figure in the narrative of the Fall of Man.\n\n1. Adam does not fit the gigachad image. No\n2. Adam's sexual activity is not depicted as immoral. Not bad\n3. Adam does secure the first wife, but not by rizz. No\n4. Adam is in a committed relationship, so not down-bad. I'm not\n5. Adam is intelligent enough to name the animals but is still deceived. not of note\n6. Adam does not display bloodlust and does not kill anyone. Nah\n7. Adam named and cared for the animals. Yes\n8. Adam directly communicates with God multiple times. Yes\n9. Adam is a central figure in the first human community. Yes\n10. There is no indication Adam drinks alcohol. No\n11. Adam shows regret but is not fundamentally sad or angry. No\n12. Despite the Fall, Adam is a foundational figure in humanity's story. Yes\n13. Adam doesn't do anything particularly outside the box. No\n14. Adam does not directly kill anyone, but his actions have severe consequences. many have been struck down\n15. Adam does not write anything, so nothing by him is in the canon. No\n16. Adam does not possess wealth. No\n17. There’s no indication that Adam wants to harm his children. No\n18. Adam works the land after the Fall, so he works in agriculture. Yes\n19. Adam does not work in construction. No\n20. Adam does not hold a governance role. No\n21. Adam does not lose a spouse in the narrative. No\n22. Adam does not possess a cool stick. No\n23. Adam does not keep his commitment to God. No\n24. Adam is depicted in a heterosexual relationship with Eve. Yes\n25. There is no indication Adam is particularly artistic. No\n26. As a man, Adam does have two nuts. Yes\n27. Adam does not have magical weirdo vibes. No\n28. Adam experiences divine judgment for his actions at the fall. Yes\n29. Adam does complain about being led astray, in a pretty whingy way for a leader. Yes\n30. There is no mention of Adam being a quick runner. No\n31. Everybody loves Persia. Yes\n32. Adam does not travel often in the narrative. No\n\nFinal answers:\n\n```Adam (gen), No, Not bad, No, I'm not, not of note, Nah, Yes, Yes, Yes, No, No, Yes, No, many have been struck down, No, No, No, Yes, No, No, No, No, No, No, Yes, No, Yes, Yes, No, Yes, No```"
#                 }
#             ]
#             },
#             {
#             "role": "user",
#             "content": [
#                 {
#                 "type": "text",
#                 "text": "Cain (gen)"
#                 }
#             ]
#             },
#             {
#             "role": "assistant",
#             "content": [
#                 {
#                 "type": "text",
#                 "text": "Cain in the Book of Genesis is the first son of Adam and Eve, known for committing the first murder by killing his brother Abel out of jealousy.\n\n1. Cain is for sure a big caveman gigachad. Yes\n2. Cain's sexual activity is not discussed in the Bible. Not bad\n3. The text does not suggest Cain has any persuasive charm or \"rizz,\" whatsoever. No\n4. Cain does seem to be struggling with jealousy and rage, which hints at \"down-bad\" vibes. it’s bad\n5. Cain’s planning and execution of Abel’s murder is pretty pea brained. small\n6. Cain is a murderer. Yeah\n7. Cain does not seem to have a notable relationship with animals. No\n8. God speaks directly to Cain before and after Abel's murder. Yes\n9. Cain is ostracized after committing murder, feeling like a wanderer. No\n10. There’s no indication of Cain drinking alcohol. No\n11. Cain is deeply troubled and angry, especially after being marked by God. Yes\n12. Cain being marked for protection by God might be seen as a very slight redeeming quality, and he does found a city. Yes\n13. Cain’s decision to kill his brother is more reactionary than innovative. No\n14. Cain has directly killed Abel. a bit\n15. Cain does not write anything in the biblical narrative. No\n16. Cain is not depicted as wealthy. No\n17. Cain does not exhibit a desire to harm his children. No\n18. Cain is a farmer before murdering Abel. Yes\n19. Cain builds a city in the land of Nod. Yes\n20. Cain does not work in governance. No\n21. Cain does not lose a spouse in the narrative. No\n22. Cain does not possess any sticks. No\n23. Cain goes against God's warning and murders his brother; thus, he does not keep his word. No\n24. Cain has children. Yes\n25. There is no indication Cain is particularly artistic. No\n26. As a man, Cain does have two nuts. Yes\n27. Cain does not have magical weirdo vibes. No\n28. Cain experiences divine judgment after killing Abel. Yes\n29. Cain does whine about his punishment. Yes\n30. There is no mention of Cain being a quick runner. No\n31. Everybody loves Persia. Yes\n32. Cain becomes a wanderer after his exile, which means he travels often. Yes\n\nFinal answers:\n\n```Cain (gen), Yes, Not bad, No, it’s bad, small, Yeah, No, Yes, No, No, Yes, Yes, No, a bit, No, No, No, Yes, Yes, No, No, No, No, No, Yes, No, Yes, Yes, Yes, No, Yes, Yes```"
#                 }
#             ]
#             },
#             {
#             "role": "user",
#             "content": [
#                 {
#                 "type": "text",
#                 "text": "Lamech (gen)"
#                 }
#             ]
#             },
#             {
#             "role": "assistant",
#             "content": [
#                 {
#                 "type": "text",
#                 "text": "Lamech in the Book of Genesis is a descendant of Cain, known for his boastful declaration to his wives about killing a man for wounding him.\n\n1. Lamech is boastful, confident, and violent; he fits the gigachad image exactly. Yes\n2. Lamech has two wives, which is not seen favourably in the biblical context. little bad\n3. Lamech's boastful nature implies some degree of rizz or confidence among his peers. Yes\n4. Lamech’s actions suggest impulsivity and aggression, but not for the sake of romance. I'm not\n5. Lamech's doesn't seem particularly smart. not of note\n6. Lamech boasts about killing a man and sees it as a point of pride. Yeah\n7. There is no specific mention of Lamech’s relationship with animals. No\n8. Lamech does not have direct conversations with God mentioned in the Bible. No\n9. Lamech seems to brag to his wives which might imply his position within a community, but does not indicate a fulfilling community relationship. It seems like people don't like him very much. No\n10. There’s no indication of Lamech drinking alcohol. No\n11. Lamech does appear boastful and aggressive, probably not altogether sad though. No\n12. Lamech is a father and a poet, which could be seen as redeeming qualities. Yes\n13. Lamech's declaration suggests he thinks outside the box, albeit in a violent way. Yes\n14. Lamech admits to killing a man. a bit\n15. Lamech does not write anything included in the biblical canon. No\n16. There's no indication that Lamech is wealthy. No\n17. Lamech does not express a desire to harm his children. No\n18. There’s no indication that Lamech works in the food industry. No\n19. There’s no indication that Lamech works in construction. No\n20. There’s no indication that Lamech works in governance. No\n21. There is no information indicating Lamech has lost a spouse. No\n22. Lamech does not possess any cool stick. No\n23. This one is unclear, so we'll give him the benefit of the doubt. Yes\n24. Lamech has multiple wives, indicating heterosexual relationships. Yes\n25. Lamech’s poetic declaration suggests some artistic inclination. Yes\n26. As a man, Lamech does have two nuts. Yes\n27. Lamech is for sure weird, but he doesn't seem magical. No\n28. Lamech does not notably experience direct divine judgment. No\n29. Lamech boasts rather than whines. No\n30. There’s no mention of Lamech being a quick runner. No\n31. Everybody loves Persia. Yes\n32. Lamech does not travel often. No\n\nFinal answers:\n\n```Lamech (gen), Yes, little bad, Yes, I'm not, not of note, Yeah, No, No, No, No, Yes, Yes, a bit, No, No, No, No, No, No, No, No, Yes, Yes, Yes, No, No, Yes, No, No, Yes, No```"
#                 }
#             ]
#             },
#             {
#             "role": "user",
#             "content": [
#                 {
#                 "type": "text",
#                 "text": "Noah (gen)"
#                 }
#             ]
#             },
#             {
#             "role": "assistant",
#             "content": [
#                 {
#                 "type": "text",
#                 "text": "Noah in the Book of Genesis is renowned for building the Ark to save his family and the Earth's animals from the Flood.\n\n1. Noah is a faithful man but doesn’t fit the typical gigachad image. No\n2. Noah's sexual activity is only weird when his son sees the nakedness of his father. little bad\n3. Noah doesn't exhibit behaviors associated with \"rizz.\" No\n4. Noah is dedicated to his mission and family, not down-bad. I'm not\n5. Noah displays wisdom and meticulous planning in building the Ark. big\n6. Noah does not display a propensity for killing. Nah\n7. Noah saves and cares for many animals. Yes\n8. God directly communicates with Noah multiple times. Yes\n9. Noah is an integral and valued part of his family. Yes\n10. Noah does end up drinking after the Flood. Yes\n11. Noah is not depicted as fundamentally sad or angry. No\n12. Noah’s righteousness and obedience are his redeeming qualities. Yes\n13. Noah exhibits outside the box thinking when sending his the dove out (not when building the ark though, that was just following instructions). Yes\n14. Noah does not personally kill anyone, or really cause anyone to die. None\n15. Noah does not write anything included in the biblical canon. No\n16. There’s no indication that Noah is wealthy. No\n17. Noah does not exhibit a desire to harm his children. No\n18. Noah is involved in agriculture after the Flood, planting a vineyard. Yes\n19. Noah works in construction for the Ark-building project. Yes\n20. Noah does not hold a governance role. No\n21. No indication that Noah loses a spouse. No\n22. Noah doesn’t possess a cool stick. No\n23. Noah doesn't renege on any promises. Yes\n24. Noah is depicted in a heterosexual relationship. Yes\n25. There’s no indication Noah is particularly artistic. No\n26. As a man, Noah does have two nuts. Yes\n27. Noah seems like a normal dude, in over his head. No\n28. Noah experiences the divine judgment of the Flood. Yes\n29. Noah doesn’t display whinging behavior. No\n30. There’s no mention of Noah being a quick runner. No\n31. Everybody loves Persia. Yes\n32. Noah undertakes significant travel during the Flood. Yes\n\nFinal answers:\n\n```Noah (gen), No, little bad, No, I'm not, big, Nah, Yes, Yes, Yes, Yes, No, Yes, Yes, None, No, No, No, Yes, Yes, No, No, No, No, Yes, Yes, No, Yes, No, Yes, No, Yes```"
#                 }
#             ]
#             },
#             {
#             "role": "user",
#             "content": [
#                 {
#                 "type": "text",
#                 "text": name
#                 }
#             ]
#             }
#         ],
#         temperature=1,
#         max_tokens=2048,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0,
#         response_format={
#             "type": "text"
#         }
#     )
#     parts = response.choices[0].message.content
#     f = open("response/" + name + ".md", "w")
#     f.write(parts)
#     f.close()
#     return parts.split("```")[1]

# print(getAnswers("Adam (gen)"))

out = open("answers.csv", "a")
peeps = open("people.txt", "r")
o = open("answers.json", "w")
o.write('{\n')
for name in peeps:
    # print(name)
    # ans = getAnswers(name)
    # print(ans)
    # out.write("\n" + ans)
    f = open("response/" + name + ".md", "r")
    name = name.strip()
    lines = f.read().splitlines()
    i = 1
    o.write('"' + name + '": {\n')
    for line in lines[2:34]:
        line = line.replace('"', '')
        reason = '.'.join(line.split(".")[1:-1]).strip()
        ans = line.split(".")[-1].strip()
        o.write('\t"' + str(i) + '": { "answer": "' + ans + '", "reason": "' + reason + '"},\n')
        i = i + 1
    o.write("},\n")
    f.close()

o.write('}')
o.close()


peeps.close()
out.close()