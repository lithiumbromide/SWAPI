---
title: "GetWitnessLineGap Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetWitnessLineGap"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetWitnessLineGap.html"
---

# GetWitnessLineGap Method (IDisplayDimension)

Gets the gap of the specified dimension extension line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWitnessLineGap( _
   ByVal WitnessIndex As System.Short, _
   ByRef UseDoc As System.Boolean, _
   ByRef Gap As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim WitnessIndex As System.Short
Dim UseDoc As System.Boolean
Dim Gap As System.Double
Dim value As System.Boolean

value = instance.GetWitnessLineGap(WitnessIndex, UseDoc, Gap)
```

### C#

```csharp
System.bool GetWitnessLineGap(
   System.short WitnessIndex,
   out System.bool UseDoc,
   out System.double Gap
)
```

### C++/CLI

```cpp
System.bool GetWitnessLineGap(
   System.short WitnessIndex,
   [Out] System.bool UseDoc,
   [Out] System.double Gap
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WitnessIndex`: Index of the extension line whose gap to get
- `UseDoc`: True if using the document default value of the gap, false if not (see **Remarks**)
- `Gap`: Gap value in system units (see **Remarks**)

### Return Value

True if the operation succeeds, false if not

## VBA Syntax

See [DisplayDimension::GetWitnessLineGap](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetWitnessLineGap.html).

## Examples

[Get and Set Dimension Extension Lines Gap (VBA)](Get_and_Set_Dimension_Extension_Lines_Gaps_Example_VB.htm)

## Remarks

The UseDoc argument is dependent on the detailing standard. You can retrieve the document default value using the [document-level user-preference swDetailingWitnessLineGap](ms-its:swconst.chm::/DP_Dimensions.htm).

The Gap argument is the document default value if UseDoc is true; otherwise, the value returned is the locally set value.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::SetWitnessLineGap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetWitnessLineGap.html)
[IView::GetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionInfo6.html)
[IView::IGetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionInfo6.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
