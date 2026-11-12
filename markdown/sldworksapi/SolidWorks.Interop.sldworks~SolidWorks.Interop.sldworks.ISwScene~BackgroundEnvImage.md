---
title: "BackgroundEnvImage Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "BackgroundEnvImage"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundEnvImage.html"
---

# BackgroundEnvImage Property (ISwScene)

Gets or sets the environment image of this scene.

## Syntax

### Visual Basic (Declaration)

```vb
Property BackgroundEnvImage As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.String

instance.BackgroundEnvImage = value

value = instance.BackgroundEnvImage
```

### C#

```csharp
System.string BackgroundEnvImage {get; set;}
```

### C++/CLI

```cpp
property System.String^ BackgroundEnvImage {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fully qualified path to an environment image file

## VBA Syntax

See [SwScene::BackgroundEnvImage](ms-its:sldworksapivb6.chm::/sldworks~SwScene~BackgroundEnvImage.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## Remarks

This property is valid only if [ISwScene::BackgroundType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundType.html) is [swSceneBackgroundType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSceneBackgroundType_e.html).swBackgroundType_UseEnvironment.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
