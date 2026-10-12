---
title: "Shape Property (IBalloonSettings)"
project: "SOLIDWORKS Inspection API Help"
interface: "IBalloonSettings"
member: "Shape"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings~Shape.html"
---

# Shape Property (IBalloonSettings)

Gets and sets the balloon shape for regular characteristics.

## Syntax

### Visual Basic (Declaration)

```vb
Property Shape As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonSettings
Dim value As System.Integer

instance.Shape = value

value = instance.Shape
```

### C#

```csharp
System.int Shape {get; set;}
```

### C++/CLI

```cpp
property System.int Shape {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Balloon shape as defined by [swiBalloonSettingsShape_e](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.swiBalloonSettingsShape_e.html)

## VBA Syntax

See [BalloonSettings](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~BalloonSettings_members.html) properties.

## See Also

[IBalloonSettings Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings.html)
[IBalloonSettings Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
