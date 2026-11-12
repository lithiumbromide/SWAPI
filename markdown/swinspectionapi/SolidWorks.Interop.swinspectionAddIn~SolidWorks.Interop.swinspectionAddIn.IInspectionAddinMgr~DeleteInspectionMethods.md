---
title: "DeleteInspectionMethods Method (IInspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionAddinMgr"
member: "DeleteInspectionMethods"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~DeleteInspectionMethods.html"
---

# DeleteInspectionMethods Method (IInspectionAddinMgr)

Deletes the specified inspection methods.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteInspectionMethods( _
   ByRef MethodList As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionAddinMgr
Dim MethodList As System.Object
Dim value As System.Object

value = instance.DeleteInspectionMethods(MethodList)
```

### C#

```csharp
System.object DeleteInspectionMethods(
   ref System.object MethodList
)
```

### C++/CLI

```cpp
System.Object^ DeleteInspectionMethods(
   System.Object^% MethodList
)
```

### Parameters

- `MethodList`: Array of inspection methods to delete

### Return Value

Array of booleans indicating whether each inspection method is successfully deleted

## VBA Syntax

See [InspectionAddinMgr](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionAddinMgr_members.html) methods.

## See Also

[IInspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr.html)
[IInspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
