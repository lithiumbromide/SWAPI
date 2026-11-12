---
title: "FloorDepth Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "FloorDepth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorDepth.html"
---

# FloorDepth Property (ISwScene)

Gets or sets the depth of the scene floor.

## Syntax

### Visual Basic (Declaration)

```vb
Property FloorDepth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Double

instance.FloorDepth = value

value = instance.FloorDepth
```

### C#

```csharp
System.double FloorDepth {get; set;}
```

### C++/CLI

```cpp
property System.double FloorDepth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Depth of the scene floor

## VBA Syntax

See [SwScene::FloorDepth](ms-its:sldworksapivb6.chm::/sldworks~SwScene~FloorDepth.html).

## Remarks

The setting of this property is valid only if [ISwScene::FloorAutoSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorAutoSize.html) is false.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
