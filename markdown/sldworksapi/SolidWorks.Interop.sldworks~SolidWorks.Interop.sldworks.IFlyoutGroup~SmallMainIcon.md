---
title: "SmallMainIcon Property (IFlyoutGroup)"
project: "SOLIDWORKS API Help"
interface: "IFlyoutGroup"
member: "SmallMainIcon"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~SmallMainIcon.html"
---

# SmallMainIcon Property (IFlyoutGroup)

Obsolete. Superseded by [IFlyoutGroup::MainIconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~MainIconList.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property SmallMainIcon As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFlyoutGroup
Dim value As System.String

instance.SmallMainIcon = value

value = instance.SmallMainIcon
```

### C#

```csharp
System.string SmallMainIcon {get; set;}
```

### C++/CLI

```cpp
property System.String^ SmallMainIcon {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path to the small bitmap or PNG used in this flyout

## VBA Syntax

See [FlyoutGroup::SmallMainIcon](ms-its:sldworksapivb6.chm::/sldworks~FlyoutGroup~SmallMainIcon.html).

## See Also

[IFlyoutGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup.html)
[IFlyoutGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
