---
title: "ISetPartingLines Method (IPartingSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingSurfaceFeatureData"
member: "ISetPartingLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~ISetPartingLines.html"
---

# ISetPartingLines Method (IPartingSurfaceFeatureData)

Sets the parting lines for this parting surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetPartingLines( _
   ByVal Count As System.Integer, _
   ByRef EntIn As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingSurfaceFeatureData
Dim Count As System.Integer
Dim EntIn As System.Object

instance.ISetPartingLines(Count, EntIn)
```

### C#

```csharp
void ISetPartingLines(
   System.int Count,
   ref System.object EntIn
)
```

### C++/CLI

```cpp
void ISetPartingLines(
   System.int Count,
   System.Object^% EntIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of parting lines
- `EntIn`: - in-process, unmanaged C++: Pointer to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) or [parting-line features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartingLineFeatureData.html) used as parting lines

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.html)
[IPartingSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData_members.html)
[IPartingSurfaceFeatureData::GetPartingLinesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~GetPartingLinesCount.html)
[IPartingSurfaceFeatureData::GetPartingLinesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~GetPartingLinesType.html)
[IPartingSurfaceFeatureData::IGetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~IGetPartingLines.html)
[IPartingSurfaceFeatureData::PartingLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~PartingLines.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
