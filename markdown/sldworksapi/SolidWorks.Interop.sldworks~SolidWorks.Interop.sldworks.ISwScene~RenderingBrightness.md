---
title: "RenderingBrightness Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "RenderingBrightness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~RenderingBrightness.html"
---

# RenderingBrightness Property (ISwScene)

Gets or sets the brightness contributed by the high dynamic range imaging (HDRI) environment.

## Syntax

### Visual Basic (Declaration)

```vb
Property RenderingBrightness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Double

instance.RenderingBrightness = value

value = instance.RenderingBrightness
```

### C#

```csharp
System.double RenderingBrightness {get; set;}
```

### C++/CLI

```cpp
property System.double RenderingBrightness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Brightness

## VBA Syntax

See [SwScene::RenderingBrightness](ms-its:sldworksapivb6.chm::/sldworks~SwScene~RenderingBrightness.html).

## Remarks

This property is valid only when a ray-trace rendering engine is activated.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
