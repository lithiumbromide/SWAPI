---
title: "Ambient Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "Ambient"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Ambient.html"
---

# Ambient Property (IRenderMaterial)

Gets or sets the ambient light intensity for illuminating this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Ambient As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.Ambient = value

value = instance.Ambient
```

### C#

```csharp
System.double Ambient {get; set;}
```

### C++/CLI

```cpp
property System.double Ambient {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Ambient light intensity

## VBA Syntax

See [RenderMaterial::Ambient](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~Ambient.html).

## Remarks

The scene should contain an ambient light.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
