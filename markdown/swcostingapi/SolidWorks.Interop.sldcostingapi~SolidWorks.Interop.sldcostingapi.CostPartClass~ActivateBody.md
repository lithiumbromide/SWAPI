---
title: "ActivateBody Method (CostPartClass)"
project: "SOLIDWORKS Costing API Help"
interface: "CostPartClass"
member: "ActivateBody"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPartClass~ActivateBody.html"
---

# ActivateBody Method (CostPartClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function ActivateBody( _
   ByVal BodyName As System.String, _
   ByRef Errors As System.Integer _
) As CostBody
```

### Visual Basic (Usage)

```vb
Dim instance As CostPartClass
Dim BodyName As System.String
Dim Errors As System.Integer
Dim value As CostBody

value = instance.ActivateBody(BodyName, Errors)
```

### C#

```csharp
public virtual CostBody ActivateBody(
   System.string BodyName,
   out System.int Errors
)
```

### C++/CLI

```cpp
public:
virtual CostBody^ ActivateBody(
   System.String^ BodyName,
   [Out] System.int Errors
)
```

### Parameters

- `BodyName`:
- `Errors`:

## See Also

[CostPartClass Class](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPartClass.html)
[CostPartClass Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPartClass_members.html)
