## Browser tests for https://computer-database.gatling.io

### Preface:
This is automation testing framework on top of [seleniumbase.io](https://seleniumbase.io/)
for testing https://computer-database.gatling.io website. This website has read only database ¯\_(ツ)_/¯ 

### Local test run (docker):
> To run tests on https://computer-database.gatling.io/ in 3 threads:
> 
>```make test```
> 
> To open test result report: ```make report```
> 
>```-k``` is defaul option so u can run particular tests like: ```make test run=create```
> where 'create' string for pattern matching with test names


![run tests in Docker](https://user-images.githubusercontent.com/12695133/131242299-38a12f72-2d23-4c1e-b27d-36c6f3df69ad.gif)


### Local installation (if you don't want to use docker and selenoid):
>1. Install [chrome browser](https://www.google.com/chrome/) to local host
>2. ```pip install -r requirements.txt```
>3. ```sbase install chromedriver latest```

### Test run (if you don't want to use docker and selenoid):
>pytest --base_url=http://url.com  --html=report.html -l -v

### Project structure:
>`conftest.py`: global fixtures and command line keys config (base_url)
> 
>`framework/urls.py`: uri's to web pages without base url
>
>`framework/actions`: python modules for repeatable browser actions
>
>`framework/actions/base_actions`:
>- setUp before browser open
>- redefining of seleniumbase methods (`open`, etc)
>- global helper methods
>- fixture injection (Faker for `self.faker.word()` inside test)
>
>`framework/actions/modules`: logically divided modules with selectors and selector builders
>
>`framework/actions/tests`: test suits grouped by product functionality
> 

### Run test in Pycharm:
>1. Select `pytest` in ```PyCharm -> Preferences… -> Tools -> Python Integrated Tools -> Testing -> Default test runner```
>
> 
>2. Replace default value for `--base_url` in `pytest_addoption` function in `conftest.py` with your url where browser should go
>
> 
>3. Click on green triangle near test function or test class:
![run tests in IDE](https://user-images.githubusercontent.com/12695133/131230536-60e5f59d-c45b-458a-b89e-ee4198c9951c.gif)

### Awesomeness approve from [seleniumbase.io](https://seleniumbase.io/) creator 😅
![run tests in IDE](https://user-images.githubusercontent.com/12695133/131457843-640adb34-c899-400a-a943-0912b687037d.png)