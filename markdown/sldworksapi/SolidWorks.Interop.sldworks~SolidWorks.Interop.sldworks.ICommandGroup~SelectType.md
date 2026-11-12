---
title: "SelectType Property (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "SelectType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SelectType.html"
---

# SelectType Property (ICommandGroup)

This property:

- gets the type of object selected on the context sensitive, pop-up menu.
- sets the type of object that the user must select to show the context sensitive, pop-up menu.

## Syntax

### Visual Basic (Declaration)

```vb
Property SelectType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim value As System.Integer

instance.SelectType = value

value = instance.SelectType
```

### C#

```csharp
System.int SelectType {get; set;}
```

### C++/CLI

```cpp
property System.int SelectType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of object as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [CommandGroup::SelectType](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~SelectType.html).

## Remarks

This property only applies to CommandGroups created using [ICommandManager::AddContextMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~AddContextMenu.html).

If setting SelectType to a custom feature type such as an attribute (swSelATTRIBUTES),
then you must use [ICommandGroup::CustomNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~CustomNames.html) to set the name of the attribute definition.

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
