---
title: "RunCommand Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RunCommand"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunCommand.html"
---

# RunCommand Method (ISldWorks)

Runs the specified SOLIDWORKS command.

## Syntax

### Visual Basic (Declaration)

```vb
Function RunCommand( _
   ByVal CommandID As System.Integer, _
   ByVal NewTitle As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim CommandID As System.Integer
Dim NewTitle As System.String
Dim value As System.Boolean

value = instance.RunCommand(CommandID, NewTitle)
```

### C#

```csharp
System.bool RunCommand(
   System.int CommandID,
   System.string NewTitle
)
```

### C++/CLI

```cpp
System.bool RunCommand(
   System.int CommandID,
   System.String^ NewTitle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandID`: SOLIDWORKS command as defined in [swCommands_e](ms-its:swcommands.chm::/SOLIDWORKS.Interop.swcommands.html) (see Remarks)
- `NewTitle`: Your title for the SOLIDWORKS PropertyManager page, if invoked by this command

### Return Value

True if the SOLIDWORKS command ran, false if not

## VBA Syntax

See [SldWorks::RunCommand](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~RunCommand.html).

## Examples

[Fire Events When PropertyManager Page Opened and Canceled (VBA)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VB.htm)
[Record Macros (C#)](Record_Macros_Example_CSharp.htm)
[Record Macros (VB.NET)](Record_Macros_Example_VBNET.htm)
[Record Macros (VBA)](Record_Macros_Example_VB.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[IModelDocExtension::RunCommand Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RunCommand.html)
[ISldWorks::IsCommandEnabled Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsCommandEnabled.html)
[ISldWorks::GetRunningCommandInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetRunningCommandInfo.html)
[DSldWorksEvents_CommandCloseNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_CommandCloseNotifyEventHandler.html)
[DSldWorksEvents_CommandOpenPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_CommandOpenPreNotifyEventHandler.html)
[ISldWorks::RecordLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLine.html)
[ISldWorks::RecordLineCSharp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLineCSharp.html)
[ISldWorks::RecordLineVBnet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLineVBnet.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
