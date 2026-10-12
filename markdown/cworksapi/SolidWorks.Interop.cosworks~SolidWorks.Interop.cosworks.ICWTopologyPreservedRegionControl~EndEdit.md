---
title: "EndEdit Method (ICWTopologyPreservedRegionControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyPreservedRegionControl"
member: "EndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl~EndEdit.html"
---

# EndEdit Method (ICWTopologyPreservedRegionControl)

Ends editing this topology study preserved region manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Function EndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyPreservedRegionControl
Dim value As System.Integer

value = instance.EndEdit()
```

### C#

```csharp
System.int EndEdit()
```

### C++/CLI

```cpp
System.int EndEdit();
```

### Return Value

Result code as defined in [swsTopologyStudy_PreservedRegionErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_PreservedRegionErrors_e.html)

## VBA Syntax

See [CWTopologyPreservedRegion::EndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyPreservedRegion~EndEdit.html).

## Examples

See the [ICWTopologyPreservedRegionControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl.html) example.

## Remarks

To begin editing this preserved region control, call [ICWTopologyPreservedRegionControl::BeginEdit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl~BeginEdit.html).

## See Also

[ICWTopologyPreservedRegionControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl.html)
[ICWTopologyPreservedRegionControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
