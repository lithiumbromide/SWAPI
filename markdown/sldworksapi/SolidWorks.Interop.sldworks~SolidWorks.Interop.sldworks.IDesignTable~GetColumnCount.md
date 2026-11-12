---
title: "GetColumnCount Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "GetColumnCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetColumnCount.html"
---

# GetColumnCount Method (IDesignTable)

Gets the number of columns in the design table that are currently visible in the model view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetColumnCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.Integer

value = instance.GetColumnCount()
```

### C#

```csharp
System.int GetColumnCount()
```

### C++/CLI

```cpp
System.int GetColumnCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of columns in the design table

## VBA Syntax

See [DesignTable::GetColumnCount](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~GetColumnCount.html).

## Examples

[Get Design Table (VBA)](Get_Design_Table_Example_VB.htm)
[Get Design Table (VB.NET)](Get_Design_Table_Example_VBNET.htm)
[Get Design Table (C#)](Get_Design_Table_Example_CSharp.htm)

## Remarks

Before using any of the [IDesignTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable.html) methods, you must use [IDesignTable::Attach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~Attach.html) to activate the design table. After you finish getting design table data, use [IDesignTable::Detach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~Detach.html) to deactivate the table.

Use [IDesignTable::GetTotalColumnCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~GetTotalColumnCount.html) to get the total number of columns in the design table.

To obtain information outside the visible region of the design table, get the Microsoft Excel worksheet that [IDesignTable::Attach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~Attach.html) activated. You can then use the Microsoft Excel API to make additional queries.

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::GetStartColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartColumnNumber.html)
[IDesignTable::GetVisibleLeftColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleLeftColumnNumber.html)
[IDesignTable::ColumnHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~ColumnHidden.html)
[IDesignTable::GetVisibleColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleColumnCount.html)
[IDesignTable::GetHeaderText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetHeaderText.html)
