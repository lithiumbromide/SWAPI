---
title: "Visible Property (IPropertyManagerPageGroup)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageGroup"
member: "Visible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~Visible.html"
---

# Visible Property (IPropertyManagerPageGroup)

Gets or sets the group box visibility state.

## Syntax

### Visual Basic (Declaration)

```vb
Property Visible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageGroup
Dim value As System.Boolean

instance.Visible = value

value = instance.Visible
```

### C#

```csharp
System.bool Visible {get; set;}
```

### C++/CLI

```cpp
property System.bool Visible {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable visibility, false to not

## VBA Syntax

See [PropertyManagerPageGroup::Visible](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageGroup~Visible.html).

## See Also

[IPropertyManagerPageGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup.html)
[IPropertyManagerPageGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
