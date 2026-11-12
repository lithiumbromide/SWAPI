---
title: "GetHeaderText Method (IBomTable)"
project: "SOLIDWORKS API Help"
interface: "IBomTable"
member: "GetHeaderText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetHeaderText.html"
---

# GetHeaderText Method (IBomTable)

Gets the header text for the specified column.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHeaderText( _
   ByVal Col As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTable
Dim Col As System.Integer
Dim value As System.String

value = instance.GetHeaderText(Col)
```

### C#

```csharp
System.string GetHeaderText(
   System.int Col
)
```

### C++/CLI

```cpp
System.String^ GetHeaderText(
   System.int Col
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Col`: Column number with the desired header text; this is a 0-based index

### Return Value

Text string from the column header

## VBA Syntax

See [BomTable::GetHeaderText](ms-its:sldworksapivb6.chm::/sldworks~BomTable~GetHeaderText.html).

## Remarks

Before you use any of the IBomTable methods, activate the BOM table using [IBomTable::Attach3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Attach3.html). After you finish getting BOM data, use [IBomTable::Detach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Detach.html) to deactivate the table.

## See Also

[IBomTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.html)
[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.html)
