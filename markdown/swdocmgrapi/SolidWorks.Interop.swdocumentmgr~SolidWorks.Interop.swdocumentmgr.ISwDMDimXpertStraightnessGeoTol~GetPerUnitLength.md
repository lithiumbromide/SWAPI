---
title: "GetPerUnitLength Method (ISwDMDimXpertStraightnessGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertStraightnessGeoTol"
member: "GetPerUnitLength"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertStraightnessGeoTol~GetPerUnitLength.html"
---

# GetPerUnitLength Method (ISwDMDimXpertStraightnessGeoTol)

Gets the per unit length for this DimXpert straightness geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPerUnitLength( _
   ByRef Enabled As System.Boolean, _
   ByRef Distance As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertStraightnessGeoTol
Dim Enabled As System.Boolean
Dim Distance As System.Double
Dim value As System.Boolean

value = instance.GetPerUnitLength(Enabled, Distance)
```

### C#

```csharp
System.bool GetPerUnitLength(
   out System.bool Enabled,
   out System.double Distance
)
```

### C++/CLI

```cpp
System.bool GetPerUnitLength(
   [Out] System.bool Enabled,
   [Out] System.double Distance
)
```

### Parameters

- `Enabled`: True if per unit length straightness tolerance is in effect; false if not
- `Distance`: Length for per unit length

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertStraightnessGeoTol::GetPerUnitLength](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertStraightnessGeoTol~GetPerUnitLength.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertStraightnessGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertStraightnessGeoTol.html)
[ISwDMDimXpertStraightnessGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertStraightnessGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
