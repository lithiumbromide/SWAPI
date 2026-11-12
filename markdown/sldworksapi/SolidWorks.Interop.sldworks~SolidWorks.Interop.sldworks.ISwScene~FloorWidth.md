---
title: "FloorWidth Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "FloorWidth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorWidth.html"
---

# FloorWidth Property (ISwScene)

Gets or sets the width of the scene floor.

## Syntax

### Visual Basic (Declaration)

```vb
Property FloorWidth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Double

instance.FloorWidth = value

value = instance.FloorWidth
```

### C#

```csharp
System.double FloorWidth {get; set;}
```

### C++/CLI

```cpp
property System.double FloorWidth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Width of the scene floor

## VBA Syntax

See [SwScene::FloorWidth](ms-its:sldworksapivb6.chm::/sldworks~SwScene~FloorWidth.html).

## Remarks

The setting of this property is valid only if [ISwScene::FloorAutoSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorAutoSize.html) is false.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
