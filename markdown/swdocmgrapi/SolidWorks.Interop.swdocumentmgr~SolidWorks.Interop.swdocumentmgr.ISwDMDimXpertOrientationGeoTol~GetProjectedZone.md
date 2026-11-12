---
title: "GetProjectedZone Method (ISwDMDimXpertOrientationGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertOrientationGeoTol"
member: "GetProjectedZone"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol~GetProjectedZone.html"
---

# GetProjectedZone Method (ISwDMDimXpertOrientationGeoTol)

Gets the projected zone value of this DimXpert orientation geometric tolerance.

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
Dim instance As ISwDMDimXpertOrientationGeoTol
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
- `Value`: Orientation projected zone value

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertOrientationGeoTol::GetProjectedZone](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertOrientationGeoTol~GetProjectedZone.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertOrientationGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol.html)
[ISwDMDimXpertOrientationGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
