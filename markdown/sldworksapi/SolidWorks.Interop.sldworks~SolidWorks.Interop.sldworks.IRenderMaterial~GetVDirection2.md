---
title: "GetVDirection2 Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "GetVDirection2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetVDirection2.html"
---

# GetVDirection2 Method (IRenderMaterial)

Gets the V direction of the texture-based appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetVDirection2( _
   ByRef VDir_X As System.Double, _
   ByRef VDir_Y As System.Double, _
   ByRef VDir_Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim VDir_X As System.Double
Dim VDir_Y As System.Double
Dim VDir_Z As System.Double

instance.GetVDirection2(VDir_X, VDir_Y, VDir_Z)
```

### C#

```csharp
void GetVDirection2(
   out System.double VDir_X,
   out System.double VDir_Y,
   out System.double VDir_Z
)
```

### C++/CLI

```cpp
void GetVDirection2(
   [Out] System.double VDir_X,
   [Out] System.double VDir_Y,
   [Out] System.double VDir_Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VDir_X`: X coordinate of the V direction
- `VDir_Y`: Y coordinate of the V direction
- `VDir_Z`: Z coordinate of the V direction

## VBA Syntax

See [RenderMaterial::GetVDirection2](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~GetVDirection2.html).

## Examples

See [IRenderMaterial](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial.html) examples.

## Remarks

The [mapping type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~MappingType.html) (surface, projection, automatic, etc.) indirectly determines the V direction. This vector is perpendicular to the U direction.

Call [IRenderMaterial::GetUDirection2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~GetUDirection2.html) to get the U direction of the appearance.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)
[IRenderMaterial::SetUDirection2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetUDirection2.html)
[IRenderMaterial::SetVDirection2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetVDirection2.html)

## Availability

SOLIDWORKS 2013 SP05, Revision 21.5
