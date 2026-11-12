---
title: "CurrentProfileType Property (ICostAnalysisStructural)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisStructural"
member: "CurrentProfileType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~CurrentProfileType.html"
---

# CurrentProfileType Property (ICostAnalysisStructural)

Gets the profile type of the weldment used in this structural Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurrentProfileType As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisStructural
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

[ICostAnalysisStructural Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html)
[ICostAnalysisStructural Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural_members.html)
[ICostAnalysisStructural::SetCurrentProfile Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~SetCurrentProfile.html)
[ICostAnalysisStructural::CurrentProfileSize Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~CurrentProfileSize.html)
[ICostAnalysisStructural::CurrentProfileStandard Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~CurrentProfileStandard.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
