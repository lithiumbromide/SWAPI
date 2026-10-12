---
title: "GetMaterials Method (ICostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisMachining"
member: "GetMaterials"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetMaterials.html"
---

# GetMaterials Method (ICostAnalysisMachining)

Gets the names of the materials in the specified class from the Costing template for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterials( _
   ByVal ClassName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisMachining
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

- `ClassName`: Name of material class

### Return Value

Array of strings of the names of the materials in the specified class

## VBA Syntax

See [CostAnalysisMachining::GetMaterials](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~GetMaterials.html).

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html)
[ICostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining_members.html)
[ICostAnalysisMachining::GetMaterialCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetMaterialCount.html)
[ICostAnalysisMachining::IGetMaterials Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IGetMaterials.html)
[ICostAnalysisMachining::CurrentMaterial Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CurrentMaterial.html)
[ICostAnalysisMachining::GetMaterialClasses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetMaterialClasses.html)
[ICostAnalysisMachining::IGetMaterialClasses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IGetMaterialClasses.html)
[ICostAnalysisMachining::CurrentMaterialClass Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CurrentMaterialClass.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
