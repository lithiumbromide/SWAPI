---
title: "IGetPartingLines Method (IDraftFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData2"
member: "IGetPartingLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~IGetPartingLines.html"
---

# IGetPartingLines Method (IDraftFeatureData2)

Gets the parting lines that define this draft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPartingLines( _
   ByVal Count As System.Short _
) As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData2
Dim Count As System.Short
Dim value As Edge

value = instance.IGetPartingLines(Count)
```

### C#

```csharp
Edge IGetPartingLines(
   System.short Count
)
```

### C++/CLI

```cpp
Edge^ IGetPartingLines(
   System.short Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of parting lines

### Return Value

- in-process, unmanaged C++: Pointer to an array of [parting lines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IDraftFeatureData2::GetPartingLinesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDraftFeatureData2~GetPartingLinesCount.html) to determine the size of the returned array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.html)
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html)
[IDraftFeatureData2::ISetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~ISetPartingLines.html)
[IDraftFeatureData2::PartingLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~PartingLines.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
