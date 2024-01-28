# Ontology Lookup Service CLI Tool

### Invoking from CLI:

Run the tool with
`python run_app.py <id>` where `<id>` is a valid ontology ID. For example: `python run_app.py efo` will return:

```
Title: Experimental Factor Ontology
Description: ...
Number of Terms: 51935
Status: LOADED
```

`python run_app.py -h` will display some help in the terminal. 

### Invoking as a library function:

Calling `fetch_ontology_details(ontology_id)` will return a dictionary with the data shown above. 
This can be printed to the command line by calling the `print_ontology_details(dict)` method.

### Docker:

A Dockerfile is provided, so running the app will have two stages: 
1. Build the image with `docker build -t ontology-app .` 
2. Run the image with `docker run -it ontology-app <id>`, where `<id>` is a valid ontology ID.