from Patient import Patient
from Mutation import Mutation

# Create patient instance
x = Patient('Rachel')
x.import_hla_types_from_file('./data/sample_types.test.txt')
x.print_hla_types()

# Create mutation instance

