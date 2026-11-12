---
title: "GetEntryValue Method (IBomTable)"
project: "SOLIDWORKS API Help"
interface: "IBomTable"
member: "GetEntryValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetEntryValue.html"
---

# GetEntryValue Method (IBomTable)

Gets the contents of the specified cell.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntryValue( _
   ByVal Row As System.Integer, _
   ByVal Col As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTable
Dim Row As System.Integer
Dim Col As System.Integer
Dim value As System.Object

value = instance.GetEntryValue(Row, Col)
```

### C#

```csharp
System.object GetEntryValue(
   System.int Row,
   System.int Col
)
```

### C++/CLI

```cpp
System.Object^ GetEntryValue(
   System.int Row,
   System.int Col
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: Row number of the desired cell; this is a 0-based index
- `Col`: Column number of the desired cell; this is a 0-based index

### Return Value

Object containing the information from the specified cell

## VBA Syntax

See [BomTable::GetEntryValue](ms-its:sldworksapivb6.chm::/sldworks~BomTable~GetEntryValue.html).

## Remarks

After you receive a valid return value, you can evaluate the for the object's data type.

To return the cell contents as a string, use [IBomTable::GetEntryText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~GetEntryText.html).

Before you use any of the IBomTable methods, activate the BOM table using [IBomTable::Attach3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Attach3.html). After you finish getting BOM data, use [IBomTable::Detach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Detach.html) to deactivate the table.

## See Also

[IBomTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.html)
[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.html)
