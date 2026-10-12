---
title: "IGetSetbackVertexDistance Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "IGetSetbackVertexDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetSetbackVertexDistance.html"
---

# IGetSetbackVertexDistance Method (IVariableFilletFeatureData2)

Gets the setback distance for the specified vertex on this variable fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSetbackVertexDistance( _
   ByVal Count As System.Integer, _
   ByVal Vtx As Vertex, _
   ByRef EdgeArr As Edge _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim Count As System.Integer
Dim Vtx As Vertex
Dim EdgeArr As Edge
Dim value As System.Double

value = instance.IGetSetbackVertexDistance(Count, Vtx, EdgeArr)
```

### C#

```csharp
System.double IGetSetbackVertexDistance(
   System.int Count,
   Vertex Vtx,
   out Edge EdgeArr
)
```

### C++/CLI

```cpp
System.double IGetSetbackVertexDistance(
   System.int Count,
   Vertex^ Vtx,
   [Out] Edge^ EdgeArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of edges and setback distances for this vertex
- `Vtx`: [Vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) for which to get setback distance
- `EdgeArr`: - in-process, unmanaged C++: Pointer to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) at the specified vertex (see **Remarks**)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

- in-process, unmanaged C++: Pointer to an array of setback distances at the specified

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

There is a one-to-one correspondence between the edge array and the setback distance array.

Before calling this method, call [IVariableFilletFeatureData2::GetSetbackDistanceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackDistanceCount.html) to get the number of edges and setback distances at the specified vertex.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::GetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::GetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVertices.html)
[IVariableFilletFeatureData2::IGetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetSetbackVertices.html)
[IVariableFilletFeatureData2::ISetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::ISetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetSetbackVertices.html)
[IVariableFilletFeatureData2::SetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::SetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetSetbackVertices.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
