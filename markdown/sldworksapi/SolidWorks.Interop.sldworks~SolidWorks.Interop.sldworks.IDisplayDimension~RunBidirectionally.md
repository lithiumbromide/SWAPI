---
title: "RunBidirectionally Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "RunBidirectionally"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~RunBidirectionally.html"
---

# RunBidirectionally Property (IDisplayDimension)

Gets or sets whether each dimension runs in a direction closest to the baseline in this angular running dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property RunBidirectionally As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.RunBidirectionally = value

value = instance.RunBidirectionally
```

### C#

```csharp
System.bool RunBidirectionally {get; set;}
```

### C++/CLI

```cpp
property System.bool RunBidirectionally {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if each dimension runs in a direction closest to the baseline, false if all dimensions run in the same direction (see **Remarks**)

## VBA Syntax

See [DisplayDimension::RunBidirectionally](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~RunBidirectionally.html).

## Examples

[Insert Angular Running Dimension (VBA)](Set_Properties_of_Angular_Running_Dimension_Example_VB.htm)
[Insert Angular Running Dimension (VB.NET)](Set_Properties_of_Angular_Running_Dimension_Example_VBNET.htm)
[Insert Angular Running Dimension (C#)](Set_Properties_of_Angular_Running_Dimension_Example_CSharp.htm)

## Remarks

| If this property is... | Then... |
| --- | --- |
| True | No angle dimension in the angular running dimension is greater than 180 ⁰ from the baseline, and each angle is measured from a direction that is closest to the baseline. |
| False | The running direction of all angle dimensions is determined by the first angle dimension added. For example, if the user places the baseline dimension at the top of the part, clicking on a feature to the right of the baseline dimension forces all subsequent angular dimensions to be measured clockwise from the baseline. |

This property corresponds to the **Run bidirectionally** check box in the **Witness/Leader Display** panel of the **Leaders** tab of the **Dimension** PropertyManager page that appears when you right-click in a drawing and select **More Dimensions > Angular Running Dimension**.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::DisplayAsChain Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsChain.html)
[IDisplayDimension::ExtensionLineExtendsFromCenterOfSet Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineExtendsFromCenterOfSet.html)
[IDisplayDimension::Jogged Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Jogged.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
