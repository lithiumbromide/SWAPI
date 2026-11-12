---
title: "DAssemblyDocEvents_PublishTo3DPDFNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_PublishTo3DPDFNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_PublishTo3DPDFNotifyEventHandler.html"
---

# DAssemblyDocEvents_PublishTo3DPDFNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when publishing an assembly document to SOLIDWORKS MBD 3D PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_PublishTo3DPDFNotifyEventHandler( _
   ByVal Path As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_PublishTo3DPDFNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_PublishTo3DPDFNotifyEventHandler(
   System.string Path
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_PublishTo3DPDFNotifyEventHandler(
   System.String^ Path
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Path`: Path where SOLIDWORKS MBD 3D PDF is saved

## VBA Syntax

See [PublishTo3DPDF Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~PublishTo3DPDFNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyPublishTo3DPDFNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
