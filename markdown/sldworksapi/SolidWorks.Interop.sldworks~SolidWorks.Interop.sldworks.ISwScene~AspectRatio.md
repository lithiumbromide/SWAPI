---
title: "AspectRatio Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "AspectRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~AspectRatio.html"
---

# AspectRatio Property (ISwScene)

Gets the aspect ratio of the scene floor.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AspectRatio As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Double

value = instance.AspectRatio
```

### C#

```csharp
System.double AspectRatio {get;}
```

### C++/CLI

```cpp
property System.double AspectRatio {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Aspect ratio

## VBA Syntax

See [SwScene::AspectRatio](ms-its:sldworksapivb6.chm::/sldworks~SwScene~AspectRatio.html).

## Remarks

To change the aspect ratio, set [ISwScene::FixedAspectRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FixedAspectRatio.html) to false and specify:

- [ISwScene::FloorDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorDepth.html)
- [ISwScene::FloorWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorWidth.html)

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
