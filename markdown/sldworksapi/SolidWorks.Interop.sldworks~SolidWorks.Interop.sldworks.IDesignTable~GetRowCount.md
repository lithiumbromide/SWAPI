---
title: "GetRowCount Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "GetRowCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetRowCount.html"
---

# GetRowCount Method (IDesignTable)

Gets the number of rows in the design table that are currently visible in the model view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRowCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.Integer

value = instance.GetRowCount()
```

### C#

```csharp
System.int GetRowCount()
```

### C++/CLI

```cpp
System.int GetRowCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of rows currently visible in the model view

## VBA Syntax

See [DesignTable::GetRowCount](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~GetRowCount.html).

## Examples

[Get Design Table (VBA)](Get_Design_Table_Example_VB.htm)
[Get Design Table (VB.NET)](Get_Design_Table_Example_VBNET.htm)
[Get Design Table (C#)](Get_Design_Table_Example_CSharp.htm)

## Remarks

Before you use any of the [IDesignTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable.html) methods, you must first activate the IDesignTable using [IDesignTable::Attach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~Attach.html). Once you are finished getting IDesignTable data, you can deactivate the table using [IDesignTable::Detach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~Detach.html).

Use [IDesignTable::GetTotalRowCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~GetTotalRowCount.html) to get the total number of rows in the design table.

To get information outside the visible region of the IDesignTable, get the Microsoft Excel worksheet activated by IDesignTable::Attach. Then, you can use the Microsoft Excel API to make additional queries.

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::GetStartRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartRowNumber.html)
[IDesignTable::GetVisibleRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleRowCount.html)
[IDesignTable::GetVisibleTopRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleTopRowNumber.html)
[IDesignTable::SetRowChanged Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetRowChanged.html)
[IDesignTable::RowHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~RowHidden.html)
[IDesignTable::AddRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AddRow.html)
