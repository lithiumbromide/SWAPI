---
title: "LargeMainIcon Property (IFlyoutGroup)"
project: "SOLIDWORKS API Help"
interface: "IFlyoutGroup"
member: "LargeMainIcon"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~LargeMainIcon.html"
---

# LargeMainIcon Property (IFlyoutGroup)

Obsolete. Superseded by [IFlyoutGroup::MainIconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~MainIconList.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property LargeMainIcon As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFlyoutGroup
Dim value As System.String

instance.LargeMainIcon = value

value = instance.LargeMainIcon
```

### C#

```csharp
System.string LargeMainIcon {get; set;}
```

### C++/CLI

```cpp
property System.String^ LargeMainIcon {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path to the large bitmap or PNG used in this flyout

## VBA Syntax

See [FlyoutGroup::LargeMainIcon](ms-its:sldworksapivb6.chm::/sldworks~FlyoutGroup~LargeMainIcon.html).

## See Also

[IFlyoutGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup.html)
[IFlyoutGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
