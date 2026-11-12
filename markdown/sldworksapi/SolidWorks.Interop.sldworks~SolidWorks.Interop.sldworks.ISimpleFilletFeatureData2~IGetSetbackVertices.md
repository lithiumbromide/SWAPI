---
title: "IGetSetbackVertices Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "IGetSetbackVertices"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetSetbackVertices.html"
---

# IGetSetbackVertices Method (ISimpleFilletFeatureData2)

Gets the setback vertices for this simple fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSetbackVertices( _
   ByVal Count As System.Integer _
) As Vertex
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
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

Before calling this method, call [ISimpleFilletFeatureData2::GetSetbackVerticesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackVerticesCount.html) to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetSetbackDistanceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackDistanceCount.html)
[ISimpleFilletFeatureData2::GetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackVertexDistance.html)
[ISimpleFilletFeatureData2::GetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackVertices.html)
[ISimpleFilletFeatureData2::IGetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetSetbackVertexDistance.html)
[ISimpleFilletFeatureData2::ISetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetSetbackVertexDistance.html)
[ISimpleFilletFeatureData2::ISetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetSetbackVertices.html)
[ISimpleFilletFeatureData2::SetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetSetbackVertexDistance.html)
[ISimpleFilletFeatureData2::SetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetSetbackVertices.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
