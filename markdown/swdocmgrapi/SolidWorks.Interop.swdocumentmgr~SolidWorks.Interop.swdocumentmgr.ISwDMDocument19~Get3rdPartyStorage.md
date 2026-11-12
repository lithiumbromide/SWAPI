---
title: "Get3rdPartyStorage Method (ISwDMDocument19)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument19"
member: "Get3rdPartyStorage"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Get3rdPartyStorage.html"
---

# Get3rdPartyStorage Method (ISwDMDocument19)

Gets an IStream interface to the specified third-party storage of this model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function Get3rdPartyStorage( _
   ByVal StringIn As System.String, _
   ByVal IsStoring As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument19
Dim StringIn As System.String
Dim IsStoring As System.Boolean
Dim value As System.Object

value = instance.Get3rdPartyStorage(StringIn, IsStoring)
```

### C#

```csharp
System.object Get3rdPartyStorage(
   System.string StringIn,
   System.bool IsStoring
)
```

### C++/CLI

```cpp
System.Object^ Get3rdPartyStorage(
   System.String^ StringIn,
   System.bool IsStoring
)
```

### Parameters

- `StringIn`: Name of the stream; the name should be less than 30 characters and must be unique and qualified among all of the software parties storing within the current session
- `IsStoring`: True if writing data, false if reading data

### Return Value

Pointer to Unknown (see **Remarks**)

## VBA Syntax

See [SwDMDocument19::Get3rdPartyStorage](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument19~Get3rdPartyStorage.html).

## Examples

[Read and Write to Third-party Storage (VB.NET)](Get_and_Set_3rd_Party_Storage_Example_VBNET.htm)
[Read and Write to Third-party Storage (C#)](Get_and_Set_3rd_Party_Storage_Example_CSharp.htm)

## Remarks

After calling this method, you must call [ISwDMDocument19::Release3rdPartyStorage](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Release3rdPartyStorage.html). Otherwise, the third-party node might remain locked and prevent future access.

NOTE: The name given to the storage stream should be registered so that no conflicts occur. Once registered, the stream name is reserved exclusively for your application.

Passing the unique ID string and a flag to determine if data is being stored or loaded returns an IUnknown pointer. You must then use QueryInterface() to get the **Microsoft.VisualStudio.OLE.Interop.IStream** interface. The stream object is used for serialization and then released in the third-party code.

SwRootStorage --|

|-- ThirdPty --|

|-- <SW Assigned IStream name 1>

|-- <SW Assigned IStream name 2>

|-- <SW Assigned IStream name 3>

...

|-- <SW Assigned IStream name `n`>

The IStream object used by the third party is written under an IStorage object called ThirdPty in the SOLIDWORKS compound document. Each third party writes to a single IStream object whose name is assigned by SOLIDWORKS.

NOTE: If you are using serialization, then be careful with the standard MFC macros. Otherwise, you may get a message like Unexpected File Format after your application is unloaded. One way of using IMPLEMENT_SERIAL:

IMPLEMENT_SERIAL( CCustomAttr, CObject, VERSIONABLE_SCHEMA|0 )

## See Also

[ISwDMDocument19 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19.html)
[ISwDMDocument19 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19_members.html)
[ISwDMDocument19::Get3rdPartyStorageStore Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~Get3rdPartyStorageStore.html)
[ISwDMDocument20::Delete3rdPartyStorage Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20~Delete3rdPartyStorage.html)

## Availability

SOLIDWORKS Document Manager API 2015 SP0
