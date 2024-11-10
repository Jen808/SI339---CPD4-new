import csv

def process_athlete_data(file_path):

   # Extracting athlete stats by year
   records = []

   # Extracting athlete races
   races = []           

   athlete_name = ""
   athlete_id = ""
   comments = ""

   with open(file_path, newline='', encoding='utf-8') as file:
      reader = csv.reader(file)
      data = list(reader)

      athlete_name = data[0][0]
      athlete_id = data[1][0]
      print(f"The athlete id for {athlete_name} is {athlete_id}")

      for row in data[5:-1]:
         if row[2]:
            records.append({"year": row[2], "sr": row[3]})
         else:
            races.append({
               "finish": row[1],
               "time": row[3],
               "meet": row[5],
               "url": row[6],
               "comments": row[7]
            })

   return {
      "name": athlete_name,
      "athlete_id": athlete_id,
      "season_records": records,
      "race_results": races,
      "comments": comments
   }    

def gen_athlete_page(data, outfile):
   # template 
   # Start building the HTML structure
   html_content = f'''<!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <!-- Get your own FontAwesome ID -->
      <script src="https://kit.fontawesome.com/42ad1a2a9b.js" crossorigin="anonymous"></script>


      <link rel = "stylesheet" href = "css/reset.css">
      <link rel = "stylesheet" href = "css/style.css">
      <script defer src="script.js"></script>

      

      <title>{data["name"]}</title>
   </head>
<body>
   <a href="#main">Skip to Main Content</a>

   
   <div class="main-header">
      <div class="name">
         <img src="../logo.jpg" class="logo-img" alt="skyline highschool athlete logo" tabindex="0">
         <a href="../index.html" class="logo" tabindex="0">Skyline CrossCountry</a>
      </div>

      <div class="toggle-menu" id="toggle-menu" tabindex="0">
         <span class="line1"></span>
         <span class="line2"></span>
         <span class="line3"></span>
      </div>

      <div class="hidden-nav">
         <ul>
            <li><a href="../index.html" tabindex="0">Home Page</a></li>
            <li><a href="../mens.html" tabindex="0">Men's Team</a></li>
            <li><a href="../womens.html" tabindex="0">Women's Team</a></li>
            <li><a href="../meets.html" tabindex="0">Meets</a></li>
         </ul>

      </div>




   </div>

   <nav id="navbar">
      <ul>
         <li><a href="../index.html" tabindex="0">Home Page</a></li>
         <li><a href="../mens.html" tabindex="0">Men's Team</a></li>
         <li><a href="../womens.html" tabindex="0">Women's Team</a></li>
         <li><a href="../meets.html" tabindex="0">Meets</a></li>
      </ul>
   </nav>
   

   <header tabindex="0">
      <!--Athlete would input headshot-->
      <h1>{data["name"]}</h1>
      <img src="../images/profiles/{data["athlete_id"]}.jpg" alt="Athlete headshot" width="200" onerror="this.onerror=null; this.src='../images/profiles/default_image.jpg';">     </header>
   <main id = "main">
      <section id= "athlete-sr-table">
         <h2 tabindex="0">Athlete's Seasonal Records (SR) per Year </h2>
            <table>
                  <thead>
                     <tr tabindex="0">
                        <th> Year </th>
                        <th> Season Record (SR)</th>
                     </tr>
                  </thead>
                  <tbody>
                  '''
   
   for sr in data["season_records"]:
      sr_row = f'''
                     <tr tabindex="0">
                        <td>{sr["year"]}</td>
                        <td>{sr["sr"]}</td>
                     </tr>                  
               '''
      html_content += sr_row

   html_content += '''                   
                </tbody>
                  </table>
                     </section>

                        <h2 tabindex="0">Race Results</h2>

                        <section id="athlete-result-table">
                           

                           <table id="athlete-table">
                              <thead>
                                 <tr tabindex="0">
                                    <th>Race</th>
                                    <th>Athlete Time</th>
                                    <th>Athlete Place</th>
                                    <th>Race Comments</th>
                                 </tr>
                              </thead>

                              <tbody>
                  '''

   # add each race as a row into the race table 
   for race in data["race_results"]:
      race_row = f'''
                                 <tr class="result-row" tabindex="0">
                                    <td>
                                       <a href="{race["url"]}">{race["meet"]}</a>
                                    </td>
                                    <td>{race["time"]}</td>
                                    <td>{race["finish"]}</td>
                                     <td>{race["comments"]}</td>
                                 </tr>
      '''
      html_content += race_row

   html_content += '''
                              </tbody>

                        </table>
                     </section>
                     <section id = "gallery">
                     <h2 tabindex="0">Gallery</h2>
                      </section>
                     </main>
                     <footer>
                        <p>
                              Skyline High School<br>
                        <address>
                              2552 North Maple Road<br>
                              Ann Arbor, MI 48103<br><br>

                              <a href="https://sites.google.com/aaps.k12.mi.us/skylinecrosscountry2021/home" tabindex="0">XC Skyline Page</a><br>

                              <a href="https://www.instagram.com/a2skylinexc/" tabindex="0">
                                 <i class="fa-brands fa-instagram" aria-hidden="true"></i>
                                 <span class="visually-hidden">Follow us on Instagram</span>
                              </a>

                     </footer>
               </body>
         </html>
   '''

   with open(outfile, 'w') as output:
      output.write(html_content)


def main():

   import os
   import glob

   # Define the folder path
   folder_path = 'mens_team/'
   # Get all csv files in the folder
   csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

   # Extract just the file names (without the full path)
   csv_file_names = [os.path.basename(file) for file in csv_files]

   # Output the list of CSV file names
   print(csv_file_names)
   for file in csv_file_names:

      # read data from file
      athlete_data = process_athlete_data("mens_team/"+file)
      # using data to generate templated athlete page
      gen_athlete_page(athlete_data, "mens_team/"+file.replace(".csv",".html"))

      # read data from file
      # athlete_data2 = process_athlete_data(filename2)
      # using data to generate templated athlete page
      # gen_athlete_page(athlete_data2, "enshu_kuan.html")


   # Define the folder path
   folder_path = 'womens_team/'
   # Get all csv files in the folder
   csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

   # Extract just the file names (without the full path)
   csv_file_names = [os.path.basename(file) for file in csv_files]

   # Output the list of CSV file names
   print(csv_file_names)
   for file in csv_file_names:

      # read data from file
      athlete_data = process_athlete_data("womens_team/"+file)
      # using data to generate templated athlete page
      gen_athlete_page(athlete_data, "womens_team/"+file.replace(".csv",".html"))

      # read data from file
      # athlete_data2 = process_athlete_data(filename2)
      # using data to generate templated athlete page
      # gen_athlete_page(athlete_data2, "enshu_kuan.html")

if __name__ == '__main__':
    main()
