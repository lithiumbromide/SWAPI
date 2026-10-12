---
title: "SectionTransparentItemsTransparent Property (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "SectionTransparentItemsTransparent"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SectionTransparentItemsTransparent.html"
---

# SectionTransparentItemsTransparent Property (ISectionViewData)

Gets or sets whether the specified sectioned bodies in the multibody part or the specified sectioned components in the assembly are transparently sectioned in this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Property SectionTransparentItemsTransparent As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim value As System.Boolean

instance.SectionTransparentItemsTransparent = value

value = instance.SectionTransparentItemsTransparent
```

### C#

```csharp
System.bool SectionTransparentItemsTransparent {get; set;}
```

### C++/CLI

```cpp
property System.bool SectionTransparentItemsTransparent {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the specified sectioned bodies in the multibody part or the specified sectioned components in the assembly are transparently sectioned in this section view; false if all sectioned bodies in the multibody part or all sectioned components in the assembly, except for the specified sectioned bodies or the specified sectioned components, are transparently sectioned in this section view (see **Remarks**)

## VBA Syntax

See [SectionViewData::SectionTransparentItemsTransparent](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~SectionTransparentItemsTransparent.html).

## Examples

[Selectively and Transparently Section a Section View (C#)](Selectively_and_Transparently_Section_a_Section_View_Example_CSharp.htm)
[Selectively and Transparently Section a Section View (VB.NET)](Selectively_and_Transparently_Section_a_Section_View_Example_VBNET.htm)
[Selectively and Transparently Section a Section View (VBA)](Selectively_and_Transparently_Section_a_Section_View_Example_VB.htm)

## Remarks

Before calling this property, call [ISectionViewData::TransparentyList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparencyList.html) to specify the sectioned bodies in the multibody part or the sectioned components in the assembly to transparently section. Call [ISectionViewData::TransparencyValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparencyValue.html) to set the level of transparency of the sectioned bodies in the multibody part or the sectioned components in the assembly.

This property is only available if [ISectionViewData::ZonalSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ZonalSection.html) and [ISectionViewData::TransparentSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparentSection.html) are true.

## See Also

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
