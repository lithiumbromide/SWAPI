---
title: "ShowPlotOnSelEntities Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "ShowPlotOnSelEntities"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~ShowPlotOnSelEntities.html"
---

# ShowPlotOnSelEntities Method (ICWPlot)

Sets whether to display this plot only for selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowPlotOnSelEntities( _
   ByVal BSelFaceOnly As System.Boolean, _
   ByVal ArraySelectedEntities As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim BSelFaceOnly As System.Boolean
Dim ArraySelectedEntities As System.Object
Dim value As System.Integer

value = instance.ShowPlotOnSelEntities(BSelFaceOnly, ArraySelectedEntities)
```

### C#

```csharp
System.int ShowPlotOnSelEntities(
   System.bool BSelFaceOnly,
   System.object ArraySelectedEntities
)
```

### C++/CLI

```cpp
System.int ShowPlotOnSelEntities(
   System.bool BSelFaceOnly,
   System.Object^ ArraySelectedEntities
)
```

### Parameters

- `BSelFaceOnly`: True to display plot only for ArraySelectedEntities, false to display plot for all entities
- `ArraySelectedEntities`: Array of selected faces and bodies; valid only if BSelFaceOnly is true

### Return Value

Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::ShowPlotOnSelEntities](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~ShowPlotOnSelEntities.html).

## Examples

See the [ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html) examples.

## Remarks

This method is valid for the following plots only if [ICWPlot::ShowShellin3D](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~ShowShellin3D.html) and [ICWPlot::ShowTensorOrVector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~ShowTensorOrVector.html) are both false:

- Acceleration
- Displacement
- Mode shape/amplitude
- Strain
- Stress
- Velocity

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
