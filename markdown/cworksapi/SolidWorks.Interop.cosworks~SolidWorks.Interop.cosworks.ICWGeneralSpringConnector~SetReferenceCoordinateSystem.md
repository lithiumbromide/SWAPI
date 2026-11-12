---
title: "SetReferenceCoordinateSystem Method (ICWGeneralSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGeneralSpringConnector"
member: "SetReferenceCoordinateSystem"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~SetReferenceCoordinateSystem.html"
---

# SetReferenceCoordinateSystem Method (ICWGeneralSpringConnector)

Sets the reference coordinate system for this general spring connector.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetReferenceCoordinateSystem( _
   ByVal DispRefEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGeneralSpringConnector
Dim DispRefEntity As System.Object

instance.SetReferenceCoordinateSystem(DispRefEntity)
```

### C#

```csharp
void SetReferenceCoordinateSystem(
   System.object DispRefEntity
)
```

### C++/CLI

```cpp
void SetReferenceCoordinateSystem(
   System.Object^ DispRefEntity
)
```

### Parameters

- `DispRefEntity`: Reference coordinate system

## VBA Syntax

See [CWGeneralSpringConnector::SetReferenceCoordinateSystem](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGeneralSpringConnector~SetReferenceCoordinateSystem.html).

## Examples

See the [ICWGeneralSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html) examples.

## Remarks

If only [ICWGeneralSpringConnector::TorsionalStiffnessValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~TorsionalStiffnessValue.html) or [ICWGeneralSpringConnector::AxialStiffnessValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~AxialStiffnessValue.html) are non-zero, then calling this method is not necessary.

If the x-axis of the coordinate system is not the same as the default axial direction as defined by a point on each spring connector surface, then the x-axis of the coordinate system is used as the default axial direction.

## See Also

[ICWGeneralSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html)
[ICWGeneralSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2025 SP0
