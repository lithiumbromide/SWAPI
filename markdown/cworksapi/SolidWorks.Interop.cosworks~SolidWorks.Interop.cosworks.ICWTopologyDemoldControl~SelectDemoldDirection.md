---
title: "SelectDemoldDirection Method (ICWTopologyDemoldControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDemoldControl"
member: "SelectDemoldDirection"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SelectDemoldDirection.html"
---

# SelectDemoldDirection Method (ICWTopologyDemoldControl)

Sets the de-mold direction of this topology study de-mold manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SelectDemoldDirection( _
   ByVal NDir As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDemoldControl
Dim NDir As System.Integer

instance.SelectDemoldDirection(NDir)
```

### C#

```csharp
void SelectDemoldDirection(
   System.int NDir
)
```

### C++/CLI

```cpp
void SelectDemoldDirection(
   System.int NDir
)
```

### Parameters

- `NDir`: De-mold direction as defined in [swsTopologyDemoldDirectionOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyDemoldDirectionOption_e.html)

## VBA Syntax

See [CWTopologyDemoldControl::SelectDemoldDirection](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDemoldControl~SelectDemoldDirection.html).

## Examples

See the [ICWTopologyDemoldControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl.html) example.

## See Also

[ICWTopologyDemoldControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl.html)
[ICWTopologyDemoldControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
