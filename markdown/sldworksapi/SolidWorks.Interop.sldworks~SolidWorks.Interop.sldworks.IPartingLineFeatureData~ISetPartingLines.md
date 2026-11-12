---
title: "ISetPartingLines Method (IPartingLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingLineFeatureData"
member: "ISetPartingLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~ISetPartingLines.html"
---

# ISetPartingLines Method (IPartingLineFeatureData)

Sets the edges to use as parting lines.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetPartingLines( _
   ByVal Count As System.Integer, _
   ByRef EntIn As Edge _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingLineFeatureData
Dim Count As System.Integer
Dim EntIn As Edge

instance.ISetPartingLines(Count, EntIn)
```

### C#

```csharp
void ISetPartingLines(
   System.int Count,
   ref Edge EntIn
)
```

### C++/CLI

```cpp
void ISetPartingLines(
   System.int Count,
   Edge^% EntIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of edges to use as parting lines
- `EntIn`: - in-process, unmanaged C++: Poitner to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) to use as parting lines of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.html)
[IPartingLineFeatureData::PartingLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PartingLines.html)
[IPartingLineFeatureData::IGetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~IGetPartingLines.html)
[IPartingLineFeatureData::GetPartingLinesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetPartingLinesCount.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
