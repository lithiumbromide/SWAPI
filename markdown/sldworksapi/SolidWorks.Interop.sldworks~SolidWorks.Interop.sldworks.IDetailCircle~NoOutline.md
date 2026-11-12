---
title: "NoOutline Property (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "NoOutline"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~NoOutline.html"
---

# NoOutline Property (IDetailCircle)

Gets or sets whether to show an outline in the detail view.

## Syntax

### Visual Basic (Declaration)

```vb
Property NoOutline As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim value As System.Boolean

instance.NoOutline = value

value = instance.NoOutline
```

### C#

```csharp
System.bool NoOutline {get; set;}
```

### C++/CLI

```cpp
property System.bool NoOutline {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to not show an outline in the detail view, false to show an outline in the detail view

## VBA Syntax

See [DetailCircle::NoOutline](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~NoOutline.html).

## Examples

[Create Detail Circle and Detail View (C#)](Create_Detail_Circle_and_Detail_View_Example_CSharp.htm)
[Create Detail Circle and Detail View (VB.NET)](Create_Detail_Circle_and_Detail_View_Example_VBNET.htm)
[Create Detail Circle and Detail View (VBA)](Create_Detail_Circle_and_Detail_View_Example_VB.htm)

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::HasFullOutline Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~HasFullOutline.html)
[IDetailCircle::SetFullOutline Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetFullOutline.html)
[IDetailCircle::JaggedOutline Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~JaggedOutline.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
