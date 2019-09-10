# CIS4930_PPA1: Unit Testing

### Naming Conventions
I used Python and the PyTest framework. I separated each function into it's own file named based on its domain (i.e. Body Mass Index = *bmi.py*). For testing, PyTest searches for test files prefixed with **test_** (i.e. *test_bmi.py*), so corresponding testing files were named accordingly. Functions were organized into a folder named *main* and *tests* in order to make it extremely readable to someone unfamiliar with the codebase.

### Setup

1. 
2. 
3. 
4. 
5. 

### Test Suites & Coverage
- [X] All Test Suites Pass
![logo](https://github.com/changrif/CIS4930_PPA1/blob/master/assets/test_suites.png)

- [X] Test Coverage Report
![logo](https://github.com/changrif/CIS4930_PPA1/blob/master/assets/test_coverage.png)

### Discussion Questions
###### Describe your unit testing & TDD experience.
- My first exposure to unit testing was academically through CEN3031 Introduction to Software Engineering. The class covered the Agile methodology as well as clean code and testing best practices. We also used TDD developing the final project. In addition, I have work experience unit testing during my internships developing for various corporate projects (using JUnit, Go, Codeception - PHP).

###### What do you think of unit testing & TDD?
- In my experience, unit testing and TDD are extremely helpful towards development. It can definitely slow things down, especially when complex state and dependencies that make testing more difficult are involved. However, it makes it easier to return to projects which you are no longer familiar and make changes to software. I am more confident making changes to software with a full testing suite because I know a new feature will not interfere with existing functionality. 

###### Do you think it's useful for a real project?
- Yes, I think it's more useful for a real project than an academic exercise. Unit testing is most useful when multiple developers are working on software, new features are being developed quickly and the software must work consistently. If unit testing is utilized properly, developers will have the confidence to make these changes alongside each other more quickly because the tests ensure that other functionality still works as expected.

###### Benefits & Drawbacks to TDD.
- Benefits:
   - Allows developers to focus on writing clean modular code from the beginning.
   - Builds confidence amongst engineers to develop new features without breaking existing ones.
   - TDD allows for a short feedback loop that allows developers to incrementally and modularly test new features without needing to test the whole program each iteration.
   - TDD also allows for an automated way to test the full functionality of a program quickly.
- Drawbacks:
   - Development takes longer in the short-run because code is being written for the features and tests.
   - Tests may provide false positives if they are not written properly.
   - Some tests can be difficult to write and not really assist in developing if they involve complex state, side-effects or a lot of database or APIs calls.
---------------------------------------
### Screencasts

##### Red. Green. Refactor. 
###### (1) BMI Function
![logo](https://github.com/changrif/CIS4930_PPA1/blob/master/assets/bmi.gif)

GIF created with [LiceCap](http://www.cockos.com/licecap/).

###### (4) Split the Tip Function
![logo](https://github.com/changrif/CIS4930_PPA1/blob/master/assets/tip.gif)

GIF created with [LiceCap](http://www.cockos.com/licecap/).

##### Full Program Execution
![logo](https://github.com/changrif/CIS4930_PPA1/blob/master/assets/full.gif)

GIF created with [LiceCap](http://www.cockos.com/licecap/).
