---
title: "GetPrevious Method (ITreeControlItem)"
project: "SOLIDWORKS API Help"
interface: "ITreeControlItem"
member: "GetPrevious"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~GetPrevious.html"
---

# GetPrevious Method (ITreeControlItem)

Gets the previous sibling of this item in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPrevious() As TreeControlItem
```

### Visual Basic (Usage)

```vb
Dim instance As ITreeControlItem
Dim value As TreeControlItem

value = instance.GetPrevious()
```

### C#

```csharp
TreeControlItem GetPrevious()
```

### C++/CLI

```cpp
TreeControlItem^ GetPrevious();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Previous sibling of this item in the FeatureManager design tree](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITreeControlItem~GetPrevious.html)

## VBA Syntax

See [TreeControlItem::GetPrevious](ms-its:sldworksapivb6.chm::/sldworks~TreeControlItem~GetPrevious.html).

## Remarks

Use [ITreeControlItem::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITreeControlItem~GetNext.html) to get the next sibling of this item in the FeatureManager design tree.

## See Also

[ITreeControlItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.html)
[ITreeControlItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem_members.html)

## Availability

SOLIDWORKS 2008 SP2, Revision Number 16.2
