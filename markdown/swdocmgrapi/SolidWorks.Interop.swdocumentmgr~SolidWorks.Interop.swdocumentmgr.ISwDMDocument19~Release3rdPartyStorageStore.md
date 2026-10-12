---
title: "Release3rdPartyStorageStore Method (ISwDMDocument19)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument19"
member: "Release3rdPartyStorageStore"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Release3rdPartyStorageStore.html"
---

# Release3rdPartyStorageStore Method (ISwDMDocument19)

Closes the specified third-party storage store.

## Syntax

### Visual Basic (Declaration)

```vb
Function Release3rdPartyStorageStore( _
   ByVal SubStorageName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument19
Dim SubStorageName As System.String
Dim value As System.Boolean

value = instance.Release3rdPartyStorageStore(SubStorageName)
```

### C#

```csharp
System.bool Release3rdPartyStorageStore(
   System.string SubStorageName
)
```

### C++/CLI

```cpp
System.bool Release3rdPartyStorageStore(
   System.String^ SubStorageName
)
```

### Parameters

- `SubStorageName`: Name of the storage to close

### Return Value

True if the storage is closed, false if not

## VBA Syntax

See [SwDMDocument19::Release3rdPartyStorageStore](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument19~Release3rdPartyStorageStore.html).

## Examples

[Read and Write to Third-party Storage (VB.NET)](Get_and_Set_3rd_Party_Storage_Example_VBNET.htm)
[Read and Write to Third-party Storage (C#)](Get_and_Set_3rd_Party_Storage_Example_CSharp.htm)

## Remarks

You must call this method after calling [ISwDMDocument19::Get3rdPartyStorageStore](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Get3rdPartyStorageStore.html).

## See Also

[ISwDMDocument19 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19.html)
[ISwDMDocument19 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19_members.html)
[ISwDMDocument19::Release3rdPartyStorage Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Release3rdPartyStorage.html)
[ISwDocument20::Delete3rdPartyStorageStore Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20~Delete3rdPartyStorageStore.html)

## Availability

SOLIDWORKS Document Manager API 2015 SP0
