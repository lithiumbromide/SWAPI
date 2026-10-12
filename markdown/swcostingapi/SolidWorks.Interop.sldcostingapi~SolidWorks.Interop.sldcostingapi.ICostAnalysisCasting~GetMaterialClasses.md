---
title: "GetMaterialClasses Method (ICostAnalysisCasting)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisCasting"
member: "GetMaterialClasses"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~GetMaterialClasses.html"
---

# GetMaterialClasses Method (ICostAnalysisCasting)

Gets the names of the material classes from the Costing template for this casting Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialClasses() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisCasting
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

See [CostAnalysisCasting::GetMaterialClasses](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisCasting~GetMaterialClasses.html).

## Examples

See the [ICostAnalysisCasting](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting.html) examples.

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostAnalysisCasting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting.html)
[ICostAnalysisCasting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting_members.html)
[ICostAnalysisCasting::GetMaterialClassesCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~GetMaterialClassesCount.html)
[ICostAnalysisCasting::CurrentMaterialClass Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~CurrentMaterialClass.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
