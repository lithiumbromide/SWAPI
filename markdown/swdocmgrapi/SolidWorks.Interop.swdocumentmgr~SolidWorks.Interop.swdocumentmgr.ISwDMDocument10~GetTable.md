---
title: "GetTable Method (ISwDMDocument10)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument10"
member: "GetTable"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetTable.html"
---

# GetTable Method (ISwDMDocument10)

Gets the specified table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTable( _
   ByVal NameIn As System.String _
) As SwDMTable
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument10
Dim NameIn As System.String
Dim value As SwDMTable

value = instance.GetTable(NameIn)
```

### C#

```csharp
SwDMTable GetTable(
   System.string NameIn
)
```

### C++/CLI

```cpp
SwDMTable^ GetTable(
   System.String^ NameIn
)
```

### Parameters

- `NameIn`: Name of table

### Return Value

[Table](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMTable.html)

## VBA Syntax

See [SwDMDocument10::GetTable](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument10~GetTable.html).

## Examples

[Get BOM Tables (C#)](Get_BOM_Tables_Example_CSharp.htm)
[Get BOM Tables (VB.NET)](Get_BOM_Tables_Example_VBNET.htm)

## Remarks

Only revision and bill of materials (BOM) tables are supported.

Before calling this method, call [ISwDMDocument10::GetTableNames](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument10~GetTableNames.html) to get the names of the tables in this document.

## See Also

[ISwDMDocument10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10.html)
[ISwDMDocument10 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10_members.html)
[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.html)
[ISwDMTable2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
