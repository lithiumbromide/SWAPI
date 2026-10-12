---
title: "GetParent Method (ITreeControlItem)"
project: "SOLIDWORKS API Help"
interface: "ITreeControlItem"
member: "GetParent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~GetParent.html"
---

# GetParent Method (ITreeControlItem)

Gets the parent of this item in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetParent() As TreeControlItem
```

### Visual Basic (Usage)

```vb
Dim instance As ITreeControlItem
Dim value As TreeControlItem

value = instance.GetParent()
```

### C#

```csharp
TreeControlItem GetParent()
```

### C++/CLI

```cpp
TreeControlItem^ GetParent();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Parent of this item in the FeatureManager design tree](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITreeControlItem.html)

## VBA Syntax

See [TreeControlItem::GetParent](ms-its:sldworksapivb6.chm::/sldworks~TreeControlItem~GetParent.html).

## See Also

[ITreeControlItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.html)
[ITreeControlItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem_members.html)

## Availability

SOLIDWORKS 2008 SP2, Revision Number 16.2
