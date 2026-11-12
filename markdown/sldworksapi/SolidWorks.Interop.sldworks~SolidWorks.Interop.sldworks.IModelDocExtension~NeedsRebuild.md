---
title: "NeedsRebuild Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "NeedsRebuild"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild.html"
---

# NeedsRebuild Property (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::NeedsRebuild2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property NeedsRebuild As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

value = instance.NeedsRebuild
```

### C#

```csharp
System.bool NeedsRebuild {get;}
```

### C++/CLI

```cpp
property System.bool NeedsRebuild {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if document needs to be rebuilt, false if not

## VBA Syntax

See [ModelDocExtension::NeedsRebuild](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~NeedsRebuild.html).

## Remarks

Because this now obsoleted property does not recognize frozen features, use [IModelDocExtension::NeedsRebuild2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html), which does.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2004 SP3, Revision Number 12.3
