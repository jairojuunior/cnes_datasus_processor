# CNES DataSUS Processor
THE CNES Datasus Processor is a suite of scritps to fetch and pre-process data on infrastructure and staff from the Brazilian Universal Healthcare System (SUS)

## High level data pipeline

1. Download zipped file from the DataSUS server
2. Unzip the file into a temporary folder (both the file and the folder are deleted at the end)
3. Import files into Pandas Dataframes
4. Merge Dataframes with respect to business rules
5. Export files to \<YYYYMM\>_output (where \<YYYYMM\> is the date of the file)
  
  ## How to run it?
  
  Edit `main.py` and replace the `daterefs` with all the dates you want to process.
  
  ---
**NOTE**

This data pipeline was tested only with files from January 2019 to now (March 2020). It might not work on previous data.

---

