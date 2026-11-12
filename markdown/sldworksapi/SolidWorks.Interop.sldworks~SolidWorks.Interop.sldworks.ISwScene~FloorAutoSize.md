---
title: "FloorAutoSize Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "FloorAutoSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorAutoSize.html"
---

# FloorAutoSize Property (ISwScene)

Gets or sets whether to resize the scene floor based on the model bounding box.

## Syntax

### Visual Basic (Declaration)

```vb
Property FloorAutoSize As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Boolean

instance.FloorAutoSize = value

value = instance.FloorAutoSize
```

### C#

```csharp
System.bool FloorAutoSize {get; set;}
```

### C++/CLI

```cpp
property System.bool FloorAutoSize {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to resize the scene floor based on the model bounding box, false to manually specify the width, depth, and rotation of the scene floor

## VBA Syntax

See [SwScene::FloorAutoSize](ms-its:sldworksapivb6.chm::/sldworks~SwScene~FloorAutoSize.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
