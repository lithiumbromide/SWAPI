---
title: "BackgroundBottomGradientColor Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "BackgroundBottomGradientColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundBottomGradientColor.html"
---

# BackgroundBottomGradientColor Property (ISwScene)

Gets or sets the bottom color of the graduated range of background colors of this scene.

## Syntax

### Visual Basic (Declaration)

```vb
Property BackgroundBottomGradientColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Integer

instance.BackgroundBottomGradientColor = value

value = instance.BackgroundBottomGradientColor
```

### C#

```csharp
System.int BackgroundBottomGradientColor {get; set;}
```

### C++/CLI

```cpp
property System.int BackgroundBottomGradientColor {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

RGB color

## VBA Syntax

See [SwScene::BackgroundBottomGradientColor](ms-its:sldworksapivb6.chm::/sldworks~SwScene~BackgroundBottomGradientColor.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## Remarks

This property is valid only if [ISwScene::BackgroundType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundType.html) is [swSceneBackgroundType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSceneBackgroundType_e.html).swBackgroundType_Graduated.

Set the top color of the graduated range of background colors with [ISwScene::BackgroundTopGradientColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundTopGradientColor.html).

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
