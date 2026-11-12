---
title: "RemoveCommandItem Method (IFlyoutGroup)"
project: "SOLIDWORKS API Help"
interface: "IFlyoutGroup"
member: "RemoveCommandItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~RemoveCommandItem.html"
---

# RemoveCommandItem Method (IFlyoutGroup)

Removes a command item at the specified position.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveCommandItem( _
   ByVal Position As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFlyoutGroup
Dim Position As System.Integer
Dim value As System.Boolean

value = instance.RemoveCommandItem(Position)
```

### C#

```csharp
System.bool RemoveCommandItem(
   System.int Position
)
```

### C++/CLI

```cpp
System.bool RemoveCommandItem(
   System.int Position
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Position`: 0-based index of the item to remove from the flyout

### Return Value

True if successful, false if not

## VBA Syntax

See [FlyoutGroup::RemoveCommandItem](ms-its:sldworksapivb6.chm::/sldworks~FlyoutGroup~RemoveCommandItem.html).

## See Also

[IFlyoutGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup.html)
[IFlyoutGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup_members.html)
[IFlyoutGroup::RemoveAllCommandItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~RemoveAllCommandItems.html)
[IFlyoutGroup::ReplaceCommandItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~ReplaceCommandItem.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
