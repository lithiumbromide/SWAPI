---
title: "AddInspectionMethod Method (IInspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionAddinMgr"
member: "AddInspectionMethod"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~AddInspectionMethod.html"
---

# AddInspectionMethod Method (IInspectionAddinMgr)

Adds the specified inspection method to the list of inspection methods.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddInspectionMethod( _
   ByVal MethodName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionAddinMgr
Dim MethodName As System.String
Dim value As System.Boolean

value = instance.AddInspectionMethod(MethodName)
```

### C#

```csharp
System.bool AddInspectionMethod(
   System.string MethodName
)
```

### C++/CLI

```cpp
System.bool AddInspectionMethod(
   System.String^ MethodName
)
```

### Parameters

- `MethodName`: Name of inspection method

### Return Value

True if inspection method successfully added, false if not

## VBA Syntax

See [InspectionAddinMgr](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionAddinMgr_members.html) methods.

## See Also

[IInspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr.html)
[IInspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
