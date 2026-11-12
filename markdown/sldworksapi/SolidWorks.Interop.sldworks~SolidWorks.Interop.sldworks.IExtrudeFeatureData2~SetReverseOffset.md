---
title: "SetReverseOffset Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "SetReverseOffset"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetReverseOffset.html"
---

# SetReverseOffset Method (IExtrudeFeatureData2)

Sets the offset direction for this extrude feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetReverseOffset( _
   ByVal Fwd As System.Boolean, _
   ByVal ValIn As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim Fwd As System.Boolean
Dim ValIn As System.Boolean

instance.SetReverseOffset(Fwd, ValIn)
```

### C#

```csharp
void SetReverseOffset(
   System.bool Fwd,
   System.bool ValIn
)
```

### C++/CLI

```cpp
void SetReverseOffset(
   System.bool Fwd,
   System.bool ValIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Fwd`: True sets the reverse offset setting in the forward direction, false sets it in the reverse direction
- `ValIn`: True enables the reverse offset setting, false disables it

## VBA Syntax

See [ExtrudeFeatureData2::SetReverseOffset](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~SetReverseOffset.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::SGetReverseOffset Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetReverseOffset.html)
[IExtrudeFeatureData2::GetTranslateSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetTranslateSurface.html)
[IExtrudeFeatureData2::SetTranslateSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetTranslateSurface.html)
[IExtrudeFeatureData2::FromOffsetDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromOffsetDistance.html)
[IExtrudeFeatureData2::FromOffsetReverse Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromOffsetReverse.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
