---
title: "SetCurrentProfile Method (CostAnalysisStructuralClass)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisStructuralClass"
member: "SetCurrentProfile"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructuralClass~SetCurrentProfile.html"
---

# SetCurrentProfile Method (CostAnalysisStructuralClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function SetCurrentProfile( _
   ByVal Standard As System.String, _
   ByVal ProfileType As System.String, _
   ByVal ProfileSize As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisStructuralClass
Dim Standard As System.String
Dim ProfileType As System.String
Dim ProfileSize As System.String
Dim value As System.Boolean

value = instance.SetCurrentProfile(Standard, ProfileType, ProfileSize)
```

### C#

```csharp
public virtual System.bool SetCurrentProfile(
   System.string Standard,
   System.string ProfileType,
   System.string ProfileSize
)
```

### C++/CLI

```cpp
public:
virtual System.bool SetCurrentProfile(
   System.String^ Standard,
   System.String^ ProfileType,
   System.String^ ProfileSize
)
```

### Parameters

- `Standard`:
- `ProfileType`:
- `ProfileSize`:

## See Also

[CostAnalysisStructuralClass Class](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructuralClass.html)
[CostAnalysisStructuralClass Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructuralClass_members.html)
