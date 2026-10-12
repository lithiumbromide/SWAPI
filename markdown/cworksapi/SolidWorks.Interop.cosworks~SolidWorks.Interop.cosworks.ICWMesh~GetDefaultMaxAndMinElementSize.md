---
title: "GetDefaultMaxAndMinElementSize Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetDefaultMaxAndMinElementSize"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetDefaultMaxAndMinElementSize.html"
---

# GetDefaultMaxAndMinElementSize Method (ICWMesh)

Gets the default maximum and minimum element sizes used for boundaries in a curvature-based mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetDefaultMaxAndMinElementSize( _
   ByVal NUnits As System.Integer, _
   ByRef DMaxElementSize As System.Double, _
   ByRef DMinElementSize As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim NUnits As System.Integer
Dim DMaxElementSize As System.Double
Dim DMinElementSize As System.Double

instance.GetDefaultMaxAndMinElementSize(NUnits, DMaxElementSize, DMinElementSize)
```

### C#

```csharp
void GetDefaultMaxAndMinElementSize(
   System.int NUnits,
   out System.double DMaxElementSize,
   out System.double DMinElementSize
)
```

### C++/CLI

```cpp
void GetDefaultMaxAndMinElementSize(
   System.int NUnits,
   [Out] System.double DMaxElementSize,
   [Out] System.double DMinElementSize
)
```

### Parameters

- `NUnits`: Mesh linear units as defined [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)
- `DMaxElementSize`: Maximum element size used for boundaries with lowest curvature
- `DMinElementSize`: Minimum element size used for boundaries with highest curvature

## VBA Syntax

See [CWMesh::GetDefaultMaxAndMinElementSize](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetDefaultMaxAndMinElementSize.html).

## Examples

[Create Curvature-based Mesh (C#)](Create_Curvature-based_Mesh_Example_CSharp.htm)
[Create Curvature-based Mesh (VB.NET)](Create_Curvature-based_Mesh_Example_VBNET.htm)
[Create Curvature-based Mesh (VBA)](Create_Curvature-based_Mesh_Example_VB.htm)

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GrowthRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GrowthRatio.html)
[ICWMesh::MaxElementSize Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MaxElementSize.html)
[ICWMesh::MinElementSize Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MinElementSize.html)
[ICWMesh::MinElementsInCircle Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MinElementsInCircle.html)
[ICWMesh::MesherType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MesherType.html)

## Availability

SOLIDWORKS Simulation API 2011 SP0
