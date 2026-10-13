---
title: "GetTotalColumnCount Method (IBomTable)"
project: "SOLIDWORKS API Help"
interface: "IBomTable"
member: "GetTotalColumnCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetTotalColumnCount.html"
---

# GetTotalColumnCount Method (IBomTable)

Gets the total number of columns in the BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTotalColumnCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTable
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

Total number of columns in the BOM table

## VBA Syntax

See [BomTable::GetTotalColumnCount](ms-its:sldworksapivb6.chm::/sldworks~BomTable~GetTotalColumnCount.html).

## Remarks

This method returns 0 if the BOM is obscured, which may occur when debugging a macro. This is a quirk in Microsoft Excel, which is used by SOLIDWORKS for the BOM functionality.

Before you use any of the IBomTable methods, activate the BOM table using [IBomTable::Attach3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Attach3.html). After you finish getting BOM data, use [IBomTable::Detach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Detach.html) to deactivate the table.

## See Also

[IBomTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.html)
[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.html)
[IBomTable::GetTotalRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetTotalRowCount.html)
[IBomTable::GetColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetColumnWidth.html)

## Availability

SOLIDWORKS 2001Plus SP5, Revision Number 10.5
