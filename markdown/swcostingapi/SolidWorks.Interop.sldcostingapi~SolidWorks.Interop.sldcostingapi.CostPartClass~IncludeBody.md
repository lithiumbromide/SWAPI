---
title: "IncludeBody Method (CostPartClass)"
project: "SOLIDWORKS Costing API Help"
interface: "CostPartClass"
member: "IncludeBody"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPartClass~IncludeBody.html"
---

# IncludeBody Method (CostPartClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function IncludeBody( _
   ByVal BodyName As System.String, _
   ByVal Include As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostPartClass
Dim BodyName As System.String
Dim Include As System.Boolean
Dim value As System.Integer

value = instance.IncludeBody(BodyName, Include)
```

### C#

```csharp
public virtual System.int IncludeBody(
   System.string BodyName,
   System.bool Include
)
```

### C++/CLI

```cpp
public:
virtual System.int IncludeBody(
   System.String^ BodyName,
   System.bool Include
)
```

### Parameters

- `BodyName`:
- `Include`:

## See Also

[CostPartClass Class](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPartClass.html)
[CostPartClass Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPartClass_members.html)
