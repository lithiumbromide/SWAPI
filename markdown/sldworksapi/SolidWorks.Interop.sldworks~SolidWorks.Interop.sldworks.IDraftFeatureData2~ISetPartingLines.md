---
title: "ISetPartingLines Method (IDraftFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData2"
member: "ISetPartingLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~ISetPartingLines.html"
---

# ISetPartingLines Method (IDraftFeatureData2)

Sets the parting lines for this draft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetPartingLines( _
   ByVal Count As System.Short, _
   ByRef LineArray As Edge _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData2
Dim Count As System.Short
Dim LineArray As Edge

instance.ISetPartingLines(Count, LineArray)
```

### C#

```csharp
void ISetPartingLines(
   System.short Count,
   ref Edge LineArray
)
```

### C++/CLI

```cpp
void ISetPartingLines(
   System.short Count,
   Edge^% LineArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of parting lines
- `LineArray`: - in-process, unmanaged C++: Pointer to an array of [parting lines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.html)
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html)
[IDraftFeatureData2::GetPartingLinesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetPartingLinesCount.html)
[IDraftFeatureData2::IGetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~IGetPartingLines.html)
[IDraftFeatureData2::PartingLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~PartingLines.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
