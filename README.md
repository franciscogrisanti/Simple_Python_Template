
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


```sh

Generate ASCII code name here --> https://www.coolgenerator.com/ascii-text-generator

```

<!-- PROJECT LOGO -->

<br />

<p align="center">
  
  <a href="https://github.com/github_username/repo_name">
    
   
  </a>

  <p align="center">
     Given ST and scRNA-seq data of a tissue, STANN models cell-types in the scRNA-seq dataset from the genes that are profiled by both ST and scRNA-seq. The trained STANN model then assigns cell-types to the ST dataset.
    <br />
    <br />
    <br />
    <a href="Link to demo">View Demo</a>
    ·
    <a href="Link to repo issues">Report Bug</a>
    ·
    <a href="Link to repo issues">Request Feature</a>
  </p>
</p>


<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

```sh
Type requisites here
```


<!-- USAGE EXAMPLES -->

## Usage

Install conda environment

```sh
conda env create -f environment.yml
```

Activate conda environment 

```sh
conda activate Project_Name
```

Run model on your data

```sh
python train.py --model XXX --data_train ./path_to_training_data/XXX.XX \
--data_predict ./path_to_predict_data/XXX.XX--output \
./path_to_output/ --project name_of_project
```

## Demo

Demo data 

<p>
  <p>
    <a href="Link to data download">Download data</a>
  </p>
</p>

Demo code can be run in a jupyter notebook

<p>
  <p>
    <a href="Link to demo notebook">View Demo</a>
  </p>
</p>


<!-- ROADMAP -->
## Roadmap

See the [open issues](Link to issues) for a list of proposed features (and known issues).


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Francisco Grisanti - franciscogrisanti@gmail.com

Project Link: [Link to repo](Link to repo)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/franciscogrisanti/Simple_Python_Template.svg?style=flat-square
[contributors-url]: https://github.com/franciscogrisanti/Simple_Python_Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/franciscogrisanti/Simple_Python_Template.svg?style=flat-square
[forks-url]: https://github.com/franciscogrisanti/Simple_Python_Template/network/members
[stars-shield]: https://img.shields.io/github/stars/franciscogrisanti/Simple_Python_Template.svg?style=flat-square
[stars-url]: https://github.com/franciscogrisanti/Simple_Python_Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/sameelab/Simple_Python_Template.svg?style=flat-square
[issues-url]: https://github.com/franciscogrisanti/Simple_Python_Template/issues
[license-shield]: https://img.shields.io/github/license/sameelab/Simple_Python_Template.svg?style=flat-square
[license-url]: https://github.com/franciscogrisanti/Simple_Python_Template/blob/master/LICENSE.txt