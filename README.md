# forward_kinematics
## Table of Contents
1. [About the Project](#about-the-project)
2. [Documentation](#documentation)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Setup Instructions](#setup-instructions)
5. [Run the Project Locally](#run-the-project-locally)
6. [Usage and Examples](#usage-and-examples)
7. [Running Tests](#running-tests)
8. [License](#license)
9. [Acknowledgements](#acknowledgements)
10. [Authors and Contact](#authors-and-contact)
11. [Badges](#badges)

## About the Project
This repository demonstrates how to perform Forward Kinematics (FK) using a specific kinematic chain example.

The kinematic chain used in this project is illustrated below:

<p align="center">
  <img src="res/kinematic_chain.png" alt="Kinematic Chain Example" width="400">
</p>

With the intermediate Denavit Hartenberg (DH) reference frames added, we get the following sketch:

<p align="center">
  <img src="res/kinematic_chain_with_frames.png" alt="Kinematic Chain Example" width="400">
</p>

From this, we determine the DH parameters:

| Link | \(a\)   | \(d\)     | \(\alpha\)      | \(\theta\)              |
|------|---------|-----------|-----------------|-------------------------|
| 1    | 0       | 0.4       | \(\pi/2\)       | \(\theta_1 + \pi/2\)    |
| 2    | 0.4     | 0         | \(-\pi/2\)      | \(\theta_2\)            |
| 3    | 0       | 0         | \(-\pi/2\)      | \(\theta_3 - \pi/2\)    |
| 4    | 0       | \(\theta_4\) | \(\pi/2\)    | 0                       |

The homogeneous transform between two reference frames is given by: 

The complete homogeneous transformation between the base of the robot and the robot TCP is then given by: 

*Note:* Here we used the classical Denavit Hartenberg convention, one could also use the modified DH convention. 

## Documentation
Detailed documentation is available at: [Documentation](https://linktodocumentation).

## Project Structure
The project is organized as follows:

## Installation
### Prerequisites
### Setup Instructions

## Run the Project Locally

## Usage and examples

## Running Tests
To run the tests in the `tests/` folder, run the following command:

```bash
pytest
```

## License
Distributed under the [MIT](https://choosealicense.com/licenses/mit/) License. See `LICENSE` for more information.

## Acknowledgements
 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

## Authors and Contact
- [@ViktorLaurens](https://github.com/ViktorLaurens/)

## Badges
Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)