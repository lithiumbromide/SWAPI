---
title: "GetEntryText Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "GetEntryText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryText.html"
---

# GetEntryText Method (IDesignTable)

Gets the contents of the specified cell as a string regardless of the cell's data type.

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
Dim instance As IDesignTable
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

- `Row`: 0-based row number of the cell
- `Col`: 0-based column number of the cell

### Return Value

Text string in the specified cell

## VBA Syntax

See [DesignTable::GetEntryText](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~GetEntryText.html).

## Examples

[Get Design Table (VBA)](Get_Design_Table_Example_VB.htm)
[Get Design Table (VB.NET)](Get_Design_Table_Example_VBNET.htm)
[Get Design Table (C#)](Get_Design_Table_Example_CSharp.htm)

## Remarks

For example, if the cell is of type double, it is returned as a string.

Use [IDesignTable::GetEntryValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~GetEntryValue.html) to get typed return values.

Before using any of the [IDesignTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable.html) methods, use [IDesignTable::Attach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~Attach.html) to activate the design table. After you are finish getting design table data, use [IDesignTable::Detach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~Detach.html) to deactivate the table.

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::GetEntryValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryValue.html)
[IDesignTable::SetEntryText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetEntryText.html)
[IDesignTable::SetEntryValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetEntryValue.html)
