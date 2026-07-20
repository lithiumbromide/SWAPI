---
title: "BumpStrength Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "BumpStrength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpStrength.html"
---

# BumpStrength Property (IRenderMaterial)

Gets or sets the amplitude of the surface layer for this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property BumpStrength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.BumpStrength = value

value = instance.BumpStrength
```

### C#

```csharp
System.double BumpStrength {get; set;}
```

### C++/CLI

```cpp
property System.double BumpStrength {
   System.double get();
   void set (    System.double value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Amplitude

## VBA Syntax

See

[RenderMaterial::BumpStrength](ms-its:sldworksapivb6.chm::/sldworks~RenderMaterial~BumpStrength.html)

.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33
