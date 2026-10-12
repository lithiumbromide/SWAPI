---
title: "DSldWorksEvents_CommandCloseNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_CommandCloseNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_CommandCloseNotifyEventHandler.html"
---

# DSldWorksEvents_CommandCloseNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a command, including a PropertyManager page, is okay'd or canceled by a user.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_CommandCloseNotifyEventHandler( _
   ByVal Command As System.Integer, _
   ByVal reason As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_CommandCloseNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_CommandCloseNotifyEventHandler(
   System.int Command,
   System.int reason
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_CommandCloseNotifyEventHandler(
   System.int Command,
   System.int reason
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Command`: Command as defined in [swCommands_e](ms-its:swcommands.chm::/SolidWorks.Interop.swcommands~SolidWorks.Interop.swcommands.swCommands_e.html)
- `reason`: Reason as defined by:

  - swCommands_e.swCommands_PmOK or swCommands_e.swCommands_PmCancel (for PropertyManager page closures)

  - swCommands_e.swCommands_Exit_Measure (for Measure dialog closures)

  - swCommands_Comp_Isolate_Exit (for Isolate dialog closures)

## VBA Syntax

See [CommandCloseNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~CommandCloseNotify_EV.html).

## Examples

[Fire Events When PropertyManager Page Opened and Canceled (VBA)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VB.htm)
[Fire Events When PropertyManager Page Opened and Canceled (VB.NET)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VBNET.htm)
[Fire Events When PropertyManager Page Opened and Canceled (C#)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_CSharp.htm)

## Remarks

If developing a C++ application, use [swAppCommandCloseNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

You can combine:

- the IAssemblyDoc [FeatureEditPreNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_FeatureEditPreNotifyEventHandler.html) event or the IPartDoc [FeatureEditPreNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_EquationEditorPreNotifyEventHandler.html) event with the ISldWorks CommandCloseNotify event and swCommands_e.swCommands_EditFeature.
- the IAssemblyDoc [FeatureSketchEditPreNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_FeatureSketchEditPreNotifyEventHandler.html) event or the IPartDoc [FeatureSketchEditPreNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FeatureSketchEditPreNotifyEventHandler.html) event with the ISldWorks CommandCloseNotify event and swCommands_e.swCommands_Sketch.

Call [CommandOpenPreNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_CommandOpenPreNotifyEventHandler.html) to fire an event before a command executes or a PropertyManager page opens.

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
