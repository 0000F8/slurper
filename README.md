# Slurper

Slurper is a set of components that work to orchestrate the collection and parsing of unstructured web data and other media to be ETL'd for use in embeddings/vectors for LLM processing.

## Requirements

Right now we rely heavily on LangChain but that may change as the modularized nature of the architecture allows us to choose optimized elements that produce more accurate outcomes.

## Components

### Slurper-react
  This is the React front-end for interfacing with the Rails API back-end. (React/Javascript/Typescript/Tailwind/MUI)

### Slurper-rails
  This is the Rails back-end for reporting agent progress. (Rails API)

### Slurper-python
  This is the Python back-end for agents processing. (Python3/FastAPI)


  *Structure*
  
  `/agents/` - Agents connect different required components to achieve a specific goal. They are labeled with their specific action.
  `/extractors/` - Extractors extract information from different mediums
  `/transformers/` - Transformers take the information from extractors and normalize them in a way that can be combined later. Right now this means taking the extracted data and vectorizing the aggregate for uniform lookups.

### Component Diagram

![Slurper Diagram](https://github.com/0000F8/slurper/blob/main/assets/diagram.png?raw=true)