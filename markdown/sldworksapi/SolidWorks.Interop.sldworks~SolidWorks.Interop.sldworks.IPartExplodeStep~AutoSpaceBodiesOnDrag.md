---
title: "AutoSpaceBodiesOnDrag Property (IPartExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IPartExplodeStep"
member: "AutoSpaceBodiesOnDrag"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~AutoSpaceBodiesOnDrag.html"
---

# AutoSpaceBodiesOnDrag Property (IPartExplodeStep)

Gets or sets whether to automatically space a group of bodies equally along an axis as you drag them in this explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoSpaceBodiesOnDrag As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartExplodeStep
Dim value As System.Boolean

instance.AutoSpaceBodiesOnDrag = value

value = instance.AutoSpaceBodiesOnDrag
```

### C#

```csharp
System.bool AutoSpaceBodiesOnDrag {get; set;}
```

### C++/CLI

```cpp
property System.bool AutoSpaceBodiesOnDrag {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to automatically space components equally along an axis as you drag them, false to not

## VBA Syntax

See [PartExplodeStep::AutoSpaceBodiesOnDrag](ms-its:sldworksapivb6.chm::/sldworks~PartExplodeStep~AutoSpaceBodiesOnDrag.html).

## Examples

See the [IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.html) example.

## See Also

[IPartExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.html)
[IPartExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
