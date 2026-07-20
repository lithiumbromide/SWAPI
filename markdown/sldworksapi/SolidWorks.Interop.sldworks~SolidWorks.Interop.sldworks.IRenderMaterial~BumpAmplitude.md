---
title: "BumpAmplitude Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "BumpAmplitude"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpAmplitude.html"
---

# BumpAmplitude Property (IRenderMaterial)

Obsolete. Superseded by

[IRenderMaterial::BumpStrength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpStrength.html)

.

## Syntax

### Visual Basic (Declaration)

```vb
Property BumpAmplitude As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.BumpAmplitude = value

value = instance.BumpAmplitude
```

### C#

```csharp
System.double BumpAmplitude {get; set;}
```

### C++/CLI

```cpp
property System.double BumpAmplitude {
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

[RenderMaterial::BumpAmplitude](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~BumpAmplitude.html)

.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
