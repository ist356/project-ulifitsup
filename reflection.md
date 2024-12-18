# Reflection

Student Name:  Xinglai Pang
Student Email:  xpang03@syr.edu

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
Early in this project I had the idea of making a web scrapping things to scrap and analyse the jobs, since I am looking for jobs, and inspired by the not so pleasant-experience of looking job in CrowdStrike, they have over 300s jobs, and most of them are seniors, which is not available for me, and yet they don't have the setting to filter those options, which inspired me for this project. However, as I later goes in to the project this is way beyond my scope. 
First, there are more than 5 templates for the job description, which frustrate me a lot, creates a huge difficulties with data cleansing, and then I said I just pick the one that has the most jobs available. 
Then the job website is in a very responsive and application-like environment, which makes query_selector barely usable, one error happened most frequently was that the script went so fast that they run before the content is loaded, which  result in I chose locator, and it is a lot better, solved the problem to wait for contents to be loaded, and located the elements.
Third, they don't have a defnite or patterns for their requirements, like before there are more than 5 templates for their job description, and the one I am using has the most jobs in, which creates some data with no valid inputs, like missing job requirements, deadline and etc. However filter out Senior jobs is easy, simply type in Sr., and works fine. 
Although there are a lot of functions that did not implement as my expectations, but generally the project works fine, it helps me to find out the job I want to apply to and the one that I will be selected. I wish in the future I can complete this project, as it is able to scrape jobs from various companies, and despite what template they are using, the project could detect the requirements and what it suit for. Although it might be a good application of AI, but solving it with raw codes is fun tough and a good practice for coding.
