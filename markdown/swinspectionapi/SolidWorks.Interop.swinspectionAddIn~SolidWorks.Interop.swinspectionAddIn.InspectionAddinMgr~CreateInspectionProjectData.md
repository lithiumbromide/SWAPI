---
title: "CreateInspectionProjectData Method (InspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionAddinMgr"
member: "CreateInspectionProjectData"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr~CreateInspectionProjectData.html"
---

# CreateInspectionProjectData Method (InspectionAddinMgr)

Creates inspection project data.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateInspectionProjectData( _
   ByVal TemplatePathIn As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionAddinMgr
Dim TemplatePathIn As System.String
Dim value As System.Object

value = instance.CreateInspectionProjectData(TemplatePathIn)
```

### C#

```csharp
System.object CreateInspectionProjectData(
   System.string TemplatePathIn
)
```

### C++/CLI

```cpp
System.Object^ CreateInspectionProjectData(
   System.String^ TemplatePathIn
)
```

### Parameters

- `TemplatePathIn`: Full path name of inspection project template (see **Remarks**)

### Return Value

[IInspectionProjectData](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)

## VBA Syntax

See [InspectionAddinMgr](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionAddinMgr_members.html) methods.

## Remarks

The templates are installed in **c:\ProgramData\SOLIDWORKS\SOLIDWORKS Inspection 2022 Addin\Templates**.

## See Also

[InspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr.html)
[InspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
