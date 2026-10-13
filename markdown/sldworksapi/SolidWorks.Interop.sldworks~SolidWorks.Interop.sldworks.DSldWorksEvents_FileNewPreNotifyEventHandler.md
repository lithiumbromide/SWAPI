---
title: "DSldWorksEvents_FileNewPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_FileNewPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileNewPreNotifyEventHandler.html"
---

# DSldWorksEvents_FileNewPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired before a new document is created using either the SOLIDWORKS API or the SOLIDWORKS application.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_FileNewPreNotifyEventHandler( _
   ByVal DocType As System.Integer, _
   ByVal TemplateName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_FileNewPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_FileNewPreNotifyEventHandler(
   System.int DocType,
   System.string TemplateName
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_FileNewPreNotifyEventHandler(
   System.int DocType,
   System.String^ TemplateName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocType`: Document type as defined by [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `TemplateName`: Template path name or file extension

## VBA Syntax

See [FileNewPreNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~FileNewPreNotify_EV.html).

## Remarks

Creating a new document using SOLIDWORKS includes:

- Clicking a document-type button on the New SOLIDWORKS Document dialog.
- Inserting a new component (part or assembly).

NOTE: This event is not raised when creating split parts.

You can cancel the creation of a new document by returning S_FALSE(1) from the event handler.

If developing a C++ application, use [swAppFileNewPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
