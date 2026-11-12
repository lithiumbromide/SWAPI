---
title: "IGetMaterials Method (CostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisMachining"
member: "IGetMaterials"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining~IGetMaterials.html"
---

# IGetMaterials Method (CostAnalysisMachining)

Gets the names of the materials in the specified class from the Costing template for this machining Costing analysis.

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
Dim instance As CostAnalysisMachining
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

Before calling this method, call [ICostAnalysisMachining::GetMaterialCount](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~GetMaterialCount.html) to get the NumMaterialNames value.

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining.html)
[CostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
