---
title: "DSldWorksEvents_FileNewNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_FileNewNotify2EventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileNewNotify2EventHandler.html"
---

# DSldWorksEvents_FileNewNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when a new file is created.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_FileNewNotify2EventHandler( _
   ByVal NewDoc As System.Object, _
   ByVal DocType As System.Integer, _
   ByVal TemplateName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_FileNewNotify2EventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_FileNewNotify2EventHandler(
   System.object NewDoc,
   System.int DocType,
   System.string TemplateName
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_FileNewNotify2EventHandler(
   System.Object^ NewDoc,
   System.int DocType,
   System.String^ TemplateName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewDoc`: New document
- `DocType`: Type of document as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `TemplateName`: Template name of the new document

## VBA Syntax

See [FileNewNotify2 Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~FileNewNotify2_EV.html).

## Examples

[Create CommandManager Tab and Tab Boxes (VB.NET)](Create_CommandManager_Tab_and_Tab_Boxes_Example_VB.NET.htm)

## Remarks

If your add-in wants to use the Dispatch pointer to the new document, then your add-in must increment the reference count using AddRef. When your add-in is done with the new document, it must decrement the reference count using Release.

If developing a C++ application, use [swAppFileNewNotify2](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SoildWorks 2001Plus FCS, Revision Number 10.0
