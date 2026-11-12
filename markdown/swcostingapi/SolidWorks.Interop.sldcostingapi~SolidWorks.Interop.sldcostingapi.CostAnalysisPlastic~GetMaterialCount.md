---
title: "GetMaterialCount Method (CostAnalysisPlastic)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisPlastic"
member: "GetMaterialCount"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic~GetMaterialCount.html"
---

# GetMaterialCount Method (CostAnalysisPlastic)

Gets the number of materials in the specified material class from the Costing template for this plastic Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialCount( _
   ByVal ClassName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisPlastic
Dim ClassName As System.String
Dim value As System.Integer

value = instance.GetMaterialCount(ClassName)
```

### C#

```csharp
System.int GetMaterialCount(
   System.string ClassName
)
```

### C++/CLI

```cpp
System.int GetMaterialCount(
   System.String^ ClassName
)
```

### Parameters

- `ClassName`: Name of the material class

### Return Value

Number of materials in ClassName

## VBA Syntax

See [CostAnalysisPlastic::GetMaterialCount](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisPlastic~GetMaterialCount.html).

## Examples

See the [ICostAnalysisPlastic](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html) examples.

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostAnalysisPlastic Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic.html)
[CostAnalysisPlastic Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
