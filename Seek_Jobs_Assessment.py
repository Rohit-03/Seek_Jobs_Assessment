import requests
from bs4 import BeautifulSoup


# Method will return an array containing the job and job data for each operining on coursera's page
def webScraper():
    
    # Result list that will contain all of the open jobs and their respective data
    job_data_list = []

    # A list that will store the html code for each open job on courseras job listing home page
    job_list = []

    # Make an API call to get the HTML code for the Job listing page and parse it using BeautifulSoup
    coursera_html = requests.get("https://boards.greenhouse.io/embed/job_board?for=coursera")
    home_page_soup = BeautifulSoup(coursera_html.content, 'html.parser')

    # Extract the html code for each job opening listed on courseras's main job page
    job_list = home_page_soup.find_all("div", {"class": "opening"})

    #iterate through each open job
    for job in job_list:
        
        # extract the job link that leads to a seperate page containing the respective job data 
        link = (job.find('a'))['href']
        
        # extract the job ID from the end of the link
        job_tokenID = link[-10:]
        
        #now create the formatted with the job id, th
        formated_link = "https://boards.greenhouse.io/embed/job_app?for=coursera&token=" + job_tokenID
        
        
        
        # Request the html code for the specific job's page which contains the job's data and parse it
        job_data_html = requests.get(formated_link)
        job_soup = BeautifulSoup(job_data_html.content, 'html.parser')
        
       
        
        
        # Create a variable that will hold all of the current job's data
        job_data = ""
        
        #Get job title 
        title = job_soup.find("h1", {"class": "app-title"})
        job_data += ("\n-----------------------------------------------------------------------\n\n")
        job_data +=(title.text + "\n\n") 
        
        # Will hold all of the html code containing the current job's data
        all_content = job_soup.find('div', id = 'content')
        
       

        # loop through all of the paragraphs on the job page and add the data to the job data variable
        i = 0
        for p in all_content:
            i=i+1
            # indicates that we have reached the end of the job data when parsing html
            if p.name == "h6" or p.text == "#LI-MB2":
                break
            # Only add content to the job data page after the third paragragraph
            if i> 3: 
                job_data +=p.text 
        
        #add the current job's data to the job_data list
        job_data_list.append(job_data)   
    
    return job_data_list
        



# Prints the elements of the resulting job_data_list
result = webScraper()
for x in result:
    print(x)

    
    

