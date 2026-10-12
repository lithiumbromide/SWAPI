---
title: "SaveAsExcelFile Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "SaveAsExcelFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SaveAsExcelFile.html"
---

# SaveAsExcelFile Method (IDesignTable)

Saves the design table to a Microsoft Excel file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveAsExcelFile( _
   ByVal Value As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim Value As System.String
Dim value As System.Boolean

value = instance.SaveAsExcelFile(Value)
```

### C#

```csharp
System.bool SaveAsExcelFile(
   System.string Value
)
```

### C++/CLI

```cpp
System.bool SaveAsExcelFile(
   System.String^ Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Value`: Path and filename for the Microsoft Excel file

### Return Value

True if the design table is saved to a Microsoft Excel file, false if not

## VBA Syntax

See [DesignTable::SaveAsExcelFile](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~SaveAsExcelFile.html).

## Examples

[Save Design Table as Microsoft Excel File (VBA)](Save_Design_Table_as_Microsoft_Excel_File_Example_VB.htm)

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::FileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~FileName.html)
[IDesignTable::SourceType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SourceType.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
