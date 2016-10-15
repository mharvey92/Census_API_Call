# Mariah Harvey
## August 12, 2016
##Argparse file

from Census.CensusAPIcall import call_API
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='This function calls demographics data from the Census Bureau API',
        formatter_class=argparse.RawTextHelpFormatter)
        
    parser.add_argument(
        '-od',
        '--output_dir',
        help='Location of the directory to put the data.',
        required=True
    )

    
    parser.add_argument(
        '-c',
        '--county',
        help='Three digit county code',
        required=True
    )

    parser.add_argument(
        '-s',
        '--state',
        help='Two digit state code',
        required=True
    )

    args = parser.parse_args()
    
    print "Reading API Census demographic data"
    census_apidata = call_API(county=args.county,
                            state=args.state)
    
    print "Writing API Census demographic data"
    census_apidata.to_csv(args.output_dir + 'census_apidata.csv')

if __name__ == '__main__':
    main()
    