---
title: "EditInspectionMethod Method (InspectionAddinMgrClass)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionAddinMgrClass"
member: "EditInspectionMethod"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgrClass~EditInspectionMethod.html"
---

# EditInspectionMethod Method (InspectionAddinMgrClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function EditInspectionMethod( _
   ByVal MethodID As System.String, _
   ByVal MethodName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionAddinMgrClass
Dim MethodID As System.String
Dim MethodName As System.String
Dim value As System.Boolean

value = instance.EditInspectionMethod(MethodID, MethodName)
```

### C#

```csharp
public virtual System.bool EditInspectionMethod(
   System.string MethodID,
   System.string MethodName
)
```

### C++/CLI

```cpp
public:
virtual System.bool EditInspectionMethod(
   System.String^ MethodID,
   System.String^ MethodName
)
```

### Parameters

- `MethodID`:
- `MethodName`:

## See Also

[InspectionAddinMgrClass Class](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgrClass.html)
[InspectionAddinMgrClass Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgrClass_members.html)
