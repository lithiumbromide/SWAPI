---
title: "FileSize Property (IEdmSearchResult5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearchResult5"
member: "FileSize"
kind: "property"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult5~FileSize.html"
---

# FileSize Property (IEdmSearchResult5)

Gets the size of this search result.

## Syntax

### Visual Basic

```vb
ReadOnly Property FileSize As System.Integer
```

### C#

```csharp
System.int FileSize {get;}
```

### C++/CLI

```cpp
property System.int FileSize {
   System.int get();
}
```

### Property Value

Size of the file; -1 for folders

## Remarks

For very large file size search results, use [IEdmSearchResult6::FileSize2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult6~FileSize2.html).

## See Also

[IEdmSearchResult5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult5.html)
[IEdmSearchResult5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
