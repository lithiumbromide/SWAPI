---
title: "Fit Property (BalloonSettings)"
project: "SOLIDWORKS Inspection API Help"
interface: "BalloonSettings"
member: "Fit"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.BalloonSettings~Fit.html"
---

# Fit Property (BalloonSettings)

Gets and sets the number of digits that fit in a regular characteristic balloon.

## Syntax

### Visual Basic (Declaration)

```vb
Property Fit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As BalloonSettings
Dim value As System.Integer

instance.Fit = value

value = instance.Fit
```

### C#

```csharp
System.int Fit {get; set;}
```

### C++/CLI

```cpp
property System.int Fit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Number of digits that fit as defined by [swiBalloonSettingsFit_e](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.swiBalloonSettingsFit_e.html)

## VBA Syntax

See [BalloonSettings](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~BalloonSettings_members.html) properties.

## See Also

[BalloonSettings Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.BalloonSettings.html)
[BalloonSettings Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.BalloonSettings_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
