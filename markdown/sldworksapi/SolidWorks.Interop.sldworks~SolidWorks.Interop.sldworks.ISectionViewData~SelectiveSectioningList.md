---
title: "SelectiveSectioningList Property (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "SelectiveSectioningList"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SelectiveSectioningList.html"
---

# SelectiveSectioningList Property (ISectionViewData)

Gets or sets the bodies in the multibody part or the components in the assembly for selective sectioning in this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Property SelectiveSectioningList As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim value As System.Object

instance.SelectiveSectioningList = value

value = instance.SelectiveSectioningList
```

### C#

```csharp
System.object SelectiveSectioningList {get; set;}
```

### C++/CLI

```cpp
property System.Object^ SelectiveSectioningList {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html) in the multibody part or an array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html) in the assembly to selectively section (see **Remarks**)

## VBA Syntax

See [SectionViewData::SelectiveSectioningList](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~SelectiveSectioningList.html).

## Examples

[Selectively and Transparently Section a Section View (C#)](Selectively_and_Transparently_Section_a_Section_View_Example_CSharp.htm)
[Selectively and Transparently Section a Section View (VB.NET)](Selectively_and_Transparently_Section_a_Section_View_Example_VBNET.htm)
[Selectively and Transparently Section a Section View (VBA)](Selectively_and_Transparently_Section_a_Section_View_Example_VB.htm)

## Remarks

To select each body in a multibody part or each component in an assembly for selective sectioning, specify a Mark of 8 for [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html). Select the section planes after selecting the bodies or components.

Call [ISectionViewData::ExcludeSelectedItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ExcludeSelectedItems.html) to exclude or include the specified bodies in the multibody part or the specified components in the assembly in selective sectioning.

ISectionViewData::SelectiveSectioningList is only available if [ISectionViewData::SelectiveSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SelectiveSection.html) is true.

## See Also

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html)
[ISectionViewData::FirstPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~FirstPlane.html)
[ISectionViewData::SecondPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SecondPlane.html)
[ISectionViewData::ThirdPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ThirdPlane.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
