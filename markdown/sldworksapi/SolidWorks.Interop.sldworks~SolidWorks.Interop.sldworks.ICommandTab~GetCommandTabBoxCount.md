---
title: "GetCommandTabBoxCount Method (ICommandTab)"
project: "SOLIDWORKS API Help"
interface: "ICommandTab"
member: "GetCommandTabBoxCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~GetCommandTabBoxCount.html"
---

# GetCommandTabBoxCount Method (ICommandTab)

Gets the number of tab boxes on this CommandManager tab.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCommandTabBoxCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandTab
Dim value As System.Integer

value = instance.GetCommandTabBoxCount()
```

### C#

```csharp
System.int GetCommandTabBoxCount()
```

### C++/CLI

```cpp
System.int GetCommandTabBoxCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of CommandManager tab boxes on this CommandManager tab

## VBA Syntax

See [CommandTab::GetCommandTabBoxCount](ms-its:sldworksapivb6.chm::/sldworks~CommandTab~GetCommandTabBoxCount.html).

## Remarks

Call this method before calling [ICommandTab::IGetCommandTabBoxes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandTab~IGetCommandTabBoxes.html) to get the size of the array for that method.

## See Also

[ICommandTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab.html)
[ICommandTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab_members.html)
[ICommandTab::AddCommandTabBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~AddCommandTabBox.html)
[ICommandTab::CommandTabBoxes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~CommandTabBoxes.html)
[ICommandTab::RemoveCommandTabBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~RemoveCommandTabBox.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
