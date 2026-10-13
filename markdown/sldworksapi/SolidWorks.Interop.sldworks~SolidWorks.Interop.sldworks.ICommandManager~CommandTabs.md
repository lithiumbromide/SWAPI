---
title: "CommandTabs Method (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "CommandTabs"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CommandTabs.html"
---

# CommandTabs Method (ICommandManager)

Gets all of the add-in CommandManager tabs for the specified document type.

## Syntax

### Visual Basic (Declaration)

```vb
Function CommandTabs( _
   ByVal DocumentType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim DocumentType As System.Integer
Dim value As System.Object

value = instance.CommandTabs(DocumentType)
```

### C#

```csharp
System.object CommandTabs(
   System.int DocumentType
)
```

### C++/CLI

```cpp
System.Object^ CommandTabs(
   System.int DocumentType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocumentType`: Document type as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

### Return Value

Array of [CommandManager tabs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandTab.html)

## VBA Syntax

See [CommandManager::CommandTabs](ms-its:sldworksapivb6.chm::/sldworks~CommandManager~CommandTabs.html).

## Remarks

To activate and query native SOLIDWORKS CommandManager tabs, call [IModelDocExtension::GetCommandTabs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetCommandTabs.html).

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[ICommandManager::IGetCommandTabs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetCommandTabs.html)
[ICommandManager::GetCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTab.html)
[ICommandManager::AddCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddCommandTab.html)
[ICommandManager::RemoveCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandTab.html)
[ICommandManager::GetCommandTabCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTabCount.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
