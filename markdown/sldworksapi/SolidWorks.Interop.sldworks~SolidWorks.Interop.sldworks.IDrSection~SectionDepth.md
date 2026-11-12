---
title: "SectionDepth Property (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "SectionDepth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SectionDepth.html"
---

# SectionDepth Property (IDrSection)

Gets or sets the distance from the section line of the section view.

## Syntax

### Visual Basic (Declaration)

```vb
Property SectionDepth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Double

instance.SectionDepth = value

value = instance.SectionDepth
```

### C#

```csharp
System.double SectionDepth {get; set;}
```

### C++/CLI

```cpp
property System.double SectionDepth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance from the section line of the section view

## VBA Syntax

See [DrSection::SectionLayer](ms-its:sldworksapivb6.chm::/sldworks~DrSection~Layer.html).

## Examples

See the [IDrSection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection.html) examples.

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
