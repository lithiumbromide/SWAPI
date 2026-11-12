---
title: "GetMaterials Method (CostAnalysisPlastic)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisPlastic"
member: "GetMaterials"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic~GetMaterials.html"
---

# GetMaterials Method (CostAnalysisPlastic)

Gets the names of the materials in the specified class from the Costing template for this plastic Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterials( _
   ByVal ClassName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisPlastic
Dim ClassName As System.String
Dim value As System.Object

value = instance.GetMaterials(ClassName)
```

### C#

```csharp
System.object GetMaterials(
   System.string ClassName
)
```

### C++/CLI

```cpp
System.Object^ GetMaterials(
   System.String^ ClassName
)
```

### Parameters

- `ClassName`: Name of the material class

### Return Value

Array of strings of the names of the materials in ClassName

## VBA Syntax

See [CostAnalysisPlastic::GetMaterials](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisPlastic~GetMaterials.html).

## Examples

See the [ICostAnalysisPlastic](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html) examples.

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostAnalysisPlastic Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic.html)
[CostAnalysisPlastic Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
