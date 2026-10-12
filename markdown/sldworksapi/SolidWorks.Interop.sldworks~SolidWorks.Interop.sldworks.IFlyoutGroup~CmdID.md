---
title: "CmdID Property (IFlyoutGroup)"
project: "SOLIDWORKS API Help"
interface: "IFlyoutGroup"
member: "CmdID"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~CmdID.html"
---

# CmdID Property (IFlyoutGroup)

Gets the command ID of this flyout.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CmdID As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFlyoutGroup
Dim value As System.Integer

value = instance.CmdID
```

### C#

```csharp
System.int CmdID {get;}
```

### C++/CLI

```cpp
property System.int CmdID {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Command ID

## VBA Syntax

See [FlyoutGroup::CmdID](ms-its:sldworksapivb6.chm::/sldworks~FlyoutGroup~CmdID.html).

## Examples

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

## See Also

[IFlyoutGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup.html)
[IFlyoutGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
