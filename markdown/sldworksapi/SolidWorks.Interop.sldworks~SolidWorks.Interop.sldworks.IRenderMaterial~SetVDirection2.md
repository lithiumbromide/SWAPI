---
title: "SetVDirection2 Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "SetVDirection2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetVDirection2.html"
---

# SetVDirection2 Method (IRenderMaterial)

Sets the V direction of the texture-based appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetVDirection2( _
   ByVal VDir_X As System.Double, _
   ByVal VDir_Y As System.Double, _
   ByVal VDir_Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim VDir_X As System.Double
Dim VDir_Y As System.Double
Dim VDir_Z As System.Double

instance.SetVDirection2(VDir_X, VDir_Y, VDir_Z)
```

### C#

```csharp
void SetVDirection2(
   System.double VDir_X,
   System.double VDir_Y,
   System.double VDir_Z
)
```

### C++/CLI

```cpp
void SetVDirection2(
   System.double VDir_X,
   System.double VDir_Y,
   System.double VDir_Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VDir_X`: X coordinate of the V direction
- `VDir_Y`: Y coordinate of the V direction
- `VDir_Z`: Z coordinate of the V direction

## VBA Syntax

See [RenderMaterial::SetVDirection2](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~SetVDirection2.html).

## Remarks

To specify the V direction in the Y direction, set:

1. VDir_X to 0.0.
2. VDir_Y to 1.0.
3. VDir_Z to 0.0.

The [mapping type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~MappingType.html) (surface, projection, automatic, etc.) indirectly determines the V direction. This vector is perpendicular to the U direction.

Call [IRenderMaterial::SetUDirection2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~SetUDirection2.html) to set the U direction.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)
[IRenderMaterial::GetUDirection2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetUDirection2.html)
[IRenderMaterial::GetVDirection2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetVDirection2.html)

## Availability

SOLIDWORKS 2013 SP05, Revision 21.5
