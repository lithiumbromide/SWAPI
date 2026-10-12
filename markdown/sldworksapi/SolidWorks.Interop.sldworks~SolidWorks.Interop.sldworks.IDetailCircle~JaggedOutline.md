---
title: "JaggedOutline Property (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "JaggedOutline"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~JaggedOutline.html"
---

# JaggedOutline Property (IDetailCircle)

Gets or sets whether to show a jagged outline in the detail view.

## Syntax

### Visual Basic (Declaration)

```vb
Property JaggedOutline As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim value As System.Boolean

instance.JaggedOutline = value

value = instance.JaggedOutline
```

### C#

```csharp
System.bool JaggedOutline {get; set;}
```

### C++/CLI

```cpp
property System.bool JaggedOutline {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to show a jagged outline in the detail view, false to not (see **Remarks**)

## VBA Syntax

See [DetailCircle::JaggedOutline](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~JaggedOutline.html).

## Examples

[Create Detail Circle and Detail View (C#)](Create_Detail_Circle_and_Detail_View_Example_CSharp.htm)
[Create Detail Circle and Detail View (VB.NET)](Create_Detail_Circle_and_Detail_View_Example_VBNET.htm)
[Create Detail Circle and Detail View (VBA)](Create_Detail_Circle_and_Detail_View_Example_VB.htm)

## Remarks

This property is only available when [IDetailCircle::NoOutline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~NoOutline.html) is false.

To set the intensity of the jagged outline, call [IDetailCircle::ShapeIntensity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~ShapeIntensity.html).

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
