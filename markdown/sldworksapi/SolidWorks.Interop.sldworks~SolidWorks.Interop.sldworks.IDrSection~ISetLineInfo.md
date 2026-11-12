---
title: "ISetLineInfo Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "ISetLineInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ISetLineInfo.html"
---

# ISetLineInfo Method (IDrSection)

Sets the location (both position and arrow heads) of the section line.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetLineInfo( _
   ByVal Count As System.Integer, _
   ByRef PLineInfo As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim Count As System.Integer
Dim PLineInfo As System.Double
Dim value As System.Boolean

value = instance.ISetLineInfo(Count, PLineInfo)
```

### C#

```csharp
System.bool ISetLineInfo(
   System.int Count,
   ref System.double PLineInfo
)
```

### C++/CLI

```cpp
System.bool ISetLineInfo(
   System.int Count,
   System.double% PLineInfo
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of the point coordinates of the section line
- `PLineInfo`: - in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if the location is set, false if not

## Remarks

The PLineInfo argument is an array consisting of several coordinate pairs and is of the same format as the array returned by [IDrSection::IGetLineInfo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection~IGetLineInfo.html). The number of coordinate pairs is determined by the number of line segments in the section line. Each coordinate pair consists of 6 doubles, the x,y,z coordinate of
each end point of the segment.

The formatted array should include the start point and end point of each line segment, including the z position even though the z position is irrelevant.

Any section line containing more than one segment contains at least one set of duplicate points. These points represent the end point of one line segment and the coincident start point of another line segment. If you change either set of points, then you must change the other set of points at the same time. These points must always be
coincident when calling this method.

To update the section view, call [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html) after calling this method.

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::SetLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetLineInfo.html)
[IDrSection::GetLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetLineInfo.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
