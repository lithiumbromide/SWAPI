---
title: "SelectThirdSymmetryPlane Method (ICWTopologySymmetryControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologySymmetryControl"
member: "SelectThirdSymmetryPlane"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl~SelectThirdSymmetryPlane.html"
---

# SelectThirdSymmetryPlane Method (ICWTopologySymmetryControl)

Sets the third symmetry plane to cut the model into eight identical bodies in this topology study symmetry manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SelectThirdSymmetryPlane( _
   ByVal PlaneDisp As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologySymmetryControl
Dim PlaneDisp As System.Object

instance.SelectThirdSymmetryPlane(PlaneDisp)
```

### C#

```csharp
void SelectThirdSymmetryPlane(
   System.object PlaneDisp
)
```

### C++/CLI

```cpp
void SelectThirdSymmetryPlane(
   System.Object^ PlaneDisp
)
```

### Parameters

- `PlaneDisp`: Third symmetry plane

## VBA Syntax

See [CWTopologySymmetryControl::SelectThirdSymmetryPlane](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologySymmetryControl~SelectThirdSymmetryPlane.html).

## Examples

See the [ICWTopologySymmetryControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl.html) example.

## Remarks

This method is not valid if [ICWTopologySymmetryControl::SelectSymmetryType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl~SelectSymmetryType.html) is set to:

- [swsTopologySymmetryControlOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologySymmetryControlOption_e.html).swsTopologySymmetryControlType_HalfSymmetry

- or -

- [swsTopologySymmetryControlOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologySymmetryControlOption_e.html).swsTopologySymmetryControlType_QuarterSymmetry

## See Also

[ICWTopologySymmetryControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl.html)
[ICWTopologySymmetryControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl_members.html)
[ICWTopologySymmetryControl::ClearSelPlanes Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl~ClearSelPlanes.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
