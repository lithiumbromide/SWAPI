---
title: "CreateInspectionProject Method (InspectionAddinMgrClass)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionAddinMgrClass"
member: "CreateInspectionProject"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgrClass~CreateInspectionProject.html"
---

# CreateInspectionProject Method (InspectionAddinMgrClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function CreateInspectionProject( _
   ByVal InspectionProjectData As System.Object, _
   ByVal DeleteOld As System.Boolean, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionAddinMgrClass
Dim InspectionProjectData As System.Object
Dim DeleteOld As System.Boolean
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.CreateInspectionProject(InspectionProjectData, DeleteOld, ErrorCode)
```

### C#

```csharp
public virtual System.object CreateInspectionProject(
   System.object InspectionProjectData,
   System.bool DeleteOld,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
public:
virtual System.Object^ CreateInspectionProject(
   System.Object^ InspectionProjectData,
   System.bool DeleteOld,
   [Out] System.int ErrorCode
)
```

### Parameters

- `InspectionProjectData`:
- `DeleteOld`:
- `ErrorCode`:

## See Also

[InspectionAddinMgrClass Class](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgrClass.html)
[InspectionAddinMgrClass Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgrClass_members.html)
