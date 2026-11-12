---
title: "GetOperations Method (InspectionAddinMgrClass)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionAddinMgrClass"
member: "GetOperations"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgrClass~GetOperations.html"
---

# GetOperations Method (InspectionAddinMgrClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function GetOperations( _
   ByRef OperationList As System.Object, _
   ByRef OperationIDs As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionAddinMgrClass
Dim OperationList As System.Object
Dim OperationIDs As System.Object
Dim value As System.Boolean

value = instance.GetOperations(OperationList, OperationIDs)
```

### C#

```csharp
public virtual System.bool GetOperations(
   out System.object OperationList,
   out System.object OperationIDs
)
```

### C++/CLI

```cpp
public:
virtual System.bool GetOperations(
   [Out] System.Object^ OperationList,
   [Out] System.Object^ OperationIDs
)
```

### Parameters

- `OperationList`:
- `OperationIDs`:

## See Also

[InspectionAddinMgrClass Class](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgrClass.html)
[InspectionAddinMgrClass Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgrClass_members.html)
