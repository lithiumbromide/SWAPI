---
title: "DPartDocEvents_ConvertToBodiesPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_ConvertToBodiesPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ConvertToBodiesPreNotifyEventHandler.html"
---

# DPartDocEvents_ConvertToBodiesPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired before the Convert to Bodies dialog opens.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_ConvertToBodiesPreNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_ConvertToBodiesPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_ConvertToBodiesPreNotifyEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_ConvertToBodiesPreNotifyEventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: File name of the part to convert to a body

## VBA Syntax

See [ConvertToBodiesPreNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~ConvertToBodiesPreNotify_EV.html).

## Remarks

This event is triggered before the Convert to Bodies dialog displays.

If developing a C++ application, use [swPartConvertToBodiesPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
