---
title: "SelectFirstSymmetryPlane Method (ICWTopologySymmetryControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologySymmetryControl"
member: "SelectFirstSymmetryPlane"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl~SelectFirstSymmetryPlane.html"
---

# SelectFirstSymmetryPlane Method (ICWTopologySymmetryControl)

Sets the first symmetry plane to cut the model into two identical bodies in this topology study symmetry manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SelectFirstSymmetryPlane( _
   ByVal PlaneDisp As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologySymmetryControl
Dim PlaneDisp As System.Object

instance.SelectFirstSymmetryPlane(PlaneDisp)
```

### C#

```csharp
void SelectFirstSymmetryPlane(
   System.object PlaneDisp
)
```

### C++/CLI

```cpp
void SelectFirstSymmetryPlane(
   System.Object^ PlaneDisp
)
```

### Parameters

- `PlaneDisp`: First symmetry plane

## VBA Syntax

See [CWTopologySymmetryControl::SelectFirstSymmetryPlane](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologySymmetryControl~SelectFirstSymmetryPlane.html).

## Examples

See the [ICWTopologySymmetryControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl.html) example.

## See Also

[ICWTopologySymmetryControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl.html)
[ICWTopologySymmetryControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl_members.html)
[ICWTopologySymmetryControl::ClearSelPlanes Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl~ClearSelPlanes.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
