---
title: "CurrentProfileSize Property (CostAnalysisStructural)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisStructural"
member: "CurrentProfileSize"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural~CurrentProfileSize.html"
---

# CurrentProfileSize Property (CostAnalysisStructural)

Gets the profile size of the weldment used in this structural Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurrentProfileSize As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisStructural
Dim value As System.String

value = instance.CurrentProfileSize
```

### C#

```csharp
System.string CurrentProfileSize {get;}
```

### C++/CLI

```cpp
property System.String^ CurrentProfileSize {
   System.String^ get();
}
```

### Property Value

Profile size

## VBA Syntax

See [CostAnalysisStructural::CurrentProfileSize](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisStructural~CurrentProfileSize.html).

## Examples

See the [ICostAnalysisStructural](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html) examples.

## Remarks

The profile size is the name of a file, excluding the filename extension, typically located in **C:\Program Files\SolidWorks Corp\SOLIDWORKS**\**lang**\`lang`\**weldment profiles\**`profile standard\profile type`.

## See Also

[CostAnalysisStructural Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural.html)
[CostAnalysisStructural Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
