---
title: "GetPerUnitArea Method (ISwDMDimXpertFlatnessGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertFlatnessGeoTol"
member: "GetPerUnitArea"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFlatnessGeoTol~GetPerUnitArea.html"
---

# GetPerUnitArea Method (ISwDMDimXpertFlatnessGeoTol)

Gets the per unit area of this flatness geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPerUnitArea( _
   ByRef Enabled As System.Boolean, _
   ByRef Length As System.Double, _
   ByRef width As System.Double, _
   ByRef I As System.Double, _
   ByRef J As System.Double, _
   ByRef K As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertFlatnessGeoTol
Dim Enabled As System.Boolean
Dim Length As System.Double
Dim width As System.Double
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetPerUnitArea(Enabled, Length, width, I, J, K)
```

### C#

```csharp
System.bool GetPerUnitArea(
   out System.bool Enabled,
   out System.double Length,
   out System.double width,
   out System.double I,
   out System.double J,
   out System.double K
)
```

### C++/CLI

```cpp
System.bool GetPerUnitArea(
   [Out] System.bool Enabled,
   [Out] System.double Length,
   [Out] System.double width,
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `Enabled`: True if per unit area flatness tolerance is in effect; false if not
- `Length`: Length for per unit area
- `width`: Width for per unit area
- `I`: i component of length direction vector used to compute flatness per unit area
- `J`: j component of length direction vector used to compute flatness per unit area
- `K`: k component of length direction vector used to compute flatness per unit area

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertFlatnessGeoTol::GetPerUnitArea](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertFlatnessGeoTol~GetPerUnitArea.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertFlatnessGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFlatnessGeoTol.html)
[ISwDMDimXpertFlatnessGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFlatnessGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
