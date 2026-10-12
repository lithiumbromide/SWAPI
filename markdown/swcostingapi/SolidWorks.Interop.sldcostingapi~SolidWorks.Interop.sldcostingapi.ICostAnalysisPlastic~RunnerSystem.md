---
title: "RunnerSystem Property (ICostAnalysisPlastic)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisPlastic"
member: "RunnerSystem"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~RunnerSystem.html"
---

# RunnerSystem Property (ICostAnalysisPlastic)

Gets or sets the runner system for this plastic Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property RunnerSystem As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisPlastic
Dim value As System.Integer

instance.RunnerSystem = value

value = instance.RunnerSystem
```

### C#

```csharp
System.int RunnerSystem {get; set;}
```

### C++/CLI

```cpp
property System.int RunnerSystem {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Runner system as defined in [swcRunnerSystem_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcRunnerSystem_e.html)

## VBA Syntax

See [CostAnalysisPlastic::RunnerSystem](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisPlastic~RunnerSystem.html).

## Examples

See the [ICostAnalysisPlastic](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html) examples.

## See Also

[ICostAnalysisPlastic Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html)
[ICostAnalysisPlastic Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
