import os 
import re 
"""
any directory of your choice where any use of cryptographic usage can be used.
I would attack a crptographic directory on the github for test case.
"""
directory = ''  

"""
https://www.ibm.com/docs/en/mq-for-hpe-nonstop/8.1.0?topic=cipherspecs-deprecated
List of other deprecated algorith could be added your choice
"""
deprecated_algorithm = {
    'MD5': re.compile(r'\bmd5\b', re.IGNORECASE),
    'SHA1': re.compile(r'\bsha1\b', re.IGNORECASE)
}

def scan_file(directory):
    try:
        with open(directory, 'r', encoding='utf-8') as dr:
            content = dr.read
            results = {algorithm: [] for algorithm in deprecated_algorithm}

            for deprac, deprac_pattern in deprecated_algorithm.items():
                if re.search(deprac_pattern, content):
                    results[deprac].append[directory]
                return results
    except Exception as e:
        print(f"Unable to access this directory {directory}: {e}")
        return None

scanned_resulut = scan_file(directory)
print("Scan Results")