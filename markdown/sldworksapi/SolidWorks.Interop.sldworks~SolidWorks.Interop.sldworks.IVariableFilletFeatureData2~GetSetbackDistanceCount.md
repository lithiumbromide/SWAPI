---
title: "GetSetbackDistanceCount Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "GetSetbackDistanceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackDistanceCount.html"
---

# GetSetbackDistanceCount Method (IVariableFilletFeatureData2)

Gets the number of setback distances for the specified vertex on this variable fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSetbackDistanceCount( _
   ByVal Vtx As Vertex _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim Vtx As Vertex
Dim value As System.Integer

value = instance.GetSetbackDistanceCount(Vtx)
```

### C#

```csharp
System.int GetSetbackDistanceCount(
   Vertex Vtx
)
```

### C++/CLI

```cpp
System.int GetSetbackDistanceCount(
   Vertex^ Vtx
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Vtx`: [Vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html)

### Return Value

Number of setback distances and number of edges

## VBA Syntax

See [VariableFilletFeatureData2::GetSetbackDistanceCount](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~GetSetbackDistanceCount.html).

## Remarks

Because there is a one-to-one correspondence between the edges and distances, the count argument also represents the number of edges at the specified vertex.

Call this method before calling [IVariableFilletFeatureData2::IGetSetbackVertexDistance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~IGetSetbackVertexDistance.html).

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::GetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::GetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVertices.html)
[IVariableFilletFeatureData2::GetSetbackVerticesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVerticesCount.html)
[IVariableFilletFeatureData2::IGetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetSetbackVertices.html)
[IVariableFilletFeatureData2::ISetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::SetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::SetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetSetbackVertices.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
