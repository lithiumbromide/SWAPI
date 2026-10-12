---
title: "BackgroundType Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "BackgroundType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundType.html"
---

# BackgroundType Property (ISwScene)

Gets or sets the type of background for this scene.

## Syntax

### Visual Basic (Declaration)

```vb
Property BackgroundType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Integer

instance.BackgroundType = value

value = instance.BackgroundType
```

### C#

```csharp
System.int BackgroundType {get; set;}
```

### C++/CLI

```cpp
property System.int BackgroundType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of background as defined in [swSceneBackgroundType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSceneBackgroundType_e.html)

## VBA Syntax

See [SwScene::BackgroundType](ms-its:sldworksapivb6.chm::/sldworks~SwScene~BackgroundType.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
