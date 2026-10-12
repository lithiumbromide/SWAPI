---
title: "SectionedZones Property (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "SectionedZones"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SectionedZones.html"
---

# SectionedZones Property (ISectionViewData)

Gets or sets the intersection zones that define how to section this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Property SectionedZones As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim value As System.Integer

instance.SectionedZones = value

value = instance.SectionedZones
```

### C#

```csharp
System.int SectionedZones {get; set;}
```

### C++/CLI

```cpp
property System.int SectionedZones {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Intersection zones as defined in [swZonalSectionViewZones_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swZonalSectionViewZones_e.html) (see **Remarks**)

## VBA Syntax

See [SectionViewData::SectionedZones](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~SectionedZones.html).

## Examples

[Selectively and Transparently Section a Section View (C#)](Selectively_and_Transparently_Section_a_Section_View_Example_CSharp.htm)
[Selectively and Transparently Section a Section View (VB.NET)](Selectively_and_Transparently_Section_a_Section_View_Example_VBNET.htm)
[Selectively and Transparently Section a Section View (VBA)](Selectively_and_Transparently_Section_a_Section_View_Example_VB.htm)

## Remarks

In the SOLIDWORKS API, zones are defined by the intersections of the sectioning planes. This table describes the intersection zones and the enumerators to which they correspond.

| Number of sectioning planes | Zones | Intersection zones | swZonalSectionViewZones_e enumerators |
| --- | --- | --- | --- |
| 1 | 1 | Front side of sectioning plane 1 | swZonalSectionViewZones_swZonalSectionViewZone_1 |
|  | 2 | Back side of sectioning plane 2 | swZonalSectionViewZones_swZonalSectionViewZone_2 |
| 2 | 1 | Front side of sectioning plane 1 Front side of sectioning plane 2 | swZonalSectionViewZones_swZonalSectionViewZone_1 |
|  | 2 | Back side of sectioning plane 1 Front side of sectioning plane 2 | swZonalSectionViewZones_swZonalSectionViewZone_2 |
|  | 3 | Front side of sectioning plane 1 Back side of sectioning plane 2 | swZonalSectionViewZones_swZonalSectionViewZone_3 |
|  | 4 | Back side of sectioning plane 1 Back side of sectioning plane 2 | swZonalSectionViewZones_swZonalSectionViewZone_4 |
| 3 | 1 | Front side of sectioning plane 1 Front side of sectioning plane 2 Front side of sectioning plane 3 | swZonalSectionViewZones_swZonalSectionViewZone_1 |
|  | 2 | Back side of sectioning plane 1 Front side of sectioning plane 2 Front side of sectioning plane 3 | swZonalSectionViewZones_swZonalSectionViewZone_2 |
|  | 3 | Front side of sectioning plane 1 Back side of sectioning plane 2 Front side of sectioning plane 3 | swZonalSectionViewZones_swZonalSectionViewZone_3 |
|  | 4 | Back side of sectioning plane 1 Back side of sectioning plane 2 Front side of sectioning plane 3 | swZonalSectionViewZones_swZonalSectionViewZone_4 |
|  | 5 | Front side of sectioning plane 1 Front side of sectioning plane 2 Back side of sectioning plane 3 | swZonalSectionViewZones_swZonalSectionViewZone_5 |
|  | 6 | Back side of sectioning plane 1 Front side of sectioning plane 2 Back side of sectioning plane 3 | swZonalSectionViewZones_swZonalSectionViewZone_6 |
|  | 7 | Front side of sectioning plane 1 Back side of sectioning plane 2 Back side of sectioning plane 3 | swZonalSectionViewZones_swZonalSectionViewZone_7 |
|  | 8 | Back side of sectioning plane 1 Back side of sectioning plane 2 Back side of sectioning plane 3 | swZonalSectionViewZones_swZonalSectionViewZone_8 |

This property is only available if [ISectionViewData::ZonalSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ZonalSection.html) is true.

## See Also

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
