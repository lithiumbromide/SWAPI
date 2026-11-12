---
title: "GetIntraFeature Method (IDimXpertCompositeDistanceBetweenDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositeDistanceBetweenDimTol"
member: "GetIntraFeature"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol~GetIntraFeature.html"
---

# GetIntraFeature Method (IDimXpertCompositeDistanceBetweenDimTol)

Gets the feature located by the feature-locating portion of this DimXpert composite distance-between dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIntraFeature( _
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

value = instance.GetIntraFeature(Feature, FosUsage)
```

### C#

```csharp
System.bool GetIntraFeature(
   out DimXpertFeature Feature,
   out swDimXpertDistanceFosUsage_e FosUsage
)
```

### C++/CLI

```cpp
System.bool GetIntraFeature(
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

See [DimXpertCompositeDistanceBetweenDimTol::GetIntraFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositeDistanceBetweenDimTol~GetIntraFeature.html).

## Examples

[Get DimXpert Tolerance2 Example (VBA)](Get_DimXpert_Tolerance2_Example_VB.htm)
[Get DimXpert Tolerance2 Example (VB.NET)](Get_DimXpert_Tolerance2_Example_VBNET.htm)

## See Also

[IDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol.html)
[IDimXpertCompositeDistanceBetweenDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
