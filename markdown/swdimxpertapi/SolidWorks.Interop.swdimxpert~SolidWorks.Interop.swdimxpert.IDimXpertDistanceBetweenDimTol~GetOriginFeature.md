---
title: "GetOriginFeature Method (IDimXpertDistanceBetweenDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertDistanceBetweenDimTol"
member: "GetOriginFeature"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDistanceBetweenDimTol~GetOriginFeature.html"
---

# GetOriginFeature Method (IDimXpertDistanceBetweenDimTol)

Gets the origin feature for this DimXpert distance-between dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOriginFeature( _
   ByRef Feature As DimXpertFeature, _
   ByRef FosUsage As swDimXpertDistanceFosUsage_e _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertDistanceBetweenDimTol
Dim Feature As DimXpertFeature
Dim FosUsage As swDimXpertDistanceFosUsage_e
Dim value As System.Boolean

value = instance.GetOriginFeature(Feature, FosUsage)
```

### C#

```csharp
System.bool GetOriginFeature(
   out DimXpertFeature Feature,
   out swDimXpertDistanceFosUsage_e FosUsage
)
```

### C++/CLI

```cpp
System.bool GetOriginFeature(
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

See [DimXpertDistanceBetweenDimTol::GetOriginFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertDistanceBetweenDimTol~GetOriginFeature.html).

## Examples

[Get and Set Location Dimension Example (C#)](Get_and_Set_Location_Dimension_Example_CSharp.htm)
[Get and Set Location Dimension Example (VB.NET)](Get_and_Set_Location_Dimension_Example_VBNET.htm)
[Get and Set Location Dimension Example (VBA)](Get_and_Set_Location_Dimension_Example_VB.htm)
[Get DimXpert Tolerance2 Example (VBA)](Get_DimXpert_Tolerance2_Example_VB.htm)
[Get DimXpert Tolerance2 Example (VB.NET)](Get_DimXpert_Tolerance2_Example_VBNET.htm)

## See Also

[IDimXpertDistanceBetweenDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDistanceBetweenDimTol.html)
[IDimXpertDistanceBetweenDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDistanceBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
