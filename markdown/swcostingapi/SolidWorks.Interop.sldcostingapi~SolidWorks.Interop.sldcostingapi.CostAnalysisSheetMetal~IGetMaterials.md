---
title: "IGetMaterials Method (CostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisSheetMetal"
member: "IGetMaterials"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal~IGetMaterials.html"
---

# IGetMaterials Method (CostAnalysisSheetMetal)

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
Dim instance As CostAnalysisSheetMetal
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

[CostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal.html)
[CostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
