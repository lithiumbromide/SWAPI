---
title: "CurrentProfileSize Property (ICostAnalysisStructural)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisStructural"
member: "CurrentProfileSize"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~CurrentProfileSize.html"
---

# CurrentProfileSize Property (ICostAnalysisStructural)

Gets the profile size of the weldment used in this structural Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurrentProfileSize As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisStructural
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

[ICostAnalysisStructural Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html)
[ICostAnalysisStructural Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural_members.html)
[ICostAnalysisStructural::SetCurrentProfile Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~SetCurrentProfile.html)
[ICostAnalysisStructural::CurrentProfileStandard Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~CurrentProfileStandard.html)
[ICostAnalysisStructural::CurrentProfileType Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~CurrentProfileType.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
