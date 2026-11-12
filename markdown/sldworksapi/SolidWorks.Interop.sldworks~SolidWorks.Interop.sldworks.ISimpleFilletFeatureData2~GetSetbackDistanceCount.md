---
title: "GetSetbackDistanceCount Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "GetSetbackDistanceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackDistanceCount.html"
---

# GetSetbackDistanceCount Method (ISimpleFilletFeatureData2)

Gets the number of setback distances for the specified vertex on this simple fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSetbackDistanceCount( _
   ByVal Vtx As Vertex _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
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

See [SimpleFilletFeatureData2::GetSetbackDistanceCount](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~GetSetbackDistanceCount.html).

## Remarks

Because there is a one-to-one correspondence between the edges and distances, the Count argument also represents the number of edges at the specified vertex.

Call this method before calling [ISimpleFilletFeatureData2::IGetSetbackVertexDistance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~IGetSetbackVertexDistance.html) to get the number setback distances and number of edges for the vertex.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackVertexDistance.html)
[ISimpleFilletFeatureData2::GetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackVertices.html)
[ISimpleFilletFeatureData2::GetSetbackVerticesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackVerticesCount.html)
[ISimpleFilletFeatureData2::IGetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetSetbackVertices.html)
[ISimpleFilletFeatureData2::ISetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetSetbackVertexDistance.html)
[ISimpleFilletFeatureData2::ISetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetSetbackVertices.html)
[ISimpleFilletFeatureData2::SetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetSetbackVertexDistance.html)
[ISimpleFilletFeatureData2::SetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetSetbackVertices.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
