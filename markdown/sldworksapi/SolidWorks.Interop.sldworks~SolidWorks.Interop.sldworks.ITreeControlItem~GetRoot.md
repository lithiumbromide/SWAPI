---
title: "GetRoot Method (ITreeControlItem)"
project: "SOLIDWORKS API Help"
interface: "ITreeControlItem"
member: "GetRoot"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~GetRoot.html"
---

# GetRoot Method (ITreeControlItem)

Gets the root item of the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRoot() As TreeControlItem
```

### Visual Basic (Usage)

```vb
Dim instance As ITreeControlItem
Dim value As TreeControlItem

value = instance.GetRoot()
```

### C#

```csharp
TreeControlItem GetRoot()
```

### C++/CLI

```cpp
TreeControlItem^ GetRoot();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Root item of the FeatureManager design tree](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITreeControlItem.html)

## VBA Syntax

See [TreeControlItem::GetRoot](ms-its:sldworksapivb6.chm::/sldworks~TreeControlItem~GetRoot.html).

## Remarks

Use [ITreeControlItem::IsRoot](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITreeControlItem~IsRoot.html) to get whether an item is the root item of the FeatureManager design tree.

## See Also

[ITreeControlItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.html)
[ITreeControlItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem_members.html)

## Availability

SOLIDWORKS 2008 SP2, Revision Number 16.2
