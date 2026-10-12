---
title: "EnableSelectIdenticalComponents Property (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "EnableSelectIdenticalComponents"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~EnableSelectIdenticalComponents.html"
---

# EnableSelectIdenticalComponents Property (IPropertyManagerPageSelectionbox)

Gets or sets whether to enable **Select Identical Components** in the context menu of this PropertyManager page selection box.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnableSelectIdenticalComponents As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Boolean

instance.EnableSelectIdenticalComponents = value

value = instance.EnableSelectIdenticalComponents
```

### C#

```csharp
System.bool EnableSelectIdenticalComponents {get; set;}
```

### C++/CLI

```cpp
property System.bool EnableSelectIdenticalComponents {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable **Select Identical Components** in this selection box's context menu, false to not

## VBA Syntax

See [PropertyManagerPageSelectionbox::EnableSelectIdenticalComponents](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSelectionbox~EnableSelectIdenticalComponents.html).

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
