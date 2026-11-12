---
title: "GetProjectedZone Method (ISwDMDimXpertCompositePositionGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompositePositionGeoTol"
member: "GetProjectedZone"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol~GetProjectedZone.html"
---

# GetProjectedZone Method (ISwDMDimXpertCompositePositionGeoTol)

Gets the projected zone value of this DimXpert composite position geometric tolerance.

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
Dim instance As ISwDMDimXpertCompositePositionGeoTol
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

- `Enabled`: True, if the projected zone is in effect; false, otherwise
- `Value`: Composite position projected zone value

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertCompositePositionGeoTol::GetProjectedZone](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompositePositionGeoTol~GetProjectedZone.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompositePositionGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol.html)
[ISwDMDimXpertCompositePositionGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
