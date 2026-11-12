---
title: "GetMaterials Method (ICostAnalysisCasting)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisCasting"
member: "GetMaterials"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~GetMaterials.html"
---

# GetMaterials Method (ICostAnalysisCasting)

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
Dim instance As ICostAnalysisCasting
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

[ICostAnalysisCasting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting.html)
[ICostAnalysisCasting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting_members.html)
[ICostAnalysisCasting::GetMaterialCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~GetMaterialCount.html)
[ICostAnalysisCasting::GetMaterialClasses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~GetMaterialClasses.html)
[ICostAnalysisCasting::CurrentMaterial Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~CurrentMaterial.html)
[ICostAnalysisCasting::CurrentMaterialClass Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~CurrentMaterialClass.html)
[ICostAnalysisCasting::GetMaterialClassesCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~GetMaterialClassesCount.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
