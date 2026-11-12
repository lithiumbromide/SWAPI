---
title: "SelectMidpoint Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SelectMidpoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectMidpoint.html"
---

# SelectMidpoint Method (IModelDoc2)

Puts the midpoint (swSelMIDPOINTS) of that edge on the selection list and removes the edge from the selection list when an edge is selected.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SelectMidpoint()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.SelectMidpoint()
```

### C#

```csharp
void SelectMidpoint()
```

### C++/CLI

```cpp
void SelectMidpoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::SelectMidpoint](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SelectMidpoint.html).

## Examples

[Select the Midpoint of an Edge (VBA)](Put_a_Midpoint_on_an_Edge_Example_VB.htm)
[Select the Midpoint of an Edge (VB.NET)](Put_a_Midpoint_on_an_Edge_Example_VBNET.htm)
[Select the Midpoint of an Edge (C#)](Put_a_Midpoint_on_an_Edge_Example_CSharp.htm)

## Remarks

If the edge whose midpoint is desired is already on the selection list and you use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select it again, then IModelDoc2::SelectMidpoint leaves both the edge and the point on the selection list.

This method does not support 3D sketches.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
