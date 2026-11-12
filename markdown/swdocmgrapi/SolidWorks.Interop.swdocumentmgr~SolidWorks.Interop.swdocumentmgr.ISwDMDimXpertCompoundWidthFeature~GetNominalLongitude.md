---
title: "GetNominalLongitude Method (ISwDMDimXpertCompoundWidthFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompoundWidthFeature"
member: "GetNominalLongitude"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature~GetNominalLongitude.html"
---

# GetNominalLongitude Method (ISwDMDimXpertCompoundWidthFeature)

Gets the longitudinal vector for this DimXpert compound width.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalLongitude( _
   ByRef I As System.Double, _
   ByRef J As System.Double, _
   ByRef K As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompoundWidthFeature
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetNominalLongitude(I, J, K)
```

### C#

```csharp
System.bool GetNominalLongitude(
   out System.double I,
   out System.double J,
   out System.double K
)
```

### C++/CLI

```cpp
System.bool GetNominalLongitude(
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `I`: i component of longitudinal unit vector of compound width
- `J`: j component of longitudinal unit vector of compound width
- `K`: k component of longitudinal unit vector of compound width

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertCompoundWidthFeature::GetNominalLongitude](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompoundWidthFeature~GetNominalLongitude.html).

## Examples

See the examples on the interface page.

## Remarks

The i, j, and k components of the longitudinal vector indicate the direction of a feature's length with respect to its part axes. For example, if the length of a feature goes along the y-axis of the part, its longitudinal vector is (0, 1, 0).

## See Also

[ISwDMDimXpertCompoundWidthFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature.html)
[ISwDMDimXpertCompoundWidthFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
