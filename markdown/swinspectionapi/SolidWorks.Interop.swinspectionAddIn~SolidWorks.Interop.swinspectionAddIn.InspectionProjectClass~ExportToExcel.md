---
title: "ExportToExcel Method (InspectionProjectClass)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectClass"
member: "ExportToExcel"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectClass~ExportToExcel.html"
---

# ExportToExcel Method (InspectionProjectClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function ExportToExcel( _
   ByVal TemplatePath As System.String, _
   ByVal FilePath As System.String, _
   ByVal Multisheet As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectClass
Dim TemplatePath As System.String
Dim FilePath As System.String
Dim Multisheet As System.Boolean
Dim value As System.Boolean

value = instance.ExportToExcel(TemplatePath, FilePath, Multisheet)
```

### C#

```csharp
public virtual System.bool ExportToExcel(
   System.string TemplatePath,
   System.string FilePath,
   System.bool Multisheet
)
```

### C++/CLI

```cpp
public:
virtual System.bool ExportToExcel(
   System.String^ TemplatePath,
   System.String^ FilePath,
   System.bool Multisheet
)
```

### Parameters

- `TemplatePath`:
- `FilePath`:
- `Multisheet`:

## See Also

[InspectionProjectClass Class](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectClass.html)
[InspectionProjectClass Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectClass_members.html)
