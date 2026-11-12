---
title: "GetVisibleLeftColumnNumber Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "GetVisibleLeftColumnNumber"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleLeftColumnNumber.html"
---

# GetVisibleLeftColumnNumber Method (IDesignTable)

Gets the number of the leftmost visible column.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVisibleLeftColumnNumber() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.Integer

value = instance.GetVisibleLeftColumnNumber()
```

### C#

```csharp
System.int GetVisibleLeftColumnNumber()
```

### C++/CLI

```cpp
System.int GetVisibleLeftColumnNumber();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of the leftmost visible column

## VBA Syntax

See [DesignTable::GetVisibleLeftColumnNumber](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~GetVisibleLeftColumnNumber.html).

## Examples

[Get Microsoft Excel Design Table Worksheet (VBA)](Get_Excel_Design_Table_Worksheet_Example_VB.htm)

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::GetColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetColumnCount.html)
[IDesignTable::GetStartColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartColumnNumber.html)
[IDesignTable::GetTotalColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalColumnCount.html)
[IDesignTable::GetVisibleColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleColumnCount.html)
[IDesignTable::ColumnHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~ColumnHidden.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
