# Curtain Rest API
**Problem Statement**: Closing and opening the blinds is a boring and tedious task. Often, one picks a state-open or closed-and
never bothers to change it. 

## Approach
Create a series of micro services to predict when to open and close the blinds.

## Service
*Curtain Client Service*: Responsible for the state of the blind and any interaction with the hardware i.e. Raspberry Pie, Stepper Motor

### Endpoints: 	

```/state```

  ```
  {
    'timestamp': 2017-06-11 19:00:57, 
    'state': 0,
    'StepperMotor': 1
  }
  ```

```/update/<int:state>/```

+ 0 to open blinds
+ 1 to close the blinds
