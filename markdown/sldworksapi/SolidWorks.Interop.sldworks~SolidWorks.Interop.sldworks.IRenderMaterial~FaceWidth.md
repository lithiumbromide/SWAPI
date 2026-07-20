---
title: "FaceWidth Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "FaceWidth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~FaceWidth.html"
---

# FaceWidth Property (IRenderMaterial)

Gets or sets the face width.

## Syntax

### Visual Basic (Declaration)

```vb
Property FaceWidth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.FaceWidth = value

value = instance.FaceWidth
```

### C#

```csharp
System.double FaceWidth {get; set;}
```

### C++/CLI

```cpp
property System.double FaceWidth {
   System.double get();
   void set (    System.double value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Face width

## VBA Syntax

See

[RenderMaterial::FaceWidth](ms-its:sldworksapivb6.chm::/sldworks~RenderMateria~FaceWidth.html)

.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33
