---
title: "GetRunningCommandInfo Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetRunningCommandInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetRunningCommandInfo.html"
---

# GetRunningCommandInfo Method (ISldWorks)

Get a command's ID or PropertyManager page's command ID, title, and whether it is active in the user-interface.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetRunningCommandInfo( _
   ByRef CommandID As System.Integer, _
   ByRef PMTitle As System.String, _
   ByRef IsUiActive As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim CommandID As System.Integer
Dim PMTitle As System.String
Dim IsUiActive As System.Boolean

instance.GetRunningCommandInfo(CommandID, PMTitle, IsUiActive)
```

### C#

```csharp
void GetRunningCommandInfo(
   out System.int CommandID,
   out System.string PMTitle,
   out System.bool IsUiActive
)
```

### C++/CLI

```cpp
void GetRunningCommandInfo(
   [Out] System.int CommandID,
   [Out] System.String^ PMTitle,
   [Out] System.bool IsUiActive
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandID`: Command's ID or PropertyManager page's command ID as defined in [swCommands_e](ms-its:swcommands.chm::/SOLIDWORKS.Interop.swcommands~SOLIDWORKS.Interop.swcommands.swCommands_e.html)
- `PMTitle`: Title of PropertyManager page
- `IsUiActive`: True if command or PropertyManager page is active in the user-interface, false if not

## VBA Syntax

See [SldWorks::GetRunningCommandInfo](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetRunningCommandInfo.html).

## Examples

[Fire Events When PropertyManager Page Opened and Canceled (VBA)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VB.htm)
[Fire Events When PropertyManager Page Opened and Canceled (VB.NET)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VBNET.htm)
[Fire Events When PropertyManager Page Opened and Canceled (C#)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_CSharp.htm)

## Remarks

Before using this method, you must add a reference to the SOLIDWORKS commands type library or DLL to access the SOLIDWORKS commands.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::RunCommand Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunCommand.html)
[ISldWorks::IsCommandEnabled Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsCommandEnabled.html)
[DSldWorksEvents_CommandOpenPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_CommandOpenPreNotifyEventHandler.html)
[DSldWorksEvents_CommandCloseNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_CommandCloseNotifyEventHandler.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
