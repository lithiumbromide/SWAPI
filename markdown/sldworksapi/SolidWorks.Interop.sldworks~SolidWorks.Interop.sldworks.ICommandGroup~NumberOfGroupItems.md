---
title: "NumberOfGroupItems Property (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "NumberOfGroupItems"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~NumberOfGroupItems.html"
---

# NumberOfGroupItems Property (ICommandGroup)

Gets the number of items in the CommandGroup.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property NumberOfGroupItems As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim value As System.Integer

value = instance.NumberOfGroupItems
```

### C#

```csharp
System.int NumberOfGroupItems {get;}
```

### C++/CLI

```cpp
property System.int NumberOfGroupItems {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of items in the CommandGroup

## VBA Syntax

See [CommandGroup::NumberOfGroupItems](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~NumberOfGroupItems.html).

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)
[ICommandGroup::AddCommandItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddCommandItem2.html)
[ICommandGroup::CommandID Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~CommandID.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
