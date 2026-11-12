---
title: "CustomNames Property (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "CustomNames"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~CustomNames.html"
---

# CustomNames Property (ICommandGroup)

Gets or sets the custom names in the CommandGroup.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomNames As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim value As System.String

instance.CustomNames = value

value = instance.CustomNames
```

### C#

```csharp
System.string CustomNames {get; set;}
```

### C++/CLI

```cpp
property System.String^ CustomNames {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

String containing the custom names in the CommandGroup (see **Remarks**)

## VBA Syntax

See [CommandGroup::CustomNames](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~CustomNames.html).

## Remarks

Format CustomNames as a semicolon-separated list of the names of the custom feature types.

This method is applicable only if[ICommandGruop::SelectType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~SelectType.html) is a custom feature type, like swSelATTRIBUTES. For example, if you want a context-sensitive, pop-up menu to appear for an attribute when the user right-clicks the attribute in the FeatureManager design tree, then:

1. Create the attribute (see [IAttributeDef::CreateInstance5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef~CreateInstance5.html))
2. Set the name of the attribute in [ICommandGroup::SelectType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~SelectType.html).
3. Set the name of the attribute definition in ICommandGroup::CustomNames.

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)
[ICommandManager::AddContextMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddContextMenu.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
