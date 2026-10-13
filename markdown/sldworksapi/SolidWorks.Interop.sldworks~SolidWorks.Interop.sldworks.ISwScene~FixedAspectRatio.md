---
title: "FixedAspectRatio Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "FixedAspectRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FixedAspectRatio.html"
---

# FixedAspectRatio Property (ISwScene)

Gets or sets whether to fix the aspect ratio of the scene floor.

## Syntax

### Visual Basic (Declaration)

```vb
Property FixedAspectRatio As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Boolean

instance.FixedAspectRatio = value

value = instance.FixedAspectRatio
```

### C#

```csharp
System.bool FixedAspectRatio {get; set;}
```

### C++/CLI

```cpp
property System.bool FixedAspectRatio {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to fix the aspect ratio of the scene floor, false to allow the scene floor width and height to change independently

## VBA Syntax

See [SwScene::FixedAspectRatio](ms-its:sldworksapivb6.chm::/sldworks~SwScene~FixedAspectRatio.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## Remarks

If this property is set to true, then you need only specify one of the following:

- [ISwScene::FloorDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorDepth.html)
- [ISwScene::FloorWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorWidth.html)

To change the [aspect ratio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~AspectRatio.html), set this property to false and set both of the following:

- ISwScene::FloorDepth
- ISwScene::FloorWidth

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
