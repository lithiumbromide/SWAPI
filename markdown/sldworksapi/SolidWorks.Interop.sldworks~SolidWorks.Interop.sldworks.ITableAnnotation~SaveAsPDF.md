---
title: "SaveAsPDF Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "SaveAsPDF"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsPDF.html"
---

# SaveAsPDF Method (ITableAnnotation)

Saves this table to a PDF file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveAsPDF( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim FileName As System.String
Dim value As System.Boolean

value = instance.SaveAsPDF(FileName)
```

### C#

```csharp
System.bool SaveAsPDF(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool SaveAsPDF(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Full path and filename of the PDF File (see **Remarks**)

### Return Value

True if the table is saved to a PDF file, false if not

## VBA Syntax

See [TableAnnotation::SaveAsPDF](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~SaveAsPDF.html).

## Examples

[Save Table to PDF (C#)](Save_Table_Annotation_to_PDF_Example_CSharp.htm)
[Save Table to PDF (VB.NET)](Save_Table_Annotation_to_PDF_Example_VBNET.htm)
[Save Table to PDF (VBA)](Save_Table_Annotation_to_PDF_Example_VB.htm)

## Remarks

You must specify a filename. It should include the path, filename, and the PDF filename extension to which to save the table.

| If a file of the specified name in the specified path... | Then it is... |
| --- | --- |
| Exists | Overwritten |
| Does not exist | Created |

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::SaveAsTemplate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsTemplate.html)
[ITableAnnotation::SaveAsText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsText.html)

## Availability

SOLIDWORKS 2012 SP04, Revision Number 20.4
