---
title: "KeepCapColor Property (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "KeepCapColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~KeepCapColor.html"
---

# KeepCapColor Property (ISectionViewData)

Gets or sets whether to color the caps of section views.

## Syntax

### Visual Basic (Declaration)

```vb
Property KeepCapColor As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim value As System.Boolean

instance.KeepCapColor = value

value = instance.KeepCapColor
```

### C#

```csharp
System.bool KeepCapColor {get; set;}
```

### C++/CLI

```cpp
property System.bool KeepCapColor {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to color the caps of section views, false to not (see **Remarks**)

## VBA Syntax

See [SectionViewData::KeepCapColor](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~KeepCapColor.html).

## Examples

[Create Section View in Model (VBA)](Create_Section_View_in_Model_Example_VB.htm)
[Create Section View in Model (VB.NET)](Create_Section_View_in_Model_Example_VBNET.htm)
[Create Section View in Model (C#)](Create_Section_View_in_Model_Example_CSharp.htm)

## Remarks

This property is valid only if [ISectionViewData::ShowSectionCap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISectionViewData~ShowSectionCap.html) is true and [ISectionViewData::GraphicsOnlySection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISectionViewData~GraphicsOnlySection.html) is false.

## See Also

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
