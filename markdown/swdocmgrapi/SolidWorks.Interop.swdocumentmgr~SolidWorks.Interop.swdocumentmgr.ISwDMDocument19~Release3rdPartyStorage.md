---
title: "Release3rdPartyStorage Method (ISwDMDocument19)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument19"
member: "Release3rdPartyStorage"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Release3rdPartyStorage.html"
---

# Release3rdPartyStorage Method (ISwDMDocument19)

Closes the specified third-party storage.

## Syntax

### Visual Basic (Declaration)

```vb
Function Release3rdPartyStorage( _
   ByVal StringIn As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument19
Dim StringIn As System.String
Dim value As System.Boolean

value = instance.Release3rdPartyStorage(StringIn)
```

### C#

```csharp
System.bool Release3rdPartyStorage(
   System.string StringIn
)
```

### C++/CLI

```cpp
System.bool Release3rdPartyStorage(
   System.String^ StringIn
)
```

### Parameters

- `StringIn`: Name of the stream to close

### Return Value

True if stream is closed, false if not

## VBA Syntax

See [SwDMDocument19::Release3rdPartyStorage](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument19~Release3rdPartyStorage.html).

## Examples

[Read and Write to Third-party Storage (VB.NET)](Get_and_Set_3rd_Party_Storage_Example_VBNET.htm)
[Read and Write to Third-party Storage (C#)](Get_and_Set_3rd_Party_Storage_Example_CSharp.htm)

## Remarks

You must call this method after calling [ISwDMDocument19::Get3rdPartyStorage](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Get3rdPartyStorage.html).

## See Also

[ISwDMDocument19 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19.html)
[ISwDMDocument19 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19_members.html)
[ISwDMDocument20::Delete3rdPartyStorage Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20~Delete3rdPartyStorage.html)
[ISwDMDocument19::Release3rdPartyStorageStore Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Release3rdPartyStorageStore.html)

## Availability

SOLIDWORKS Document Manager API 2015 SP0
