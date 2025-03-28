# Full-Stack AI Powered Customer Portal

### Self Service Portal for customers to 

<ul> 
<li> Check Account Balance </li>
<li> Apply for a loan and receive AI generated recommendations</li>
<li> View dispute history and Track Resolution </li>
</ul>

## How to build the MVP

So, to start building the MVP, first lets see what all things are we going to need

`.` A user portal for letting users login, apply for a loan, get recommendation and check and track disputes. <br>
`.` A backend server for managing authentication, collecting and processing data and generating responses.<br>
`.` A database to store the user data securely. <br>
`.` An LLM like Gemini or Open AI's models to generate recommendations based on the collected data.

Given the timeframe of 24 hours and the fact that AI tools can be leveraged to build the tool, I'll follow the following strategy to develop the MVP.

1. I usually start building the server side first. So, we can have a couple of choices to espouse for the backend, powered by AI. Some logic, for e.g auth logic and quick API development can be done with the help of AI like GitHub copilot or Chat GPT etc. We can also use Supabase, which provides quick backend and data storage solutions, but I'm not pretty familiar with that, so I'd skip this option. So, I'd quickly get the API structure built using AI agents, then modify that as per the business logic and this should take no more than three hours.
2. For data storage and authentication management, a quick implementation would be Firebase. Alternatively, we can setup MongoDB as well.
3. For developing the UI, I will use AI assisted tools like v0.dev or lovable.dev to develop simple and intuitive designs quickly. Using AI tools only, I can setup the base for API integration and then I can quickly get the code setup on local and integrate the actual APIs.
4. Once done, the things would need a little testing against different test cases including the edge cases.
5. Once this thing is tested, we can move ahead with the LLM integration part. We can do a quick implementation of any LLM using Langchain, which would take no more than three hours.
6. This way we can wrap up the MVP development of a self-service customer portal.

## If low code platforms were available, how would you use them to accelerate the development

1. If low code platforms were available, a lot of manual work could be reduced. For e.g the UI that we could earlier build using v0 and lovable, can now be built in less than half the time using low code UI building tools like Glide Apps or Bubble. 
2. Rather than using a database, we can integrate Airtable or Google sheets again saving a ton of time. 
3. Also, in MVPs are mostly to check if the product would work or not. So, if the business logic is connected to a streamlit app, it can be verified there as well. A few lines of code, and donnne.
