---
title: "ShapeIntensity Property (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "ShapeIntensity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~ShapeIntensity.html"
---

# ShapeIntensity Property (IDetailCircle)

Gets or sets the shape intensity of the jagged outline in the detail view.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShapeIntensity As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim value As System.Integer

instance.ShapeIntensity = value

value = instance.ShapeIntensity
```

### C#

```csharp
System.int ShapeIntensity {get; set;}
```

### C++/CLI

```cpp
property System.int ShapeIntensity {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Shape intensity of the jagged outline; valid range is 1 (most) to 5 (least) (see **Remarks**)

## VBA Syntax

See [DetailCircle::ShapeIntensity](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~ShapeIntensity.html).

## Examples

[Create Detail Circle and Detail View (C#)](Create_Detail_Circle_and_Detail_View_Example_CSharp.htm)
[Create Detail Circle and Detail View (VB.NET)](Create_Detail_Circle_and_Detail_View_Example_VBNET.htm)
[Create Detail Circle and Detail View (VBA)](Create_Detail_Circle_and_Detail_View_Example_VB.htm)

## Remarks

This property is only available when [IDetailCircle::JaggedOutline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~JaggedOutline.html) is true and [IDetailCircle::NoOutline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~NoOutline.html) is false.

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
