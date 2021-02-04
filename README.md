# Dead-List
A web application used for documenting and discussing recently the deceased.

The intent of this application is to replicate and eventually replace and preserve a longstanding 'game' traditionally played through a listserve.  Members of which would send a properly formatted email notifying the group of a recently passed famous person along with basic details of their death.  Usually in the form of a link to a reputable website / news organization.  Other participants would then reply with puns based on the work of the individual that had passed.



## Installation

> The following installation instructions are subject to change based on the final technical implementation of the application.  They will likely still include steps similar to those outlined below.

### Required Software
In order to increase the portability and ease of installation and use, this application was built to take advantage of Docker containers.

As such users will need to have `Docker` installed to setup and run the app.
Please see [these instructions](https://docs.docker.com/desktop/) for more information on how to install `Docker` on your machine.

The only other software needed to retrieve and run this application is `Git`.

See [these instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for more information on how to install `Git` on your machine.

### Installing the application

* Clone this repository
 * `git clone git@github.com:TravisIngram/Dead-List.git`
* From the root directory, run the following command
 * docker-compose build
* Once built you will want to run the following commands within the containerized environment.
 * docker-compose run django bash
 * python3 manage.py migrate
 * exit

From here the application should be ready to launch.

## Getting Started

Once installed, run the following command to launch the application.

`docker-compose up`

## License

MIT License

Copyright (c) 2021 Travis Ingram

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.