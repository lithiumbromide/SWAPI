---
title: "Direction2RotationAngle Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "Direction2RotationAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Direction2RotationAngle.html"
---

# Direction2RotationAngle Property (IRenderMaterial)

Gets or sets the angle at which to rotate the texture relative to the vertical axis for mapping this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Direction2RotationAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.Direction2RotationAngle = value

value = instance.Direction2RotationAngle
```

### C#

```csharp
System.double Direction2RotationAngle {get; set;}
```

### C++/CLI

```cpp
property System.double Direction2RotationAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle at which to rotate the texture relative to the vertical axis

## VBA Syntax

See [RenderMaterial::Direction2RotationAngle](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~Direction2RotationAngle.html).

## Remarks

This property affects spheres only.

Call [IRenderMaterial::Direction1RotationAngle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~Direction1RotationAngle.html) to get or set the angle to rotate the texture to the horizontal axis.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
