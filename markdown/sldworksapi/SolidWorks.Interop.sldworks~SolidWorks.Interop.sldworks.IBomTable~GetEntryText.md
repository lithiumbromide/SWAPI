---
title: "GetEntryText Method (IBomTable)"
project: "SOLIDWORKS API Help"
interface: "IBomTable"
member: "GetEntryText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetEntryText.html"
---

# GetEntryText Method (IBomTable)

Retrieves the contents of the specified cell as a string regardless of the cell's data type.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntryText( _
   ByVal Row As System.Integer, _
   ByVal Col As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTable
Dim Row As System.Integer
Dim Col As System.Integer
Dim value As System.String

value = instance.GetEntryText(Row, Col)
```

### C#

```csharp
System.string GetEntryText(
   System.int Row,
   System.int Col
)
```

### C++/CLI

```cpp
System.String^ GetEntryText(
   System.int Row,
   System.int Col
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: Row number of the desired cell; this is a 0-based index
- `Col`: Column number of the desired cell; this is a 0-based index

### Return Value

Text string from the specified cell

## VBA Syntax

See [BomTable::GetEntryText](ms-its:sldworksapivb6.chm::/sldworks~BomTable~GetEntryText.html).

## Remarks

Use [IBomTable::GetEntryValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~GetEntryValue.html) for typed return values.

Before you use any of the IBomTable methods, activate the BOM table using [IBomTable::Attach3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Attach3.html). After you finish getting BOM data, use [IBomTable::Detach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Detach.html) to deactivate the table.

## See Also

[IBomTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.html)
[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.html)
