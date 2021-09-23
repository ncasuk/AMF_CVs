# How to create a new release of the AMF CVs

## Overview

The AMF controlled vocubularies and product definitions are stored 
in this repository:

 https://github.com/ncasuk/AMF_CVs

They are tagged with releases that coincide with the versions
captured in directory names of the google spreadsheets that are
used to generate them.

The releases are listed at:

 https://github.com/ncasuk/AMF_CVs/releases

This document explains how to create a new release of the AMF CVs.

## Contents

The repository holds 3 main directories:

 - .../AMF_CVs/             - the controlled vocabularies in JSON format
 - .../product-definitions/ - spreadsheets and parsed spreadsheets (as 
                              tab-delimited files - ".tsv"), relating
                              to each of the products and generic rules
                              about compliance checking the AMF data
 - .../pyessv-vocabs        - the controlled vocabularies in PYESSV format 

## Release Procedure

The release procedure is laid out as follows:

 1. Clone the repository locally
 2. Create a release branch (e.g. `v1.1.0`)
 3. Create a new version of the CVs from the script: `create-cvs`
 4. Run the `code/scripts/compare-contents.sh` script to check the differences
    between the previous version and the new version
 5. Fix/check any issues if necessary (depending on the results from (4))
 6. Delete files that are no longer defined in the current version (`git rm ...`)
 7. Add and commit the changes (`git add ...`, `git commit -m "...`)
 8. Push the changes to github
 9. Create a Pull Request in github, and Accept it
10. Prepare a tagged release on github


