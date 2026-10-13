---
title: "GetMaterialClasses Method (ICostAnalysisStructural)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisStructural"
member: "GetMaterialClasses"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~GetMaterialClasses.html"
---

# GetMaterialClasses Method (ICostAnalysisStructural)

Gets the names of the material classes from the Costing template for this structural Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialClasses() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisStructural
Dim value As System.Object

value = instance.GetMaterialClasses()
```

### C#

```csharp
System.object GetMaterialClasses()
```

### C++/CLI

```cpp
System.Object^ GetMaterialClasses();
```

### Return Value

Array of strings of the names of the material classes

## VBA Syntax

See [CostAnalysisStructural::GetMaterialClasses](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisStructural~GetMaterialClasses.html).

## Examples

See the [ICostAnalysisStructural](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html) examples.

## See Also

[ICostAnalysisStructural Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html)
[ICostAnalysisStructural Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural_members.html)
[ICostAnalysisStructural::GetMaterialClassesCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~GetMaterialClassesCount.html)
[ICostAnalysisStructural::CurrentMaterialClass Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~CurrentMaterialClass.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
