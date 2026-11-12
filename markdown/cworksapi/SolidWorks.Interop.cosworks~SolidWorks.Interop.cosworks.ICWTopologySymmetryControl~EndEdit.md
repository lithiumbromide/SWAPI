---
title: "EndEdit Method (ICWTopologySymmetryControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologySymmetryControl"
member: "EndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl~EndEdit.html"
---

# EndEdit Method (ICWTopologySymmetryControl)

Ends editing this topology study symmetry manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Function EndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologySymmetryControl
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

Result code as defined in [swsTopologyStudy_SymmetryControlErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_SymmetryControlErrors_e.html)

## VBA Syntax

See [CWTopologySymmetryControl::EndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologySymmetryControl~EndEdit.html).

## Examples

See the [ICWTopologySymmetryControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl.html) example.

## Remarks

To begin editing this symmetry control, call [ICWTopologySymmetryControl::BeginEdit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl~BeginEdit.html).

## See Also

[ICWTopologySymmetryControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl.html)
[ICWTopologySymmetryControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
