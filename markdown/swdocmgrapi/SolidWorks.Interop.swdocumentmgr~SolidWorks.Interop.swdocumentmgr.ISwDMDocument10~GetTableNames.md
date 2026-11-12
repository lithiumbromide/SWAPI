---
title: "GetTableNames Method (ISwDMDocument10)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument10"
member: "GetTableNames"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetTableNames.html"
---

# GetTableNames Method (ISwDMDocument10)

Gets the names of the tables in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableNames( _
   ByVal TableType As SwDmTableType _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument10
Dim TableType As SwDmTableType
Dim value As System.Object

value = instance.GetTableNames(TableType)
```

### C#

```csharp
System.object GetTableNames(
   SwDmTableType TableType
)
```

### C++/CLI

```cpp
System.Object^ GetTableNames(
   SwDmTableType TableType
)
```

### Parameters

- `TableType`: Type of table as defined by [swDMTableType](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmTableType.html)

### Return Value

Array of table names

## VBA Syntax

See [SwDMDocument10::GetTableNames](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument10~GetTableNames.html).

## Examples

[Get BOM Tables (C#)](Get_BOM_Tables_Example_CSharp.htm)
[Get BOM Tables (VB.NET)](Get_BOM_Tables_Example_VBNET.htm)

## See Also

[ISwDMDocument10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10.html)
[ISwDMDocument10 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10_members.html)
[ISwDMDocument10::GetTable Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetTable.html)
[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.html)
[ISwDMTable2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
