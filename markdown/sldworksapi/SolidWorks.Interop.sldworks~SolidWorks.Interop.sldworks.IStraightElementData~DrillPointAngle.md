---
title: "DrillPointAngle Property (IStraightElementData)"
project: "SOLIDWORKS API Help"
interface: "IStraightElementData"
member: "DrillPointAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData~DrillPointAngle.html"
---

# DrillPointAngle Property (IStraightElementData)

Gets or sets the drill point angle of this straight hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property DrillPointAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IStraightElementData
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

See [StraightElementData::DrillPointAngle](ms-its:sldworksapivb6.chm::/sldworks~StraightElementData~DrillPointAngle.html).

## Remarks

This property is valid only if [IStraightElementData::EndShape](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData~EndShape.html) is set to [swEndShape_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndShape_e.html).swEndShape_DrillPoint and [IStraightElementData::DrillPointAngleOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData~DrillPointAngleOverride.html) is set to true.

## See Also

[IStraightElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData.html)
[IStraightElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
