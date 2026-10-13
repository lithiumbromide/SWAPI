---
title: "BackgroundTopGradientColor Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "BackgroundTopGradientColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundTopGradientColor.html"
---

# BackgroundTopGradientColor Property (ISwScene)

Gets or sets the background color of this scene.

## Syntax

### Visual Basic (Declaration)

```vb
Property BackgroundTopGradientColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Integer

instance.BackgroundTopGradientColor = value

value = instance.BackgroundTopGradientColor
```

### C#

```csharp
System.int BackgroundTopGradientColor {get; set;}
```

### C++/CLI

```cpp
property System.int BackgroundTopGradientColor {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

RGB color

## VBA Syntax

See [SwScene::BackgroundTopGradientColor](ms-its:sldworksapivb6.chm::/sldworks~SwScene~BackgroundTopGradientColor.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## Remarks

| If ISwScene::BackgroundType is... | Then this property sets... |
| --- | --- |
| swSceneBackgroundType_e .swBackgroundType_Plain | a single background color. |
| swSceneBackgroundType_e.swBackgroundType_Graduated | the top color in the graduated range of background colors; Use ISwScene::BackgroundBottomGradientColor to set the bottom color in the graduated range of background colors. |

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
