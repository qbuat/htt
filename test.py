from mva.samples import Data
from mva.categories import Category_VBF

a = Data(2012)
print a.records(Category_VBF, 'OS', ['tau1_pt'])
print a.partitioned_records(Category_VBF, 'OS', ['tau1_pt'], num_partitions=10)
