---
title: "Layer Property (BalloonSettings)"
project: "SOLIDWORKS Inspection API Help"
interface: "BalloonSettings"
member: "Layer"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.BalloonSettings~Layer.html"
---

# Layer Property (BalloonSettings)

Gets and sets the drawing layer to which to add this balloon.

## Syntax

### Visual Basic (Declaration)

```vb
Property Layer As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As BalloonSettings
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

[BalloonSettings Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.BalloonSettings.html)
[BalloonSettings Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.BalloonSettings_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
