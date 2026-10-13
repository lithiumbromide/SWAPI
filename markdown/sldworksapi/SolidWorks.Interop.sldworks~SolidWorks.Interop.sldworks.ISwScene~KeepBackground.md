---
title: "KeepBackground Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "KeepBackground"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~KeepBackground.html"
---

# KeepBackground Property (ISwScene)

Gets or sets whether to retain the background when replacing the scene.

## Syntax

### Visual Basic (Declaration)

```vb
Property KeepBackground As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Boolean

instance.KeepBackground = value

value = instance.KeepBackground
```

### C#

```csharp
System.bool KeepBackground {get; set;}
```

### C++/CLI

```cpp
property System.bool KeepBackground {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to retain the background when replacing a scene, false to not

## VBA Syntax

See [SwScene::KeepBackground](ms-its:sldworksapivb6.chm::/sldworks~SwScene~KeepBackground.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## Remarks

This property is valid only if [ISwScene::BackgroundType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundType.html) is set to one of the following:

- [swSceneBackgroundType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSceneBackgroundType_e.html).swBackgroundType_Image
- swSceneBackgroundType_e.swBackgroundType_Graduated
- swSceneBackgroundType_e.swBackgroundType_Plain

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
