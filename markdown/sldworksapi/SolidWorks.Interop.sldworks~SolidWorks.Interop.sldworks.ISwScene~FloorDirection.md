---
title: "FloorDirection Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "FloorDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorDirection.html"
---

# FloorDirection Property (ISwScene)

Gets or sets whether to flip the direction of the floor of this scene.

## Syntax

### Visual Basic (Declaration)

```vb
Property FloorDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Boolean

instance.FloorDirection = value

value = instance.FloorDirection
```

### C#

```csharp
System.bool FloorDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool FloorDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the direction of the floor, false to not

## VBA Syntax

See [SwScene::FloorDirection](ms-its:sldworksapivb6.chm::/sldworks~SwScene~FloorDirection.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
