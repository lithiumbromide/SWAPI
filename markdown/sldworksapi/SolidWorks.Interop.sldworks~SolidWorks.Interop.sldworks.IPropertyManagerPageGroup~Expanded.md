---
title: "Expanded Property (IPropertyManagerPageGroup)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageGroup"
member: "Expanded"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~Expanded.html"
---

# Expanded Property (IPropertyManagerPageGroup)

Gets or sets the group box expansion state.

## Syntax

### Visual Basic (Declaration)

```vb
Property Expanded As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageGroup
Dim value As System.Boolean

instance.Expanded = value

value = instance.Expanded
```

### C#

```csharp
System.bool Expanded {get; set;}
```

### C++/CLI

```cpp
property System.bool Expanded {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to expand, false to not

## VBA Syntax

See [PropertyManagerPageGroup::Expanded](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageGroup~Expanded.html).

## See Also

[IPropertyManagerPageGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup.html)
[IPropertyManagerPageGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
