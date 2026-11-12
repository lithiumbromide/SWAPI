---
title: "GetExternalDesignTable Method (ISwDMDocument13)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument13"
member: "GetExternalDesignTable"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetExternalDesignTable.html"
---

# GetExternalDesignTable Method (ISwDMDocument13)

Gets the path to an external (i.e., linked) design table, if one exists.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExternalDesignTable( _
   ByVal pSrcOption As SwDMSearchOption, _
   ByRef Status As SwDmDesignTableDataError _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument13
Dim pSrcOption As SwDMSearchOption
Dim Status As SwDmDesignTableDataError
Dim value As System.String

value = instance.GetExternalDesignTable(pSrcOption, Status)
```

### C#

```csharp
System.string GetExternalDesignTable(
   SwDMSearchOption pSrcOption,
   out SwDmDesignTableDataError Status
)
```

### C++/CLI

```cpp
System.String^ GetExternalDesignTable(
   SwDMSearchOption^ pSrcOption,
   [Out] SwDmDesignTableDataError Status
)
```

### Parameters

- `pSrcOption`: Pointer to an [ISwDMSerachOption](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSearchOption.html) object
- `Status`: Error status as defined by [SwDmDesignTableDataError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmDesignTableDataError.html)

## VBA Syntax

See [SwDMDocument13::GetExternalDesignTable](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument13~GetExternalDesignTable.html).

## See Also

[ISwDMDocument13 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13.html)
[ISwDMDocument13 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13_members.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
