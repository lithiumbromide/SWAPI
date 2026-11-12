---
title: "RemoveSearchPath Method (ISwDMSearchOption)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMSearchOption"
member: "RemoveSearchPath"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption~RemoveSearchPath.html"
---

# RemoveSearchPath Method (ISwDMSearchOption)

Removes the specified search path.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveSearchPath( _
   ByVal remPath As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMSearchOption
Dim remPath As System.String

instance.RemoveSearchPath(remPath)
```

### C#

```csharp
void RemoveSearchPath(
   System.string remPath
)
```

### C++/CLI

```cpp
void RemoveSearchPath(
   System.String^ remPath
)
```

### Parameters

- `remPath`: Search path to remove; for example, C:\parts

## VBA Syntax

See [SwDMSearchOption::RemoveSearchPath](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMSearchOption~RemoveSearchPath.html).

## See Also

[ISwDMSearchOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.html)
[ISwDMSearchOption Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
