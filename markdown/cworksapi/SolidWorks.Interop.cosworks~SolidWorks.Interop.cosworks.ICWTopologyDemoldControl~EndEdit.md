---
title: "EndEdit Method (ICWTopologyDemoldControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDemoldControl"
member: "EndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~EndEdit.html"
---

# EndEdit Method (ICWTopologyDemoldControl)

Ends editing this topology study de-mold manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Function EndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDemoldControl
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

Result code as defined in [swsTopologyStudy_DemoldControlErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_DemoldControlErrors_e.html)

## VBA Syntax

See [CWTopologyDemoldControl::EndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDemoldControl~EndEdit.html).

## Examples

See the [ICWTopologyDemoldControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl.html) example.

## Remarks

To begin editing this de-mold control, call [ICWTopologyDemoldControl::BeginEdit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~BeginEdit.html).

## See Also

[ICWTopologyDemoldControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl.html)
[ICWTopologyDemoldControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
