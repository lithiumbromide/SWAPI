---
title: "FloorOffset Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "FloorOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorOffset.html"
---

# FloorOffset Property (ISwScene)

Gets or sets the height of the model above or below the floor of this scene.

## Syntax

### Visual Basic (Declaration)

```vb
Property FloorOffset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Double

instance.FloorOffset = value

value = instance.FloorOffset
```

### C#

```csharp
System.double FloorOffset {get; set;}
```

### C++/CLI

```cpp
property System.double FloorOffset {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance between the scene floor and the model

## VBA Syntax

See [SwScene::FloorOffset](ms-its:sldworksapivb6.chm::/sldworks~SwScene~FloorOffset.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
