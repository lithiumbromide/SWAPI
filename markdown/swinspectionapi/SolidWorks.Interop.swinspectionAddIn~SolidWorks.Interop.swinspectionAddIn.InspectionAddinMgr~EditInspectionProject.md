---
title: "EditInspectionProject Method (InspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionAddinMgr"
member: "EditInspectionProject"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr~EditInspectionProject.html"
---

# EditInspectionProject Method (InspectionAddinMgr)

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
Dim instance As InspectionAddinMgr
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

[InspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr.html)
[InspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
