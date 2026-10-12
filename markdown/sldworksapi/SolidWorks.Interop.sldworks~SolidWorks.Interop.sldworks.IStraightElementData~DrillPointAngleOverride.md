---
title: "DrillPointAngleOverride Property (IStraightElementData)"
project: "SOLIDWORKS API Help"
interface: "IStraightElementData"
member: "DrillPointAngleOverride"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData~DrillPointAngleOverride.html"
---

# DrillPointAngleOverride Property (IStraightElementData)

Gets or sets whether to override the drill point angle of this straight hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property DrillPointAngleOverride As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStraightElementData
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

See [StraightElementData::DrillPointAngleOverride](ms-its:sldworksapivb6.chm::/sldworks~StraightElementData~DrillPointAngleOverride.html).

## Remarks

This property is valid only if [IStraightElementData::EndShape](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData~EndShape.html) is set to [swEndShape_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndShape_e.html).swEndShape_DrillPoint.

## See Also

[IStraightElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData.html)
[IStraightElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData_members.html)
[IStraightElementData::DrillPointAngle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~DrillPointAngle.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
