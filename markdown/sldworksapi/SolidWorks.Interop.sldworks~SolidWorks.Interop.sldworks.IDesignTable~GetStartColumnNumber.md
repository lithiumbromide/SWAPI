---
title: "GetStartColumnNumber Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "GetStartColumnNumber"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartColumnNumber.html"
---

# GetStartColumnNumber Method (IDesignTable)

Gets the number of the first column in which a dimension is displayed.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStartColumnNumber() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim value As System.Integer

value = instance.GetStartColumnNumber()
```

### C#

```csharp
System.int GetStartColumnNumber()
```

### C++/CLI

```cpp
System.int GetStartColumnNumber();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of the first column in which a dimensions is displayed

## VBA Syntax

See [DesignTable::GetStartColumnNumber](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~GetStartColumnNumber.html).

## Examples

[Get Microsoft Excel Design Table Worksheet (VBA)](Get_Excel_Design_Table_Worksheet_Example_VB.htm)

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::GetColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetColumnCount.html)
[IDesignTable::GetTotalColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalColumnCount.html)
[IDesignTable::GetVisibleLeftColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleLeftColumnNumber.html)
[IDesignTable::ColumnHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~ColumnHidden.html)
[IDesignTable::GetStartRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartRowNumber.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
