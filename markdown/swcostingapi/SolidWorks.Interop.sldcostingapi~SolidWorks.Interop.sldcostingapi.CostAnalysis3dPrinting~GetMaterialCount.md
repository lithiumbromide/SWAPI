---
title: "GetMaterialCount Method (CostAnalysis3dPrinting)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysis3dPrinting"
member: "GetMaterialCount"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis3dPrinting~GetMaterialCount.html"
---

# GetMaterialCount Method (CostAnalysis3dPrinting)

Gets the number of materials in the specified material class from the Costing template for this 3D printing Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialCount( _
   ByVal ClassName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysis3dPrinting
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

See [CostAnalysis3dPrinting::GetMaterialCount](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis3dPrinting~GetMaterialCount.html).

## Examples

See the [ICostAnalysis3dPrinting](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting.html) examples.

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostAnalysis3dPrinting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis3dPrinting.html)
[CostAnalysis3dPrinting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis3dPrinting_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
