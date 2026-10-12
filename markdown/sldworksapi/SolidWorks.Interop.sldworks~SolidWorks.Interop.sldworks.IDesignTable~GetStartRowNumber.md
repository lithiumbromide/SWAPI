---
title: "GetStartRowNumber Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "GetStartRowNumber"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartRowNumber.html"
---

# GetStartRowNumber Method (IDesignTable)

Gets the number of the first row in which dimensions are displayed.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStartRowNumber() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.Integer

value = instance.GetStartRowNumber()
```

### C#

```csharp
System.int GetStartRowNumber()
```

### C++/CLI

```cpp
System.int GetStartRowNumber();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of the first row in which dimensions are displayed

## VBA Syntax

See [DesignTable::GetStartRowNumber](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~GetStartRowNumber.html).

## Examples

[Get Microsoft Excel Design Table Worksheet (VBA)](Get_Excel_Design_Table_Worksheet_Example_VB.htm)

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::GetRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetRowCount.html)
[IDesignTable::GetStartColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartColumnNumber.html)
[IDesignTable::GetTotalRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalRowCount.html)
[IDesignTable::GetVisibleRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleRowCount.html)
[IDesignTable::GetVisibleTopRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleTopRowNumber.html)
[IDesignTable::RowHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~RowHidden.html)
[IDesignTable::AddRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AddRow.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
