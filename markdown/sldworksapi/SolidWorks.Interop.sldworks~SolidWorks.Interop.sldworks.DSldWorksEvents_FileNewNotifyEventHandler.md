---
title: "DSldWorksEvents_FileNewNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_FileNewNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileNewNotifyEventHandler.html"
---

# DSldWorksEvents_FileNewNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Obsolete. Superseded by [DSldWorksEvents_FileNewNotify2EventHandler](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_FileNewNotify2EventHandler.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_FileNewNotifyEventHandler( _
   ByVal NewDoc As System.Object, _
   ByVal DocType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_FileNewNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_FileNewNotifyEventHandler(
   System.object NewDoc,
   System.int DocType
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_FileNewNotifyEventHandler(
   System.Object^ NewDoc,
   System.int DocType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewDoc`:
- `DocType`:

## VBA Syntax

See [FileNewNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~FileNewNotify_EV.html).

## Availability
