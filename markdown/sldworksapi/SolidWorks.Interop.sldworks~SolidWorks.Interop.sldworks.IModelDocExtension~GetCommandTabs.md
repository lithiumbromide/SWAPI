---
title: "GetCommandTabs Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetCommandTabs"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCommandTabs.html"
---

# GetCommandTabs Method (IModelDocExtension)

Gets all of the SOLIDWORKS CommandManager tab names in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCommandTabs() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Object

value = instance.GetCommandTabs()
```

### C#

```csharp
System.object GetCommandTabs()
```

### C++/CLI

```cpp
System.Object^ GetCommandTabs();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of CommandManager tab names

## VBA Syntax

See [ModelDocExtension::GetCommandTabs](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetCommandTabs.html).

## Examples

[Activate SOLIDWORKS CommandManager Tab (VBA)](Activate_SOLIDWORKS_CommandManager_Tab_Example_VB.htm)
[Activate SOLIDWORKS CommandManager Tab (VB.NET)](Activate_SOLIDWORKS_CommandManager_Tab_Example_VBNET.htm)
[Activate SOLIDWORKS CommandManager Tab (C#)](Activate_SOLIDWORKS_CommandManager_Tab_Example_CSharp.htm)

## Remarks

To activate and query the add-in CommandManager tabs, call [ICommandManager::CommandTabs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~CommandTabs.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[ICommandManager::GetCommandTab Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTab.html)
[ICommandManager::IGetCommandTabs Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetCommandTabs.html)
[ICommandManager::GetCommandTabCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTabCount.html)
[IModelDocExtension::ActiveCommandTab Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActiveCommandTab.html)
[IModelDocExtension::ActiveCommandTabIndex Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActiveCommandTabIndex.html)
[IModelDocExtension::CommandTabVisible Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CommandTabVisible.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
