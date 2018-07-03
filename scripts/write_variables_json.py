import simplejson 
import arrow
from collections import OrderedDict as OD

VARS_SHEET = 'variables_all.tsv'

NUMERIC_TYPES = ('valid_min', 'valid_max')


def parse_line(line): return [i.strip() for i in line.split("\t")]

def parse_common_vars_sheet(vars_sheet=VARS_SHEET):

    d = OD()

    with open(vars_sheet) as reader:
        _headers = parse_line(reader.readline())

        for line in reader:
            items = parse_line(line)

            if items[0]: 
                scope = items[0].split()[-1].lower()
                d[scope] = OD()

            if items[1]:
                variable = items[1]
                d[scope].setdefault(variable, OD())

            if items[2] and items[3]:
                attr, value = items[2:4]
                if attr in NUMERIC_TYPES and value[0] != "<": # ignore "<derived from file>" stuff
                    value = float(value)
       
                d[scope][variable][attr] = value

            # NOTE: If no value provided then we DO NOT set the attribute
             
    return d


def main():

    dct = parse_common_vars_sheet()

    for key in dct: 

        data = {"variable": dct[key],
                "version_metadata": {
                    "author": "Ag Stephens <ag.stephens@stfc.ac.uk>",
                    "creation_date": str(arrow.now()),
                    "institution_id": "STFC",
                    "previous_commit": ""
               }
           }

        output_path = "../AMF_variable.json".format(key)

        # Write output to JSON
        with open(output_path, 'w') as writer:
            simplejson.dump(data, writer, indent=4)

        print "Wrote: {}".format(output_path)

        return


if __name__ == '__main__':

    main()
