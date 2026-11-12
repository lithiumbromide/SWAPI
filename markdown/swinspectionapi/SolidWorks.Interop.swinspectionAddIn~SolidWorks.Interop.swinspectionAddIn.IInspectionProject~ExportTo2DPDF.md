---
title: "ExportTo2DPDF Method (IInspectionProject)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProject"
member: "ExportTo2DPDF"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProject~ExportTo2DPDF.html"
---

# ExportTo2DPDF Method (IInspectionProject)

Exports the inspection report in 2D PDF format.

## Syntax

### Visual Basic (Declaration)

```vb
Function ExportTo2DPDF( _
   ByVal FilePath As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProject
Dim FilePath As System.String
Dim value As System.Boolean

value = instance.ExportTo2DPDF(FilePath)
```

### C#

```csharp
System.bool ExportTo2DPDF(
   System.string FilePath
)
```

### C++/CLI

```cpp
System.bool ExportTo2DPDF(
   System.String^ FilePath
)
```

### Parameters

- `FilePath`: Full path name of the PDF to export

### Return Value

True if export is successful, false if not

## VBA Syntax

See [InspectionProject](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProject_members.html) methods.

## See Also

[IInspectionProject Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProject.html)
[IInspectionProject Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProject_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
