---
title: "DeleteOperations Method (IInspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionAddinMgr"
member: "DeleteOperations"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~DeleteOperations.html"
---

# DeleteOperations Method (IInspectionAddinMgr)

Deletes the specified operations.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteOperations( _
   ByRef OperationList As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionAddinMgr
Dim OperationList As System.Object
Dim value As System.Object

value = instance.DeleteOperations(OperationList)
```

### C#

```csharp
System.object DeleteOperations(
   ref System.object OperationList
)
```

### C++/CLI

```cpp
System.Object^ DeleteOperations(
   System.Object^% OperationList
)
```

### Parameters

- `OperationList`: Array of operations to delete

### Return Value

Array of booleans indicating whether each operation is successfully deleted

## VBA Syntax

See [InspectionAddinMgr](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionAddinMgr_members.html) methods.

## See Also

[IInspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr.html)
[IInspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
