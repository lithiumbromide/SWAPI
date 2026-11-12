---
title: "GetMaterials Method (ICostAnalysisStructural)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisStructural"
member: "GetMaterials"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~GetMaterials.html"
---

# GetMaterials Method (ICostAnalysisStructural)

Gets the names of the materials in the specified class from the Costing template for this structural Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterials( _
   ByVal ClassName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisStructural
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

See [CostAnalysisStructural::GetMaterials](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisStructural~GetMaterials.html).

## Examples

See the [ICostAnalysisStructural](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html) examples.

## See Also

[ICostAnalysisStructural Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html)
[ICostAnalysisStructural Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural_members.html)
[ICostAnalysisStructural::GetMaterialClasses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~GetMaterialClasses.html)
[ICostAnalysisStructural::GetMaterialClassesCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~GetMaterialClassesCount.html)
[ICostAnalysisStructural::GetMaterialCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~GetMaterialCount.html)
[ICostAnalysisStructural::CurrentMaterial Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~CurrentMaterial.html)
[ICostAnalysisStructural::CurrentMaterialClass Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~CurrentMaterialClass.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
