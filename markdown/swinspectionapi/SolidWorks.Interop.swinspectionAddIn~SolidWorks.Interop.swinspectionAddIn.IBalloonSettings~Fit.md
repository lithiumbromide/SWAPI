---
title: "Fit Property (IBalloonSettings)"
project: "SOLIDWORKS Inspection API Help"
interface: "IBalloonSettings"
member: "Fit"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings~Fit.html"
---

# Fit Property (IBalloonSettings)

Gets and sets the number of digits that fit in a regular characteristic balloon.

## Syntax

### Visual Basic (Declaration)

```vb
Property Fit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonSettings
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

[IBalloonSettings Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings.html)
[IBalloonSettings Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
