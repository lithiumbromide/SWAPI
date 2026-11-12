---
title: "TransparencyValue Property (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "TransparencyValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparencyValue.html"
---

# TransparencyValue Property (ISectionViewData)

Gets or sets the level of transparency for the specified transparently sectioned bodies in the multibody part or the specified transparently sectioned components in the assembly in this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Property TransparencyValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim value As System.Double

instance.TransparencyValue = value

value = instance.TransparencyValue
```

### C#

```csharp
System.double TransparencyValue {get; set;}
```

### C++/CLI

```cpp
property System.double TransparencyValue {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.01 (least transparent) to 1.0 (most transparent)

## VBA Syntax

See [SectionViewData::TransparencyValue](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~TransparencyValue.html).

## Examples

[Selectively and Transparently Section a Section View (C#)](Selectively_and_Transparently_Section_a_Section_View_Example_CSharp.htm)
[Selectively and Transparently Section a Section View (VB.NET)](Selectively_and_Transparently_Section_a_Section_View_Example_VBNET.htm)
[Selectively and Transparently Section a Section View (VBA)](Selectively_and_Transparently_Section_a_Section_View_Example_VB.htm)

## Remarks

To specify the sectioned bodies in the multibody part or the sectioned components in the assembly to transparently section, call [ISectionViewData::TransparencyList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparencyList.html) and [ISectionViewData::SectionTransparentItemsTransparent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SectionTransparentItemsTransparent.html).

This property is only available if [ISectionViewData::ZonalSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ZonalSection.html) and [ISectionViewData::TransparentSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparentSection.html) are true.

## See Also

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
