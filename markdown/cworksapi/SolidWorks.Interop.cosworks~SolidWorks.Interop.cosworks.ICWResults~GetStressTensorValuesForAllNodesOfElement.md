---
title: "GetStressTensorValuesForAllNodesOfElement Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetStressTensorValuesForAllNodesOfElement"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStressTensorValuesForAllNodesOfElement.html"
---

# GetStressTensorValuesForAllNodesOfElement Method (ICWResults)

Gets the stress tensor values for all nodes of the specified mesh elements at the specified solution step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStressTensorValuesForAllNodesOfElement( _
   ByVal ElementNumbers As System.Object, _
   ByVal NUnits As System.Integer, _
   ByVal NStepNum As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim ElementNumbers As System.Object
Dim NUnits As System.Integer
Dim NStepNum As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetStressTensorValuesForAllNodesOfElement(ElementNumbers, NUnits, NStepNum, ErrorCode)
```

### C#

```csharp
System.object GetStressTensorValuesForAllNodesOfElement(
   System.object ElementNumbers,
   System.int NUnits,
   System.int NStepNum,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetStressTensorValuesForAllNodesOfElement(
   System.Object^ ElementNumbers,
   System.int NUnits,
   System.int NStepNum,
   [Out] System.int ErrorCode
)
```

### Parameters

- `ElementNumbers`: An array of mesh element numbers for which to return nodal results; specify the element number of a single element (see Remarks)
- `NUnits`: Units as defined in [swsStrengthUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStrengthUnit_e.html)
- `NStepNum`: Solution step number (use 1 for steady state)
- `ErrorCode`: Error as defined in [swsNodalResultsOfElementError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsNodalResultsOfElementError_e.html)

### Return Value

Two-dimensional array of tensor stress values (see **Remarks**)

## VBA Syntax

See [CWResults::GetStressTensorValuesForAllNodesOfElement](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetStressTensorValuesForAllNodesOfElement.html).

## Examples

[Get Stress Tensor Values For Mesh (VBA)](Get_Stress_Tensor_Values_for_Mesh_Example_VB.htm)
[Get Stress Tensor Values For Mesh (VB.NET)](Get_Stress_Tensor_Values_For_Mesh_Example_VBNET.htm)
[Get Stress Tensor Values For Mesh (C#)](Get_Stress_Tensor_Values_For_Mesh_Example_CSharp.htm)

## Remarks

This method is valid only for solid and shell meshes. Beam meshes are not supported.

Call [ICWMesh::ElementCount](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ElementCount.html) to specify ElementNumbers.

The number of rows in the returned two-dimensional array is:

```
    (n * m * p)
```

where:

- `n` = # elements in the mesh
- `m` = # nodes for each element
- `p =` 2 for shell meshes (top and bottom faces); 1 for solid meshes

Each row contains nine values:

```
    element_i, shell_face_i, node_i, tensor_value_1, tensor_value_2, tensor_value_3, tensor_value_4, tensor_value_5, tensor_value_6
```

where:

- `element_i` = the zero-based index of the element in the mesh
- `shell_face_i` = 0 for the top face of a shell mesh, 1 for the bottom face of a shell mesh, and -1 for a solid mesh
- `node_i` = the zero-based index of the node for this row's element

Therefore, the array returned for a shell mesh contains 18*`n`*`m` values in the following order:

```
[
```

```
   element_1, shell_face_0, node_1, tensor_value_1, tensor_value_2, tensor_value_3, tensor_value_4, tensor_value_5, tensor_value_6
```

```
   element_1, shell_face_0, node_2, tensor_value_1, tensor_value_2, tensor_value_3, tensor_value_4, tensor_value_5, tensor_value_6
```

```
   ...
```

```
   element_1, shell_face_0, node_m, tensor_value_1, tensor_value_2, tensor_value_3, tensor_value_4, tensor_value_5, tensor_value_6
```

```
   (repeat above for shell_face_1)
```

```
   (repeat above for element_2 through element_n)
```

```
]
```

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetStressForEntities3 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStressForEntities3.html)
[ICWResults::GetStressComponentForAllStepsAtNode Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStressComponentForAllStepsAtNode.html)
[ICWResults::GetStress Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStress.html)
[ICWResults::GetMinMaxStress Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxStress.html)

## Availability

SOLIDWORKS Simulation API 2016 SP05
