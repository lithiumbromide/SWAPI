---
title: "IsRoot Property (ITreeControlItem)"
project: "SOLIDWORKS API Help"
interface: "ITreeControlItem"
member: "IsRoot"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~IsRoot.html"
---

# IsRoot Property (ITreeControlItem)

Gets whether this item is the root item of the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsRoot As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITreeControlItem
Dim value As System.Boolean

value = instance.IsRoot
```

### C#

```csharp
System.bool IsRoot {get;}
```

### C++/CLI

```cpp
property System.bool IsRoot {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this item is the root item of the FeatureManager design tree, false if not

## VBA Syntax

See [TreeControlItem::IsRoot](ms-its:sldworksapivb6.chm::/sldworks~TreeControlItem~IsRoot.html).

## Remarks

Use [ITreeControlItem::GetRoot](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITreeControlItem~GetRoot.html) to get the root item of the FeatureManager design tree.

## See Also

[ITreeControlItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.html)
[ITreeControlItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem_members.html)

## Availability

SOLIDWORKS 2008 SP2, Revision Number 16.2
