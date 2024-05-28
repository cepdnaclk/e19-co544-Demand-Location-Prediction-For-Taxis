<div align="center">
  <h1><b>Highest Demanded Location Prediction System for Taxi Drivers</b></h1>
</div>
   
<h3 align="center">Highest Demanded Location Prediction System for Taxi Drivers 🚖 | Optimized Fleet Management 📈 | Enhanced Customer Experience 🌟</h3>

<div align="center">
    <a href="https://github.com/cepdnaclk/e19-co544-Demand-Location-Prediction-For-Taxis/issues">
        <img src="https://img.shields.io/github/issues/cepdnaclk/e19-co544-Demand-Location-Prediction-For-Taxis" alt="GitHub issues">
    </a>
    <a href="https://github.com/cepdnaclk/e19-co544-Demand-Location-Prediction-For-Taxis/pulls">
        <img src="https://img.shields.io/github/issues-pr/cepdnaclk/e19-co544-Demand-Location-Prediction-For-Taxis" alt="GitHub pull requests">
    </a>
    <a href="https://github.com/cepdnaclk/e19-co544-Demand-Location-Prediction-For-Taxis/releases">
        <img src="https://img.shields.io/github/downloads/cepdnaclk/e19-co544-Demand-Location-Prediction-For-Taxis/total" alt="GitHub downloads">
    </a>
    <a href="https://github.com/cepdnaclk/e19-co544-Demand-Location-Prediction-For-Taxis/releases">
        <img src="https://img.shields.io/github/v/release/cepdnaclk/e19-co544-Demand-Location-Prediction-For-Taxis" alt="GitHub release">
    </a>
</div>

<br></br>

## Table of Content

1. <a href="#introduction">Introduction</a>
2. <a href="#problem">Problem</a>
3. <a href="#opportunity-in-domain">Opportunity in Domain</a>
4. <a href="#detailed-solution">Detailed Solution</a>
5. <a href="#data-collection">Data Collection</a>
6. <a href="#exploratory-data-analysis">Exploratory Data Analysis</a>
7. <a href="#getting-started">Getting Started</a>
8. <a href="#contributors">Contributors</a>
9. <a href="#links">Links</a>

<h2 id="introduction">📚 Introduction</h2>
<p>This project leverages machine learning to predict taxi ride demand across different regions. By forecasting ride numbers for specific locations and time, we aim to create a more efficient and profitable ecosystem for taxi services.</p>

<h2 id="problem">🚧 Problem</h2>
<p><strong>For Taxi Drivers:</strong></p>
<ul>
  <li><strong>Less Availability:</strong> Long waits without passengers.</li>
  <li><strong>Less Profit:</strong> Inefficient positioning reduces earnings.</li>
  <li><strong>Safety Concerns:</strong> Operating in less secure areas.</li>
</ul>

<p><strong>For Customers:</strong></p>
<ul>
  <li><strong>High Stand Time:</strong> Long wait times for taxis.</li>
  <li><strong>Time Wastage:</strong> Delays due to inefficient taxi distribution.</li>
  <li><strong>Unfair Pricing:</strong> Surge pricing during peak demand.</li>
</ul>

<h2 id="detailed-solution">🛠️ Detailed Solution</h2>

<h2 id="data-collection">📊 Data Collection</h2>
<p>Our primary data source is the New York City Taxi and Limousine Commission website. From this resource, we can obtain approximately 20 features categorized by monthly data spanning over 20 years.</p>

<h2 id="exploratory-data-analysis">🔍 Exploratory Data Analysis</h2>

<br>
<img src="docs/images/Screenshot 2024-05-29 043436.png" alt="University of Peradeniya" style="max-width:100%">

<p>Steps Involved</p>
<ol>
  <li>Remove colums with higher percentage with Null values.</li>
  <li>Removes any rows from the dataFrame that contain missing values (NaN) </li>
  <li>Calculate trip times and speed. Then we can remove more data with unusual values. Using this we could remove the rows with unusual speeds, and trip times.</li>
  <li>Visualize interested parameters in the box plots. And checked for outliers.</li>
  <li>Convert pickup times raw into date time object. Since we are not intersted on the time we could remove that.</li>
  <li>Fianally, we could filer only date of ride (based on the pickup time) and PUlocation.</li>
  <li>Collect .csv files based on month in format.  Finally we have 12 csv files for a year with naming format YYYY-MM.
 
  
  </li>
  
</ol>





<h2 id="getting-started">🚀 Getting Started</h2>
<p>Anybody can explore this project and gain insights. It's easy.</p>
<ol>
  <li>Clone the repository to the htdocs folder inside the XAMPP installation location.</li>
</ol>

<h2 id="contributors">Contributors</h2>
<ul>
  <li>E/19/034, H.M.K.D. Bambaragama, <a href="mailto:e19034@eng.pdn.ac.lk">email</a></li>
  <li>E/19/226, K.G.M. Madushanka, <a href="mailto:e19226@eng.pdn.ac.lk">email</a></li>
  <li>E/19/278, A.P.T.T. Perera, <a href="mailto:e19278@eng.pdn.ac.lk">email</a></li>
  <li>E/19/409, D.P. Udugamasooriya, <a href="mailto:e19409@eng.pdn.ac.lk">email</a></li>
  <li>E/19/432, U.I. Wickramaarachchi, <a href="mailto:e19432@eng.pdn.ac.lk">email</a></li>
</ul>

<h2 id="links">Links</h2>
<ul>
  <li><a href="https://github.com/cepdnaclk/e19-co544-Demand-Location-Prediction-For-Taxis/{{ page.repository-name }}" target="_blank">Project Repository</a></li>
  <li><a href="https://cepdnaclk.github.io/{{ page.repository-name}}" target="_blank">Project Page</a></li>
  <li><a href="http://www.ce.pdn.ac.lk/" target="_blank">Department of Computer Engineering</a></li>
  <li><a href="https://eng.pdn.ac.lk/" target="_blank">University of Peradeniya</a></li>
</ul>
