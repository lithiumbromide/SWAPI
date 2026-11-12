---
title: "SetUDirection Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "SetUDirection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetUDirection.html"
---

# SetUDirection Method (IRenderMaterial)

Obsolete. Superseded by [IRenderMaterial::SetUDirection2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~SetUDirection2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetUDirection( _
   ByRef UDir As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim UDir As System.Double

instance.SetUDirection(UDir)
```

### C#

```csharp
void SetUDirection(
   ref System.double UDir
)
```

### C++/CLI

```cpp
void SetUDirection(
   System.double% UDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UDir`: Array of doubles representing the U direction for the texture-based appearance (see **Remarks**)

## VBA Syntax

See [RenderMaterial::SetUDirection](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~SetUDirection.html).

## Remarks

To specify the U direction in the X direction, set UDir to {1, 0, 0}.

Call [IRenderMaterial::SetVDirection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~SetVDirection.html) to set the V direction of the appearance.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)
[IRenderMaterial::GetUDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetUDirection.html)
[IRenderMaterial::GetVDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetVDirection.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
