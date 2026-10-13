---
title: "GetLastToolbarID Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetLastToolbarID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLastToolbarID.html"
---

# GetLastToolbarID Method (ISldWorks)

Gets the ID of the last toolbar added to the [CommandManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLastToolbarID() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Integer

value = instance.GetLastToolbarID()
```

### C#

```csharp
System.int GetLastToolbarID()
```

### C++/CLI

```cpp
System.int GetLastToolbarID();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

ID of the last toolbar added to the CommandManager

## VBA Syntax

See [SldWorks::GetLastToolbarID](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetLastToolbarID.html).

## Remarks

See [CommandManager and CommandGroups](sldworksAPIProgGuide.chm::/OVERVIEW/CommandManager_and_CommandGroups.htm) to learn how to create a CommandManager and add and remove CommandGroups.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetCommandID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCommandID.html)
[ISldWorks::GetCommandManager Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCommandManager.html)
[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
