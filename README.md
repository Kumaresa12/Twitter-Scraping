# Twitter-Scraping
**Are you tired of collecting data from twitter?** <br />
You got the solution now. <br />
Just follow the steps to scrap data from hashtags and not only just scrapping. You can store those data in json and csv files. Need more? Okay... You have another option too. Store those data in Mongodb. 

**Getting excited right!!!**

Let's start...

### APPLICATION

The code helps to scrap data from twitter through hashtag. It scrapes data like date, id, url, tweet content, user name, reply count, retweet count, language, source, like count relating to given hashtag. You can also select the number of tweets needed and the date range. Download the data in the form of json or csv format if you needed or store the data in Mongodb if required.

### REQUIREMENTS

*Python* - used for programming

*Pandas* - used for dataframe

*snscrape* - used for scraping twitter data

*streamlit* - used for web layout

*pymongo* - used for storing data

### INSTALL

pip install snscrape <br />
pip install streamlit <br />
pip install pymongo <br />

## BASIC WORKFLOW
import libraries given below <br />

![Screenshot (18)](https://user-images.githubusercontent.com/108707363/197338512-fa9279d3-b663-4640-a141-8fe8b56dc568.png)

Below code produces web layout < br />

![Screenshot (20)](https://user-images.githubusercontent.com/108707363/197338704-c8ff09c9-c71b-4cc0-a225-1d70a48749fd.png)
![Screenshot (21)](https://user-images.githubusercontent.com/108707363/197338843-f5ff4a68-a952-4b48-9f50-a5958ee1065f.png)

After entering hashtag, Date range and number of tweets , click submit button. <br />
You will get a display of table with date, id, url, tweet content, user name, reply count, retweet count, language, source, like count of each tweets related to hashtags

![Screenshot (23)](https://user-images.githubusercontent.com/108707363/197339288-c805eab3-e0d0-42d1-9935-379773380b79.png)

You can download those data in csv or json file by clicking the download button.

![Screenshot (25)](https://user-images.githubusercontent.com/108707363/197339557-1d222347-99a7-4d2c-9deb-7f27d6f11001.png)
 If you choose json or csv file format, the file gets downloaded automatically

Suppose you need to store those data in MongoDB, just click this button <br />
![Screenshot (26)](https://user-images.githubusercontent.com/108707363/197339757-b5dc7d81-bc29-40ab-aab4-c828c6120d3f.png)
The code calls the storage function to store those data combining everything with hashtag.<br />

![Screenshot (27)](https://user-images.githubusercontent.com/108707363/197340014-1bce7f9f-eb15-42eb-b671-f6feff1feca0.png)

![Screenshot (28)](https://user-images.githubusercontent.com/108707363/197340075-0c9f1a87-5c19-4d6f-9037-8d9d6c868ab9.png)

## RUNNING THE CODE:
Install the required libraries before running the code and install MongoDB. Connect the locol host of Mongodb. Then run the program in a python IDE.

### CHALLENGES FACED

The main challenge faced was storing the data in pymongo. It took more time to solve the problem compared to other things. We required to add hashtag with those scraping data and then make them into one collection. With few attempts the problem solved.
