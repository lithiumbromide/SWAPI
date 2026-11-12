---
title: "Enabled Property (IPropertyManagerPageControl)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageControl"
member: "Enabled"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~Enabled.html"
---

# Enabled Property (IPropertyManagerPageControl)

Gets or sets the state of the PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Property Enabled As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageControl
Dim value As System.Boolean

instance.Enabled = value

value = instance.Enabled
```

### C#

```csharp
System.bool Enabled {get; set;}
```

### C++/CLI

```cpp
property System.bool Enabled {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable the page, false to not

## VBA Syntax

See [PropertyManagerPageControl::Enabled](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageControl~Enabled.html).

## See Also

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.html)
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
