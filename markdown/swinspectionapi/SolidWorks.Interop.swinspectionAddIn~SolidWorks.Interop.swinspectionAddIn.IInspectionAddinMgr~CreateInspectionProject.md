---
title: "CreateInspectionProject Method (IInspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionAddinMgr"
member: "CreateInspectionProject"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~CreateInspectionProject.html"
---

# CreateInspectionProject Method (IInspectionAddinMgr)

Creates an inspection project using the specified template and project data and balloons the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateInspectionProject( _
   ByVal InspectionProjectData As System.Object, _
   ByVal DeleteOld As System.Boolean, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionAddinMgr
Dim InspectionProjectData As System.Object
Dim DeleteOld As System.Boolean
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.CreateInspectionProject(InspectionProjectData, DeleteOld, ErrorCode)
```

### C#

```csharp
System.object CreateInspectionProject(
   System.object InspectionProjectData,
   System.bool DeleteOld,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ CreateInspectionProject(
   System.Object^ InspectionProjectData,
   System.bool DeleteOld,
   [Out] System.int ErrorCode
)
```

### Parameters

- `InspectionProjectData`: [IInspectionProjectData](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
- `DeleteOld`: True to delete the existing project and create a new one, false to get the existing project
- `ErrorCode`: Error code as defined by [swiErrorCode_e](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.swiErrorCode_e.html)

### Return Value

[IInspectionProject](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProject.html)

## VBA Syntax

See [InspectionAddinMgr](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionAddinMgr_members.html) methods.

## See Also

[IInspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr.html)
[IInspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
