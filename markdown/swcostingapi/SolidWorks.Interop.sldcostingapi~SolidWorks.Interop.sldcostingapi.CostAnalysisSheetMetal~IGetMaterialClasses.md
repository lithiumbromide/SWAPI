---
title: "IGetMaterialClasses Method (CostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisSheetMetal"
member: "IGetMaterialClasses"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal~IGetMaterialClasses.html"
---

# IGetMaterialClasses Method (CostAnalysisSheetMetal)

Gets the names of the material classes from the Costing template for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMaterialClasses( _
   ByVal NumClassNames As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisSheetMetal
Dim NumClassNames As System.Integer
Dim value As System.String

value = instance.IGetMaterialClasses(NumClassNames)
```

### C#

```csharp
System.string IGetMaterialClasses(
   System.int NumClassNames
)
```

### C++/CLI

```cpp
System.String^ IGetMaterialClasses(
   System.int NumClassNames
)
```

### Parameters

- `NumClassNames`: Number of material classes

### Return Value

- in-process, unmanaged C++: Pointer to an array of strings of the names of the material classes

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Before calling this method, call [ICostAnalysisSheetMetal::GetMaterialClassesCount](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal~GetMaterialClassesCount.html) to get the NumClassNames value.

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal.html)
[CostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
