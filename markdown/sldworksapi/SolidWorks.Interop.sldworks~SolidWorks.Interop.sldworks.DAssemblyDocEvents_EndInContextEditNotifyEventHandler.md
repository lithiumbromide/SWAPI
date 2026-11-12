---
title: "DAssemblyDocEvents_EndInContextEditNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_EndInContextEditNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_EndInContextEditNotifyEventHandler.html"
---

# DAssemblyDocEvents_EndInContextEditNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the application that the user is done editing an assembly component within the context of the assembly (inside the assembly document window).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_EndInContextEditNotifyEventHandler( _
   ByVal docBeingEdited As System.Object, _
   ByVal DocType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_EndInContextEditNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_EndInContextEditNotifyEventHandler(
   System.object docBeingEdited,
   System.int DocType
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_EndInContextEditNotifyEventHandler(
   System.Object^ docBeingEdited,
   System.int DocType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `docBeingEdited`: File name of the component document being edited
- `DocType`: Type of component document as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

## VBA Syntax

See [EndInContextEditNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~EndInContextEditNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyEndInContextEditNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
