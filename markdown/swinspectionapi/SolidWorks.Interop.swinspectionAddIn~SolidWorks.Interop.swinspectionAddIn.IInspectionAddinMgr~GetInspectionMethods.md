---
title: "GetInspectionMethods Method (IInspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionAddinMgr"
member: "GetInspectionMethods"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~GetInspectionMethods.html"
---

# GetInspectionMethods Method (IInspectionAddinMgr)

Gets the list of inspection methods.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInspectionMethods( _
   ByRef MethodList As System.Object, _
   ByRef MethodIDs As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionAddinMgr
Dim MethodList As System.Object
Dim MethodIDs As System.Object
Dim value As System.Boolean

value = instance.GetInspectionMethods(MethodList, MethodIDs)
```

### C#

```csharp
System.bool GetInspectionMethods(
   out System.object MethodList,
   out System.object MethodIDs
)
```

### C++/CLI

```cpp
System.bool GetInspectionMethods(
   [Out] System.Object^ MethodList,
   [Out] System.Object^ MethodIDs
)
```

### Parameters

- `MethodList`: Array of inspection methods
- `MethodIDs`: Array of inspection method IDs

### Return Value

True if inspection methods successfully retrieved, false if not

## VBA Syntax

See [InspectionAddinMgr](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionAddinMgr_members.html) methods.

## See Also

[IInspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr.html)
[IInspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
