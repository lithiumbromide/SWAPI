---
title: "ExcludeSelectedItems Property (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "ExcludeSelectedItems"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ExcludeSelectedItems.html"
---

# ExcludeSelectedItems Property (ISectionViewData)

Gets or sets whether to exclude or include the specific bodies in the multibody part or specific components in the assembly in selective sectioning in this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExcludeSelectedItems As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim value As System.Boolean

instance.ExcludeSelectedItems = value

value = instance.ExcludeSelectedItems
```

### C#

```csharp
System.bool ExcludeSelectedItems {get; set;}
```

### C++/CLI

```cpp
property System.bool ExcludeSelectedItems {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to exclude specific bodies in the multibody part or specific components in the assembly in selective sectioning, false to include only the specific bodies in the part or the specific components in the assembly in selective sectioning (see **Remarks**)

## VBA Syntax

See [SectionViewData::ExcludeSelectedItems](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~ExcludeSelectedItems.html).

## Examples

[Selectively and Transparently Section a Section View (C#)](Selectively_and_Transparently_Section_a_Section_View_Example_CSharp.htm)
[Selectively and Transparently Section a Section View (VB.NET)](Selectively_and_Transparently_Section_a_Section_View_Example_VBNET.htm)
[Selectively and Transparently Section a Section View (VBA)](Selectively_and_Transparently_Section_a_Section_View_Example_VB.htm)

## Remarks

Before calling this property, call [ISectionViewData::SelectiveSectioningList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SelectiveSectioningList.html) to specify the bodies in the multibody part or the components in the assembly to exclude or include in selective sectioning.

ISectionViewData::ExcludeSelectedItems is only available if [ISectionViewData::SelectiveSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SelectiveSection.html) is true.

## See Also

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
