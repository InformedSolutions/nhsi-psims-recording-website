# nhsi-psims-recording-website
A generic Django application implementing GOV.UK elements and styles that can be forked and extended

## Development notes

For an introduction to Django and structuring your project please see https://jira.informed.com:8444/pages/viewpage.action?spaceKey=ISPS&title=Django%3A+A+Whistle-Stop+Tour

### Key points to note:

1. If you are adding any custom style rules, do not make any changes to the govuk_template/static/stylesheets/base.css file
(as these will be lost if a package update is made to the govuk_template module). Any custom CSS should be added to template/static/stylesheets/custom.css
1. A series of common commands (inclusive of Docker build instructions) have been included in a Makefile for convenience.
Please consult the Makefile to see what commands are available.
1. To run the template in Pycharm, you will need to pass a settings file as part of your run command
(e.g. runserver 0.0.0.0:8000 --settings=django_govuk_app.settings.dev). This can be setup using Pycharm's "Edit Configurations" menu.

## Branching and Merging Strategy

The branching and merging strategy for code housed in this repository adopts the git flow model. 

For further details on the particulars of this model please see [Introducing GitFlow](https://datasift.github.io/gitflow/IntroducingGitFlow.html).

To configure your environment for git flow usage, please clone this repository, then in your git bash console issue the command `git flow init --defaults`.