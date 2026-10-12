---
title: "RotationAngle Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "RotationAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~RotationAngle.html"
---

# RotationAngle Property (IRenderMaterial)

Gets or sets the angle by which to rotate the texture relative to the axes for mapping this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property RotationAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.RotationAngle = value

value = instance.RotationAngle
```

### C#

```csharp
System.double RotationAngle {get; set;}
```

### C++/CLI

```cpp
property System.double RotationAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle by which to rotate the texture relative to the axes

## VBA Syntax

See [RenderMaterial::RotationAngle](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~RotationAngle.html).

## Remarks

This property is only valid when either a spherical or cylindrical [mapping type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~MappingType.html) is selected.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
