# AMF_CVs

AMF controlled vocabularies

These files were generated by [amf-check-writer](https://github.com/ncasuk/amf-check-writer).

## Structure

Directories and files are structured as follows:
 - `AMF_CVs/<vocabulary>.json` - JSON version of each vocubulary - for use with `pyessv` library.
 - `product-definitions/spreadsheet/<spreadsheet_name>.xlsx` - directly converted from google spreadsheets used to develop the product definitions.
 - `product-definitions/tsv/<spreadsheet_name>/*.tsv` - each worksheet with the product definition google spreadsheets is converted to a *tab-delimited variables* file.
