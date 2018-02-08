from patient import Patient
from mutation import Mutation
from allele import Allele

# Create patient instance
x = Patient('Rachel')
x.import_hla_types_from_file('./data/sample_types.test.txt')
x.print_hla_types()

# Create mutation instance

