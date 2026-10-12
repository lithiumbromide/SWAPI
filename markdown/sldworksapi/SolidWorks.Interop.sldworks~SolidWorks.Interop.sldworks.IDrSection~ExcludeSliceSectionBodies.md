---
title: "ExcludeSliceSectionBodies Property (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "ExcludeSliceSectionBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ExcludeSliceSectionBodies.html"
---

# ExcludeSliceSectionBodies Property (IDrSection)

Gets or sets whether to exclude slice section bodies in this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExcludeSliceSectionBodies As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Boolean

instance.ExcludeSliceSectionBodies = value

value = instance.ExcludeSliceSectionBodies
```

### C#

```csharp
System.bool ExcludeSliceSectionBodies {get; set;}
```

### C++/CLI

```cpp
property System.bool ExcludeSliceSectionBodies {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to exclude slice section bodies, false to include them

## VBA Syntax

See [DrSection::ExcludeSliceSectionBodies](ms-its:sldworksapivb6.chm::/sldworks~DrSection~ExcludeSliceSectionBodies.html).

## Examples

See the [IDrSection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection.html) examples.

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
