---
title: "AddOperation Method (InspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionAddinMgr"
member: "AddOperation"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr~AddOperation.html"
---

# AddOperation Method (InspectionAddinMgr)

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
Dim instance As InspectionAddinMgr
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

[InspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr.html)
[InspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
