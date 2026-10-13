---
title: "EditInspectionMethod Method (IInspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionAddinMgr"
member: "EditInspectionMethod"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~EditInspectionMethod.html"
---

# EditInspectionMethod Method (IInspectionAddinMgr)

Edits the specified inspection method.

## Syntax

### Visual Basic (Declaration)

```vb
Function EditInspectionMethod( _
   ByVal MethodID As System.String, _
   ByVal MethodName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionAddinMgr
Dim MethodID As System.String
Dim MethodName As System.String
Dim value As System.Boolean

value = instance.EditInspectionMethod(MethodID, MethodName)
```

### C#

```csharp
System.bool EditInspectionMethod(
   System.string MethodID,
   System.string MethodName
)
```

### C++/CLI

```cpp
System.bool EditInspectionMethod(
   System.String^ MethodID,
   System.String^ MethodName
)
```

### Parameters

- `MethodID`: ID of inspection method
- `MethodName`: Name of inspection method

### Return Value

True if inspection method successfully modified, false if not

## VBA Syntax

See [InspectionAddinMgr](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionAddinMgr_members.html) methods.

## See Also

[IInspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr.html)
[IInspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
