---
title: "DSldWorksEvents_DocumentLoadNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_DocumentLoadNotify2EventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_DocumentLoadNotify2EventHandler.html"
---

# DSldWorksEvents_DocumentLoadNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when a SOLIDWORKS document is loaded.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_DocumentLoadNotify2EventHandler( _
   ByVal docTitle As System.String, _
   ByVal docPath As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_DocumentLoadNotify2EventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_DocumentLoadNotify2EventHandler(
   System.string docTitle,
   System.string docPath
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_DocumentLoadNotify2EventHandler(
   System.String^ docTitle,
   System.String^ docPath
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `docTitle`: Document title
- `docPath`: Document path

## VBA Syntax

See [DocumentLoadNotify2 Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~DocumentLoadNotify2_EV.html).

## Examples

[Create CommandManager Tab and Tab Boxes (VB.NET)](Create_CommandManager_Tab_and_Tab_Boxes_Example_VB.NET.htm)

## Remarks

This event is fired for documents referenced by assemblies and drawings. Client code should expect multiple calls to this event handler when an assembly or drawing is loaded.

If developing a C++ application, use [swAppDocumentLoadNotify2](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
