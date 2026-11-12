---
title: "GetVisibleColumnCount Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "GetVisibleColumnCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleColumnCount.html"
---

# GetVisibleColumnCount Method (IDesignTable)

Gets the number of columns visible in this design table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVisibleColumnCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.Integer

value = instance.GetVisibleColumnCount()
```

### C#

```csharp
System.int GetVisibleColumnCount()
```

### C++/CLI

```cpp
System.int GetVisibleColumnCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of columns visible in this design table

## VBA Syntax

See [DesignTable::GetVisibleColumnCount](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~GetVisibleColumnCount.html).

## Examples

[Get Microsoft Design Table Worksheet (VBA)](Get_Excel_Design_Table_Worksheet_Example_VB.htm)
[Get Design Table (VBA)](Get_Design_Table_Example_VB.htm)
[Get Design Table (VB.NET)](Get_Design_Table_Example_VBNET.htm)
[Get Design Table (C#)](Get_Design_Table_Example_CSharp.htm)

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::GetColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetColumnCount.html)
[IDesignTable::GetStartColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartColumnNumber.html)
[IDesignTable::GetVisibleLeftColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleLeftColumnNumber.html)
[IDesignTable::ColumnHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~ColumnHidden.html)
[IDesignTable::GetTotalColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalColumnCount.html)

## Availability

SOLIDWORKS 2000 SP01, Revision Number 8.1
