---
title: "FlyoutType Property (IFlyoutGroup)"
project: "SOLIDWORKS API Help"
interface: "IFlyoutGroup"
member: "FlyoutType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~FlyoutType.html"
---

# FlyoutType Property (IFlyoutGroup)

Gets or sets the type of this flyout.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlyoutType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFlyoutGroup
Dim value As System.Integer

instance.FlyoutType = value

value = instance.FlyoutType
```

### C#

```csharp
System.int FlyoutType {get; set;}
```

### C++/CLI

```cpp
property System.int FlyoutType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Flyout type as defined in [swCommandFlyoutStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCommandFlyoutStyle_e.html)

## VBA Syntax

See [FlyoutGroup::FlyoutType](ms-its:sldworksapivb6.chm::/sldworks~FlyoutGroup~FlyoutType.html).

## Examples

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

## See Also

[IFlyoutGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup.html)
[IFlyoutGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
