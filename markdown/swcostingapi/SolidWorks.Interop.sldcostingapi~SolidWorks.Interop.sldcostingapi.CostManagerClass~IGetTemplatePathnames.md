---
title: "IGetTemplatePathnames Method (CostManagerClass)"
project: "SOLIDWORKS Costing API Help"
interface: "CostManagerClass"
member: "IGetTemplatePathnames"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostManagerClass~IGetTemplatePathnames.html"
---

# IGetTemplatePathnames Method (CostManagerClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function IGetTemplatePathnames( _
   ByVal CostingType As System.Integer, _
   ByVal NumTemplates As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CostManagerClass
Dim CostingType As System.Integer
Dim NumTemplates As System.Integer
Dim value As System.String

value = instance.IGetTemplatePathnames(CostingType, NumTemplates)
```

### C#

```csharp
public virtual System.string IGetTemplatePathnames(
   System.int CostingType,
   System.int NumTemplates
)
```

### C++/CLI

```cpp
public:
virtual System.String^ IGetTemplatePathnames(
   System.int CostingType,
   System.int NumTemplates
)
```

### Parameters

- `CostingType`:
- `NumTemplates`:

## See Also

[CostManagerClass Class](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostManagerClass.html)
[CostManagerClass Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostManagerClass_members.html)
