---
title: "Emission Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "Emission"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Emission.html"
---

# Emission Property (IRenderMaterial)

Gets or sets how much light is projected from the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Emission As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.Emission = value

value = instance.Emission
```

### C#

```csharp
System.double Emission {get; set;}
```

### C++/CLI

```cpp
property System.double Emission {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Amount of light projected from the appearance

## VBA Syntax

See[RenderMaterial::Emission](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~Emission.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
