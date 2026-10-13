---
title: "DSldWorksEvents_BackgroundProcessingEndNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_BackgroundProcessingEndNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_BackgroundProcessingEndNotifyEventHandler.html"
---

# DSldWorksEvents_BackgroundProcessingEndNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program when background processing has ended.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_BackgroundProcessingEndNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_BackgroundProcessingEndNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_BackgroundProcessingEndNotifyEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_BackgroundProcessingEndNotifyEventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Drawing file for which background processing has ended

## VBA Syntax

See [BackgroundProcessingEndNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~BackgroundProcessingEndNotify_EV.html).

## Examples

[Fire Notifications for Background Processing Events (VBA)](Fire_Notification_for_Background_Processing_Events_Example_VB.htm)
[Fire Notifications for Background Processing Events (VB.NET)](Fire_Notification_for_Background_Processing_Events_Example_VBNET.htm)
[Fire Notifications for Background Processing Events (C#)](Fire_Notification_for_Background_Processing_Events_Example_CSharp.htm)

## Remarks

If developing a C++ application, use [swAppBackgroundProcessingEndNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
