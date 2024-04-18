<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#analisis-sentimen-dpr">Analisis Sentimen DPR</a>
      <ul>
        <li><a href="#about">About</a></li>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#screenshot">Screenshot</a></li>
      </ul>
    </li>
  </ol>
</details>


## Analisis Sentimen DPR

### About
This Application evaluating the sentiment analysis performance of the Indonesian House of Representatives (DPR RI) website using a Naive Bayes model. The primary objective is to predict whether user-entered sentences are positive or negative in sentiment, providing insights into public perception of the DPR RI. There are also feature that Users can upload CSV files containing multiple sentences for sentiment analysis. This batch prediction feature enables efficient analysis of large datasets related to DPR RI performance. The website includes a feature for labeling datasets relevant to the performance of the DPR RI. Users can manually assign sentiment labels to data entries, contributing to the improvement of the sentiment analysis model. A summary of predictions made by the sentiment analysis model is provided, offering an overview of sentiment trends and patterns related to the DPR RI.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Flask][Flask]][Flask-url]
* [![MySQL][MySQL.com]][MySQL-url]
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Screenshot
* Klasifikasi (Classification)
  <br>You can enter sentences related to the DPR RI into the field provided then click submit to find out whether the sentence is negative or positive.<br>
  ![Screenshot from 2024-04-18 16-22-14](https://github.com/Jundix/analisis-sentimen-dpr/assets/56110716/391e04cd-f49c-4433-8522-233b9c74c37c)

* Batch Prediction
  <br>To use batch predictions, just click choose file then select the dataset that will be predicted after that click submit<br>
  ![image](https://github.com/Jundix/analisis-sentimen-dpr/assets/56110716/00b9f8a5-3c44-4b17-be0e-e5681f607aea)

* Rekap (Recap)
  <br>To see a recap of the predictions in the chart, select the month and year first, then click submit.And you can also download the dataset by clicking one of the CSV, Excel and PDF buttons.<br>
  ![image](https://github.com/Jundix/analisis-sentimen-dpr/assets/56110716/7ef89063-0ef5-458d-9fc9-355a5435da52)
  ![image](https://github.com/Jundix/analisis-sentimen-dpr/assets/56110716/6a16bb24-905a-48a3-9143-9839d8c5eaa5)
  ![image](https://github.com/Jundix/analisis-sentimen-dpr/assets/56110716/185bff5b-a0f5-4683-b8ea-69531a0e1a06)

* About
  <br>about itself contains a brief description of the application being created.<br>
  ![image](https://github.com/Jundix/analisis-sentimen-dpr/assets/56110716/eb3e9dac-d907-4794-8463-2c7eeaa129e5)

* Labelling
  <br>To be able to label a dataset file, click labeling on the navigation bar then click choose file and select the dataset you want to label. And then click submit.You can also look at the chart graph to see the positive and negative percentages. Then, to download the labeled dataset, you can click one of the Export CSV, Export PDF, and Export Excel buttons.<br>
  ![image](https://github.com/Jundix/analisis-sentimen-dpr/assets/56110716/e731cef2-fb70-49e8-8cab-cb5c489b1dee)
  ![image](https://github.com/Jundix/analisis-sentimen-dpr/assets/56110716/2833b420-ab55-43f8-a6d5-409c383d5088)
  ![image](https://github.com/Jundix/analisis-sentimen-dpr/assets/56110716/dd58b453-b0d2-4ef9-b953-6aa323c28fbf)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[MySQL.com]: https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white
[MySQL-url]: https://www.mysql.com/
[codeigniter.com]: https://img.shields.io/badge/CodeIgniter-%23EF4223.svg?style=for-the-badge&logo=codeIgniter&logoColor=white
[codeigniter-url]: https://www.codeigniter.com/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
[PHP.com]: https://img.shields.io/badge/php-%23777BB4.svg?style=for-the-badge&logo=php&logoColor=white
[PHP-url]: https://www.php.net/
[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white
[Java-url]: https://www.java.com/
[Kotlin]: https://img.shields.io/badge/kotlin-%237F52FF.svg?style=for-the-badge&logo=kotlin&logoColor=white
[Kotlin-url]: https://kotlinlang.org/
[SQLite]: https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white
[SQLite-url]: https://www.sqlite.org/
[Flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/

