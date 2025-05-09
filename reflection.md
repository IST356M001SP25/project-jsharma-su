# Reflection

Student Name:  Jiya Sharma
Student Email:  jsharma@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

Although I had used these tools and technologies during the assignments before, as in Streamlit, Pandas, and Plotly, this project still challenged me in multiple ways. The part I struggled the most with was web scraping. I was fine with writing the code but having it extracted properly and getting put into the folders for cache and data was difficult. Structuring the scraping process using Playwright, handling the content on the website I found, and making sure the data was clean and as consistent as I could make it was a lot of trial an error. In the data folder the passing json file was showing the name of the players on the team in the age section of the file so I had to end up writing a seperate part of the code to make sure when I was running the Streamlit it would put the name for all three of the rushing, receiving, and passing. 

What made it even more challenging was figuring out how to organize the extracted data in a reusable way. I had to think carefully about when to save raw versus cleaned data, and how to structure the files so they could be easily loaded for the visualization file. Getting the flow right between extraction, transformation, and loading was where I had spent the most time. Once the data was in good shape, the visualization and dashboard building part felt a lot more comfortable. I enjoyed using Streamlit to create the interface and Plotly to build the charts. Being able to see the the charts come to life was the most rewarding part. 

Overall, this project helped me reinforce what I already knew while pushing me to improve in areas I was less confident in, espeically scraping and data pipeline structure. I feel like I now have a much better understanding of how to handle more ral world data from messy sources like the one I foun and turn it into something interactive and useful.