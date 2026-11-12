---
title: "SelectSymmetryType Method (ICWTopologySymmetryControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologySymmetryControl"
member: "SelectSymmetryType"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl~SelectSymmetryType.html"
---

# SelectSymmetryType Method (ICWTopologySymmetryControl)

Sets the type of symmetry in this topology study symmetry manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SelectSymmetryType( _
   ByVal NType As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologySymmetryControl
Dim NType As System.Integer

instance.SelectSymmetryType(NType)
```

### C#

```csharp
void SelectSymmetryType(
   System.int NType
)
```

### C++/CLI

```cpp
void SelectSymmetryType(
   System.int NType
)
```

### Parameters

- `NType`: Type of symmetry as defined in [swsTopologySymmetryControlOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologySymmetryControlOption_e.html)

## VBA Syntax

See [CWTopologySymmetryControl::SelectSymmetryType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologySymmetryControl~SelectSymmetryType.html).

## Examples

See the [ICWTopologySymmetryControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl.html) example.

## See Also

[ICWTopologySymmetryControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl.html)
[ICWTopologySymmetryControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
