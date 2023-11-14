# Playing with Modal

Modal (modal.com) is an abstracted, runtime engine that can run functions on remote computers, with dynamically provisioned containers and dependencies.

Here are some key features that I tried:

* Run simple python code with stubs that run on remote containers
* Provision custom images with dependencies on which the function will run
* Access secrets from the Modal platform
* Schedule functions that will at pre-defined times on remote containers

Some sample code that you can use:

* **get_started.py** - simple function that runs remotely
* **scrape.py** - python based web scraper that runs remotely on custom image
* **scrape_adv.py** - web scraper that runs remotely on custom image, schedules jobs and trigger notifications to slack channel

For more tutorials, refer to documentation from Modal here - https://modal.com/docs/examples