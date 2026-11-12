---
title: "IRelease3rdPartyStorage Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IRelease3rdPartyStorage"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IRelease3rdPartyStorage.html"
---

# IRelease3rdPartyStorage Method (IModelDoc2)

Releases the specified third-party stream.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IRelease3rdPartyStorage( _
   ByVal StringIn As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim StringIn As System.String

instance.IRelease3rdPartyStorage(StringIn)
```

### C#

```csharp
void IRelease3rdPartyStorage(
   System.string StringIn
)
```

### C++/CLI

```cpp
void IRelease3rdPartyStorage(
   System.String^ StringIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StringIn`: Name of the stream to release

## VBA Syntax

See [ModelDoc2::IRelease3rdPartyStorage](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IRelease3rdPartyStorage.html).

## Remarks

You can use this method with [IModelDoc2::IGet3rdPartyStorage](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGet3rdPartyStorage.html). You must use it if you are not using the LoadFromStorageNotify event. You must call this method when the call to IModelDoc2::IGet3rdPartyStorage returns a NULL stream.

NOTE: If you are using serialization, then be careful with the standard MFC macros; otherwise, you can get messages like Unexpected File Format after your application is unloaded. One way of using IMPLEMENT_SERIAL is:

```vb
IMPLEMENT_SERIAL( CCustomAttr, CObject, VERSIONABLE_SCHEMA|0 )
```

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[DAssemblyDocEvents_LoadFromStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_LoadFromStorageNotifyEventHandler.html)
[DAssemblyDocEvents_SaveToStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SaveToStorageNotifyEventHandler.html)
[DDrawingDocEvents_LoadFromStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_LoadFromStorageNotifyEventHandler.html)
[DDrawingDocEvents_SaveToStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_SaveToStorageNotifyEventHandler.html)
[DPartDocEvents_LoadFromStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_LoadFromStorageNotifyEventHandler.html)
[DPartDocEvents_SaveToStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SaveToStorageNotifyEventHandler.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
