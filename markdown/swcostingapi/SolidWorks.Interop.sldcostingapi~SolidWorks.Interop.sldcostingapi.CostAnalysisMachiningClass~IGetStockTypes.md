---
title: "IGetStockTypes Method (CostAnalysisMachiningClass)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisMachiningClass"
member: "IGetStockTypes"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachiningClass~IGetStockTypes.html"
---

# IGetStockTypes Method (CostAnalysisMachiningClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function IGetStockTypes( _
   ByVal MaterialClass As System.String, _
   ByVal MaterialName As System.String, _
   ByVal NumStockTypes As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisMachiningClass
Dim MaterialClass As System.String
Dim MaterialName As System.String
Dim NumStockTypes As System.Integer
Dim value As System.Integer

value = instance.IGetStockTypes(MaterialClass, MaterialName, NumStockTypes)
```

### C#

```csharp
public virtual System.int IGetStockTypes(
   System.string MaterialClass,
   System.string MaterialName,
   System.int NumStockTypes
)
```

### C++/CLI

```cpp
public:
virtual System.int IGetStockTypes(
   System.String^ MaterialClass,
   System.String^ MaterialName,
   System.int NumStockTypes
)
```

### Parameters

- `MaterialClass`:
- `MaterialName`:
- `NumStockTypes`:

## See Also

[CostAnalysisMachiningClass Class](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachiningClass.html)
[CostAnalysisMachiningClass Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachiningClass_members.html)
