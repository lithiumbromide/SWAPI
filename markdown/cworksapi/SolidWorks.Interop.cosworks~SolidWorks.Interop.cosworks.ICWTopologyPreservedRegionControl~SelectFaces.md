---
title: "SelectFaces Method (ICWTopologyPreservedRegionControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyPreservedRegionControl"
member: "SelectFaces"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl~SelectFaces.html"
---

# SelectFaces Method (ICWTopologyPreservedRegionControl)

Adds the specified faces to the selection list for this topology study preserved region manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectFaces( _
   ByVal ArraySelFaces As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyPreservedRegionControl
Dim ArraySelFaces As System.Object
Dim value As System.Integer

value = instance.SelectFaces(ArraySelFaces)
```

### C#

```csharp
System.int SelectFaces(
   System.object ArraySelFaces
)
```

### C++/CLI

```cpp
System.int SelectFaces(
   System.Object^ ArraySelFaces
)
```

### Parameters

- `ArraySelFaces`: Array of selected faces

### Return Value

Result code as defined in [swsTopologyStudy_PreservedRegionErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_PreservedRegionErrors_e.html)

## VBA Syntax

See [CWTopologyPreservedRegion::SelectFaces](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyPreservedRegion~SelectFaces.html).

## Examples

See the [ICWTopologyPreservedRegionControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl.html) example.

## See Also

[ICWTopologyPreservedRegionControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl.html)
[ICWTopologyPreservedRegionControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl_members.html)
[ICWTopologyPreservedRegionControl::RemoveAllSelections Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl~RemoveAllSelections.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
