---
title: "GetPlusAndMinusToleranceIntraFeature Method (IDimXpertCompositeDistanceBetweenDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositeDistanceBetweenDimTol"
member: "GetPlusAndMinusToleranceIntraFeature"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol~GetPlusAndMinusToleranceIntraFeature.html"
---

# GetPlusAndMinusToleranceIntraFeature Method (IDimXpertCompositeDistanceBetweenDimTol)

Gets the plus and minus tolerance values for the feature-locating portion of this DimXpert composite distance-between dimension tolerance.

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
Dim instance As IDimXpertCompositeDistanceBetweenDimTol
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

- `Plus`: Plus tolerance value
- `Minus`: Minus tolerance value

### Return Value

True if the method call is successful; false otherwise

## VBA Syntax

See [DimXpertCompositeDistanceBetweenDimTol::GetPlusAndMinusToleranceIntraFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositeDistanceBetweenDimTol~GetPlusAndMinusToleranceIntraFeature.html).

## Examples

[Get DimXpert Tolerance2 Example (VBA)](Get_DimXpert_Tolerance2_Example_VB.htm)
[Get DimXpert Tolerance2 Example (VB.NET)](Get_DimXpert_Tolerance2_Example_VBNET.htm)

## See Also

[IDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol.html)
[IDimXpertCompositeDistanceBetweenDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
