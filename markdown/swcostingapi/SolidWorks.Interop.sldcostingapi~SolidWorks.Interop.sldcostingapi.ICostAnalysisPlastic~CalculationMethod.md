---
title: "CalculationMethod Property (ICostAnalysisPlastic)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisPlastic"
member: "CalculationMethod"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~CalculationMethod.html"
---

# CalculationMethod Property (ICostAnalysisPlastic)

Gets or sets the calculation method for this plastic Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CalculationMethod As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisPlastic
Dim value As System.Integer

instance.CalculationMethod = value

value = instance.CalculationMethod
```

### C#

```csharp
System.int CalculationMethod {get; set;}
```

### C++/CLI

```cpp
property System.int CalculationMethod {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Calculation method as defined in [swcMoldCalculationMethod_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcMoldCalculationMethod_e.html)

## VBA Syntax

See [CostAnalysisPlastic::CalculationMethod](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisPlastic~CalculationMethod.html).

## Examples

See the [ICostAnalysisPlastic](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html) examples.

## See Also

[ICostAnalysisPlastic Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html)
[ICostAnalysisPlastic Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic_members.html)
[ICostAnalysisPlastic::MaxWallThickness Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~MaxWallThickness.html)
[ICostAnalysisPlastic::CycleTime Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~CycleTime.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
