---
title: "AddOperation Method (IInspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionAddinMgr"
member: "AddOperation"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~AddOperation.html"
---

# AddOperation Method (IInspectionAddinMgr)

Adds the specified operation to the list of operations.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddOperation( _
   ByVal Operation As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionAddinMgr
Dim Operation As System.String
Dim value As System.Boolean

value = instance.AddOperation(Operation)
```

### C#

```csharp
System.bool AddOperation(
   System.string Operation
)
```

### C++/CLI

```cpp
System.bool AddOperation(
   System.String^ Operation
)
```

### Parameters

- `Operation`: Name of operation

### Return Value

True if operation successfully added, false if not

## VBA Syntax

See [InspectionAddinMgr](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionAddinMgr_members.html) methods.

## See Also

[IInspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr.html)
[IInspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
