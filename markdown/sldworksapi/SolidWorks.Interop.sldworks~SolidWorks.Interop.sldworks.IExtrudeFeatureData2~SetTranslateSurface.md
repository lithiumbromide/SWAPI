---
title: "SetTranslateSurface Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "SetTranslateSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetTranslateSurface.html"
---

# SetTranslateSurface Method (IExtrudeFeatureData2)

Sets the translate surface setting for this extrude feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetTranslateSurface( _
   ByVal Fwd As System.Boolean, _
   ByVal ValIn As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim Fwd As System.Boolean
Dim ValIn As System.Boolean

instance.SetTranslateSurface(Fwd, ValIn)
```

### C#

```csharp
void SetTranslateSurface(
   System.bool Fwd,
   System.bool ValIn
)
```

### C++/CLI

```cpp
void SetTranslateSurface(
   System.bool Fwd,
   System.bool ValIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Fwd`: True makes the end of the extrusion a translation of the reference surface in the forward direction, false makes the end of the extrusion a translation of the reference surface in the reverse direction
- `ValIn`: True to enable the translate surface setting, false to disable it

## VBA Syntax

See [ExtrudeFeatureData2::SetTranslateSurface](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~SetTranslateSurface.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::GetTranslateSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetTranslateSurface.html)
[IExtrudeFeatureData2::GetReverseOffset Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetReverseOffset.html)
[IExtrudeFeatureData2::SetReverseOffset Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetReverseOffset.html)
[IExtrudeFeatureData2::FromOffsetDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromOffsetDistance.html)
[IExtrudeFeatureData2::FromOffsetReverse Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromOffsetReverse.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
