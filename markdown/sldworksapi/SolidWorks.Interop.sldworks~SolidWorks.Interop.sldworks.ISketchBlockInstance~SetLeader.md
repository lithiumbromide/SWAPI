---
title: "SetLeader Method (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "SetLeader"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~SetLeader.html"
---

# SetLeader Method (ISketchBlockInstance)

Sets the leader style for this block instance.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLeader( _
   ByVal LeaderStyle As System.Integer, _
   ByVal ArrowHeadStyle As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim LeaderStyle As System.Integer
Dim ArrowHeadStyle As System.Integer
Dim value As System.Boolean

value = instance.SetLeader(LeaderStyle, ArrowHeadStyle)
```

### C#

```csharp
System.bool SetLeader(
   System.int LeaderStyle,
   System.int ArrowHeadStyle
)
```

### C++/CLI

```cpp
System.bool SetLeader(
   System.int LeaderStyle,
   System.int ArrowHeadStyle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LeaderStyle`: Leader style as defined in [swLeaderStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderStyle_e.html)
- `ArrowHeadStyle`: Arrowhead style as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

### Return Value

True if the leader style is set, false if not

## VBA Syntax

See [SketchBlockInstance::SetLeader](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~SetLeader.html).

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)
[ISketchBlockInstance::GetArrowHeadStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetArrowHeadStyle.html)
[ISketchBlockInstance::GetLeaderPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetLeaderPoints.html)
[ISketchBlockInstance::GetLeaderStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetLeaderStyle.html)
[ISketchBlockInstance::IGetLeaderPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~IGetLeaderPoints.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
