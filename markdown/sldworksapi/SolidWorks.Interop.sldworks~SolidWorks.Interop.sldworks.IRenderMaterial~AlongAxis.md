---
title: "AlongAxis Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "AlongAxis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~AlongAxis.html"
---

# AlongAxis Property (IRenderMaterial)

Gets or sets the along axis value for a cylindrical mapping type.

## Syntax

### Visual Basic (Declaration)

```vb
Property AlongAxis As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.AlongAxis = value

value = instance.AlongAxis
```

### C#

```csharp
System.double AlongAxis {get; set;}
```

### C++/CLI

```cpp
property System.double AlongAxis {
   System.double get();
   void set (    System.double value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Along axis value

## VBA Syntax

See

[RenderMaterial::AlongAxis](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~AlongAxis.html)

.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33
