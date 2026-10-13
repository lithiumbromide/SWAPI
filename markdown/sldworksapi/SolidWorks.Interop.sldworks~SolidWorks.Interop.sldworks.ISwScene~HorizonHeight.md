---
title: "HorizonHeight Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "HorizonHeight"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~HorizonHeight.html"
---

# HorizonHeight Property (ISwScene)

Gets or sets the height on the high dynamic range imaging (HDRI) scene sphere where the scene floor starts to flatten.

## Syntax

### Visual Basic (Declaration)

```vb
Property HorizonHeight As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Double

instance.HorizonHeight = value

value = instance.HorizonHeight
```

### C#

```csharp
System.double HorizonHeight {get; set;}
```

### C++/CLI

```cpp
property System.double HorizonHeight {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 <= Horizon height <= 1.0

## VBA Syntax

See [SwScene::HorizonHeight](ms-its:sldworksapivb6.chm::/sldworks~SwScene~HorizonHeight.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## Remarks

This property is valid only if [ISwScene::FlattenFloor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FlattenFloor.html) is set to true.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
