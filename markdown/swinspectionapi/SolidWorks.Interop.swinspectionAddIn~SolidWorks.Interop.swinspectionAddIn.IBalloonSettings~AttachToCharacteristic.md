---
title: "AttachToCharacteristic Property (IBalloonSettings)"
project: "SOLIDWORKS Inspection API Help"
interface: "IBalloonSettings"
member: "AttachToCharacteristic"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings~AttachToCharacteristic.html"
---

# AttachToCharacteristic Property (IBalloonSettings)

Gets and sets whether to attach this balloon to each characteristic (item extracted from the drawing).

## Syntax

### Visual Basic (Declaration)

```vb
Property AttachToCharacteristic As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonSettings
Dim value As System.Boolean

instance.AttachToCharacteristic = value

value = instance.AttachToCharacteristic
```

### C#

```csharp
System.bool AttachToCharacteristic {get; set;}
```

### C++/CLI

```cpp
property System.bool AttachToCharacteristic {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to attach this balloon to each characteristic, false to not

## VBA Syntax

See [BalloonSettings](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~BalloonSettings_members.html) properties.

## Remarks

This property is valid only for drawings.

If this property is set to true, then when the balloon moves the dimension characteristic moves with it.

## See Also

[IBalloonSettings Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings.html)
[IBalloonSettings Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
