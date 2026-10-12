---
title: "GetMaterialCount Method (ICostAnalysisCasting)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisCasting"
member: "GetMaterialCount"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~GetMaterialCount.html"
---

# GetMaterialCount Method (ICostAnalysisCasting)

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
Dim instance As ICostAnalysisCasting
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

[ICostAnalysisCasting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting.html)
[ICostAnalysisCasting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting_members.html)
[ICostAnalysisCasting::GetMaterials Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~GetMaterials.html)
[ICostAnalysisCasting::CurrentMaterial Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~CurrentMaterial.html)
[ICostAnalysisCasting::GetMaterialClasses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~GetMaterialClasses.html)
[ICostAnalysisCasting::CurrentMaterialClass Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~CurrentMaterialClass.html)
[ICostAnalysisCasting::GetMaterialClassesCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~GetMaterialClassesCount.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
