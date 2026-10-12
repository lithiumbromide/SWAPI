---
title: "GetNominalVector Method (ISwDMDimXpertIntersectPointFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertIntersectPointFeature"
member: "GetNominalVector"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature~GetNominalVector.html"
---

# GetNominalVector Method (ISwDMDimXpertIntersectPointFeature)

Gets the direction vector of this DimXpert intersect point.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalVector( _
   ByRef I As System.Double, _
   ByRef J As System.Double, _
   ByRef K As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertIntersectPointFeature
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetNominalVector(I, J, K)
```

### C#

```csharp
System.bool GetNominalVector(
   out System.double I,
   out System.double J,
   out System.double K
)
```

### C++/CLI

```cpp
System.bool GetNominalVector(
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `I`: i component of the direction vector of the intersect point
- `J`: j component of the direction vector of the intersect point
- `K`: k component of the direction vector of the intersect point

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertIntersectPointFeature::GetNominalVector](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertIntersectPointFeature~GetNominalVector.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertIntersectPointFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature.html)
[ISwDMDimXpertIntersectPointFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
