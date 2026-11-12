---
title: "GetMaterialCount Method (CostAnalysisCasting)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisCasting"
member: "GetMaterialCount"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisCasting~GetMaterialCount.html"
---

# GetMaterialCount Method (CostAnalysisCasting)

Gets the number of materials in the specified material class from the Costing template for this casting Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialCount( _
   ByVal ClassName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisCasting
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

See [CostAnalysisCasting::GetMaterialCount](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisCasting~GetMaterialCount.html).

## Examples

See the [ICostAnalysisCasting](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting.html) examples.

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostAnalysisCasting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisCasting.html)
[CostAnalysisCasting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisCasting_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
