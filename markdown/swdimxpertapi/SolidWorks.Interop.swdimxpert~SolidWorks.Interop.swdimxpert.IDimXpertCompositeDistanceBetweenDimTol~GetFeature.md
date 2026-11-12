---
title: "GetFeature Method (IDimXpertCompositeDistanceBetweenDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositeDistanceBetweenDimTol"
member: "GetFeature"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol~GetFeature.html"
---

# GetFeature Method (IDimXpertCompositeDistanceBetweenDimTol)

Gets the feature to which this DimXpert composite distance-between dimension tolerance is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeature( _
   ByRef Feature As DimXpertFeature, _
   ByRef FosUsage As swDimXpertDistanceFosUsage_e _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompositeDistanceBetweenDimTol
Dim Feature As DimXpertFeature
Dim FosUsage As swDimXpertDistanceFosUsage_e
Dim value As System.Boolean

value = instance.GetFeature(Feature, FosUsage)
```

### C#

```csharp
System.bool GetFeature(
   out DimXpertFeature Feature,
   out swDimXpertDistanceFosUsage_e FosUsage
)
```

### C++/CLI

```cpp
System.bool GetFeature(
   [Out] DimXpertFeature^ Feature,
   [Out] swDimXpertDistanceFosUsage_e FosUsage
)
```

### Parameters

- `Feature`: [IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)
- `FosUsage`: Feature of size usage as defined in [swDimXpertDistanceFosUsage_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertDistanceFosUsage_e.html)

### Return Value

True if the method call is successful; false otherwise

## VBA Syntax

See [DimXpertCompositeDistanceBetweenDimTol::GetFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositeDistanceBetweenDimTol~GetFeature.html).

## Examples

[Get DimXpert Tolerance2 Example (VBA)](Get_DimXpert_Tolerance2_Example_VB.htm)
[Get DimXpert Tolerance2 Example (VB.NET)](Get_DimXpert_Tolerance2_Example_VBNET.htm)

## See Also

[IDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol.html)
[IDimXpertCompositeDistanceBetweenDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
