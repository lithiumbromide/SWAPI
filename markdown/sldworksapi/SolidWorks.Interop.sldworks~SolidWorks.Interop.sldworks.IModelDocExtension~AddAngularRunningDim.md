---
title: "AddAngularRunningDim Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "AddAngularRunningDim"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddAngularRunningDim.html"
---

# AddAngularRunningDim Method (IModelDocExtension)

Adds the specified angular running dimension for selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddAngularRunningDim( _
   ByVal DisplayAsChain As System.Boolean, _
   ByVal RunBidirectionally As System.Boolean, _
   ByVal ExtensionLineExtendsFromCenterOfSet As System.Boolean, _
   ByVal LocX As System.Double, _
   ByVal LocY As System.Double, _
   ByVal LocZ As System.Double, _
   ByRef Retval As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim DisplayAsChain As System.Boolean
Dim RunBidirectionally As System.Boolean
Dim ExtensionLineExtendsFromCenterOfSet As System.Boolean
Dim LocX As System.Double
Dim LocY As System.Double
Dim LocZ As System.Double
Dim Retval As System.Integer
Dim value As System.Object

value = instance.AddAngularRunningDim(DisplayAsChain, RunBidirectionally, ExtensionLineExtendsFromCenterOfSet, LocX, LocY, LocZ, Retval)
```

### C#

```csharp
System.object AddAngularRunningDim(
   System.bool DisplayAsChain,
   System.bool RunBidirectionally,
   System.bool ExtensionLineExtendsFromCenterOfSet,
   System.double LocX,
   System.double LocY,
   System.double LocZ,
   out System.int Retval
)
```

### C++/CLI

```cpp
System.Object^ AddAngularRunningDim(
   System.bool DisplayAsChain,
   System.bool RunBidirectionally,
   System.bool ExtensionLineExtendsFromCenterOfSet,
   System.double LocX,
   System.double LocY,
   System.double LocZ,
   [Out] System.int Retval
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DisplayAsChain`: True to chain the angular dimensions together, false to not
- `RunBidirectionally`: True if each angular dimension runs in a direction closest to the baseline, false if all angular dimensions run in the same direction (see **Remarks**)
- `ExtensionLineExtendsFromCenterOfSet`: True to extend the extension lines from the center of the set of angular running dimensions, false to not
- `LocX`: X coordinate of baseline dimension (see **Remarks**)
- `LocY`: Y coordinate of baseline dimension (see **Remarks**)
- `LocZ`: Z coordinate of baseline dimension (see **Remarks**)
- `Retval`: Error as defined by [swCreateAngRunDimError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateAngRunDimError_e.html)

### Return Value

Array of [IDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html)s

## VBA Syntax

See [ModelDocExtension::AddAngularRunningDim](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~AddAngularRunningDim.html).

## Examples

[Insert Angular Running Dimension (VBA)](Set_Properties_of_Angular_Running_Dimension_Example_VB.htm)
[Insert Angular Running Dimension (VB.NET)](Set_Properties_of_Angular_Running_Dimension_Example_VBNET.htm)
[Insert Angular Running Dimension (C#)](Set_Properties_of_Angular_Running_Dimension_Example_CSharp.htm)

## Remarks

Before calling this method, call [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with Append set to true to select the baseline entity and all entities whose angles from the baseline entity you want to measure and display.

A vertical line is constructed between [LocX, LocY, LocZ] and the baseline entity. The baseline dimension (0⁰) is displayed at [LocX, LocY, LocZ].

| If RunBidirectionally is... | Then... |
| --- | --- |
| True | No angle dimension in the angular running dimension is greater than 180 ⁰ from the baseline, and each angle is measured from a direction that is closest to the baseline. |
| False | The running direction of all angle dimensions is determined by the first angle dimension added. For example, if the user places the baseline dimension at the top of the part, clicking on a feature to the right of the baseline dimension forces all subsequent angular dimensions to be measured clockwise from the baseline. |

Selections made after this method is called add angular dimensions to the set. When you have finished adding angular dimensions to the set, call [IModelDoc2::SetPickMode](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetPickMode.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IDrawingDoc::InsertAngularRunningDim Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertAngularRunningDim.html)
[IModelDocExtension::AlignRunningDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AlignRunningDimension.html)
[IModelDocExtension::ReJogRunningDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReJogRunningDimension.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
