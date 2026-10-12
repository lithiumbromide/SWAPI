---
title: "GetStockTypes Method (ICostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisMachining"
member: "GetStockTypes"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetStockTypes.html"
---

# GetStockTypes Method (ICostAnalysisMachining)

Gets the stock types for the specified material from the Costing template for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStockTypes( _
   ByVal MaterialClass As System.String, _
   ByVal MaterialName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisMachining
Dim MaterialClass As System.String
Dim MaterialName As System.String
Dim value As System.Object

value = instance.GetStockTypes(MaterialClass, MaterialName)
```

### C#

```csharp
System.object GetStockTypes(
   System.string MaterialClass,
   System.string MaterialName
)
```

### C++/CLI

```cpp
System.Object^ GetStockTypes(
   System.String^ MaterialClass,
   System.String^ MaterialName
)
```

### Parameters

- `MaterialClass`: Name of the material class
- `MaterialName`: Name of the material

### Return Value

Array of integers, or longs if using VBA, of the stock types of the specified material as defined in [swcStockType_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcStockType_e.html)

## VBA Syntax

See [CostAnalysisMachining::GetStockTypes](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~GetStockTypes.html).

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html)
[ICostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining_members.html)
[ICostAnalysisMachining::IGetStockTypes Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IGetStockTypes.html)
[ICostAnalysisMachining::GetStockTypeCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetStockTypeCount.html)
[ICostAnalysisMachining::CurrentStockType Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CurrentStockType.html)
[ICostAnalysisMachining::GetMaterialClasses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetMaterialClasses.html)
[ICostAnalysisMachining::GetMaterials Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetMaterials.html)
[ICostAnalysisMachining::IGetMaterialClasses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IGetMaterialClasses.html)
[ICostAnalysisMachining::IGetMaterials Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IGetMaterials.html)
[ICostAnalysisMachining::CustomStockImportType Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CustomStockImportType.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
