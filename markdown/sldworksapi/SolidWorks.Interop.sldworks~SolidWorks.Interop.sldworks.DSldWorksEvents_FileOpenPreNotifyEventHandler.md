---
title: "DSldWorksEvents_FileOpenPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_FileOpenPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileOpenPreNotifyEventHandler.html"
---

# DSldWorksEvents_FileOpenPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program of a [FileOpenNotify2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_FileOpenNotify2EventHandler.html) event.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_FileOpenPreNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_FileOpenPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_FileOpenPreNotifyEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_FileOpenPreNotifyEventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Full path and name of file to open

## VBA Syntax

See [FileOpenPreNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~FileOpenPreNotify_EV.html).

## Remarks

This event is only fired when opening these SOLIDWORKS files: parts, drawings, and assemblies. It is not fired when opening files like templates, translator files, and so on.

This event is fired before SOLIDWORKS begins loading the file. A SOLIDWORKS file can be opened in many ways; for example, File, Open in the user interface, [ISldWorks::OpenDoc6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html) in the API, Load Model from a Detached drawing, Lightweight component being resolved, and so on. This event is fired in all of these cases.

If you want to allow SOLIDWORKS to open the file, return S_OK (or 0) from the handler. If you do not want to allow SOLIDWORKS to open the file, return S_false (or any code other than S_OK) from the handler.

The event that occurs after this event is [DocumentLoadNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_DocumentLoadNotifyEventHandler.html).

If developing a C++ application, use [swAppFileOpenPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
