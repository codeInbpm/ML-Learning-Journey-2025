# 基础知识
NumPy 的主要对象是同质多维数组。它是一个元素表（通常是数字），所有元素都具有相同类型，通过非负整数元组进行索引。在 NumPy 中，维度被称为 轴。

例如，三维空间中一个点的坐标数组 [1, 2, 1] 具有一个轴。该轴包含 3 个元素，因此我们说它的长度为 3。在下图所示的示例中，数组具有 2 个轴。第一个轴的长度为 2，第二个轴的长度为 3。

[[1., 0., 0.],
 [0., 1., 2.]]
NumPy 的数组类名为 ndarray。它也以别名 array 著称。请注意，numpy.array 与标准 Python 库中的 array.array 类不同，后者只处理一维数组，功能较少。ndarray 对象更重要的属性是

ndarray.ndim
数组的轴（维度）数量。

ndarray.shape
数组的维度。这是一个整数元组，指示数组在每个维度上的大小。对于一个具有 n 行 m 列的矩阵，shape 将是 (n,m)。shape 元组的长度因此是轴的数量，即 ndim。

ndarray.size
数组的元素总数。这等于 shape 中元素的乘积。

ndarray.dtype
描述数组中元素类型的对象。可以使用标准 Python 类型创建或指定 dtype。此外，NumPy 提供自己的类型。numpy.int32、numpy.int16 和 numpy.float64 是一些示例。

ndarray.itemsize
数组中每个元素的字节大小。例如，一个类型为 float64 的数组，其 itemsize 为 8 (=64/8)，而类型为 complex32 的数组，其 itemsize 为 4 (=32/8)。它等同于 ndarray.dtype.itemsize。

ndarray.data
包含数组实际元素的缓冲区。通常，我们不需要使用此属性，因为我们将使用索引工具访问数组中的元素。