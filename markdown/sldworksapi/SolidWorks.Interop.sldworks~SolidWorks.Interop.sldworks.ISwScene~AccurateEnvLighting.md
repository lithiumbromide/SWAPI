---
title: "AccurateEnvLighting Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "AccurateEnvLighting"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~AccurateEnvLighting.html"
---

# AccurateEnvLighting Property (ISwScene)

Gets or sets whether to use the accurate environment lighting calculations from the high dynamic range imaging (HDRI) scene environment.

## Syntax

### Visual Basic (Declaration)

```vb
Property AccurateEnvLighting As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Boolean

instance.AccurateEnvLighting = value

value = instance.AccurateEnvLighting
```

### C#

```csharp
System.bool AccurateEnvLighting {get; set;}
```

### C++/CLI

```cpp
property System.bool AccurateEnvLighting {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the accurate environment lighting calculations from the HDRI scene environment, false to not

## VBA Syntax

See [SwScene::AccurateEnvLighting](ms-its:sldworksapivb6.chm::/sldworks~SwScene~AccurateEnvLighting.html).

## Remarks

This property is valid only when a ray-trace rendering engine is active.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
