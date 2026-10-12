---
title: "SmallIconList Property (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "SmallIconList"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SmallIconList.html"
---

# SmallIconList Property (ICommandGroup)

Obsolete. Superseded by [ICommandGroup::IconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~IconList.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property SmallIconList As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim value As System.String

instance.SmallIconList = value

value = instance.SmallIconList
```

### C#

```csharp
System.string SmallIconList {get; set;}
```

### C++/CLI

```cpp
property System.String^ SmallIconList {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path for the bitmap or PNG file containing all of the small images of the buttons and separators for this CommandGroup

## VBA Syntax

See [CommandGroup::SmallIconList](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~SmallIconList.html).

## Examples

[Create Submenus in the CommandManager (C#)](Create_Submenus_in_the_CommandManager_Example_CSharp.htm)

## Remarks

The bitmap or PNG file should contain all of the images for all of the small buttons and separators for this CommandGroup, in a single bitmap for both parent and child toolbars. Each image of each button must be 16x16. The images should use a 256-color palette.

You can only set this property for the top-level CommandGroup.

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)
[ICommandGroup::AddCommandItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddCommandItem2.html)
[ICommandGroup::LargeIconList Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~LargeIconList.html)
[ICommandGroup::LargeMainIcon Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~LargeMainIcon.html)
[ICommandGroup::SmallMainIcon Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SmallMainIcon.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
