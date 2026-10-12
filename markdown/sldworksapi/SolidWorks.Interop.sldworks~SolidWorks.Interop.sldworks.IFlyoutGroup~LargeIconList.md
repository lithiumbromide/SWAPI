---
title: "LargeIconList Property (IFlyoutGroup)"
project: "SOLIDWORKS API Help"
interface: "IFlyoutGroup"
member: "LargeIconList"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~LargeIconList.html"
---

# LargeIconList Property (IFlyoutGroup)

Obsolete. Superseded by [IFlyoutGroup::IconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~IconList.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property LargeIconList As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFlyoutGroup
Dim value As System.String

instance.LargeIconList = value

value = instance.LargeIconList
```

### C#

```csharp
System.string LargeIconList {get; set;}
```

### C++/CLI

```cpp
property System.String^ LargeIconList {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path to the bitmap or PNG containing all of the large button and separator images for this flyout

## VBA Syntax

See [FlyoutGroup::LargeIconList](ms-its:sldworksapivb6.chm::/sldworks~FlyoutGroup~LargeIconList.html).

## See Also

[IFlyoutGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup.html)
[IFlyoutGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup_members.html)
[IFlyoutGroup::AddCommandItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~AddCommandItem.html)
[IFlyoutGroup::ReplaceCommandItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~ReplaceCommandItem.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
