---
title: "IGetMaterials Method (CostAnalysisSheetMetalClass)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisSheetMetalClass"
member: "IGetMaterials"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetalClass~IGetMaterials.html"
---

# IGetMaterials Method (CostAnalysisSheetMetalClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function IGetMaterials( _
   ByVal ClassName As System.String, _
   ByVal NumMaterialNames As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisSheetMetalClass
Dim ClassName As System.String
Dim NumMaterialNames As System.Integer
Dim value As System.String

value = instance.IGetMaterials(ClassName, NumMaterialNames)
```

### C#

```csharp
public virtual System.string IGetMaterials(
   System.string ClassName,
   System.int NumMaterialNames
)
```

### C++/CLI

```cpp
public:
virtual System.String^ IGetMaterials(
   System.String^ ClassName,
   System.int NumMaterialNames
)
```

### Parameters

- `ClassName`:
- `NumMaterialNames`:

## See Also

[CostAnalysisSheetMetalClass Class](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetalClass.html)
[CostAnalysisSheetMetalClass Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetalClass_members.html)
