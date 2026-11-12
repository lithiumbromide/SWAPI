---
title: "EndEdit Method (ICWTopologyThicknessControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyThicknessControl"
member: "EndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl~EndEdit.html"
---

# EndEdit Method (ICWTopologyThicknessControl)

Ends editing this topology study thickness manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Function EndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyThicknessControl
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

Result code as defined in [swsTopologyStudy_ThicknessControlErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_ThicknessControlErrors_e.html)

## VBA Syntax

See [CWTopologyThicknessControl::EndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyThicknessControl~EndEdit.html).

## Examples

See the [ICWTopologyThicknessControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html) example.

## Remarks

To begin editing this thickness control, call [ICWTopologyThicknessControl::BeginEdit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl~BeginEdit.html).

## See Also

[ICWTopologyThicknessControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html)
[ICWTopologyThicknessControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
