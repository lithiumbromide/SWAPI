---
title: "IGetCommandTabs Method (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "IGetCommandTabs"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetCommandTabs.html"
---

# IGetCommandTabs Method (ICommandManager)

Gets the CommandManager tabs for the specified document type.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCommandTabs( _
   ByVal DocumentType As System.Integer, _
   ByVal CommandTabCount As System.Integer _
) As CommandTab
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim DocumentType As System.Integer
Dim CommandTabCount As System.Integer
Dim value As CommandTab

value = instance.IGetCommandTabs(DocumentType, CommandTabCount)
```

### C#

```csharp
CommandTab IGetCommandTabs(
   System.int DocumentType,
   System.int CommandTabCount
)
```

### C++/CLI

```cpp
CommandTab^ IGetCommandTabs(
   System.int DocumentType,
   System.int CommandTabCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocumentType`: Document type as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `CommandTabCount`: Number of CommandManager tabs for DocumentType

### Return Value

- in-process, unmanaged C++: Pointer to an array of [CommandManager tabs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandTab.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ICommandManager::GetCommandTabCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~GetCommandTabCount.html) to get the size of the array for this method.

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[ICommandManager::AddCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddCommandTab.html)
[ICommandManager::CommandTabs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CommandTabs.html)
[ICommandManager::GetCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTab.html)
[ICommandManager::RemoveCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandTab.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
