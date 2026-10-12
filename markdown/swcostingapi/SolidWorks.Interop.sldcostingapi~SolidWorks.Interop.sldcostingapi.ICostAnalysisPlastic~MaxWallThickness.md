---
title: "MaxWallThickness Property (ICostAnalysisPlastic)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisPlastic"
member: "MaxWallThickness"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~MaxWallThickness.html"
---

# MaxWallThickness Property (ICostAnalysisPlastic)

Gets or sets the maximum wall thickness for this plastic Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaxWallThickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisPlastic
Dim value As System.Double

instance.MaxWallThickness = value

value = instance.MaxWallThickness
```

### C#

```csharp
System.double MaxWallThickness {get; set;}
```

### C++/CLI

```cpp
property System.double MaxWallThickness {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Maximum wall thickness in meters; valid for use in calculations only if [ICostAnalysis::CalculationMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~CalculationMethod.html) is set to swcMoldCalculationMethod_e.swMoldCalculationMethod_WallThickness

## VBA Syntax

See [CostAnalysisPlastic::MaxWallThickness](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisPlastic~MaxWallThickness.html).

## Examples

See the [ICostAnalysisPlastic](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html) examples.

## Remarks

## See Also

[ICostAnalysisPlastic Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html)
[ICostAnalysisPlastic Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic_members.html)
[ICostAnalysisPlastic::CycleTime Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~CycleTime.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
