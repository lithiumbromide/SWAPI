---
title: "GetEntryValue Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "GetEntryValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryValue.html"
---

# GetEntryValue Method (IDesignTable)

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
Dim instance As IDesignTable
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

- `Row`: 0-based row number of the cell
- `Col`: 0-based column number of the cell

### Return Value

Object containing the information from the specified cell

## VBA Syntax

See [DesignTable::GetEntryValue](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~GetEntryValue.html).

## Remarks

After you receive a valid return value from this method, you can evaluate the the data type of the object (for example, double, long, or string).

Use [IDesignTable::GetEntryText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~GetEntryText.html) to return the cell contents as a string.

Before you use any of the design table methods, you must first activate the design table using [IDesignTable::Attach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~Attach.html). After you are finished getting design table data, you can deactivate the table using [IDesignTable::Detach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~Detach.html).

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::GetEntryText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryText.html)
[IDesignTable::SetEntryText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetEntryText.html)
[IDesignTable::SetEntryValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetEntryValue.html)
