---
title: "GetProjectedZone Method (ISwDMDimXpertPositionGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertPositionGeoTol"
member: "GetProjectedZone"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol~GetProjectedZone.html"
---

# GetProjectedZone Method (ISwDMDimXpertPositionGeoTol)

Gets the projected zone value of this DimXpert position geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProjectedZone( _
   ByRef Enabled As System.Boolean, _
   ByRef Value As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertPositionGeoTol
Dim Enabled As System.Boolean
Dim Value As System.Double
Dim value As System.Boolean

value = instance.GetProjectedZone(Enabled, Value)
```

### C#

```csharp
System.bool GetProjectedZone(
   out System.bool Enabled,
   out System.double Value
)
```

### C++/CLI

```cpp
System.bool GetProjectedZone(
   [Out] System.bool Enabled,
   [Out] System.double Value
)
```

### Parameters

- `Enabled`: True if the projected zone is in effect; false otherwise
- `Value`: Position projected zone value

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertPositionGeoTol::GetProjectedZone](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertPositionGeoTol~GetProjectedZone.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertPositionGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol.html)
[ISwDMDimXpertPositionGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
