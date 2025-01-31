# Visualizer for sorting algorithms

## To download:

```console
    git clone https://github.com/se04-aizu-2024/se04project-the_gaijins.git
    cd se04project-the_gaijins
```

## Executables:
    
    Executables can be found under /dist. 

    - Windows: main.exe
    - Mac: main

## Process to run locally


*Note it is recommended to perform the following in a virtual python environment with the pip updated and upgraded

- install pipenv using the following command:
        
```console
    pip3 install pipenv
```

- Download the necessary dependancies using the following commands:

```console
    pipenv install --system
```

- Run the File

```console
    python3 main.py
```

## How to recreate the Executable:

```console
    pyinstaller --onefile main.py
```


## Available Algorithms:

- bubble sort
- heap sort
- insert sort
- merge sort
- quick sort
- radix sort
- selection sort


