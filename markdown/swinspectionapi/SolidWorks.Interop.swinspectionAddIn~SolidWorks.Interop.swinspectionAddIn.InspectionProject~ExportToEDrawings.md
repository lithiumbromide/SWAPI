---
title: "ExportToEDrawings Method (InspectionProject)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProject"
member: "ExportToEDrawings"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProject~ExportToEDrawings.html"
---

# ExportToEDrawings Method (InspectionProject)

Exports the inspection report to eDrawings.

## Syntax

### Visual Basic (Declaration)

```vb
Function ExportToEDrawings( _
   ByVal FilePath As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProject
Dim FilePath As System.String
Dim value As System.Boolean

value = instance.ExportToEDrawings(FilePath)
```

### C#

```csharp
System.bool ExportToEDrawings(
   System.string FilePath
)
```

### C++/CLI

```cpp
System.bool ExportToEDrawings(
   System.String^ FilePath
)
```

### Parameters

- `FilePath`: Full path name of the eDrawings file to export

### Return Value

True if export is successful, false if not

## VBA Syntax

See [InspectionProject](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProject_members.html) methods.

## See Also

[InspectionProject Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProject.html)
[InspectionProject Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProject_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
