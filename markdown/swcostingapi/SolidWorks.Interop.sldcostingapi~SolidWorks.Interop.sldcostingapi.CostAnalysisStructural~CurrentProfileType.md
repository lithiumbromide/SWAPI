---
title: "CurrentProfileType Property (CostAnalysisStructural)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisStructural"
member: "CurrentProfileType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural~CurrentProfileType.html"
---

# CurrentProfileType Property (CostAnalysisStructural)

Gets the profile type of the weldment used in this structural Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurrentProfileType As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisStructural
Dim value As System.String

value = instance.CurrentProfileType
```

### C#

```csharp
System.string CurrentProfileType {get;}
```

### C++/CLI

```cpp
property System.String^ CurrentProfileType {
   System.String^ get();
}
```

### Property Value

Profile type

## VBA Syntax

See [CostAnalysisStructural::CurrentProfileType](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisStructural~CurrentProfileType.html).

## Examples

See the [ICostAnalysisStructural](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html) examples.

## Remarks

The profile type is the name of a profiles type folder, typically located in **C:\Program Files\SolidWorks Corp\SOLIDWORKS**\**lang**\`lang`\**weldment profiles\**`profile standard.`

## See Also

[CostAnalysisStructural Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural.html)
[CostAnalysisStructural Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
