---
title: "GetTotalColumnCount Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "GetTotalColumnCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalColumnCount.html"
---

# GetTotalColumnCount Method (IDesignTable)

Gets the number of columns in the design table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTotalColumnCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.Integer

value = instance.GetTotalColumnCount()
```

### C#

```csharp
System.int GetTotalColumnCount()
```

### C++/CLI

```cpp
System.int GetTotalColumnCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of columns in the design table

## VBA Syntax

See [DesignTable::GetTotalColumnCount](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~GetTotalColumnCount.html).

## Examples

[Get Microsoft Excel Design Table Worksheet (VBA)](Get_Excel_Design_Table_Worksheet_Example_VB.htm)
[Get Design Table (C#)](Get_Design_Table_Example_CSharp.htm)
[Get Design Table (VB.NET)](Get_Design_Table_Example_VBNET.htm)
[Get Design Table (VBA)](Get_Design_Table_Example_VB.htm)

## Remarks

The column index ranges from 1 to the return value.

Before you use any of the [IDesignTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable.html) methods, use [IDesignTable::Attach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~Attach.html) to activate the IDesignTable. After you finish getting IDesignTable data, use [IDesignTable::Detach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~Detach.html) to deactivate the table.

This method differs from [IDesignTable::GetColumnCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~GetColumnCount.html) in that it counts all the columns in the design table. IDesignTable::GetColumnCount counts only the columns that are currently visible in the [IModelView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView.html).

To get information outside of the visible region of the design table, get the Microsoft Excel worksheet activated by IDesignTable::Attach. Then, you can use the Microsoft Excel API to make additional queries.

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::GetColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetColumnCount.html)
[IDesignTable::GetStartColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartColumnNumber.html)
[IDesignTable::GetVisibleColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleColumnCount.html)
[IDesignTable::GetVisibleLeftColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleLeftColumnNumber.html)
[IDesignTable::ColumnHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~ColumnHidden.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
