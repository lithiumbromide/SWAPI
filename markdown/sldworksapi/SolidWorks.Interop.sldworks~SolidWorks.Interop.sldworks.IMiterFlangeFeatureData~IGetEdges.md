---
title: "IGetEdges Method (IMiterFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMiterFlangeFeatureData"
member: "IGetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~IGetEdges.html"
---

# IGetEdges Method (IMiterFlangeFeatureData)

Gets the edges for this miter flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEdges() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMiterFlangeFeatureData
Dim value As System.Object

value = instance.IGetEdges()
```

### C#

```csharp
System.object IGetEdges()
```

### C++/CLI

```cpp
System.Object^ IGetEdges();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) used to define the miter flange feature

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.html)
[IMiterFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData_members.html)
[IMiterFlangeFeatureData::IGetEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~IGetEdgesCount.html)
[IMiterFlangeFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~ISetEdges.html)
[IMiterFlangeFeatureData::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~Edges.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
