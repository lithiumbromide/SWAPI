---
title: "Shape Property (BalloonSettings)"
project: "SOLIDWORKS Inspection API Help"
interface: "BalloonSettings"
member: "Shape"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.BalloonSettings~Shape.html"
---

# Shape Property (BalloonSettings)

Gets and sets the balloon shape for regular characteristics.

## Syntax

### Visual Basic (Declaration)

```vb
Property Shape As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As BalloonSettings
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

[BalloonSettings Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.BalloonSettings.html)
[BalloonSettings Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.BalloonSettings_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
