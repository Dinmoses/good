data=[{"type":"general","setup":"How do you steal a coat?","punchline":"You jacket.","id":130},
      {"type":"programming","setup":"Where did the API go to eat?","punchline":"To the RESTaurant.","id":390},
      {"type":"programming","setup":"['hip', 'hip']","punchline":"(hip hip array)","id":26},
      {"type":"general","setup":"Which side of the chicken has more feathers?","punchline":"The outside.","id":295},
      {"type":"general","setup":"What type of music do balloons hate?","punchline":"Pop music!","id":261},
      {"type":"general","setup":"What do you call cheese by itself?","punchline":"Provolone.","id":222},
      {"type":"general","setup":"If you see a robbery at an Apple Store...","punchline":"Does that make you an iWitness?","id":41},
      {"type":"general","setup":"Did you watch the new comic book movie?","punchline":"It was very graphic!","id":66},
      {"type":"general","setup":"What does C.S. Lewis keep at the back of his wardrobe?","punchline":"Narnia business!","id":22},
      {"type":"general","setup":"What do you call a nervous javelin thrower?","punchline":"Shakespeare.","id":211}]
# The number 4 tells python to get the fifth item in the list called data (indexing starts at 0)
# The word 'setup' tells python to get the value associated with the key 'setup' from that item(which is a dictionary)
print(data[4]['setup']) 

