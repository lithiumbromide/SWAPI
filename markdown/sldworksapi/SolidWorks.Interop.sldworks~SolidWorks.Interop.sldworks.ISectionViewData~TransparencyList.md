---
title: "TransparencyList Property (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "TransparencyList"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparencyList.html"
---

# TransparencyList Property (ISectionViewData)

Gets or sets the sectioned bodies in the multibody part or the sectioned components in the assembly to transparently section in this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Property TransparencyList As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim value As System.Object

instance.TransparencyList = value

value = instance.TransparencyList
```

### C#

```csharp
System.object TransparencyList {get; set;}
```

### C++/CLI

```cpp
property System.Object^ TransparencyList {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html) in the multibody part or an array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html) to transparently section (see **Remarks**)

## VBA Syntax

See [SectionViewData::TransparencyList](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~TransparencyList.html).

## Examples

[Selectively and Transparently Section a Section View (C#)](Selectively_and_Transparently_Section_a_Section_View_Example_CSharp.htm)
[Selectively and Transparently Section a Section View (VB.NET)](Selectively_and_Transparently_Section_a_Section_View_Example_VBNET.htm)
[Selectively and Transparently Section a Section View (VBA)](Selectively_and_Transparently_Section_a_Section_View_Example_VB.htm)

## Remarks

Call this property before calling [ISectionViewData::SectionTransparentItemsTransparent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SectionTransparentItemsTransparent.html) to specify which sectioned bodies in the multibody part or which sectioned components in the assembly to transparently section.

To select each sectioned body or component, specify a Mark of 32 for [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html). Select the section planes after selecting the sectioned bodies or components.

This property is only available if [ISectionViewData::ZonalSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ZonalSection.html) and [ISectionViewData::TransparentSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparentSection.html) are true.

## See Also

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html)
[ISectionViewData::FirstPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~FirstPlane.html)
[ISectionViewData::SecondPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SecondPlane.html)
[ISectionViewData::ThirdPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ThirdPlane.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
