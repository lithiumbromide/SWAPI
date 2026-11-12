---
title: "ExtensionLineSameAsLeaderStyle Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "ExtensionLineSameAsLeaderStyle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineSameAsLeaderStyle.html"
---

# ExtensionLineSameAsLeaderStyle Property (IDisplayDimension)

Gets or sets whether to use leader line styles for extension line styles.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExtensionLineSameAsLeaderStyle As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.ExtensionLineSameAsLeaderStyle = value

value = instance.ExtensionLineSameAsLeaderStyle
```

### C#

```csharp
System.bool ExtensionLineSameAsLeaderStyle {get; set;}
```

### C++/CLI

```cpp
property System.bool ExtensionLineSameAsLeaderStyle {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use leader line styles for extension line styles, false to not

## VBA Syntax

See [DisplayDimension::ExtensionLineSameAsLeaderStyle](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~ExtensionLineSameAsLeaderStyle.html).

## Examples

[Insert Angular Running Dimension (VBA)](Set_Properties_of_Angular_Running_Dimension_Example_VB.htm)
[Insert Angular Running Dimension (VB.NET)](Set_Properties_of_Angular_Running_Dimension_Example_VBNET.htm)
[Insert Angular Running Dimension (C#)](Set_Properties_of_Angular_Running_Dimension_Example_CSharp.htm)

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::ExtensionLineExtendsFromCenterOfSet Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineExtendsFromCenterOfSet.html)
[IDisplayDimension::ExtensionLineUseDocumentDisplay Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineUseDocumentDisplay.html)
[IDisplayDimension::ResetExtensionLineStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ResetExtensionLineStyle.html)
[IDisplayDimension::DisplayAsChain Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsChain.html)
[IDisplayDimension::RunBidirectionally Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~RunBidirectionally.html)
[IDisplayDimension::Jogged Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Jogged.html)
[IDisplayDimension::SetLineFontExtensionStyle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLineFontExtensionStyle.html)
[IDisplayDimension::SetLineFontExtensionThickness Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLineFontExtensionThickness.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
