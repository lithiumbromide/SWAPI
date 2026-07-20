---
title: "AboutAxis Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "AboutAxis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~AboutAxis.html"
---

# AboutAxis Property (IRenderMaterial)

Gets or sets the about axis value for a cylindrical mapping type.

## Syntax

### Visual Basic (Declaration)

```vb
Property AboutAxis As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.AboutAxis = value

value = instance.AboutAxis
```

### C#

```csharp
System.double AboutAxis {get; set;}
```

### C++/CLI

```cpp
property System.double AboutAxis {
   System.double get();
   void set (    System.double value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

About axis value

## VBA Syntax

See

[RenderMaterial::AboutAxis](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~AboutAxis.html)

.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33
