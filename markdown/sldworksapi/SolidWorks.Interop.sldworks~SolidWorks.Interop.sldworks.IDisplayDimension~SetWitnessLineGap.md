---
title: "SetWitnessLineGap Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SetWitnessLineGap"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetWitnessLineGap.html"
---

# SetWitnessLineGap Method (IDisplayDimension)

Sets the gap for the specified dimension extension line.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetWitnessLineGap( _
   ByVal WitnessIndex As System.Short, _
   ByVal UseDoc As System.Boolean, _
   ByVal Gap As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim WitnessIndex As System.Short
Dim UseDoc As System.Boolean
Dim Gap As System.Double
Dim value As System.Boolean

value = instance.SetWitnessLineGap(WitnessIndex, UseDoc, Gap)
```

### C#

```csharp
System.bool SetWitnessLineGap(
   System.short WitnessIndex,
   System.bool UseDoc,
   System.double Gap
)
```

### C++/CLI

```cpp
System.bool SetWitnessLineGap(
   System.short WitnessIndex,
   System.bool UseDoc,
   System.double Gap
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WitnessIndex`: Index of the extension line whose gap to get
- `UseDoc`: True to use the document default value of the gap, false to not (see **Remarks**)
- `Gap`: Gap value in system units; ignored if UseDoc is true

### Return Value

True if the operation succeeds, false if not

## VBA Syntax

See [DisplayDimension::SetWitnessLineGap](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SetWitnessLineGap.html).

## Examples

[Get and Set Dimension Extension Lines Gaps (VBA)](Get_and_Set_Dimension_Extension_Lines_Gaps_Example_VB.htm)

## Remarks

The UseDoc argument is dependent on the detailing standard. You can retrieve the document default value using the [document-level user-preference swDetailingWitnessLineGap](ms-its:swconst.chm::/DP_Dimensions.htm).

Call [IModelView::GraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GraphicsRedraw.html) after calling this method to redraw the graphics area.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::SetWitnessLineGap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetWitnessLineGap.html)
[IView::GetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionInfo6.html)
[IView::IGetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionInfo6.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
