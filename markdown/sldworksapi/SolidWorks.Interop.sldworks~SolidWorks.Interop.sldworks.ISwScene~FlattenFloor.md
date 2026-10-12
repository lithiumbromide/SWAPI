---
title: "FlattenFloor Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "FlattenFloor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FlattenFloor.html"
---

# FlattenFloor Property (ISwScene)

Get or sets whether to flatten the floor of a spherical environment to improve the look of models that naturally rest on flat floors.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlattenFloor As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Boolean

instance.FlattenFloor = value

value = instance.FlattenFloor
```

### C#

```csharp
System.bool FlattenFloor {get; set;}
```

### C++/CLI

```cpp
property System.bool FlattenFloor {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flatten the floor, false to not

## VBA Syntax

See [SwScene::FlattenFloor](ms-its:sldworksapivb6.chm::/sldworks~SwScene~FlattenFloor.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## Remarks

This property is valid only if [ISwScene::BackgroundType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundType.html) is [swSceneBackgroundType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSceneBackgroundType_e.html).swBackgroundType_UseEnvironment.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
