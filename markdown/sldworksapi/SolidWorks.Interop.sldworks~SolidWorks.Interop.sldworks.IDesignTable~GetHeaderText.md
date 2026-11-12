---
title: "GetHeaderText Method (IDesignTable)"
project: "SOLIDWORKS API Help"
interface: "IDesignTable"
member: "GetHeaderText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetHeaderText.html"
---

# GetHeaderText Method (IDesignTable)

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
Dim instance As IDesignTable
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

- `Col`: 0-based column number with the header text

### Return Value

Text string from the column header

## VBA Syntax

See [DesignTable::GetHeaderText](ms-its:sldworksapivb6.chm::/sldworks~DesignTable~GetHeaderText.html).

## Remarks

Before you use any of the design table methods, you must first activate the design table using [IDesignTable::Attach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~Attach.html). After you are finished getting design table data, you can deactivate the table using [IDesignTable::Detach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable~Detach.html).

## See Also

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html)
[IDesignTable::GetColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetColumnCount.html)
[IDesignTable::GetStartColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartColumnNumber.html)
[IDesignTable::GetTotalColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalColumnCount.html)
[IDesignTable::GetVisibleColumnCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleColumnCount.html)
[IDesignTable::GetVisibleLeftColumnNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleLeftColumnNumber.html)
[IDesignTable::ColumnHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~ColumnHidden.html)
