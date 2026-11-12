---
title: "KeyCharShape Property (IBalloonSettings)"
project: "SOLIDWORKS Inspection API Help"
interface: "IBalloonSettings"
member: "KeyCharShape"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings~KeyCharShape.html"
---

# KeyCharShape Property (IBalloonSettings)

Gets and sets the balloon shape for key characteristics.

## Syntax

### Visual Basic (Declaration)

```vb
Property KeyCharShape As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonSettings
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

[IBalloonSettings Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings.html)
[IBalloonSettings Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
