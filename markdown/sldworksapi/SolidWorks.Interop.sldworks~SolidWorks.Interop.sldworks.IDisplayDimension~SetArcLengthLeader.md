---
title: "SetArcLengthLeader Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SetArcLengthLeader"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetArcLengthLeader.html"
---

# SetArcLengthLeader Method (IDisplayDimension)

Sets the leader style of this arc-length dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetArcLengthLeader( _
   ByVal AutoLeader As System.Boolean, _
   ByVal LeaderType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim AutoLeader As System.Boolean
Dim LeaderType As System.Integer
Dim value As System.Integer

value = instance.SetArcLengthLeader(AutoLeader, LeaderType)
```

### C#

```csharp
System.int SetArcLengthLeader(
   System.bool AutoLeader,
   System.int LeaderType
)
```

### C++/CLI

```cpp
System.int SetArcLengthLeader(
   System.bool AutoLeader,
   System.int LeaderType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AutoLeader`: True if the leader style is automatically selected, false if the leader style is
  selected by the user
- `LeaderType`: Leader style as defined in [swArcLengthLeaderType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArcLengthLeaderType_e.html) if autoLeader is false

### Return Value

Return status:

| 0 | Command was successful, leader style values were set |
| --- | --- |
| -1 | Command failed for an unknown reason, no leader style values were set |
| -2 | Specified leader style value is not valid |

## VBA Syntax

See [DisplayDimension::SetArcLengthLeader](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SetArcLengthLeader.html).

## Remarks

The leader style of an arc length dimension is specific to each display dimension. The leader style can be parallel (the leaders are parallel to each other) or radial (the leaders are perpendicular to the extension line and would extend through the center of the arc). The style can be selected automatically by SOLIDWORKS, or specified by the user.

If the autoLeader value is passed in as True to automatically select the leader style, then SOLIDWORKS ignores the leaderStyle value.

This method applies only to arc length dimensions. It does not affect any other types of dimensions.

After using this method, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimensioin::GetArcLengthLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetArcLengthLeader.html)

## Availability

SOLIDWORKS 99, datecode 1999207
