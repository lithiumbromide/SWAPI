---
title: "ZonalSection Property (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "ZonalSection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ZonalSection.html"
---

# ZonalSection Property (ISectionViewData)

Gets or sets whether the section method is zonal or planar.

## Syntax

### Visual Basic (Declaration)

```vb
Property ZonalSection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim value As System.Boolean

instance.ZonalSection = value

value = instance.ZonalSection
```

### C#

```csharp
System.bool ZonalSection {get; set;}
```

### C++/CLI

```cpp
property System.bool ZonalSection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the section method is zonal, false if it is planar

## VBA Syntax

See [SectionViewData::ZonalSection](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~ZonalSection.html).

## Examples

[Selectively and Transparently Section a Section View (C#)](Selectively_and_Transparently_Section_a_Section_View_Example_CSharp.htm)
[Selectively and Transparently Section a Section View (VB.NET)](Selectively_and_Transparently_Section_a_Section_View_Example_VBNET.htm)
[Selectively and Transparently Section a Section View (VBA)](Selectively_and_Transparently_Section_a_Section_View_Example_VB.htm)

## Remarks

Call [ISectionViewData::SectionedZones](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SectionedZones.html) to specify the section zones.

ISectionViewData::ZonalSection must be true for [transparent sectioning](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparentSection.html).

**NOTE:** Zonal sectioning is only supported on graphics cards that support OpenGL 4.0; zonal sectioning is not supported in Software Only OpenGL.

## See Also

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
