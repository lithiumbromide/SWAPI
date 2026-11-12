---
title: "GetMaterialClasses Method (ICostAnalysisPlastic)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisPlastic"
member: "GetMaterialClasses"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~GetMaterialClasses.html"
---

# GetMaterialClasses Method (ICostAnalysisPlastic)

Gets the names of the material classes from the Costing template for this plastic Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialClasses() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisPlastic
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

See [CostAnalysisPlastic::GetMaterialClasses](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisPlastic~GetMaterialClasses.html).

## Examples

See the [ICostAnalysisPlastic](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html) examples.

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostAnalysisPlastic Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html)
[ICostAnalysisPlastic Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic_members.html)
[ICostAnalysisPlastic::GetMaterialClassesCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~GetMaterialClassesCount.html)
[ICostAnalysisPlastic::CurrentMaterialClass Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~CurrentMaterialClass.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
