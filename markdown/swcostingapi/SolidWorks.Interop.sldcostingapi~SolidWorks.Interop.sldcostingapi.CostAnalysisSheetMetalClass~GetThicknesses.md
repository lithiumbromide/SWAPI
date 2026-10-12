---
title: "GetThicknesses Method (CostAnalysisSheetMetalClass)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisSheetMetalClass"
member: "GetThicknesses"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetalClass~GetThicknesses.html"
---

# GetThicknesses Method (CostAnalysisSheetMetalClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function GetThicknesses( _
   ByVal ClassName As System.String, _
   ByVal MaterialName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisSheetMetalClass
Dim ClassName As System.String
Dim MaterialName As System.String
Dim value As System.Object

value = instance.GetThicknesses(ClassName, MaterialName)
```

### C#

```csharp
public virtual System.object GetThicknesses(
   System.string ClassName,
   System.string MaterialName
)
```

### C++/CLI

```cpp
public:
virtual System.Object^ GetThicknesses(
   System.String^ ClassName,
   System.String^ MaterialName
)
```

### Parameters

- `ClassName`:
- `MaterialName`:

## See Also

[CostAnalysisSheetMetalClass Class](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetalClass.html)
[CostAnalysisSheetMetalClass Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetalClass_members.html)
