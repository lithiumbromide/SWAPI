---
title: "Transparency Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "Transparency"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Transparency.html"
---

# Transparency Property (IRenderMaterial)

Gets or sets the degree to which a material allows light to pass through for illuminating the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Transparency As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.Transparency = value

value = instance.Transparency
```

### C#

```csharp
System.double Transparency {get; set;}
```

### C++/CLI

```cpp
property System.double Transparency {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Degree to which a material allows light to pass through

## VBA Syntax

See [RenderMaterial::Transparency](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~Transparency.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
