---
title: "CutSurfaceBodies Property (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "CutSurfaceBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~CutSurfaceBodies.html"
---

# CutSurfaceBodies Property (IDrSection)

Gets or sets whether to hide cut surface bodies in this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Property CutSurfaceBodies As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Boolean

instance.CutSurfaceBodies = value

value = instance.CutSurfaceBodies
```

### C#

```csharp
System.bool CutSurfaceBodies {get; set;}
```

### C++/CLI

```cpp
property System.bool CutSurfaceBodies {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to hide cut surface bodies in this section view, false to show them

## VBA Syntax

See [DrSection::CutSurfaceBodies](ms-its:sldworksapivb6.chm::/sldworks~DrSection~CutSurfaceBodies.html).

## Examples

See the [IDrSection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection.html) examples.

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::GetDisplayOnlySurfaceCut Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetDisplayOnlySurfaceCut.html)
[IDrSection::SetDisplayOnlySurfaceCut Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetDisplayOnlySurfaceCut.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
