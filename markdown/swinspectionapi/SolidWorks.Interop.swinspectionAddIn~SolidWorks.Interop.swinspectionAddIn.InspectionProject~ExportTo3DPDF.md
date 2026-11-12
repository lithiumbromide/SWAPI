---
title: "ExportTo3DPDF Method (InspectionProject)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProject"
member: "ExportTo3DPDF"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProject~ExportTo3DPDF.html"
---

# ExportTo3DPDF Method (InspectionProject)

Exports the inspection report in 3D PDF format.

## Syntax

### Visual Basic (Declaration)

```vb
Function ExportTo3DPDF( _
   ByVal FilePath As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProject
Dim FilePath As System.String
Dim value As System.Boolean

value = instance.ExportTo3DPDF(FilePath)
```

### C#

```csharp
System.bool ExportTo3DPDF(
   System.string FilePath
)
```

### C++/CLI

```cpp
System.bool ExportTo3DPDF(
   System.String^ FilePath
)
```

### Parameters

- `FilePath`: Full path name of the PDF to export

### Return Value

True if export is successful, false if not

## VBA Syntax

See [InspectionProject](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProject_members.html) methods.

## Remarks

This method is valid only for parts.

## See Also

[InspectionProject Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProject.html)
[InspectionProject Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProject_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
