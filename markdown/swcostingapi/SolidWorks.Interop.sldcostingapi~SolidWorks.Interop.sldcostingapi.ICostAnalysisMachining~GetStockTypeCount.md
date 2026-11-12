---
title: "GetStockTypeCount Method (ICostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisMachining"
member: "GetStockTypeCount"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetStockTypeCount.html"
---

# GetStockTypeCount Method (ICostAnalysisMachining)

Gets the number of stock types for the specified material from the Costing template for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStockTypeCount( _
   ByVal MaterialClass As System.String, _
   ByVal MaterialName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisMachining
Dim MaterialClass As System.String
Dim MaterialName As System.String
Dim value As System.Integer

value = instance.GetStockTypeCount(MaterialClass, MaterialName)
```

### C#

```csharp
System.int GetStockTypeCount(
   System.string MaterialClass,
   System.string MaterialName
)
```

### C++/CLI

```cpp
System.int GetStockTypeCount(
   System.String^ MaterialClass,
   System.String^ MaterialName
)
```

### Parameters

- `MaterialClass`: Name of the material class
- `MaterialName`: Name of the material

### Return Value

Number of stock types for the specified material

## VBA Syntax

See [CostAnalysisMachining::GetStockTypeCount](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~GetStockTypeCount.html).

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html)
[ICostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining_members.html)
[ICostAnalysisMachining::GetStockTypes Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetStockTypes.html)
[ICostAnalysisMachining::IGetStockTypes Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IGetStockTypes.html)
[ICostAnalysisMachining::GetMaterialClasses ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetMaterialClasses.html)
[ICostAnalysisMachining::GetMaterials Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetMaterials.html)
[ICostAnalysisMachining::IGetMaterialClasses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IGetMaterialClasses.html)
[ICostAnalysisMachining::IGetMaterials Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IGetMaterials.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
