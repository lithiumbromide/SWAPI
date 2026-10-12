---
title: "DPartDocEvents_RenameDisplayTitleNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_RenameDisplayTitleNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RenameDisplayTitleNotifyEventHandler.html"
---

# DPartDocEvents_RenameDisplayTitleNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the display title is changed for an item in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_RenameDisplayTitleNotifyEventHandler( _
   ByVal oldName As System.String, _
   ByVal NewName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_RenameDisplayTitleNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_RenameDisplayTitleNotifyEventHandler(
   System.string oldName,
   System.string NewName
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_RenameDisplayTitleNotifyEventHandler(
   System.String^ oldName,
   System.String^ NewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `oldName`: Previous display title
- `NewName`: New display title

## VBA Syntax

See [RenameDisplayTitleNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~RenameDisplayTitleNotify_EV.html).

## Remarks

Change the display title by using [IModelDocExtension::DisplayTitle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayTitle.html).

If developing a C++ application, use [swPartRenamedDisplayTitleNotify](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2020 SP4, Revision Number 28.4
