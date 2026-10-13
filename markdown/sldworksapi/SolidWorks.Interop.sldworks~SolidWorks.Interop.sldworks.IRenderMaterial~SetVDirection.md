---
title: "SetVDirection Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "SetVDirection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetVDirection.html"
---

# SetVDirection Method (IRenderMaterial)

Obsolete. Superseded by [IRenderMaterial::SetVDirection2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~SetVDirection2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetVDirection( _
   ByRef VDir As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim VDir As System.Double

instance.SetVDirection(VDir)
```

### C#

```csharp
void SetVDirection(
   ref System.double VDir
)
```

### C++/CLI

```cpp
void SetVDirection(
   System.double% VDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VDir`: Array of doubles representing the V direction of the texture-based appearance (see Remarks)

## VBA Syntax

See [RenderMaterial::SetVDirection](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~SetVDirection.html).

## Remarks

To specify the V direction in the Y direction, set VDir to {0,1,0}.

The [mapping type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~MappingType.html) (surface, projection, automatic, etc.) indirectly determines the V direction. This vector is perpendicular to the U direction.

Call [IRenderMaterial::SetUDirection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~SetUDirection.html) to set the U direction.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)
[IRenderMaterial::GetUDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetUDirection.html)
[IRenderMaterial::GetVDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetVDirection.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
