---
title: "AddCommandTab Method (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "AddCommandTab"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddCommandTab.html"
---

# AddCommandTab Method (ICommandManager)

Adds a tab to the CommandManager for the specified document type.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCommandTab( _
   ByVal DocumentType As System.Integer, _
   ByVal TabName As System.String _
) As CommandTab
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim DocumentType As System.Integer
Dim TabName As System.String
Dim value As CommandTab

value = instance.AddCommandTab(DocumentType, TabName)
```

### C#

```csharp
CommandTab AddCommandTab(
   System.int DocumentType,
   System.string TabName
)
```

### C++/CLI

```cpp
CommandTab^ AddCommandTab(
   System.int DocumentType,
   System.String^ TabName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocumentType`: Document type as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `TabName`: Name of CommandManager tab (see Remarks)

### Return Value

[CommandManager tab](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandTab.html)

## VBA Syntax

See [CommandManager::AddCommandTab](ms-its:sldworksapivb6.chm::/sldworks~CommandManager~AddCommandTab.html).

## Examples

[Create CommandManager Tab and Tab Boxes (VB.NET)](Create_CommandManager_Tab_and_Tab_Boxes_Example_VB.NET.htm)

## Remarks

The CommandManager tab is always created in the last position on the CommandManager. If another CommandManager tab exists with the same name, then another CommandManager tab is still created because CommandManager tab names are not unique.

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[ICommandManager::CommandTabs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CommandTabs.html)
[ICommandManager::GetCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTab.html)
[ICommandManager::GetCommandTabCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTabCount.html)
[ICommandManager::IGetCommandTabs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetCommandTabs.html)
[ICommandManager::RemoveCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandTab.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
