---
title: "SetCostingMethod Method (CostPartClass)"
project: "SOLIDWORKS Costing API Help"
interface: "CostPartClass"
member: "SetCostingMethod"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPartClass~SetCostingMethod.html"
---

# SetCostingMethod Method (CostPartClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function SetCostingMethod( _
   ByVal BodyName As System.String, _
   ByVal MethodType As System.Integer _
) As CostBody
```

### Visual Basic (Usage)

```vb
Dim instance As CostPartClass
Dim BodyName As System.String
Dim MethodType As System.Integer
Dim value As CostBody

value = instance.SetCostingMethod(BodyName, MethodType)
```

### C#

```csharp
public virtual CostBody SetCostingMethod(
   System.string BodyName,
   System.int MethodType
)
```

### C++/CLI

```cpp
public:
virtual CostBody^ SetCostingMethod(
   System.String^ BodyName,
   System.int MethodType
)
```

### Parameters

- `BodyName`:
- `MethodType`:

## See Also

[CostPartClass Class](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPartClass.html)
[CostPartClass Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPartClass_members.html)
