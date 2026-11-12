---
title: "GetMaterialClasses Method (ICostAnalysis3dPrinting)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis3dPrinting"
member: "GetMaterialClasses"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting~GetMaterialClasses.html"
---

# GetMaterialClasses Method (ICostAnalysis3dPrinting)

Gets the names of the material classes from the Costing template for this 3D printing Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialClasses() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis3dPrinting
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

See [CostAnalysis3dPrinting::GetMaterialClasses](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis3dPrinting~GetMaterialClasses.html).

## Examples

See the [ICostAnalysis3dPrinting](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting.html) examples.

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostAnalysis3dPrinting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting.html)
[ICostAnalysis3dPrinting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting_members.html)
[ICostAnalysis3dPrinting::GetMaterialClassesCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting~GetMaterialClassesCount.html)
[ICostAnalysis3dPrinting::CurrentMaterialClass Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting~CurrentMaterialClass.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
