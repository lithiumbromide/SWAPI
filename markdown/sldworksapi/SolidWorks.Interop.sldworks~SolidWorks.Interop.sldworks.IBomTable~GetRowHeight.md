---
title: "GetRowHeight Method (IBomTable)"
project: "SOLIDWORKS API Help"
interface: "IBomTable"
member: "GetRowHeight"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetRowHeight.html"
---

# GetRowHeight Method (IBomTable)

Gets the specified row height in meters.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRowHeight( _
   ByVal Row As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTable
Dim Row As System.Integer
Dim value As System.Double

value = instance.GetRowHeight(Row)
```

### C#

```csharp
System.double GetRowHeight(
   System.int Row
)
```

### C++/CLI

```cpp
System.double GetRowHeight(
   System.int Row
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: Row number; this is a 0-based index

### Return Value

Height of the specified row in meters

## VBA Syntax

See [BomTable::GetRowHeight](ms-its:sldworksapivb6.chm::/sldworks~BomTable~GetRowHeight.html).

## Remarks

Before you use any of the IBomTable methods, activate the BOM table using [IBomTable::Attach3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Attach3.html). After you finish getting BOM data, use [IBomTable::Detach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Detach.html) to deactivate the table.

## See Also

[IBomTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.html)
[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.html)
[IBomTable::GetTotalRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetTotalRowCount.html)
