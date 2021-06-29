<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<p align="center">
<a href="https://github.com/miguelcamposfernandes/afterib/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/miguelcamposfernandes/afterib"></a>
<a href="https://www.python.org/downloads/release/python-360/"><img alt="Python3" src="https://img.shields.io/badge/built%20for-Python≥3.6-red.svg?style=flat"></a>
<a href="https://github.com/miguelcamposfernandes/afterib/stargazers"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/miguelcamposfernandes/afterib"></a>
<a href="https://github.com/miguelcamposfernandes/afterib/issues?q=is%3Aissue+is%3Aopen"><img alt="GitHub open issues" src="https://img.shields.io/github/issues/miguelcamposfernandes/afterib"></a>
</p>


  <h3 align="center">YT2Video</h3>

  <p align="center">
    Convert and download all YouTube videos to high quality .mp4 files, by just inputting the url.
    <br />
    <a href="https://github.com/miguelcamposfernandes/yt2video/blob/main/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://yt2video.herokuapp.com/">View a Demo</a>
    ·
    <a href="https://github.com/miguelcamposfernandes/yt2video/issues">Report Bug</a>
    ·
    <a href="https://github.com/miguelcamposfernandes/yt2video/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project was originated by a group of [IBDP](https://www.ibo.org/programmes/diploma-programme/) students, who wanted to facilitate the process of choosing the **right** university.
So, with the help of [Flask](https://flask.palletsprojects.com/en/2.0.x/) and other very useful web development frameworks we started the project.

### Built With

This project was developed with the following frameworks:

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [PyTube](https://github.com/pytube/pytube)
* [Bootstrap](https://getbootstrap.com)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/miguelcamposfernandes/yt2video.git
   ```
2. Create a virtual enviroment
   ```sh
   python3 -m venv env
   ```

3. Activate the virtual enviroment

   *If operating on macOS or Linux:*
  
   ```sh
   source env/bin/activate
   ```
   *If operating on Windows*
  
   ```sh
   env/Scripts/activate
   ```
4. Install all required dependicies
   ```sh
   pip install -r requirements.txt
   ```
5. Run the app.py file
   ```sh
   python3 app.py
   ```

<!-- USAGE EXAMPLES -->
## Usage

This web application is targeted to IBDP students, and can be simply used by acessing the [form](https://afterib.herokuapp.com/form) page and giving the subject and targeted city as input. Then, with the help of our database we will find an university that meets your requirements.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

E-Mail - miguelfernandes.personal@gmail.com

My GitHub: [https://github.com/miguelcamposfernandes](https://github.com/miguelcamposfernandes)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Heroku: Cloud Application Platform](https://www.heroku.com)
