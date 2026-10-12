---
title: "DAssemblyDocEvents_CommandManagerTabActivatedPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_CommandManagerTabActivatedPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_CommandManagerTabActivatedPreNotifyEventHandler.html"
---

# DAssemblyDocEvents_CommandManagerTabActivatedPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies you that a SOLIDWORKS CommandManager tab is about to be activated.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_CommandManagerTabActivatedPreNotifyEventHandler( _
   ByVal CommandTabIndex As System.Integer, _
   ByVal CommandTabName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_CommandManagerTabActivatedPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_CommandManagerTabActivatedPreNotifyEventHandler(
   System.int CommandTabIndex,
   System.string CommandTabName
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_CommandManagerTabActivatedPreNotifyEventHandler(
   System.int CommandTabIndex,
   System.String^ CommandTabName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandTabIndex`: Index of the tab that is about to be activated
- `CommandTabName`: Name of the tab

## VBA Syntax

See [CommandManagerTabActivatedPreNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~CommandManagerTabActivatedPreNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyCommandManagerTabActivatedPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
