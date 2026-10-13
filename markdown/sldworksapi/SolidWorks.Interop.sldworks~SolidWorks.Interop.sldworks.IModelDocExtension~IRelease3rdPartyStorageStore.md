---
title: "IRelease3rdPartyStorageStore Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IRelease3rdPartyStorageStore"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IRelease3rdPartyStorageStore.html"
---

# IRelease3rdPartyStorageStore Method (IModelDocExtension)

Releases the specified third-party storage in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function IRelease3rdPartyStorageStore( _
   ByVal SubStorageName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim SubStorageName As System.String
Dim value As System.Boolean

value = instance.IRelease3rdPartyStorageStore(SubStorageName)
```

### C#

```csharp
System.bool IRelease3rdPartyStorageStore(
   System.string SubStorageName
)
```

### C++/CLI

```cpp
System.bool IRelease3rdPartyStorageStore(
   System.String^ SubStorageName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SubStorageName`: Name of the third-party storage

### Return Value

True if the data is released, false if not

## VBA Syntax

See [ModelDocExtension::IRelease3rdPartyStorageStore](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~IRelease3rdPartyStorageStore.html).

## Remarks

You can use this method with [IModelDocExtension::IGet3rdPartyStorageStore](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGet3rdPartyStorageStore.html). You must use it if you are not using the LoadFromStorageStoreNotify event. You must call this method when the call to IModelDocExtension::IGet3rdPartyStorageStore returns a NULL stream.

NOTE: If you are using serialization, then be careful with the standard MFC macros; otherwise, you can get messages like "Unexpected File Format" after your application is unloaded. One way of using IMPLEMENT_SERIAL is:

```vb
IMPLEMENT_SERIAL( CCustomAttr, CObject, VERSIONABLE_SCHEMA|0 )
```

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[DAssemblyDocEvents LoadFromStorageNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_LoadFromStorageNotifyEventHandler.html)
[DDrawingDocEvents LoadFromStorageNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_LoadFromStorageNotifyEventHandler.html)
[DPartDocEvents LoadFromStorageNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_LoadFromStorageNotifyEventHandler.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
