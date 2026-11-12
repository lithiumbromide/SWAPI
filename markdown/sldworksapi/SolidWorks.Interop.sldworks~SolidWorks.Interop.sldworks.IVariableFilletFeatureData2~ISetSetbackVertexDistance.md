---
title: "ISetSetbackVertexDistance Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "ISetSetbackVertexDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetSetbackVertexDistance.html"
---

# ISetSetbackVertexDistance Method (IVariableFilletFeatureData2)

Sets the setback distance for the specified vertex and its edges on this variable fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetSetbackVertexDistance( _
   ByVal Count As System.Integer, _
   ByVal Vtx As Vertex, _
   ByRef EdgeArr As Edge, _
   ByRef DistArr As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim Count As System.Integer
Dim Vtx As Vertex
Dim EdgeArr As Edge
Dim DistArr As System.Double
Dim value As System.Boolean

value = instance.ISetSetbackVertexDistance(Count, Vtx, EdgeArr, DistArr)
```

### C#

```csharp
System.bool ISetSetbackVertexDistance(
   System.int Count,
   Vertex Vtx,
   ref Edge EdgeArr,
   ref System.double DistArr
)
```

### C++/CLI

```cpp
System.bool ISetSetbackVertexDistance(
   System.int Count,
   Vertex^ Vtx,
   Edge^% EdgeArr,
   System.double% DistArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of setback distances
- `Vtx`: [Vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) for which to set the setback distance
- `EdgeArr`: - in-process, unmanaged C++: Pointer to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) at the specified vertex (see **Remarks**)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `DistArr`: - in-process, unmanaged C++: Pointer to an array of setback distances at the specified

  VBA, VB.NET, C#, and C++/CLI: Not supported

### Return Value

TRUE if setback distance is set, FALSE if not

## VBA Syntax

See [VariableFilletFeatureData2::ISetSetbackVertexDistance](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~ISetSetbackVertexDistance.html).

## Remarks

There is a one-to-one correspondence between the edge array and the distance array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::SetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::SetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetSetbackVertices.html)
[IVariableFilletFeatureData2::ISetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetSetbackVertices.html)
[IVariableFilletFeatureData2::GetSetbackDistanceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackDistanceCount.html)
[IVariableFilletFeatureData2::GetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::GetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVertices.html)
[IVariableFilletFeatureData2::GetSetbackVerticesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVerticesCount.html)
[IVariableFilletFeatureData2::IGetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::IGetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetSetbackVertices.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
