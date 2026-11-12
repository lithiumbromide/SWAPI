---
title: "DSldWorksEvents_BeginRecordNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_BeginRecordNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_BeginRecordNotifyEventHandler.html"
---

# DSldWorksEvents_BeginRecordNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program when a macro recording has started.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_BeginRecordNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_BeginRecordNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_BeginRecordNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_BeginRecordNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [BeginRecordNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~BeginRecordNotify_EV.html).

## Examples

[Record Macros (C#)](Record_Macros_Example_CSharp.htm)
[Record Macros (VB.NET)](Record_Macros_Example_VBNET.htm)
[Record Macros (VBA)](Record_Macros_Example_VB.htm)

## Remarks

This event informs the user program when a macro recording has started so that the add-in can add its own initialization code to a macro using [ISldWorks::RecordLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RecordLine.html), [ISldWorks::RecordLineCSharp](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RecordLineCSharp.html), or [ISldWorks::RecordLineVBnet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RecordLineVBnet.html). This is useful if the add-in is recording its own lines of code to the macro and needs to declare and initialize variables.

The SOLIDWORKS event [EndRecordNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_EndRecordNotifyEventHandler.html) is sent when the macro recording is stopping.

These events are not sent when the macro is paused and restarted. ISldWorks::RecordLine, ISldWorks::RecordLineCSharp, or ISldWorks::RecordLineVBnet can be used at any time, regardless of whether a macro is currently recording or not. Even if no macro is running, writing to the SOLIDWORKS journal file occurs.

If developing a C++ application, use [swAppBeginRecordNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
