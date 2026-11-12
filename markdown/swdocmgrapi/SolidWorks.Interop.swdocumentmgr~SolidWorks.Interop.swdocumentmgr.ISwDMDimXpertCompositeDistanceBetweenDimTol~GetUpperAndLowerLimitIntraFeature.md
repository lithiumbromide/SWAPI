---
title: "GetUpperAndLowerLimitIntraFeature Method (ISwDMDimXpertCompositeDistanceBetweenDimTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompositeDistanceBetweenDimTol"
member: "GetUpperAndLowerLimitIntraFeature"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~GetUpperAndLowerLimitIntraFeature.html"
---

# GetUpperAndLowerLimitIntraFeature Method (ISwDMDimXpertCompositeDistanceBetweenDimTol)

Gets the upper and lower tolerance limits used by the feature-locating portion of this DimXpert composite distance-between dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUpperAndLowerLimitIntraFeature( _
   ByRef Upper As System.Double, _
   ByRef Lower As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompositeDistanceBetweenDimTol
Dim Upper As System.Double
Dim Lower As System.Double
Dim value As System.Boolean

value = instance.GetUpperAndLowerLimitIntraFeature(Upper, Lower)
```

### C#

```csharp
System.bool GetUpperAndLowerLimitIntraFeature(
   out System.double Upper,
   out System.double Lower
)
```

### C++/CLI

```cpp
System.bool GetUpperAndLowerLimitIntraFeature(
   [Out] System.double Upper,
   [Out] System.double Lower
)
```

### Parameters

- `Upper`: Upper tolerance limit for feature-locating
- `Lower`: Lower tolerance limit for feature-locating

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertCompositeDistanceBetweenDimTol::GetUpperAndLowerLimitIntraFeature](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompositeDistanceBetweenDimTol~GetUpperAndLowerLimitIntraFeature.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol.html)
[ISwDMDimXpertCompositeDistanceBetweenDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
