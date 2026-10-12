---
title: "GetPlusAndMinusToleranceIntraFeature Method (ISwDMDimXpertCompositeDistanceBetweenDimTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompositeDistanceBetweenDimTol"
member: "GetPlusAndMinusToleranceIntraFeature"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~GetPlusAndMinusToleranceIntraFeature.html"
---

# GetPlusAndMinusToleranceIntraFeature Method (ISwDMDimXpertCompositeDistanceBetweenDimTol)

Gets the plus and minus tolerance values used by the feature-locating portion of this DimXpert composite distance-between dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlusAndMinusToleranceIntraFeature( _
   ByRef Plus As System.Double, _
   ByRef Minus As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompositeDistanceBetweenDimTol
Dim Plus As System.Double
Dim Minus As System.Double
Dim value As System.Boolean

value = instance.GetPlusAndMinusToleranceIntraFeature(Plus, Minus)
```

### C#

```csharp
System.bool GetPlusAndMinusToleranceIntraFeature(
   out System.double Plus,
   out System.double Minus
)
```

### C++/CLI

```cpp
System.bool GetPlusAndMinusToleranceIntraFeature(
   [Out] System.double Plus,
   [Out] System.double Minus
)
```

### Parameters

- `Plus`: Plus tolerance value for feature-locating
- `Minus`: Minus tolerance value for feature-locating

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertCompositeDistanceBetweenDimTol::GetPlusAndMinusToleranceIntraFeature](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompositeDistanceBetweenDimTol~GetPlusAndMinusToleranceIntraFeature.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol.html)
[ISwDMDimXpertCompositeDistanceBetweenDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
