---
title: "TransparentSection Property (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "TransparentSection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparentSection.html"
---

# TransparentSection Property (ISectionViewData)

Gets or sets whether transparent sectioning is enabled in this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Property TransparentSection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim value As System.Boolean

instance.TransparentSection = value

value = instance.TransparentSection
```

### C#

```csharp
System.bool TransparentSection {get; set;}
```

### C++/CLI

```cpp
property System.bool TransparentSection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if transparent sectioning is enabled, false if not

## VBA Syntax

See [SectionViewData::TransparentSection](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~TransparentSection.html).

## Examples

[Selectively and Transparently Section a Section View (C#)](Selectively_and_Transparently_Section_a_Section_View_Example_CSharp.htm)
[Selectively and Transparently Section a Section View (VB.NET)](Selectively_and_Transparently_Section_a_Section_View_Example_VBNET.htm)
[Selectively and Transparently Section a Section View (VBA)](Selectively_and_Transparently_Section_a_Section_View_Example_VB.htm)

## Remarks

You can specify which sectioned bodies in multibody parts or which sectioned components in assemblies to transparently section. See [ISectionViewData::TransparencyList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparencyList.html) and [ISectionViewData::SectionTransparentItemsTransparent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SectionTransparentItemsTransparent.html).

ISectionViewData::TransparentSection is only available if [ISectionViewData::ZonalSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ZonalSection.html) is true.

## See Also

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html)
[ISectionViewData::TransparencyValue Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparencyValue.html)
[ISectionViewData::SelectiveSection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SelectiveSection.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
