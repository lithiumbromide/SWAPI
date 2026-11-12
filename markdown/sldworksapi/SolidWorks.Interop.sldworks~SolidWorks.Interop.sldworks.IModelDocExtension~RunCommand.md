---
title: "RunCommand Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "RunCommand"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RunCommand.html"
---

# RunCommand Method (IModelDocExtension)

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
Dim instance As IModelDocExtension
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

- `CommandID`: SOLIDWORKS command as defined in [swCommands_e](ms-its:swcommands.chm::/SOLIDWORKS.Interop.swcommands~SOLIDWORKS.Interop.swcommands.swCommands_e.html)
- `NewTitle`: Your title for the SOLIDWORKS PropertyManager page, if invoked by this command

### Return Value

True if the SOLIDWORKS command ran, false if not

## VBA Syntax

See [ModelDocExtension::RunCommand](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~RunCommand.html).

## Examples

[Run SOLIDWORKS Commands (VBA)](Run_SOLIDWORKS_Commands_Example_VB.htm)
[Fire Events When PropertyManager Page Opened and Canceled (C#)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_CSharp.htm)
[Fire Events When PropertyManager Page Opened and Canceled (VB.NET)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VBNET.htm)
[Fire Events When PropertyManager Page Opened and Canceled (VBA)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[ISldWorks::RunCommand Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunCommand.html)
[ISldWorks::IsCommandEnabled Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsCommandEnabled.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
