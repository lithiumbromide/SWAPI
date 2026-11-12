---
title: "SelectiveSection Property (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "SelectiveSection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SelectiveSection.html"
---

# SelectiveSection Property (ISectionViewData)

Gets or sets whether selective sectioning is enabled in this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Property SelectiveSection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim value As System.Boolean

instance.SelectiveSection = value

value = instance.SelectiveSection
```

### C#

```csharp
System.bool SelectiveSection {get; set;}
```

### C++/CLI

```cpp
property System.bool SelectiveSection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if selective sectioning is enabled, false if not (see **Remarks**)

## VBA Syntax

See [SectionViewData::SelectiveSection](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~SelectiveSection.html).

## Examples

[Selectively and Transparently Section a Section View (C#)](Selectively_and_Transparently_Section_a_Section_View_Example_CSharp.htm)
[Selectively and Transparently Section a Section View (VB.NET)](Selectively_and_Transparently_Section_a_Section_View_Example_VBNET.htm)
[Selectively and Transparently Section a Section View (VBA)](Selectively_and_Transparently_Section_a_Section_View_Example_VB.htm)

## Remarks

| If this property is... | Then... |
| --- | --- |
| True | You can specify which bodies in the multibody part or which components in the assembly to selectively section. Call: ISectionViewData::SelectiveSectioningList to specify the bodies or components to selectively section. ISectionViewData::ExcludeSelectedItems to specify the bodies or components to exclude or include in selective sectioning. |
| False | All bodies in the multibody part and all components in the assembly are sectioned. |

## See Also

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html)
[ISectionViewData::TransparentSection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparentSection.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
