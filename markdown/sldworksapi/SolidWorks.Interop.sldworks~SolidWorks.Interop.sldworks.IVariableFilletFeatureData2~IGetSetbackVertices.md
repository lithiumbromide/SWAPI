---
title: "IGetSetbackVertices Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "IGetSetbackVertices"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetSetbackVertices.html"
---

# IGetSetbackVertices Method (IVariableFilletFeatureData2)

Gets the setback vertices for this variable fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSetbackVertices( _
   ByVal Count As System.Integer _
) As Vertex
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim Count As System.Integer
Dim value As Vertex

value = instance.IGetSetbackVertices(Count)
```

### C#

```csharp
Vertex IGetSetbackVertices(
   System.int Count
)
```

### C++/CLI

```cpp
Vertex^ IGetSetbackVertices(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of setback vertices

### Return Value

- in-process, unmanaged C++: Pointer to an array of setback [vertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IVariableFilletFeatureData2::GetSetbackVerticesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVerticesCount.html).

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::GetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVertices.html)
[IVariableFilletFeatureData2::GetSetbackDistanceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackDistanceCount.html)
[IVariableFilletFeatureData2::GetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::IGetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::ISetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::ISetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetSetbackVertices.html)
[IVariableFilletFeatureData2::SetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetSetbackVertexDistance.html)
[IVariableFilletFeatureData2::SetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetSetbackVertices.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
