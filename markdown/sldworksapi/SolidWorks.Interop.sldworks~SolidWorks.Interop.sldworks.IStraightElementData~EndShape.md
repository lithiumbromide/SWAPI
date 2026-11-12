---
title: "EndShape Property (IStraightElementData)"
project: "SOLIDWORKS API Help"
interface: "IStraightElementData"
member: "EndShape"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData~EndShape.html"
---

# EndShape Property (IStraightElementData)

Gets or sets the end shape for this straight hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndShape As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStraightElementData
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

See [StraightElementData::EndShape](ms-its:sldworksapivb6.chm::/sldworks~StraightElementData~EndShape.html).

## See Also

[IStraightElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData.html)
[IStraightElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData_members.html)
[IStraightElementData::DrillPointAngle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData~DrillPointAngle.html)
[IStraightElementData::DrillPointAngleOverride Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData~DrillPointAngleOverride.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
