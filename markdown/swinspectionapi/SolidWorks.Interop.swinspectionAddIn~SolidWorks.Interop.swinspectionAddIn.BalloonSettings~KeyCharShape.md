---
title: "KeyCharShape Property (BalloonSettings)"
project: "SOLIDWORKS Inspection API Help"
interface: "BalloonSettings"
member: "KeyCharShape"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.BalloonSettings~KeyCharShape.html"
---

# KeyCharShape Property (BalloonSettings)

Gets and sets the balloon shape for key characteristics.

## Syntax

### Visual Basic (Declaration)

```vb
Property KeyCharShape As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As BalloonSettings
Dim value As System.Integer

instance.KeyCharShape = value

value = instance.KeyCharShape
```

### C#

```csharp
System.int KeyCharShape {get; set;}
```

### C++/CLI

```cpp
property System.int KeyCharShape {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Balloon shape as defined by [swiBalloonSettingsShape_e](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.swiBalloonSettingsShape_e.html)

## VBA Syntax

See [BalloonSettings](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~BalloonSettings_members.html) properties.

## Remarks

Key characteristics are characteristics whose variation has a significant impact on the quality of the part.

## See Also

[BalloonSettings Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.BalloonSettings.html)
[BalloonSettings Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.BalloonSettings_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
