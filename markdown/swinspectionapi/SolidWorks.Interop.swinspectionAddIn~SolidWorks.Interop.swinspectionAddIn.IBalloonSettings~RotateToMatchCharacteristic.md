---
title: "RotateToMatchCharacteristic Property (IBalloonSettings)"
project: "SOLIDWORKS Inspection API Help"
interface: "IBalloonSettings"
member: "RotateToMatchCharacteristic"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings~RotateToMatchCharacteristic.html"
---

# RotateToMatchCharacteristic Property (IBalloonSettings)

Gets and sets whether to rotate this balloon to match the angle of the characteristic.

## Syntax

### Visual Basic (Declaration)

```vb
Property RotateToMatchCharacteristic As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonSettings
Dim value As System.Boolean

instance.RotateToMatchCharacteristic = value

value = instance.RotateToMatchCharacteristic
```

### C#

```csharp
System.bool RotateToMatchCharacteristic {get; set;}
```

### C++/CLI

```cpp
property System.bool RotateToMatchCharacteristic {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to rotate the balloon to match the characteristic's angle, false to not

## VBA Syntax

See [BalloonSettings](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~BalloonSettings_members.html) properties.

## Remarks

This property is valid only for drawings.

## See Also

[IBalloonSettings Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings.html)
[IBalloonSettings Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
