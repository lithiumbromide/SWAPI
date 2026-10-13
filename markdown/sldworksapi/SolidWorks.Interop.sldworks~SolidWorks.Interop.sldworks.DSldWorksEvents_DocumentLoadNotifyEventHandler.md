---
title: "DSldWorksEvents_DocumentLoadNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_DocumentLoadNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_DocumentLoadNotifyEventHandler.html"
---

# DSldWorksEvents_DocumentLoadNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Obsolete. Superseded by [DSldWorksEvetns_DocumentLoadNotify2EventHandler](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_DocumentLoadNotify2EventHandler.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_DocumentLoadNotifyEventHandler( _
   ByVal docTitle As System.String, _
   ByVal docPath As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_DocumentLoadNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_DocumentLoadNotifyEventHandler(
   System.string docTitle,
   System.string docPath
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_DocumentLoadNotifyEventHandler(
   System.String^ docTitle,
   System.String^ docPath
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `docTitle`:
- `docPath`:

## VBA Syntax

See [DocumentLoadNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~DocumentLoadNotify_EV.html).

## Availability
