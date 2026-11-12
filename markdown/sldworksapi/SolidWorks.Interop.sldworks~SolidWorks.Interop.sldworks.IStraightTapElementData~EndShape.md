---
title: "EndShape Property (IStraightTapElementData)"
project: "SOLIDWORKS API Help"
interface: "IStraightTapElementData"
member: "EndShape"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~EndShape.html"
---

# EndShape Property (IStraightTapElementData)

Gets or sets the end shape for this straight tap hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndShape As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStraightTapElementData
Dim value As System.Integer

instance.EndShape = value

value = instance.EndShape
```

### C#

```csharp
System.int EndShape {get; set;}
```

### C++/CLI

```cpp
property System.int EndShape {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

End shape as defined in [swEndShape_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndShape_e.html)

## VBA Syntax

See [StraightTapElementData::EndShape](ms-its:sldworksapivb6.chm::/sldworks~StraightTapElementData~EndShape.html).

## See Also

[IStraightTapElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.html)
[IStraightTapElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData_members.html)
[IStraightTapElementData::DrillPointAngle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~DrillPointAngle.html)
[IStraightTapElementData::DrillPointAngleOverride Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~DrillPointAngleOverride.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
