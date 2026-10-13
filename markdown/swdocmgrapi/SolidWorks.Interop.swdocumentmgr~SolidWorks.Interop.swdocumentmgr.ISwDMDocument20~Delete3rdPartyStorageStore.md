---
title: "Delete3rdPartyStorageStore Method (ISwDMDocument20)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument20"
member: "Delete3rdPartyStorageStore"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20~Delete3rdPartyStorageStore.html"
---

# Delete3rdPartyStorageStore Method (ISwDMDocument20)

Deletes the specified third-party storage store.

## Syntax

### Visual Basic (Declaration)

```vb
Function Delete3rdPartyStorageStore( _
   ByVal SubStorageName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument20
Dim SubStorageName As System.String
Dim value As System.Boolean

value = instance.Delete3rdPartyStorageStore(SubStorageName)
```

### C#

```csharp
System.bool Delete3rdPartyStorageStore(
   System.string SubStorageName
)
```

### C++/CLI

```cpp
System.bool Delete3rdPartyStorageStore(
   System.String^ SubStorageName
)
```

### Parameters

- `SubStorageName`: Name of the storage to delete

### Return Value

True if the storage is deleted, false if not

## VBA Syntax

See [SwDMDocument20::Delete3rdPartyStorageStore](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument20~Delete3rdPartyStorageStore.html).

## See Also

[ISwDMDocument20 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20.html)
[ISwDMDocument20 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20_members.html)
[ISwDMDocument19::Get3rdPartyStorageStore Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Get3rdPartyStorageStore.html)
[ISwDMDocument19::Release3rdPartyStorageStore Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Release3rdPartyStorageStore.html)
[ISwDMDocument20::Delete3rdPartyStorage Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20~Delete3rdPartyStorage.html)

## Availability

SOLIDWORKS Document Manager API 2016 FCS
