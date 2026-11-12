---
title: "EditInspectionProject Method (IInspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionAddinMgr"
member: "EditInspectionProject"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~EditInspectionProject.html"
---

# EditInspectionProject Method (IInspectionAddinMgr)

Edits the inspection project and re-balloons the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function EditInspectionProject( _
   ByVal InspectionProjectData As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionAddinMgr
Dim InspectionProjectData As System.Object
Dim value As System.Boolean

value = instance.EditInspectionProject(InspectionProjectData)
```

### C#

```csharp
System.bool EditInspectionProject(
   System.object InspectionProjectData
)
```

### C++/CLI

```cpp
System.bool EditInspectionProject(
   System.Object^ InspectionProjectData
)
```

### Parameters

- `InspectionProjectData`: [IInspectionProjectData](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)

### Return Value

True if inspection project successfully modified, false if not

## VBA Syntax

See [InspectionAddinMgr](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionAddinMgr_members.html) methods.

## See Also

[IInspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr.html)
[IInspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
