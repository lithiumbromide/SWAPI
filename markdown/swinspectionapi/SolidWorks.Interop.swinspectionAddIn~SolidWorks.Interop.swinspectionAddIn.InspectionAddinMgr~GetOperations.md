---
title: "GetOperations Method (InspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionAddinMgr"
member: "GetOperations"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr~GetOperations.html"
---

# GetOperations Method (InspectionAddinMgr)

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
Dim instance As InspectionAddinMgr
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

[InspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr.html)
[InspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
