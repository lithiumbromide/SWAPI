---
title: "SelectSecondSymmetryPlane Method (ICWTopologySymmetryControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologySymmetryControl"
member: "SelectSecondSymmetryPlane"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl~SelectSecondSymmetryPlane.html"
---

# SelectSecondSymmetryPlane Method (ICWTopologySymmetryControl)

Sets the second symmetry plane to cut the model into four identical bodies in this topology study symmetry manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SelectSecondSymmetryPlane( _
   ByVal PlaneDisp As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologySymmetryControl
Dim PlaneDisp As System.Object

instance.SelectSecondSymmetryPlane(PlaneDisp)
```

### C#

```csharp
void SelectSecondSymmetryPlane(
   System.object PlaneDisp
)
```

### C++/CLI

```cpp
void SelectSecondSymmetryPlane(
   System.Object^ PlaneDisp
)
```

### Parameters

- `PlaneDisp`: Second symmetry plane

## VBA Syntax

See [CWTopologySymmetryControl::SelectSecondSymmetryPlane](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologySymmetryControl~SelectSecondSymmetryPlane.html).

## Examples

See the [ICWTopologySymmetryControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl.html) example.

## Remarks

This method is not valid if [ICWTopologySymmetryControl::SelectSymmetryType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl~SelectSymmetryType.html) is set to [swsTopologySymmetryControlOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologySymmetryControlOption_e.html).swsTopologySymmetryControlType_HalfSymmetry.

## See Also

[ICWTopologySymmetryControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl.html)
[ICWTopologySymmetryControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl_members.html)
[ICWTopologySymmetryControl::ClearSelPlanes Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl~ClearSelPlanes.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
