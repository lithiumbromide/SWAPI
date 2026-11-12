---
title: "FloorAlignment Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "FloorAlignment"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorAlignment.html"
---

# FloorAlignment Property (ISwScene)

Gets or sets the plane with which to align the scene floor.

## Syntax

### Visual Basic (Declaration)

```vb
Property FloorAlignment As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Integer

instance.FloorAlignment = value

value = instance.FloorAlignment
```

### C#

```csharp
System.int FloorAlignment {get; set;}
```

### C++/CLI

```cpp
property System.int FloorAlignment {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Scene floor alignment plane as defined by [swSceneFloorAlign_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSceneFloorAlign_e.html)

## VBA Syntax

See [SwScene::FloorAlignment](ms-its:sldworksapivb6.chm::/sldworks~SwScene~FloorAlignment.html).

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
