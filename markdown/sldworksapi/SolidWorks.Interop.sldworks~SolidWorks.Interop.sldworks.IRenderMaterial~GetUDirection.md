---
title: "GetUDirection Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "GetUDirection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetUDirection.html"
---

# GetUDirection Method (IRenderMaterial)

Obsolete. Superseded by [IRenderMaterial::GetUDirection2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~GetUDirection2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetUDirection( _
   ByRef UDir As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim UDir As System.Double

instance.GetUDirection(UDir)
```

### C#

```csharp
void GetUDirection(
   out System.double UDir
)
```

### C++/CLI

```cpp
void GetUDirection(
   [Out] System.double UDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UDir`: Array of doubles representing the U direction for the texture-based appearance (see Remarks)

## VBA Syntax

See [RenderMaterial::GetUDirection](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~GetUDirection.html).

## Remarks

Call [IRenderMaterial::GetVDirection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~GetVDirection.html) to get the V direction of the appearance.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)
[IRenderMaterial::SetUDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetUDirection.html)
[IRenderMaterial::SetVDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetVDirection.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
