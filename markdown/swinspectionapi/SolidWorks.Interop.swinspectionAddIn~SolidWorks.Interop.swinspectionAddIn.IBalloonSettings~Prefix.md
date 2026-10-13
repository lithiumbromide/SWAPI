---
title: "Prefix Property (IBalloonSettings)"
project: "SOLIDWORKS Inspection API Help"
interface: "IBalloonSettings"
member: "Prefix"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings~Prefix.html"
---

# Prefix Property (IBalloonSettings)

Gets and sets the prefix to add to the balloons of regular characteristics.

## Syntax

### Visual Basic (Declaration)

```vb
Property Prefix As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonSettings
Dim value As System.String

instance.Prefix = value

value = instance.Prefix
```

### C#

```csharp
System.string Prefix {get; set;}
```

### C++/CLI

```cpp
property System.String^ Prefix {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Prefix

## VBA Syntax

See [BalloonSettings](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~BalloonSettings_members.html) properties.

## See Also

[IBalloonSettings Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings.html)
[IBalloonSettings Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
