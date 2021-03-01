# Dead-List
A web application used for documenting and discussing recently the deceased.

The intent of this application is to replicate and eventually replace and preserve a longstanding 'game' traditionally played through a listserve.  Members of which would send a properly formatted email notifying the group of a recently passed famous person along with basic details of their death.  Usually in the form of a link to a reputable website / news organization.  Other participants would then reply with puns based on the work of the individual that had passed.

## Installation

> The following installation instructions are subject to change based on the final technical implementation of the application.  They will likely still include steps similar to those outlined below.

### Required Software
While the intent of this project was to ensure the application was portable and easily installed via Docker, that particular functionality hasn't been implemented.

To install this application locally you will need to have Python and Django installed on your computer.

Please see [these instructions](https://docs.djangoproject.com/en/3.1/topics/install/) for more information on how to install `Django` and `Python` on your machine.

In addition, you will need `Node.js` and the `Ember CLI`. Instructions for these can be found in the `frontend` directory.

----

**In the future**, this app will make use of Docker so we'll keep the instructions below.

In order to run the app, `Docker` needs to be installed.
Please see [these instructions](https://docs.docker.com/desktop/) for more information on how to install `Docker` on your machine.

The only other software needed to retrieve and run this application is `Git`.

See [these instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for more information on how to install `Git` on your machine.

### Installing the application

* Clone this repository
  * `git clone git@github.com:TravisIngram/Dead-List.git`
* From the `backend` directory, run the following command
  * `python3 manage.py makemigrations`
  * `python3 manage.py migrate`
* Once these commands are run, the backend API will be ready to launch.
* From there, you will need to refer to the install instructions available for the [frontend](https://github.com/TravisIngram/Dead-List/tree/main/frontend).

From here the application (in its current state) should be ready to launch.

----

## Getting Started

Once installed, run the following commands to launch the application.

From the command line `cd` to the `backend` directory.
 * `python3 manage.py runserver`
   * `http://127.0.0.1:8000/admin`

In a separate window, `cd` to the frontend` directory.
* `ember serve`
  * Visit the app at `http://localhost:4200/index`


### Application Use

Visitors of the site are able to view `calls` and information about the recently deceased.

Once registered, members of the site are able to make new calls by clicking on the `Make Call` button.  They will also be able to post replies or `puns` to other users calls.  Rating puns is also possible by up or down voting them.

----

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