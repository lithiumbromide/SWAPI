---
title: "KeyCharPrefix Property (IBalloonSettings)"
project: "SOLIDWORKS Inspection API Help"
interface: "IBalloonSettings"
member: "KeyCharPrefix"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings~KeyCharPrefix.html"
---

# KeyCharPrefix Property (IBalloonSettings)

Gets and sets the prefix to add to the balloons for key characteristics.

## Syntax

### Visual Basic (Declaration)

```vb
Property KeyCharPrefix As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonSettings
Dim value As System.String

instance.KeyCharPrefix = value

value = instance.KeyCharPrefix
```

### C#

```csharp
System.string KeyCharPrefix {get; set;}
```

### C++/CLI

```cpp
property System.String^ KeyCharPrefix {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Prefix

## VBA Syntax

See [BalloonSettings](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~BalloonSettings_members.html) properties.

## Remarks

Key characteristics are characteristics whose variation has a significant impact on the quality of the part.

## See Also

[IBalloonSettings Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings.html)
[IBalloonSettings Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
