---
title: "FitToSWWindow Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "FitToSWWindow"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FitToSWWindow.html"
---

# FitToSWWindow Property (ISwScene)

Gets or sets whether to stretch an image to fit the SOLIDWORKS window.

## Syntax

### Visual Basic (Declaration)

```vb
Property FitToSWWindow As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Boolean

instance.FitToSWWindow = value

value = instance.FitToSWWindow
```

### C#

```csharp
System.bool FitToSWWindow {get; set;}
```

### C++/CLI

```cpp
property System.bool FitToSWWindow {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to stretch an image to fit, false to not

## VBA Syntax

See [SwScene::FitToSWWindow](ms-its:sldworksapivb6.chm::/sldworks~SwScene~FitToSWWindow.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## Remarks

This property is valid only if [ISwScene::BackgroundType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundType.html) is [swSceneBackgroundType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSceneBackgroundType_e.html).swBackgroundType_Image.

Set the background image with [ISwScene::BackgroundImage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundImage.html).

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
