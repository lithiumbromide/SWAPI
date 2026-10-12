---
title: "ButtonCount Property (IFlyoutGroup)"
project: "SOLIDWORKS API Help"
interface: "IFlyoutGroup"
member: "ButtonCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~ButtonCount.html"
---

# ButtonCount Property (IFlyoutGroup)

Gets the number of buttons in this flyout.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ButtonCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFlyoutGroup
Dim value As System.Integer

value = instance.ButtonCount
```

### C#

```csharp
System.int ButtonCount {get;}
```

### C++/CLI

```cpp
property System.int ButtonCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of buttons in the flyout

## VBA Syntax

See [FlyoutGroup::ButtonCount](ms-its:sldworksapivb6.chm::/sldworks~FlyoutGroup~ButtonCount.html).

## Examples

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

## See Also

[IFlyoutGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup.html)
[IFlyoutGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
