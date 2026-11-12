---
title: "GetMaxTolerance Method (ISwDMDimXpertSymmetryGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertSymmetryGeoTol"
member: "GetMaxTolerance"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSymmetryGeoTol~GetMaxTolerance.html"
---

# GetMaxTolerance Method (ISwDMDimXpertSymmetryGeoTol)

Gets the maximum tolerance for this DimXpert symmetry geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaxTolerance( _
   ByRef IsMax As System.Boolean, _
   ByRef Tolerance As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertSymmetryGeoTol
Dim IsMax As System.Boolean
Dim Tolerance As System.Double
Dim value As System.Boolean

value = instance.GetMaxTolerance(IsMax, Tolerance)
```

### C#

```csharp
System.bool GetMaxTolerance(
   out System.bool IsMax,
   out System.double Tolerance
)
```

### C++/CLI

```cpp
System.bool GetMaxTolerance(
   [Out] System.bool IsMax,
   [Out] System.double Tolerance
)
```

### Parameters

- `IsMax`: True, if maximum tolerance is set; false, otherwise
- `Tolerance`: Maximum tolerance

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertSymmetryGeoTol::GetMaxTolerance](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertSymmetryGeoTol~GetMaxTolerance.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertSymmetryGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSymmetryGeoTol.html)
[ISwDMDimXpertSymmetryGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSymmetryGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
