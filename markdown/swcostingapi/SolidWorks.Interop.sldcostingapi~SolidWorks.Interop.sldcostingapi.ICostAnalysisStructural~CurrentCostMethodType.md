---
title: "CurrentCostMethodType Property (ICostAnalysisStructural)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisStructural"
member: "CurrentCostMethodType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~CurrentCostMethodType.html"
---

# CurrentCostMethodType Property (ICostAnalysisStructural)

Gets or sets the structural stock cost method in the Costing analysis for this structural Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentCostMethodType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisStructural
Dim value As System.Integer

instance.CurrentCostMethodType = value

value = instance.CurrentCostMethodType
```

### C#

```csharp
System.int CurrentCostMethodType {get; set;}
```

### C++/CLI

```cpp
property System.int CurrentCostMethodType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of structural stock cost method as defined by [swcStructuralStockCostType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcStructuralStockCostType_e.html)

## VBA Syntax

See [CostAnalysisStructural::CurrentCostMethodType](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisStructural~CurrentCostMethodType.html).

## Examples

See the [ICostAnalysisStructural](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html) examples.

## Remarks

Setting of a structural stock cost method must match the data in the template. For example, if the **cost per unit length** option is not available in the template, then setting this method to swcStructuralStockCostType_e.swcStructuralStockCost_PerUnitLength fails.

## See Also

[ICostAnalysisStructural Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html)
[ICostAnalysisStructural Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural_members.html)
[ICostAnalysisStructural::CurrentStockUnitLength Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~CurrentStockUnitLength.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
