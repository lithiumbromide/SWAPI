---
title: "IGetCommandTabBoxes Method (ICommandTab)"
project: "SOLIDWORKS API Help"
interface: "ICommandTab"
member: "IGetCommandTabBoxes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~IGetCommandTabBoxes.html"
---

# IGetCommandTabBoxes Method (ICommandTab)

Gets the CommandManager tab boxes on this CommandManager tab.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCommandTabBoxes( _
   ByVal TabBoxCount As System.Integer _
) As CommandTabBox
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandTab
Dim TabBoxCount As System.Integer
Dim value As CommandTabBox

value = instance.IGetCommandTabBoxes(TabBoxCount)
```

### C#

```csharp
CommandTabBox IGetCommandTabBoxes(
   System.int TabBoxCount
)
```

### C++/CLI

```cpp
CommandTabBox^ IGetCommandTabBoxes(
   System.int TabBoxCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TabBoxCount`: Number of CommandManager tab boxes on this CommandManager tab

### Return Value

- in-process, unmanaged C++: Pointer to an array of [CommandManager tab boxes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandTabBox.html) on this CommandManager tab

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ICommandTab::GetCommandTabBoxCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandTab~GetCommandTabBoxCount.html) before calling this method to get the value of TabBoxCount.

## See Also

[ICommandTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab.html)
[ICommandTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab_members.html)
[ICommandTab::AddCommandTabBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~AddCommandTabBox.html)
[ICommandTab::CommandTabBoxes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~CommandTabBoxes.html)
[ICommandTab::RemoveCommandTabBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~RemoveCommandTabBox.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
