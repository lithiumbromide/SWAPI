---
title: "GetEdgesCount Method (IRuledSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRuledSurfaceFeatureData"
member: "GetEdgesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~GetEdgesCount.html"
---

# GetEdgesCount Method (IRuledSurfaceFeatureData)

Gets the number of edges to use as a base for this ruled-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRuledSurfaceFeatureData
Dim value As System.Integer

value = instance.GetEdgesCount()
```

### C#

```csharp
System.int GetEdgesCount()
```

### C++/CLI

```cpp
System.int GetEdgesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of edges

## VBA Syntax

See [RuledSurfaceFeatureData::GetEdgesCount](ms-its:sldworksapivb6.chm::/sldworks~RuledSurfaceFeatureData~GetEdgesCount.html).

## Remarks

Call this method before calling [IRuledSurfaceFeatureData::IGetEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRuledSurfaceFeatureData~IGetEdges.html) to get the size of the array for that method.

## See Also

[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.html)
[IRuledSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData_members.html)
[IRuledSurfaceFeatureData::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~GetEdges.html)
[IRuledSurfaceFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~ISetEdges.html)
[IRuledSurfaceFeatureData::SetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~SetEdges.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
