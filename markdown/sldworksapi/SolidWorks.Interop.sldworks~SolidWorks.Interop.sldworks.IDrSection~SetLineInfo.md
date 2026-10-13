---
title: "SetLineInfo Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "SetLineInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetLineInfo.html"
---

# SetLineInfo Method (IDrSection)

Sets the location (both position and arrow heads) of the section line.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLineInfo( _
   ByVal VLineInfo As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim VLineInfo As System.Object
Dim value As System.Boolean

value = instance.SetLineInfo(VLineInfo)
```

### C#

```csharp
System.bool SetLineInfo(
   System.object VLineInfo
)
```

### C++/CLI

```cpp
System.bool SetLineInfo(
   System.Object^ VLineInfo
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VLineInfo`: Array (see **Remarks**)

## VBA Syntax

See [DrSection::SetLineInfo](ms-its:sldworksapivb6.chm::/sldworks~DrSection~SetLineInfo.html).

## Remarks

The VLineInfo argument is an array consisting of several coordinate pairs and is of the same format as the array returned by [IDrSection::GetLineInfo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection~GetLineInfo.html). The number of coordinate pairs is determined by the number of line segments in the section line. Each coordinate pair consists of 6 doubles, the x,y,z coordinate of
each end point of the segment.

The formatted array should include the start point and end point of each line segment, including the z position even though the z position is irrelevant.

Any section line containing more than one segment contains at least one set of duplicate points. These points represent the end point of one line segment and the coincident start point of another line segment. If you change either set of points, then you must change the other set of points at the same time. These points must always be
coincident when calling this method.

To update the section view, call [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html) after calling this method.

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::IGetLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetLineInfo.html)
[IDrSection::IGetLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetLineInfo.html)
