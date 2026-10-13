---
title: "BumpRoughLow Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "BumpRoughLow"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpRoughLow.html"
---

# BumpRoughLow Property (IRenderMaterial)

Gets or sets the low threshold of the surface finish for this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property BumpRoughLow As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.BumpRoughLow = value

value = instance.BumpRoughLow
```

### C#

```csharp
System.double BumpRoughLow {get; set;}
```

### C++/CLI

```cpp
property System.double BumpRoughLow {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Low threshold of the surface finish

## VBA Syntax

See [RenderMaterial::BumpRoughLow](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~BumpRoughLow.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
