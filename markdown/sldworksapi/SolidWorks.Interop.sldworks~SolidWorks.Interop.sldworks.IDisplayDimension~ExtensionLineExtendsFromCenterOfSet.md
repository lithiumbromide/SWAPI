---
title: "ExtensionLineExtendsFromCenterOfSet Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "ExtensionLineExtendsFromCenterOfSet"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineExtendsFromCenterOfSet.html"
---

# ExtensionLineExtendsFromCenterOfSet Property (IDisplayDimension)

Gets or sets whether extension lines extend from the center of this set of angular running dimensions.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExtensionLineExtendsFromCenterOfSet As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.ExtensionLineExtendsFromCenterOfSet = value

value = instance.ExtensionLineExtendsFromCenterOfSet
```

### C#

```csharp
System.bool ExtensionLineExtendsFromCenterOfSet {get; set;}
```

### C++/CLI

```cpp
property System.bool ExtensionLineExtendsFromCenterOfSet {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if extension lines extend from the center of the set of angular running dimensions, false if they extend from the selection point

## VBA Syntax

See [DisplayDimension::ExtensionLineExtendsFromCenterOfSet](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~ExtensionLineExtendsFromCenterofSet.html).

## Examples

[Insert Angular Running Dimension (VBA)](Set_Properties_of_Angular_Running_Dimension_Example_VB.htm)
[Insert Angular Running Dimension (VB.NET)](Set_Properties_of_Angular_Running_Dimension_Example_VBNET.htm)
[Insert Angular Running Dimension (C#)](Set_Properties_of_Angular_Running_Dimension_Example_CSharp.htm)

## Remarks

This property corresponds to the **Extension line extends from center of set** check box in the **Witness/Leader Display** panel of the **Leaders** tab of the **Dimension** PropertyManager page that appears when you right-click in a drawing and select **More Dimensions > Angular Running Dimension**.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::DisplayAsChain Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsChain.html)
[IDisplayDimension::RunBidirectionally Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~RunBidirectionally.html)
[IDisplayDimension::Jogged Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Jogged.html)
[IDisplayDimension::ExtensionLineSameAsLeaderStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineSameAsLeaderStyle.html)
[IDisplayDimension::ExtensionLineUseDocumentDisplay Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineUseDocumentDisplay.html)
[IDisplayDimension::ResetExtensionLineStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ResetExtensionLineStyle.html)
[IDisplayDimension::SetLineFontExtensionStyle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLineFontExtensionStyle.html)
[IDisplayDimension::SetLineFontExtensionThickness Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLineFontExtensionThickness.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
