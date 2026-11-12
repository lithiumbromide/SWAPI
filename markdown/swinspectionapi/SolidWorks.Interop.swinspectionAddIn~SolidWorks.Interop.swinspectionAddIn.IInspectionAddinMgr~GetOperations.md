---
title: "GetOperations Method (IInspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionAddinMgr"
member: "GetOperations"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~GetOperations.html"
---

# GetOperations Method (IInspectionAddinMgr)

Gets the list of operations.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOperations( _
   ByRef OperationList As System.Object, _
   ByRef OperationIDs As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionAddinMgr
Dim OperationList As System.Object
Dim OperationIDs As System.Object
Dim value As System.Boolean

value = instance.GetOperations(OperationList, OperationIDs)
```

### C#

```csharp
System.bool GetOperations(
   out System.object OperationList,
   out System.object OperationIDs
)
```

### C++/CLI

```cpp
System.bool GetOperations(
   [Out] System.Object^ OperationList,
   [Out] System.Object^ OperationIDs
)
```

### Parameters

- `OperationList`: Array of operations
- `OperationIDs`: Array of operation IDs

### Return Value

True if operations successfully retrieved, false if not

## VBA Syntax

See [InspectionAddinMgr](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionAddinMgr_members.html) methods.

## See Also

[IInspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr.html)
[IInspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
