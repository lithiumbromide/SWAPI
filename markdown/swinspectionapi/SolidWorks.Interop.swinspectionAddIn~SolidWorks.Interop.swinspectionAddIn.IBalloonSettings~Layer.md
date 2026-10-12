---
title: "Layer Property (IBalloonSettings)"
project: "SOLIDWORKS Inspection API Help"
interface: "IBalloonSettings"
member: "Layer"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings~Layer.html"
---

# Layer Property (IBalloonSettings)

Gets and sets the drawing layer to which to add this balloon.

## Syntax

### Visual Basic (Declaration)

```vb
Property Layer As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonSettings
Dim value As System.Integer

instance.Layer = value

value = instance.Layer
```

### C#

```csharp
System.int Layer {get; set;}
```

### C++/CLI

```cpp
property System.int Layer {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Drawing layer as defined by [swiBalloonSettingLayer_e](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.swiBalloonSettingLayer_e.html)

## VBA Syntax

See [BalloonSettings](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~BalloonSettings_members.html) properties.

## Remarks

This property is valid only for drawings.

If you set this property to swiLayer_UseSpecificLayer, use [IBalloonSettings::UserSpecifiedLayer](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings~UserSpecifiedLayer.html) to set the name of the layer.

## See Also

[IBalloonSettings Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings.html)
[IBalloonSettings Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
