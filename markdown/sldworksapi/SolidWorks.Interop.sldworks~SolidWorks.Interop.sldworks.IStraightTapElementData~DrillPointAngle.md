---
title: "DrillPointAngle Property (IStraightTapElementData)"
project: "SOLIDWORKS API Help"
interface: "IStraightTapElementData"
member: "DrillPointAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~DrillPointAngle.html"
---

# DrillPointAngle Property (IStraightTapElementData)

Gets or sets the drill point angle of this straight tap hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property DrillPointAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IStraightTapElementData
Dim value As System.Double

instance.DrillPointAngle = value

value = instance.DrillPointAngle
```

### C#

```csharp
System.double DrillPointAngle {get; set;}
```

### C++/CLI

```cpp
property System.double DrillPointAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Drill point angle

## VBA Syntax

See [StraightTapElementData::DrillPointAngle](ms-its:sldworksapivb6.chm::/sldworks~StraightTapElementData~DrillPointAngle.html).

## Remarks

This property is valid only if [IStraightTapElementData::EndShape](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~EndShape.html) is set to [swEndShape_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndShape_e.html).swEndShape_DrillPoint and [IStraightTapElementData::DrillPointAngleOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~DrillPointAngleOverride.html) is set to true.

## See Also

[IStraightTapElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.html)
[IStraightTapElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
