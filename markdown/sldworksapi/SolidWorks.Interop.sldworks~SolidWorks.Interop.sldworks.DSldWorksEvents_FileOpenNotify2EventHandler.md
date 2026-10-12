---
title: "DSldWorksEvents_FileOpenNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_FileOpenNotify2EventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileOpenNotify2EventHandler.html"
---

# DSldWorksEvents_FileOpenNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when an existing file has been opened.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_FileOpenNotify2EventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_FileOpenNotify2EventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_FileOpenNotify2EventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_FileOpenNotify2EventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the opened file

## VBA Syntax

See [FileOpenNotify2 Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~FileOpenNotify2_EV.html).

## Remarks

You can use [ISldWorks::GetOpenDocumentByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetOpenDocumentByName.html) or [ISldWorks::IGetOpenDocumentByName2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.html) with FileName to get a pointer to the newly opened document. Because it is possible to have a NULL active document when an add-in is notified by swAppFileOpenNotify2, use [ISldWorks::IGetOpenDocumentByName2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.html) instead of [ISldWorks::IActiveDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IActiveDoc2.html).

This event is very similar to the now obsolete SldWorks events [FileOpenNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_FileOpenNotifyEventHandler.html) event. The difference is that the SOLIDWORKS event FileOpenNotify2 is fired later in the process than the SOLIDWORKS event FileOpenNotify, so that if end-users respond to the event by opening a new part, then NewDocument, NewPart, NewAssembly, or NewDrawing2 is successful.

This event is sent to any application when a file is opened programmatically using [ISldWorks::OpenDoc6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html). Your application can detect the newly opened document by watching the the SOLIDWORKS events [ActiveModelDocChangeNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_ActiveDocChangeNotifyEventHandler.html) event.

With the exception of Parasolid files (that is, *.x_t, *.x_b), this event is not sent for the opening of non-native SOLIDWORKS files (that is, *.igs, *.dxf, and so on). Opening non-native files is typically handled with the creation of a new SOLIDWORKS file (that is, *.sldprt, *.sldasm, *.slddrw) and the subsequent construction of the foreign geometry within that file.

If developing a C++ application, use [swAppFileOpenNotify2](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
