---
title: "SceneReflectivity Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "SceneReflectivity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~SceneReflectivity.html"
---

# SceneReflectivity Property (ISwScene)

Gets or sets the amount of reflectivity provided by the high dynamic range imaging (HDRI) environment.

## Syntax

### Visual Basic (Declaration)

```vb
Property SceneReflectivity As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Double

instance.SceneReflectivity = value

value = instance.SceneReflectivity
```

### C#

```csharp
System.double SceneReflectivity {get; set;}
```

### C++/CLI

```cpp
property System.double SceneReflectivity {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Reflectivity

## VBA Syntax

See [SwScene::SceneReflectivity](ms-its:sldworksapivb6.chm::/sldworks~SwScene~SceneReflectivity.html).

## Remarks

This property is valid only when a ray-trace rendering engine is activated.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
