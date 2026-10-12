---
title: "SaveAsTemplate Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "SaveAsTemplate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsTemplate.html"
---

# SaveAsTemplate Method (ITableAnnotation)

Saves the format of this table as a template file, which you can then use to create other tables of the same type and that look the same.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveAsTemplate( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim FileName As System.String
Dim value As System.Boolean

value = instance.SaveAsTemplate(FileName)
```

### C#

```csharp
System.bool SaveAsTemplate(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool SaveAsTemplate(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Full path and filename to which to save the table template file (see **Remarks**)

### Return Value

True if the table is saved as a template file, false if not

## VBA Syntax

See [TableAnnotation::SaveAsTemplate](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~SaveAsTemplate.html).

## Remarks

You must specify a filename. It should include the path, filename, and filename extension to which to save the table as a template file.

| If a file of the specified name in the specified path... | Then it is... |
| --- | --- |
| Exists | Overwritten |
| Does not exist | Created |

The filename extension of the file does not matter, but to be consistent with the SOLIDWORKS naming conventions, the following extensions should be used:

- .**sldbomtbt** for BOM tables
- .**sldrevtbt** for revision tables
- .**sldholtbt** for hole tables
- .**sldtbt** for general tables

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::SaveAsPDF Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsPDF.html)
[ITableAnnotation::SaveAsText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SaveAsText.html)
