---
title: "CurrentProfileStandard Property (CostAnalysisStructural)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisStructural"
member: "CurrentProfileStandard"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural~CurrentProfileStandard.html"
---

# CurrentProfileStandard Property (CostAnalysisStructural)

Gets the profile standard of the weldment used in this structural Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurrentProfileStandard As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisStructural
Dim value As System.String

value = instance.CurrentProfileStandard
```

### C#

```csharp
System.string CurrentProfileStandard {get;}
```

### C++/CLI

```cpp
property System.String^ CurrentProfileStandard {
   System.String^ get();
}
```

### Property Value

Profile standard

## VBA Syntax

See [CostAnalysisStructural::CurrentProfileStandard](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisStructural~CurrentProfileStandard.html).

## Examples

See the [ICostAnalysisStructural](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html) examples.

## Remarks

The profile standard is the name of a folder, typically located in **C:\Program Files\SolidWorks Corp\SOLIDWORKS**\**lang**\`lang`\**weldment profiles**.

## See Also

[CostAnalysisStructural Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural.html)
[CostAnalysisStructural Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
