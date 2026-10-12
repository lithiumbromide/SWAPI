---
title: "GetMaterials Method (CostAnalysisCasting)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisCasting"
member: "GetMaterials"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisCasting~GetMaterials.html"
---

# GetMaterials Method (CostAnalysisCasting)

Gets the names of the materials in the specified class from the Costing template for this casting Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterials( _
   ByVal ClassName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisCasting
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

See [CostAnalysisCasting::GetMaterials](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisCasting~GetMaterials.html).

## Examples

See the [ICostAnalysisCasting](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting.html) examples.

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostAnalysisCasting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisCasting.html)
[CostAnalysisCasting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisCasting_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
