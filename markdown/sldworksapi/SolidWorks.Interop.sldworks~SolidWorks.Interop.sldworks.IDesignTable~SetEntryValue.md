---
title: "SetEntryValue Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "SetEntryValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetEntryValue.html"
---

# SetEntryValue Method (IDesignTable)

Sets the data type and value in the specified cell.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetEntryValue( _
   ByVal Row As System.Integer, _
   ByVal Col As System.Integer, _
   ByVal IsText As System.Boolean, _
   ByVal Retval As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim Row As System.Integer
Dim Col As System.Integer
Dim IsText As System.Boolean
Dim Retval As System.String

instance.SetEntryValue(Row, Col, IsText, Retval)
```

### C#

```csharp
void SetEntryValue(
   System.int Row,
   System.int Col,
   System.bool IsText,
   System.string Retval
)
```

### C++/CLI

```cpp
void SetEntryValue(
   System.int Row,
   System.int Col,
   System.bool IsText,
   System.String^ Retval
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: Row number
- `Col`: Column number
- `IsText`: True for text, false for general
- `Retval`: Value of the specific cell

## VBA Syntax

See [DesignTable::SetEntryValue](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~SetEntryValue.html).

## Remarks

This method lets you change the data type from text to general and from general to text and specify a value.

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::GetEntryText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryText.html)
[IDesignTable::GetEntryValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryValue.html)
[IDesignTable::SetEntryText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetEntryText.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
