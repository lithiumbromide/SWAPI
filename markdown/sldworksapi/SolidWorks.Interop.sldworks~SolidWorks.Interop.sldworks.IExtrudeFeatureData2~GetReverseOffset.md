---
title: "GetReverseOffset Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "GetReverseOffset"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetReverseOffset.html"
---

# GetReverseOffset Method (IExtrudeFeatureData2)

Gets the offset direction for this extrude feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReverseOffset( _
   ByVal Fwd As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim Fwd As System.Boolean
Dim value As System.Boolean

value = instance.GetReverseOffset(Fwd)
```

### C#

```csharp
System.bool GetReverseOffset(
   System.bool Fwd
)
```

### C++/CLI

```cpp
System.bool GetReverseOffset(
   System.bool Fwd
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Fwd`: True gets the reverse offset setting in the forward direction, false gets it in the reverse direction

### Return Value

True if the reverse offset setting is enabled, false if it is disabled

## VBA Syntax

See [ExtrudeFeatureData2::GetReverseOffset](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~GetReverseOffset.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::SetReverseOffset Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetReverseOffset.html)
[IExtrudeFeatureData2::FromOffsetReverse Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromOffsetReverse.html)
[IExtrudeFeatureData2::FromOffsetDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromOffsetDistance.html)
[IExtrudeFeatureData2::GetTranslateSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetTranslateSurface.html)
[IExtrudeFeatureData2::SetTranslateSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetTranslateSurface.html)

## Availability

SOLIDWORKS 2003 FCS, Revisioin Number 11.0
