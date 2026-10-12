---
title: "FloorRotation Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "FloorRotation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorRotation.html"
---

# FloorRotation Property (ISwScene)

Gets or sets the rotation of the scene floor relative to the environment of this scene.

## Syntax

### Visual Basic (Declaration)

```vb
Property FloorRotation As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Double

instance.FloorRotation = value

value = instance.FloorRotation
```

### C#

```csharp
System.double FloorRotation {get; set;}
```

### C++/CLI

```cpp
property System.double FloorRotation {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 <= Rotation in degrees <= 360.0

## VBA Syntax

See [SwScene::FloorRotation](ms-its:sldworksapivb6.chm::/sldworks~SwScene~FloorRotation.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## Remarks

This property is valid only if [ISwScene::FloorAutoSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorAutoSize.html) is false.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
