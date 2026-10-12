---
title: "DSldWorksEvents_EndRecordNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_EndRecordNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_EndRecordNotifyEventHandler.html"
---

# DSldWorksEvents_EndRecordNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program when a macro recording has ended, including if the user cancels the recording (i.e., the user cancels out of the Save As dialog and says No to the Continue recording? dialog).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_EndRecordNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_EndRecordNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_EndRecordNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_EndRecordNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [EndRecordNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~EndRecordNotify_EV.html).

## Examples

[Record Macros (C#)](Record_Macros_Example_CSharp.htm)
[Record Macros (VB.NET)](Record_Macros_Example_VBNET.htm)
[Record Macros (VBA)](Record_Macros_Example_VB.htm)

## Remarks

This event informs the user program when a macro recording has stopped so that the add-in can add its own cleanup code to a macro using [ISldWorks::RecordLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RecordLine.html), [ISldWorks::RecordLineCSharp](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RecordLineCSharp.html), or [ISldWorks::RecordLineVBnet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RecordLineVBnet.html). This is useful if the add-in has been recording its own lines of code to the macro and needs to clean up variables that have been used.

The SOLIDWORKS event [BeginRecordNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_BeginRecordNotifyEventHandler.html) is sent when the macro recording is starting.

These events are not sent when the macro is paused and restarted. SldWorks::RecordLine, ISldWorks::RecordLineCSharp, or ISldWorks::RecordLineVBnet can be used at any time, regardless of whether a macro is currently recording or not. Even if no macro is running, writing to the journal file occurs.

If developing a C++ application, use [swAppEndRecordNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
