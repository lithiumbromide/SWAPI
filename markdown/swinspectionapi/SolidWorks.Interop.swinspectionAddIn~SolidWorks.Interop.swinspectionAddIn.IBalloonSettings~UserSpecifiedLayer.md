---
title: "UserSpecifiedLayer Property (IBalloonSettings)"
project: "SOLIDWORKS Inspection API Help"
interface: "IBalloonSettings"
member: "UserSpecifiedLayer"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings~UserSpecifiedLayer.html"
---

# UserSpecifiedLayer Property (IBalloonSettings)

Gets and sets the user-specified layer.

## Syntax

### Visual Basic (Declaration)

```vb
Property UserSpecifiedLayer As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonSettings
Dim value As System.String

instance.UserSpecifiedLayer = value

value = instance.UserSpecifiedLayer
```

### C#

```csharp
System.string UserSpecifiedLayer {get; set;}
```

### C++/CLI

```cpp
property System.String^ UserSpecifiedLayer {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of user-specified layer

## VBA Syntax

See [BalloonSettings](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~BalloonSettings_members.html) properties.

## Remarks

This property is valid only:

- for drawings.
- when [IBalloonSettings::Layer](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings~Layer.html) is set to [swiBalloonSettingLayer_e](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.swiBalloonSettingLayer_e.html).swiLayer_UseSpecificLayer.

## See Also

[IBalloonSettings Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings.html)
[IBalloonSettings Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
