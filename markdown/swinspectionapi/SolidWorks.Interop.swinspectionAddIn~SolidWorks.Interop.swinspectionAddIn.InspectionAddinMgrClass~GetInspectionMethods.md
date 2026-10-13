---
title: "GetInspectionMethods Method (InspectionAddinMgrClass)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionAddinMgrClass"
member: "GetInspectionMethods"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgrClass~GetInspectionMethods.html"
---

# GetInspectionMethods Method (InspectionAddinMgrClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function GetInspectionMethods( _
   ByRef MethodList As System.Object, _
   ByRef MethodIDs As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionAddinMgrClass
Dim MethodList As System.Object
Dim MethodIDs As System.Object
Dim value As System.Boolean

value = instance.GetInspectionMethods(MethodList, MethodIDs)
```

### C#

```csharp
public virtual System.bool GetInspectionMethods(
   out System.object MethodList,
   out System.object MethodIDs
)
```

### C++/CLI

```cpp
public:
virtual System.bool GetInspectionMethods(
   [Out] System.Object^ MethodList,
   [Out] System.Object^ MethodIDs
)
```

### Parameters

- `MethodList`:
- `MethodIDs`:

## See Also

[InspectionAddinMgrClass Class](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgrClass.html)
[InspectionAddinMgrClass Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgrClass_members.html)
