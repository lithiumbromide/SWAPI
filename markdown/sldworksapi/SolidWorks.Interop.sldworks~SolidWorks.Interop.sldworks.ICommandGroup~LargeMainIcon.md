---
title: "LargeMainIcon Property (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "LargeMainIcon"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~LargeMainIcon.html"
---

# LargeMainIcon Property (ICommandGroup)

Obsolete. Superseded by [ICommandGroup::MainIconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~MainIconList.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property LargeMainIcon As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim value As System.String

instance.LargeMainIcon = value

value = instance.LargeMainIcon
```

### C#

```csharp
System.string LargeMainIcon {get; set;}
```

### C++/CLI

```cpp
property System.String^ LargeMainIcon {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path of the large bitmap or PNG for this CommandGroup

## VBA Syntax

See [CommandGroup::LargeMainIcon](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~LargeMainIcon.html).

## Examples

[Create Submenus in the CommandManager (C#)](Create_Submenus_in_the_CommandManager_Example_CSharp.htm)

## Remarks

The large bitmap or PNG must be 24x24 and use a 256-color palette.

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)
[ICommandGroup::AddCommandItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddCommandItem2.html)
[ICommandGroup::LargeIconList Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~LargeIconList.html)
[ICommandGroup::SmallIconList Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SmallIconList.html)
[ICommandGroup::SmallMainIcon Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SmallMainIcon.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
