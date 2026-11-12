---
title: "SaveAsExcel Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "SaveAsExcel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~SaveAsExcel.html"
---

# SaveAsExcel Method (IBomTableAnnotation)

Saves this BOM table annotation as a Microsoft Excel document with the specified properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveAsExcel( _
   ByVal FileName As System.String, _
   ByVal IncludeHidden As System.Boolean, _
   ByVal IncludeFileImages As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim FileName As System.String
Dim IncludeHidden As System.Boolean
Dim IncludeFileImages As System.Boolean
Dim value As System.Boolean

value = instance.SaveAsExcel(FileName, IncludeHidden, IncludeFileImages)
```

### C#

```csharp
System.bool SaveAsExcel(
   System.string FileName,
   System.bool IncludeHidden,
   System.bool IncludeFileImages
)
```

### C++/CLI

```cpp
System.bool SaveAsExcel(
   System.String^ FileName,
   System.bool IncludeHidden,
   System.bool IncludeFileImages
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Full path and file name of the Microsoft Excel file to save to (***.xls**)
- `IncludeHidden`: True to include text in hidden cells, false to not
- `IncludeFileImages`: True to include file images, false to not

### Return Value

True if the table is saved as a Microsoft Excel file, false if not

## VBA Syntax

See [BomTableAnnotation::SaveAsExcel](ms-its:sldworksapivb6.chm::/sldworks~BomTableAnnotation~SaveAsExcel.html).

## Examples

[Save Table to Microsoft Excel (VBA)](Save_Table_to_Microsoft_Excel_Example_VB.htm)

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
