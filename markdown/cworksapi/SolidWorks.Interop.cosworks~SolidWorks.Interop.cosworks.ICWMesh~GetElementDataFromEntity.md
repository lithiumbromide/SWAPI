---
title: "GetElementDataFromEntity Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetElementDataFromEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElementDataFromEntity.html"
---

# GetElementDataFromEntity Method (ICWMesh)

Gets the element associated with an entity.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetElementDataFromEntity( _
   ByVal DispEntity As System.Object, _
   ByRef NCount As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim DispEntity As System.Object
Dim NCount As System.Integer
Dim value As System.Object

value = instance.GetElementDataFromEntity(DispEntity, NCount)
```

### C#

```csharp
System.object GetElementDataFromEntity(
   System.object DispEntity,
   out System.int NCount
)
```

### C++/CLI

```cpp
System.Object^ GetElementDataFromEntity(
   System.Object^ DispEntity,
   [Out] System.int NCount
)
```

### Parameters

- `DispEntity`: Entity
- `NCount`: Number of elements

### Return Value

Array of element data (see **Remarks**)

## VBA Syntax

See [CWMesh::GetElementDataFromEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetElementDataFromEntity.html).

## Remarks

Array of element data:

[

`E1, N1E1, N2E1, N3E1, N4E1, N5E1, N6E1, N7E1, N8E1, N9E1, N10E1, X1, Y1, Z1, AR1, JR1,`

`E2, N1E2, N2E2, N3E2, N4E2, N5E2, N6E2, N7E2, N8E2, N9E2, N10E2, X2, Y2, Z2, AR2, JR2,`

`...,`

`Ei, N1Ei, N2Ei, N3Ei, N4Ei, N5Ei, N6Ei, N7Ei, N8Ei, N9Ei, N10Ei, Xi, Yi, Zi, ARi, JRi`

]

where:

- E`i` = `i`th element number
- N1E`i` to N10E`i` = Node numbers associated with element E`i`; returns 10 node numbers for higher order solid elements; returns -1 for shells and lower order meshes.
- X`i`, Y`i`, Z`i` = x, y and z coordinates of center of E`i`
- AR`i` = Aspect ratio for element E`i`
- JR`i` = Jacobian ratio for element E`i`; returns -1 if not applicable

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetDefaultElementSizeAndTolerance Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetDefaultElementSizeAndTolerance.html)
[ICWMesh::GetElementLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElementLocation.html)
[ICWMesh::GetElements Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElements.html)
[ICWMesh::ElementCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ElementCount.html)
[ICWMesh::ElementSize Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ElementSize.html)
[ICWMesh::MinElementsInCircle Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MinElementsInCircle.html)
[ICWMesh::MaxAspectRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MaxAspectRatio.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
