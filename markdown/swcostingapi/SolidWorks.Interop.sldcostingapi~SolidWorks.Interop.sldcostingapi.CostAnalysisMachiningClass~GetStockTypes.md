---
title: "GetStockTypes Method (CostAnalysisMachiningClass)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisMachiningClass"
member: "GetStockTypes"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachiningClass~GetStockTypes.html"
---

# GetStockTypes Method (CostAnalysisMachiningClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function GetStockTypes( _
   ByVal MaterialClass As System.String, _
   ByVal MaterialName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisMachiningClass
Dim MaterialClass As System.String
Dim MaterialName As System.String
Dim value As System.Object

value = instance.GetStockTypes(MaterialClass, MaterialName)
```

### C#

```csharp
public virtual System.object GetStockTypes(
   System.string MaterialClass,
   System.string MaterialName
)
```

### C++/CLI

```cpp
public:
virtual System.Object^ GetStockTypes(
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
