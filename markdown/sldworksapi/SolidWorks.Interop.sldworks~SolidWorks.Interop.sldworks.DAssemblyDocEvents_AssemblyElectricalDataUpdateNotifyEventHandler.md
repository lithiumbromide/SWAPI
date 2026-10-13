---
title: "DAssemblyDocEvents_AssemblyElectricalDataUpdateNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_AssemblyElectricalDataUpdateNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_AssemblyElectricalDataUpdateNotifyEventHandler.html"
---

# DAssemblyDocEvents_AssemblyElectricalDataUpdateNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the SOLIDWORKS Design software updates the electrical data.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_AssemblyElectricalDataUpdateNotifyEventHandler( _
   ByVal saveType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_AssemblyElectricalDataUpdateNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_AssemblyElectricalDataUpdateNotifyEventHandler(
   System.int saveType
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_AssemblyElectricalDataUpdateNotifyEventHandler(
   System.int saveType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `saveType`: - 0 = All streams
  - 2 = From-To list stream
  - 3 = Segment data stream
  - 4 = Wire list stream

## VBA Syntax

See [AssemblyElectricalDataUpdateNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~AssemblyElectricalDataUpdateNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyElectricalDataUpdateNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Third-party applications should handle this notification to reload the electrical data from the data streams when the SOLIDWORKS Design software writes to them. Currently, this event only occurs when a user exits a route.

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
