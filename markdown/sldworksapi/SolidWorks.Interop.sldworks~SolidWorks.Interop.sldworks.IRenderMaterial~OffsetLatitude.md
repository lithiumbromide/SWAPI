---
title: "OffsetLatitude Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "OffsetLatitude"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~OffsetLatitude.html"
---

# OffsetLatitude Property (IRenderMaterial)

Gets or sets the offset latitude value for a spherical mapping type.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetLatitude As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.OffsetLatitude = value

value = instance.OffsetLatitude
```

### C#

```csharp
System.double OffsetLatitude {get; set;}
```

### C++/CLI

```cpp
property System.double OffsetLatitude {
   System.double get();
   void set (    System.double value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Offset latitude value

## VBA Syntax

See

[RenderMaterial::OffsetLatitude](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~OffsetLatitude.html)

.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33
