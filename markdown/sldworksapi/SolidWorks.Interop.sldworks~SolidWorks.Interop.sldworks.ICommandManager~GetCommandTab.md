---
title: "GetCommandTab Method (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "GetCommandTab"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTab.html"
---

# GetCommandTab Method (ICommandManager)

Gets the specified CommandManager tab for the specified document type.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCommandTab( _
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

value = instance.GetCommandTab(DocumentType, TabName)
```

### C#

```csharp
CommandTab GetCommandTab(
   System.int DocumentType,
   System.string TabName
)
```

### C++/CLI

```cpp
CommandTab^ GetCommandTab(
   System.int DocumentType,
   System.String^ TabName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocumentType`: Document type as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `TabName`: Name of CommandManager tab

### Return Value

[CommandManager tab](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandTab.html)

## VBA Syntax

See [CommandManager::GetCommandTab](ms-its:sldworksapivb6.chm::/sldworks~CommandManager~GetCommandTab.html).

## Examples

[Create CommandManager Tab and Tab Boxes (VB.NET)](Create_CommandManager_Tab_and_Tab_Boxes_Example_VB.NET.htm)

## Remarks

The names of CommandManager tabs are not unique. If multiple CommandManager tabs exists with the same name for the specified document type, then the first matching tab is returned. If no tabs match the specified name for the specified document type, then NULL is returned.

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[ICommandManager::AddCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddCommandTab.html)
[ICommandManager::CommandTabs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CommandTabs.html)
[ICommandManager::GetCommandTabCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTabCount.html)
[ICommandManager::IGetCommandTabs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetCommandTabs.html)
[ICommandManager::RemoveCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandTab.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
