---
title: "KeyCharFit Property (IBalloonSettings)"
project: "SOLIDWORKS Inspection API Help"
interface: "IBalloonSettings"
member: "KeyCharFit"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings~KeyCharFit.html"
---

# KeyCharFit Property (IBalloonSettings)

Gets and sets the number of digits that fit in a key characteristic balloon.

## Syntax

### Visual Basic (Declaration)

```vb
Property KeyCharFit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonSettings
Dim value As System.Integer

instance.KeyCharFit = value

value = instance.KeyCharFit
```

### C#

```csharp
System.int KeyCharFit {get; set;}
```

### C++/CLI

```cpp
property System.int KeyCharFit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Number of digits that fit as defined by [swiBalloonSettingsFit_e](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.swiBalloonSettingsFit_e.html)

## VBA Syntax

See [BalloonSettings](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~BalloonSettings_members.html) properties.

## Remarks

Key characteristics are characteristics whose variation has a significant impact on the quality of the part.

## See Also

[IBalloonSettings Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings.html)
[IBalloonSettings Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
