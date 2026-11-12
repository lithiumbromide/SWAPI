---
title: "DrillPointAngleOverride Property (IStraightTapElementData)"
project: "SOLIDWORKS API Help"
interface: "IStraightTapElementData"
member: "DrillPointAngleOverride"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~DrillPointAngleOverride.html"
---

# DrillPointAngleOverride Property (IStraightTapElementData)

Gets or sets whether to override the drill point angle of this straight tap hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property DrillPointAngleOverride As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStraightTapElementData
Dim value As System.Boolean

instance.DrillPointAngleOverride = value

value = instance.DrillPointAngleOverride
```

### C#

```csharp
System.bool DrillPointAngleOverride {get; set;}
```

### C++/CLI

```cpp
property System.bool DrillPointAngleOverride {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the drill point angle, false to not

## VBA Syntax

See [StraightTapElementData::DrillPointAngleOverride](ms-its:sldworksapivb6.chm::/sldworks~StraightTapElementData~DrillPointAngleOverride.html).

## Remarks

This property is valid only if [IStraightTapElementData::EndShape](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~EndShape.html) is set to [swEndShape_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndShape_e.html).swEndShape_DrillPoint.

## See Also

[IStraightTapElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.html)
[IStraightTapElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData_members.html)
[IStraightTapElementData::DrillPointAngle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~DrillPointAngle.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
