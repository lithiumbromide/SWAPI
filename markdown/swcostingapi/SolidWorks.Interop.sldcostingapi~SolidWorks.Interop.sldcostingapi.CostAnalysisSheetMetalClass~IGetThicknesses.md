---
title: "IGetThicknesses Method (CostAnalysisSheetMetalClass)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisSheetMetalClass"
member: "IGetThicknesses"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetalClass~IGetThicknesses.html"
---

# IGetThicknesses Method (CostAnalysisSheetMetalClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function IGetThicknesses( _
   ByVal ClassName As System.String, _
   ByVal MaterialName As System.String, _
   ByVal NumThicknesses As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisSheetMetalClass
Dim ClassName As System.String
Dim MaterialName As System.String
Dim NumThicknesses As System.Integer
Dim value As System.Double

value = instance.IGetThicknesses(ClassName, MaterialName, NumThicknesses)
```

### C#

```csharp
public virtual System.double IGetThicknesses(
   System.string ClassName,
   System.string MaterialName,
   System.int NumThicknesses
)
```

### C++/CLI

```cpp
public:
virtual System.double IGetThicknesses(
   System.String^ ClassName,
   System.String^ MaterialName,
   System.int NumThicknesses
)
```

### Parameters

- `ClassName`:
- `MaterialName`:
- `NumThicknesses`:

## See Also

[CostAnalysisSheetMetalClass Class](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetalClass.html)
[CostAnalysisSheetMetalClass Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetalClass_members.html)
