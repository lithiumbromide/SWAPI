---
title: "GetVDirection Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "GetVDirection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetVDirection.html"
---

# GetVDirection Method (IRenderMaterial)

Obsolete. Superseded by [IRenderMaterial::GetVDirection2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~GetVDirection2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetVDirection( _
   ByRef VDir As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim VDir As System.Double

instance.GetVDirection(VDir)
```

### C#

```csharp
void GetVDirection(
   out System.double VDir
)
```

### C++/CLI

```cpp
void GetVDirection(
   [Out] System.double VDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VDir`: Array of doubles representing the V direction of the texture-based appearance (see Remarks)

## VBA Syntax

See [RenderMaterial::GetVDirection](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~GetVDirection.html).

## Examples

The [mapping type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~MappingType.html) (surface, projection, automatic, etc.) indirectly determines the V direction. This vector is perpendicular to the U direction.

Call [IRenderMaterial::GetUDirection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~GetUDirection.html) to get the U direction of the appearance.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)
[IRenderMaterial::SetUDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetUDirection.html)
[IRenderMaterial::SetVDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetVDirection.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
