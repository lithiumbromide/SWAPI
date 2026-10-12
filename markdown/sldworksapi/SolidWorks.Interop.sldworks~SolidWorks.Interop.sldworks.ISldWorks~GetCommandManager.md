---
title: "GetCommandManager Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetCommandManager"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCommandManager.html"
---

# GetCommandManager Method (ISldWorks)

Gets the CommandManager for the specified add-in.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCommandManager( _
   ByVal Cookie As System.Integer _
) As CommandManager
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim value As CommandManager

value = instance.GetCommandManager(Cookie)
```

### C#

```csharp
CommandManager GetCommandManager(
   System.int Cookie
)
```

### C++/CLI

```cpp
CommandManager^ GetCommandManager(
   System.int Cookie
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Cookie`: Cookie specified in [ISwAddin::ConnectToSW](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.html)

### Return Value

[CommandManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager.html)

## VBA Syntax

See [SldWorks::GetCommandManager](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetCommandManager.html).

## Examples

[Create Submenus in the CommandManager (C#)](Create_Submenus_in_the_CommandManager_Example_CSharp.htm)

## Remarks

See [CommandManager and CommandGroups](sldworksAPIProgGuide.chm::/OVERVIEW/CommandManager_and_CommandGroups.htm) for details.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
