---
title: "Delete3rdPartyStorage Method (ISwDMDocument20)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument20"
member: "Delete3rdPartyStorage"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20~Delete3rdPartyStorage.html"
---

# Delete3rdPartyStorage Method (ISwDMDocument20)

Deletes the specified third-party storage.

## Syntax

### Visual Basic (Declaration)

```vb
Function Delete3rdPartyStorage( _
   ByVal StringIn As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument20
Dim StringIn As System.String
Dim value As System.Boolean

value = instance.Delete3rdPartyStorage(StringIn)
```

### C#

```csharp
System.bool Delete3rdPartyStorage(
   System.string StringIn
)
```

### C++/CLI

```cpp
System.bool Delete3rdPartyStorage(
   System.String^ StringIn
)
```

### Parameters

- `StringIn`: Name of the stream to delete

### Return Value

True if the stream is deleted, false if not

## VBA Syntax

See [SwDMDocument20::Delete3rdPartyStorage](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument20~Delete3rdPartyStorage.html).

## See Also

[ISwDMDocument20 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20.html)
[ISwDMDocument20 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20_members.html)
[ISwDMDocument19::Get3rdPartyStorage Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Get3rdPartyStorage.html)
[ISwDMDocument19::Release3rdPartyStorage Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Release3rdPartyStorage.html)
[ISwDMDocument20::Delete3rdPartyStorageStore Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20~Delete3rdPartyStorageStore.html)

## Availability

SOLIDWORKS Document Manager API 2016 FCS
