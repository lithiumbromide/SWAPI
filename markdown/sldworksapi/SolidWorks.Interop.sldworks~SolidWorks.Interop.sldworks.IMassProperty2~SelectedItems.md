---
title: "SelectedItems Property (IMassProperty2)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty2"
member: "SelectedItems"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~SelectedItems.html"
---

# SelectedItems Property (IMassProperty2)

Gets or sets the list of bodies/components for which to calculate mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Property SelectedItems As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty2
Dim value As System.Object

instance.SelectedItems = value

value = instance.SelectedItems
```

### C#

```csharp
System.object SelectedItems {get; set;}
```

### C++/CLI

```cpp
property System.Object^ SelectedItems {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html) for the part or [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html) for the assembly

## VBA Syntax

See [MassProperty2::SelectedItems](ms-its:sldworksapivb6.chm::/sldworks~MassProperty2~SelectedItems.html).

## Remarks

Pre-selected bodies/components are included in the returned array.

## See Also

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html)
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.html)
[IMassProperty2::IncludeHiddenBodiesOrComponents Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~IncludeHiddenBodiesOrComponents.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
