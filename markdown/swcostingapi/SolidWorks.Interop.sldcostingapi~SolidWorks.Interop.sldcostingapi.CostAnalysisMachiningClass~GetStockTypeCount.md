---
title: "GetStockTypeCount Method (CostAnalysisMachiningClass)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisMachiningClass"
member: "GetStockTypeCount"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachiningClass~GetStockTypeCount.html"
---

# GetStockTypeCount Method (CostAnalysisMachiningClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function GetStockTypeCount( _
   ByVal MaterialClass As System.String, _
   ByVal MaterialName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisMachiningClass
Dim MaterialClass As System.String
Dim MaterialName As System.String
Dim value As System.Integer

value = instance.GetStockTypeCount(MaterialClass, MaterialName)
```

### C#

```csharp
public virtual System.int GetStockTypeCount(
   System.string MaterialClass,
   System.string MaterialName
)
```

### C++/CLI

```cpp
public:
virtual System.int GetStockTypeCount(
   System.String^ MaterialClass,
   System.String^ MaterialName
)
```

### Parameters

- `MaterialClass`:
- `MaterialName`:

## See Also

[CostAnalysisMachiningClass Class](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachiningClass.html)
[CostAnalysisMachiningClass Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachiningClass_members.html)
