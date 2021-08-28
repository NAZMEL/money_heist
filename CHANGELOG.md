Money Heist CHANGELOG
=========================
This file is used to list changes made in each version of the Money Heist.


v1.1.5 - Released
------
### New features
- Add export-csv functionality
- Add swagger documentation, write docstrings

v1.1.4
------
### Bug
- Fix test functions
### Added
- Add tests for user_profile
- Add tests for spendings and categories, Fix profile

v1.1.3
------
### Bug
- Fix bugs, add tests for spendings and sign-up
- Fix the CRUD for categories after merging
### New Feature
- Add filtering and searching functionality
- Add validators for specific user and category, also for spending

v1.1.2
------
### New Feature
- Make celery beat task work
- Add celery beat task, template for notification, refactor code
- Add categories CRUD methods, add tasks for spending notification
### Bug
- Fix celery task, add creating category endpoint, brake get/update/delete spending endpoints

v1.1.1
------
### New feature
- Add beta-functions for manage categories
- Add endpoint for manage spendings (view/create/update/delete)
- Add models, serializers, urls for spending application
- Add spendings application, refactor code


v1.0.5
------
### Added
- Add requirements, rewrite README
- Add tests for user_profile app
- Add tests function for user sign-up and sign-in
- Refactor code, delete unused files, add comments to functions

v1.0.4
------
### Bug
- Fix bugs

### New feature
- Add Change email endpoint
- Add Change password endpoint
- Add Sign-Up, implement MailJet
- Add get users info end-point

v1.0.3
------
### Added
- Add tasks
- Add Get Users data endpoint
- Add Sign-Up function
- Add Celery

v1.0.2
------
### Bug
- Fix bugs in tests for authentication

### Added
- Add tests for user's authentication
- Add auth, fix bugs
- Add update and partial_update methods to ProfileViewSet, add endpoints for profile/, auth/, etc


v1.0.1
------
- Create README.md
- Fix CustomUserModel class, add user_profile app
- Merge pull request 
- Add Authentication app, level Architecture UML tables
- 2021.08.1: Install project