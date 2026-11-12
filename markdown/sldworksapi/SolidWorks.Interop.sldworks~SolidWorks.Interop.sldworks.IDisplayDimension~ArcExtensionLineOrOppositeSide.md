---
title: "ArcExtensionLineOrOppositeSide Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "ArcExtensionLineOrOppositeSide"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ArcExtensionLineOrOppositeSide.html"
---

# ArcExtensionLineOrOppositeSide Property (IDisplayDimension)

Gets or sets whether to attach or extend the radial dimension leader on this radial display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property ArcExtensionLineOrOppositeSide As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.ArcExtensionLineOrOppositeSide = value

value = instance.ArcExtensionLineOrOppositeSide
```

### C#

```csharp
System.bool ArcExtensionLineOrOppositeSide {get; set;}
```

### C++/CLI

```cpp
property System.bool ArcExtensionLineOrOppositeSide {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

| If... | Then... |
| --- | --- |
| True | Attach the radial dimension leader to the arc extension line. - or - If the radial dimension leader encounters arc geometry, then extend the radial dimension leader to the opposite side of the arc. |
| False | Neither attach nor extend the radial dimension leader. |

## VBA Syntax

See [DisplayDimension::ArcExtensionLineOrOppositeSide](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~ArcExtensionLineOrOppositeSide.html).

## Examples

[Set Radial Dimension Leader (C#)](Edit_Radial_Dimension_Example_CSharp.htm)
[Set Radial Dimension Leader (VB.NET)](Edit_Radial_Dimension_Example_VBNET.htm)
[Set Radial Dimension Leader (VBA)](Edit_Radial_Dimension_Example_VB.htm)

## Remarks

This property is only valid for radial display dimensions.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IModelDoc2::AddRadialDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddRadialDimension2.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
