---
title: "GetStockTypes Method (CostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisMachining"
member: "GetStockTypes"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining~GetStockTypes.html"
---

# GetStockTypes Method (CostAnalysisMachining)

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
Dim instance As CostAnalysisMachining
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

[CostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining.html)
[CostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
