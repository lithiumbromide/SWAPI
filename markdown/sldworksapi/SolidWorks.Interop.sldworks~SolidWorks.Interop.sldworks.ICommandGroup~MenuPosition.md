---
title: "MenuPosition Property (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "MenuPosition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~MenuPosition.html"
---

# MenuPosition Property (ICommandGroup)

Gets or sets the position of the CommandGroup for the specified document templates.

## Syntax

### Visual Basic (Declaration)

```vb
Property MenuPosition( _
   ByVal Context As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim Context As System.Integer
Dim value As System.Integer

instance.MenuPosition(Context) = value

value = instance.MenuPosition(Context)
```

### C#

```csharp
System.int MenuPosition(
   System.int Context
) {get; set;}
```

### C++/CLI

```cpp
property System.int MenuPosition {
   System.int get(System.int Context);
   void set (System.int Context, System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Context`: Context as defined in [swDocTemplateTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocTemplateTypes_e.html)

### Property Value

Position of the CommandGroup in the CommandManager

**NOTE:** Specify 0 to add the CommandGroup to the beginning of the CommandMananger, or specify -1 to add it to the end of the CommandManager.

## VBA Syntax

See [CommandGroup::MenuPosition](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~MenuPosition.html).

## Remarks

If setting the position of the CommandGroup using this property, you must use it before using [ICommandGroup::Activate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~Activate.html). If you use this property after using ICommandGroup::Activate, then this property has no effect.

If you do not use this property to set the position of the ICommandGroup, then the position specified in [ICommandManager::CreateCommandGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~CreateCommandGroup.html) is used.

Calling this property to get the position of the CommandGroup returns the position of the CommandGroup set by either this property or ICommandManager::CreateCommandGroup.

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)
[ICommandGroup::HasMenu Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasMenu.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
