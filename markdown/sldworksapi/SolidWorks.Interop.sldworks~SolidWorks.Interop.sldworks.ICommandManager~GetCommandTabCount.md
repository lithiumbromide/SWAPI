---
title: "GetCommandTabCount Method (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "GetCommandTabCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTabCount.html"
---

# GetCommandTabCount Method (ICommandManager)

Gets the number of tabs on the CommandManager for the specified document type.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCommandTabCount( _
   ByVal DocumentType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim DocumentType As System.Integer
Dim value As System.Integer

value = instance.GetCommandTabCount(DocumentType)
```

### C#

```csharp
System.int GetCommandTabCount(
   System.int DocumentType
)
```

### C++/CLI

```cpp
System.int GetCommandTabCount(
   System.int DocumentType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocumentType`: Document type as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

### Return Value

Number of tabs on the CommandManager

## VBA Syntax

See [CommandManager::GetCommandTabCount](ms-its:sldworksapivb6.chm::/sldworks~CommandManager~GetCommandTabCount.html).

## Remarks

Call this method before [ICommandManager::IGetCommandTabs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~IGetCommandTabs.html) to get the size of the array for that method.

All CommandManager tabs are returned. Some CommandManager tabs may not be active or visible.

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[ICommandManager::AddCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddCommandTab.html)
[ICommandManager::CommandTabs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CommandTabs.html)
[ICommandManager::GetCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTab.html)
[ICommandManager::RemoveCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandTab.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
