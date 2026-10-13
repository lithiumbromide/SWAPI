---
title: "EnvironmentSize Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "EnvironmentSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~EnvironmentSize.html"
---

# EnvironmentSize Property (ISwScene)

Gets or sets the size of the high dynamic range imaging (HDRI) scene sphere that surrounds the model.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnvironmentSize As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Double

instance.EnvironmentSize = value

value = instance.EnvironmentSize
```

### C#

```csharp
System.double EnvironmentSize {get; set;}
```

### C++/CLI

```cpp
property System.double EnvironmentSize {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Size of the HDRI scene sphere

## VBA Syntax

See [SwScene::EnvironmentSize](ms-its:sldworksapivb6.chm::/sldworks~SwScene~EnvironmentSize.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## Remarks

This property is valid only if [ISwScene::FlattenFloor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FlattenFloor.html) is set to true.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
