---
title: "DSldWorksEvents_CommandOpenPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_CommandOpenPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_CommandOpenPreNotifyEventHandler.html"
---

# DSldWorksEvents_CommandOpenPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired before a command, including a PropertyManager page, executes or opens.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_CommandOpenPreNotifyEventHandler( _
   ByVal Command As System.Integer, _
   ByVal UserCommand As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_CommandOpenPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_CommandOpenPreNotifyEventHandler(
   System.int Command,
   System.int UserCommand
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_CommandOpenPreNotifyEventHandler(
   System.int Command,
   System.int UserCommand
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Command`: SOLIDWORKS command ID as defined in [swCommands_e](ms-its:swcommands.chm::/SolidWorks.Interop.swcommands~SolidWorks.Interop.swcommands.swCommands_e.html)
- `UserCommand`: Third-party application's command item's ID (see **Remarks**)

### Return Value

0 to execute the command or open a PropertyManager page, 1 to not

## VBA Syntax

See [CommandOpenPreNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~CommandOpenPreNotify_EV.html).

## Examples

[Fire Events When PropertyManager Page Opened and Canceled (VBA)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VB.htm)
[Fire Events When PropertyManager Page Opened and Canceled (VB.NET)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VBNET.htm)
[Fire Events When PropertyManager Page Opened and Canceled (C#)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_CSharp.htm)

## Remarks

If developing a C++ application, use [swAppCommandOpenPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

The UserCommand argument is the ID assigned to your application's command item when it was added to a CommandGroup. For example:

```
cmdIndex0 = cmdGroup.AddCommandItem("CreateCube", -1, "Create a cube", "Create cube", 0, "CreateCube", "", 0);
```

```
cmdIds[0] = cmdGroup.get_CommandID(cmdIndex0);
```

Selecting the **Create cube** command in the user interface causes the CommandOpenPreNotify event to fire. The Command parameter is swCommands_e.swCommands_User_Toolbar_Min, and the userCommand parameter is cmdIDs[0].

Call [CommandCloseNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_CommandCloseNotifyEventHandler.html) to fire an event when the PropertyManager page is okay'd or canceled.

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
