=====================
Continuous Deployment
=====================

Idea
====

* Once a *Merge Request* is merged everything happens automatically
* typical use-cases are:

   * releasing a new version
   * building the corresponding apps
   * building new documentation


Purpose
=======

* allow developers to be lazy
* automated processes are less error prone
* maintain documentation in Git


Webhook
=======

A Webhook is an Api Endpoint that you can call in order to make a change
on a website.


Simple Example
______________

When you post a comment on Reddit, you trigger a webhook as well. In the
background some code puts your comment into some reddit database. Afterwards
it makes a call to a Reddit webhook that tells it to fetch the newest state
from the database.


Elaborate Example: Read the Docs
________________________________

A similar use-case is to public your documentation to the internet. Therefore
we will establish a webhook on Read the Docs. That means our code versioning
system (GitLab) will call the webhook when there are changes.


