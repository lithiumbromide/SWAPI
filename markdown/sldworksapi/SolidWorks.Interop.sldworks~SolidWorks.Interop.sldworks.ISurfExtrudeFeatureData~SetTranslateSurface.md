---
title: "SetTranslateSurface Method (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "SetTranslateSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetTranslateSurface.html"
---

# SetTranslateSurface Method (ISurfExtrudeFeatureData)

Sets the translate surface setting for this extruded surface.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetTranslateSurface( _
   ByVal Fwd As System.Boolean, _
   ByVal Trans As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
Dim Fwd As System.Boolean
Dim Trans As System.Boolean

instance.SetTranslateSurface(Fwd, Trans)
```

### C#

```csharp
void SetTranslateSurface(
   System.bool Fwd,
   System.bool Trans
)
```

### C++/CLI

```cpp
void SetTranslateSurface(
   System.bool Fwd,
   System.bool Trans
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Fwd`: True sets the translate surface setting in the forward direction, false sets it in the reverse direction
- `Trans`: True enables the translate surface setting, false disables it

## VBA Syntax

See [SurfExtrudeFeatureData::SetTranslateSurface](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~SetTranslateSurface.html).

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)
[ISurfExtrudeFeatureData::GetTranslateSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetTranslateSurface.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
