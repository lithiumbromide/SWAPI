---
title: "IGetMaterials Method (ICostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisSheetMetal"
member: "IGetMaterials"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~IGetMaterials.html"
---

# IGetMaterials Method (ICostAnalysisSheetMetal)

Gets the names of the materials in the specified class from the Costing template for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMaterials( _
   ByVal ClassName As System.String, _
   ByVal NumMaterialNames As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisSheetMetal
Dim ClassName As System.String
Dim NumMaterialNames As System.Integer
Dim value As System.String

value = instance.IGetMaterials(ClassName, NumMaterialNames)
```

### C#

```csharp
System.string IGetMaterials(
   System.string ClassName,
   System.int NumMaterialNames
)
```

### C++/CLI

```cpp
System.String^ IGetMaterials(
   System.String^ ClassName,
   System.int NumMaterialNames
)
```

### Parameters

- `ClassName`: Name of material class
- `NumMaterialNames`: Number of the materials in the specified material class

### Return Value

- in-process, unmanaged C++: Pointer to an array of strings of the materials in the specified class

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Before calling this method, call [ICostAnalysisSheetMetal::GetMaterialCount](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal~GetMaterialCount.html) to get the NumMaterialNames value.

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal.html)
[ICostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal_members.html)
[ICostAnalysisSheetMetal::GetMaterialClasses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~GetMaterialClasses.html)
[ICostAnalysisSheetMetal::GetMaterials Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~GetMaterials.html)
[ICostAnalysisSheetMetal::IGetMaterialClasses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~IGetMaterialClasses.html)
[ICostAnalysisSheetMetal::CurrentMaterialClass Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~CurrentMaterialClass.html)
[ICostAnalysisSheetMetal::CurrentMaterial Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~CurrentMaterial.html)
[ICostAnalysisSheetMetal::MaterialCost Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~MaterialCost.html)
[ICostAnalysisSheetMetal::MaterialCostFromTemplate Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~MaterialCostFromTemplate.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
