---
title: "BackgroundBrightness Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "BackgroundBrightness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundBrightness.html"
---

# BackgroundBrightness Property (ISwScene)

Gets or sets the brightness of the background.

## Syntax

### Visual Basic (Declaration)

```vb
Property BackgroundBrightness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Double

instance.BackgroundBrightness = value

value = instance.BackgroundBrightness
```

### C#

```csharp
System.double BackgroundBrightness {get; set;}
```

### C++/CLI

```cpp
property System.double BackgroundBrightness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Brightness

## VBA Syntax

See [SwScene::BackgroundBrightness](ms-its:sldworksapivb6.chm::/sldworks~SwScene~BackgroundBrightness.html).

## Remarks

This property is valid only when:

- a ray-trace rendering engine is activated
- [ISwScene::BackgroundType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundType.html) is not [swSceneBackgroundType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSceneBackgroundType_e.html).swBackgroundType_None

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
