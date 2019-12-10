<h1 align ="center">Data Representation Project 2019</h1>

<p align ="center"></p>

<h2 align ="center">Created by Richard Feeney. Student Number : G00376345</h2>
<br>

# Introduction

Please note that I have used Plotly's Python graphing library to create interactive, publication-quality graphs. If the notebook is run from Github it will not display all of the graphs. I recommand visiting https://nbviewer.jupyter.org/github/richardfeeney7/Programming-for-Data-Analysis-Project/blob/dcd48d26e6c65c162b53e20849ac47d556b7ff3b/%20Programming-for-Data-Analysis-Project.ipynb to view the project or download the files and run on your own mchine. Also with regards the tables within the notebook, because I have used plotly you have the ability to move the columns around if you wanted to see specific information side by side. 

### How To Run Project
<div align="justify">
1. Download Cmder command line or use the command line on your computer. (Please note that this project uses JS that might not display on github<br>
2. Go to Github, find my repository or use the following link https://github.com/richardfeeney7/Data-Representation-Project then click on the Clone/Download button and select download zip. <br>
3. Once downloaded go to the command line and navigate to this  download using the cd command. When I download the zip file, I first had to unzip it and cd into it, and within that folder I had another folder that I need to cd into also.<br><br>
4. Once in the correct location type "set FLASK_APP=..\Data-Representation-Project\BigProject" then " echo %FLASK_APP%" and finally flask run. This will give you a web address that you will have to search for. The first page has a username and password and both are set to uppercase ADMIN <br>.

### Project sections to note

1. I have created this project using mySQL, Python and Flask.<br>
2. I have created three tables in mySQL that will hold information / data on Music Genres. One the application is live these tables can be modified using CRUD and the queries are all generated from the musicDAO.py file.
3. I have used Bootstrap within my website and added some of my own external and internal CSS. AJAX calls are also made within the HTML files and the contents will  be displayed nicely pn the webpage. I have also implemented a YouTube API on each page that is linked to three different playlists that I have created for this project. 
4. BigProject.py file is used to make the requested server queries and will return it in the form of a JSON objects.
