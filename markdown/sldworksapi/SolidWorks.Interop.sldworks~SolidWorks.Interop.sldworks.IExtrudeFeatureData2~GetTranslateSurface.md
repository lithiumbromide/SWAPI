---
title: "GetTranslateSurface Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "GetTranslateSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetTranslateSurface.html"
---

# GetTranslateSurface Method (IExtrudeFeatureData2)

Gets the translate surface setting for this extrude feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTranslateSurface( _
   ByVal Fwd As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim Fwd As System.Boolean
Dim value As System.Boolean

value = instance.GetTranslateSurface(Fwd)
```

### C#

```csharp
System.bool GetTranslateSurface(
   System.bool Fwd
)
```

### C++/CLI

```cpp
System.bool GetTranslateSurface(
   System.bool Fwd
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Fwd`: True makes the end of the extrusion a translation of the reference surface in the forward direction, false makes the end of the extrusion a translation of the reference surface in the reverse direction

### Return Value

True if the translate surface setting is enabled, false if it is disabled

## VBA Syntax

See [ExtrudeFeatureData2::GetTranslateSurface](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~GetTranslateSurface.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::SetTranslateSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetTranslateSurface.html)
[IExtrudeFeatureData2::FromOffsetDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromOffsetDistance.html)
[IExtrudeFeatureData2::GetReverseOffset Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetReverseOffset.html)
[IExtrudeFeatureData2::SetReverseOffset Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetReverseOffset.html)
[IExtrudeFeatureData2::FromOffsetReverse Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromOffsetReverse.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
