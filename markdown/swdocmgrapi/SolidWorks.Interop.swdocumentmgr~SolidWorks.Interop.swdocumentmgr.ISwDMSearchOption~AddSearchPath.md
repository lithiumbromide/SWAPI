---
title: "AddSearchPath Method (ISwDMSearchOption)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMSearchOption"
member: "AddSearchPath"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption~AddSearchPath.html"
---

# AddSearchPath Method (ISwDMSearchOption)

Adds a new search path.

## Syntax

### Visual Basic (Declaration)

```vb
Sub AddSearchPath( _
   ByVal newPath As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMSearchOption
Dim newPath As System.String

instance.AddSearchPath(newPath)
```

### C#

```csharp
void AddSearchPath(
   System.string newPath
)
```

### C++/CLI

```cpp
void AddSearchPath(
   System.String^ newPath
)
```

### Parameters

- `newPath`: Search path; for example, C:\parts

## VBA Syntax

See [SwDMSearchOption::AddSearchPath](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMSearchOption~AddSearchPath.html).

## See Also

[ISwDMSearchOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.html)
[ISwDMSearchOption Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
