---
title: "Name Property (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "Name"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~Name.html"
---

# Name Property (ICommandGroup)

Gets the name of the CommandGroup.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim value As System.String

value = instance.Name
```

### C#

```csharp
System.string Name {get;}
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the CommandGroup that corresponds to the name specified in [ICommandManager::AddContextMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~AddContextMenu.html),
and [ICommandManager::CreateCommandGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~CreateCommandGroup.html).

## VBA Syntax

See [CommandGroup::Name](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~Name.html).

## Remarks

If you used [ICommandManager::GetGroups](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~GetGroups.html) or [ICommandManager::IGetGroups](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~IGetGroups.html), then use this property to get the specific CommandGroup with which you want to work.

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
