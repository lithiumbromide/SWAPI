---
title: "DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler.html"
---

# DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program when the display title changes for an item in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler( _
   ByVal oldName As System.String, _
   ByVal NewName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler(
   System.string oldName,
   System.string NewName
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler(
   System.String^ oldName,
   System.String^ NewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `oldName`: Previous display title
- `NewName`: New display title

## VBA Syntax

See [RenameDisplayTitleNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~RenameDisplayTitleNotify_EV.html).

## Remarks

Change the display title by using [IModelDocExtension::DisplayTitle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayTitle.html).

If developing a C++ application, use [swDrawingRenamedDisplayTitleNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2020 SP4, Revision Number 28.4
