# Unsplash Web Automation Framework

##  Overview
This project is a **test automation framework** for the [Unsplash](https://unsplash.com) **web application**,  
built with **Python, Selenium WebDriver, and UnitTest**.

The goal is to provide a clean, reusable, and extendable framework for functional and UI testing.

##  Features
- Automated browser-based testing with Selenium WebDriver  
- Test structure implemented using Python’s built-in **UnitTest** framework  
- Page Object Model (POM) for better maintainability
- Extendable Framework, easy to add more coverage

##  Project Management
Development and test planning for this project are managed in **Agile sprints** using **Taiga**.  
👉 [View Taiga Dashboard](https://tree.taiga.io/project/alena_taiga-unsplash)
## Documentation
- [Test Plan](https://docs.google.com/document/d/1tm548FLV4bos1Z75BkLcsleonigmQP45MnnsRPEQlMw/edit?usp=sharing)  
- [Unsplash Modules](https://docs.google.com/document/d/1MqmD69fXbS3oSpW8mTyGfHoDgFNRDsKRkh1PJ-fXqsw/edit?tab=t.0)  
- [Test Cases (Google Sheets – View Only)](https://docs.google.com/spreadsheets/d/17MzdQiObWmTMnRw4cOxQy2NPTkIN_YQXqckYR2PeWx8/edit?gid=2052949129)  


##  Project Structure
unsplash-automation/
│── config/ # Test data
│── screenshots/ # Screenshot folder
│── suites/ # TBD
│── tests/ # Test cases
│── pages/ # Page Object classes
│── toolkit/ # Base Classes, Page Classes, Locators, helpers(TBD)
│── reports/ # Test execution reports(TBD)
│── utils: README.md # Project documentation