---
title: "GetColumnWidth Method (IBomTable)"
project: "SOLIDWORKS API Help"
interface: "IBomTable"
member: "GetColumnWidth"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetColumnWidth.html"
---

# GetColumnWidth Method (IBomTable)

Gets the specified column width in meters.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetColumnWidth( _
   ByVal Col As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTable
Dim Col As System.Integer
Dim value As System.Double

value = instance.GetColumnWidth(Col)
```

### C#

```csharp
System.double GetColumnWidth(
   System.int Col
)
```

### C++/CLI

```cpp
System.double GetColumnWidth(
   System.int Col
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Col`: Column number; this is a 0-based index

### Return Value

Width of the specified column in meters

## VBA Syntax

See [BomTable::GetColumnWidth](ms-its:sldworksapivb6.chm::/sldworks~BomTable~GetColumnWidth.html).

## Remarks

Before you use any of the IBomTable methods, activate the BOM table using [IBomTable::Attach3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Attach3.html). After you finish getting BOM data, use [IBomTable::Detach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Detach.html) to deactivate the table.

## See Also

[IBomTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.html)
[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.html)
[IBomTable::GetTotalColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetTotalColumnCount.html)
