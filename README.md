# pymvc
mvc design pattern framework with eample demo code in python.

## Overview

PyMVC is a lightweight Python framework that helps you structure your applications using the Model-View-Controller (MVC) architectural pattern. It provides a foundational structure and reusable base classes to help developers build maintainable, scalable applications with clear separation of concerns.

### usage example
[Here is a demo example](demo/main.py) - you can copy this demo into your project and then add or remove features as needed.

### what is mvc design pattern
```
It is a high-level structure for writing code. It provides a way to create professional,
easily maintainable, and easy-to-understand code.
We should separate the code into three components: Model, View, and Controller (MVC).

it means:

   * Execution must start from the controller
   * The controller will initialize and manage the graphical user interface (view functions)
   * The controller will also initialize and manage the core backend code (model functions)
   * View functions should NOT be called from the model, and model functions should NOT be called from the view
   * The controller can call both view and model functions, enabling communication between them
   
If you implement this basic code structure, your application automatically becomes professional,
maintainable, and well-organized.
```

## Directory Structure

```
pymvc/
├── mvc.py              Main framework entry point - base MVC class that initializes View, Model, and Controller
├── model.py            Base Model class for inheritance - extend this to implement your business logic
├── view.py             Base View class for inheritance - extend this to implement your user interface
└── controller.py       Base Controller class for inheritance - extend this to orchestrate Model and View

demo/
└── main.py             Example implementation showing how to extend the MVC framework with your own logic
```

### what are these files

**mvc.py**
- Contains the starting point and main framework code
- Runs the controller to orchestrate the application
- Base class that you extend for your application's entry point

**model.py**
- Contains backend/business logic code
- Implements low-level functions and data operations
- Should be extended with your application-specific logic
- Example: database operations, algorithms, data processing

**view.py**
- Contains the graphical user interface (GUI) or presentation layer
- Handles user input and output display
- Should be extended with your application-specific UI
- Example: prompts, output formatting, UI rendering

**controller.py**
- Responsible for managing and orchestrating the model and view
- Runs both view and model functions
- Acts as the mediator between view and model layers
- Should be extended to implement your application's control flow

## How the Components Work Together

1. **Application Starts**: Your application inherits from `mvc.mvc` and initializes an instance of each component (View, Model, Controller)
2. **Controller Runs**: The controller's `run()` method is called, which orchestrates the application flow
3. **User Interaction**: The view captures user input or triggers actions
4. **Controller Coordinates**: The controller receives input from the view and delegates operations to the model
5. **Model Processes**: The model executes business logic and returns results
6. **View Updates**: The controller updates the view with results from the model
7. **Loop Continues**: The process repeats until the application ends

## Getting Started

### Basic Implementation Steps

1. Create your own view class extending `view.view`
2. Create your own model class extending `model.model`
3. Create your own controller class extending `controller.controller`
4. Create a main class extending `mvc.mvc` that initializes all three components
5. Implement the `run()` method in your controller to define your application's logic

### Example Usage

See [demo/main.py](demo/main.py) for a complete working example of how to implement an application using this framework.
