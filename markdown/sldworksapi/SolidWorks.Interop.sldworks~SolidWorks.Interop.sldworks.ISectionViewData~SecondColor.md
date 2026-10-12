---
title: "SecondColor Property (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "SecondColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SecondColor.html"
---

# SecondColor Property (ISectionViewData)

Gets or sets the second color of the section view in the part or assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property SecondColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim value As System.Integer

instance.SecondColor = value

value = instance.SecondColor
```

### C#

```csharp
System.int SecondColor {get; set;}
```

### C++/CLI

```cpp
property System.int SecondColor {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

RGB value of the second color

## VBA Syntax

See [SectionViewData::SecondColor](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~SecondColor.html).

## Examples

[Create Section View in Model (C#)](Create_Section_View_in_Model_Example_CSharp.htm)
[Create Section View in Model (VB.NET)](Create_Section_View_in_Model_Example_VBNET.htm)
[Create Section View in Model (VBA)](Create_Section_View_in_Model_Example_VB.htm)
[Get Section View Data (C#)](Get_Section_View_Data_Example_CSharp.htm)
[Get Section View Data (VB.NET)](Get_Section_View_Data_Example_VBNET.htm)
[Get Section View Data (VBA)](Get_Section_View_Data_Example_VB.htm)

## Remarks

Use [ISectionViewData::ShowSectionCap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISectionViewData~ShowSectionCap.html) to display the caps of section views and [ISectionView::KeepCapColor](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISectionViewData~KeepCapColor.html) to color them.

## See Also

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html)
[ISectionViewData::FirstColor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~FirstColor.html)
[ISectionViewData::ThirdColor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ThirdColor.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
