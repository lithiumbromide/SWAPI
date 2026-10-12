---
title: "IGetPartingLines Method (IPartingLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingLineFeatureData"
member: "IGetPartingLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~IGetPartingLines.html"
---

# IGetPartingLines Method (IPartingLineFeatureData)

Gets the edges used as parting lines.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPartingLines( _
   ByVal Count As System.Integer _
) As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingLineFeatureData
Dim Count As System.Integer
Dim value As Edge

value = instance.IGetPartingLines(Count)
```

### C#

```csharp
Edge IGetPartingLines(
   System.int Count
)
```

### C++/CLI

```cpp
Edge^ IGetPartingLines(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of edges used as parting lines

### Return Value

- in-process, unmanaged C++: Pointer to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) used as parting lines of size Count
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IPartingLineFeatureData::GetPartingLinesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartingLineFeatureData~GetPartingLinesCount.html) before calling this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.html)
[IPartingLineFeatureData::ISetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~ISetPartingLines.html)
[IPartingLineFeatureData::PartingLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PartingLines.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
