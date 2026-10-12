---
title: "AddInspectionMethod Method (InspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionAddinMgr"
member: "AddInspectionMethod"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr~AddInspectionMethod.html"
---

# AddInspectionMethod Method (InspectionAddinMgr)

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
Dim instance As InspectionAddinMgr
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

[InspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr.html)
[InspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
