---
title: "KeyCharPrefix Property (BalloonSettings)"
project: "SOLIDWORKS Inspection API Help"
interface: "BalloonSettings"
member: "KeyCharPrefix"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.BalloonSettings~KeyCharPrefix.html"
---

# KeyCharPrefix Property (BalloonSettings)

Gets and sets the prefix to add to the balloons for key characteristics.

## Syntax

### Visual Basic (Declaration)

```vb
Property KeyCharPrefix As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As BalloonSettings
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

[BalloonSettings Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.BalloonSettings.html)
[BalloonSettings Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.BalloonSettings_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
