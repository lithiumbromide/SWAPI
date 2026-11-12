---
title: "FloorOffsetDirection Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "FloorOffsetDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorOffsetDirection.html"
---

# FloorOffsetDirection Property (ISwScene)

Gets or sets whether to swap the positions of the scene floor and the model.

## Syntax

### Visual Basic (Declaration)

```vb
Property FloorOffsetDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Boolean

instance.FloorOffsetDirection = value

value = instance.FloorOffsetDirection
```

### C#

```csharp
System.bool FloorOffsetDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool FloorOffsetDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to swap positions of the scene floor and the model, false to not

## VBA Syntax

See [SwScene::FloorOffsetDirection](ms-its:sldworksapivb6.chm::/sldworks~SwScene~FloorOffsetDirection.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
