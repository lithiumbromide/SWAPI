---
title: "SetEntryText Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "SetEntryText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetEntryText.html"
---

# SetEntryText Method (IDesignTable)

Sets the text value of the specified entry.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetEntryText( _
   ByVal Row As System.Integer, _
   ByVal Col As System.Integer, _
   ByVal TextIn As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDesignTable
Dim Row As System.Integer
Dim Col As System.Integer
Dim TextIn As System.String

instance.SetEntryText(Row, Col, TextIn)
```

### C#

```csharp
void SetEntryText(
   System.int Row,
   System.int Col,
   System.string TextIn
)
```

### C++/CLI

```cpp
void SetEntryText(
   System.int Row,
   System.int Col,
   System.String^ TextIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: Row number
- `Col`: Column number
- `TextIn`: Text value for entry

## VBA Syntax

See [DesignTable::SetEntryText](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~SetEntryText.html).

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::SetEntryValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetEntryValue.html)
[IDesignTable::GetEntryText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryText.html)
[IDesignTable::GetEntryValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetEntryValue.html)

## Availability

SOLIDWORKS 2000 SP01, Revision Number 8.1
