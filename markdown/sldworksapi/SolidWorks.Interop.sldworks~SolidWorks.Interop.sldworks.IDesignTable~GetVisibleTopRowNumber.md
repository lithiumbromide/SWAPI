---
title: "GetVisibleTopRowNumber Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "GetVisibleTopRowNumber"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleTopRowNumber.html"
---

# GetVisibleTopRowNumber Method (IDesignTable)

Gets the number of the topmost visible row.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVisibleTopRowNumber() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.Integer

value = instance.GetVisibleTopRowNumber()
```

### C#

```csharp
System.int GetVisibleTopRowNumber()
```

### C++/CLI

```cpp
System.int GetVisibleTopRowNumber();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of the topmost visible row

## VBA Syntax

See [DesignTable::GetVisibleTopRowNumber](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~GetVisibleTopRowNumber.html).

## Examples

[Get Microsoft Excel Design Table Worksheet (VBA)](Get_Excel_Design_Table_Worksheet_Example_VB.htm)

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::AddRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AddRow.html)
[IDesignTable::GetRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetRowCount.html)
[IDesignTable::GetStartRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartRowNumber.html)
[IDesignTable::GetTotalRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalRowCount.html)
[IDesignTable::GetVisibleRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleRowCount.html)
[IDesignTable::RowHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~RowHidden.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
