---
title: "SaveAsText Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "SaveAsText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsText.html"
---

# SaveAsText Method (ITableAnnotation)

Obsolete. Superseded by [ITableAnnotation::SaveAsText2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsText2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveAsText( _
   ByVal FileName As System.String, _
   ByVal Separator As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim FileName As System.String
Dim Separator As System.String
Dim value As System.Boolean

value = instance.SaveAsText(FileName, Separator)
```

### C#

```csharp
System.bool SaveAsText(
   System.string FileName,
   System.string Separator
)
```

### C++/CLI

```cpp
System.bool SaveAsText(
   System.String^ FileName,
   System.String^ Separator
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Full path and filename of text data file (see **Remarks**)
- `Separator`: Character or string to use to separate each of the text within each of the cells in the table in the text file

### Return Value

True if table is saved as a text file, false if not

## VBA Syntax

See [TableAnnotation::SaveAsText](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~SaveAsText.html).

## Remarks

You must specify a filename. It should include the path, filename, and filename extension to which to save the table as a text file.

| If a file of the specified name in the specified path... | Then it is... |
| --- | --- |
| Exists | Overwritten |
| Does not exist | Created |

The Separator argument is typically a single character, but it can be a string. If Separator is empty, then the tab character is used.

**NOTE**: Although you can save a table as a text file for use with other applications like Microsoft Excel, you cannot currently import a text file to a table in SOLIDWORKS.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::SaveAsPDF Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsPDF.html)
[ITableAnnotation::SaveAsTemplate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsTemplate.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
