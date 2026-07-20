---
title: "OffsetLongitude Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "OffsetLongitude"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~OffsetLongitude.html"
---

# OffsetLongitude Property (IRenderMaterial)

Gets or sets the offset longitude value for a spherical mapping type.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetLongitude As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.OffsetLongitude = value

value = instance.OffsetLongitude
```

### C#

```csharp
System.double OffsetLongitude {get; set;}
```

### C++/CLI

```cpp
property System.double OffsetLongitude {
   System.double get();
   void set (    System.double value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Offset longitude value

## VBA Syntax

See

[RenderMaterial::OffsetLongitude](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~OffsetLongitude.html)

.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33
