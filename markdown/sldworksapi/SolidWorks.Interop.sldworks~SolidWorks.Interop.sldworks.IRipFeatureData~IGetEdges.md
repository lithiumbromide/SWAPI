---
title: "IGetEdges Method (IRipFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRipFeatureData"
member: "IGetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~IGetEdges.html"
---

# IGetEdges Method (IRipFeatureData)

Gets the edges for this rip feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEdges( _
   ByVal EdgeCount As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRipFeatureData
Dim EdgeCount As System.Integer
Dim value As System.Object

value = instance.IGetEdges(EdgeCount)
```

### C#

```csharp
System.object IGetEdges(
   System.int EdgeCount
)
```

### C++/CLI

```cpp
System.Object^ IGetEdges(
   System.int EdgeCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EdgeCount`: Number of edges

### Return Value

- in-process, unmanaged C++: Pointer to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) of size EdgeCount

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IRipFeatureData::GetEdgesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRipFeatureData~GetEdgesCount.html) before calling this method to get the value for EdgeCount.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRipFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.html)
[IRipFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData_members.html)
[IRipFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~ISetEdges.html)
[IRipFeatureData::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~Edges.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
