---
title: "SetCoordinateSystem Method (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "SetCoordinateSystem"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~SetCoordinateSystem.html"
---

# SetCoordinateSystem Method (ICWPressure)

Sets the coordinate system that defines this nonuniform pressure.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCoordinateSystem( _
   ByVal DispCoordinateSystem As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
Dim DispCoordinateSystem As System.Object

instance.SetCoordinateSystem(DispCoordinateSystem)
```

### C#

```csharp
void SetCoordinateSystem(
   System.object DispCoordinateSystem
)
```

### C++/CLI

```cpp
void SetCoordinateSystem(
   System.Object^ DispCoordinateSystem
)
```

### Parameters

- `DispCoordinateSystem`: Coordinate system

## VBA Syntax

See [CWPressure::SetCoordinateSystem](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~SetCoordinateSystem.html).

## Examples

See the [ICWPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html) examples.

## Remarks

This method is valid only if [ICWPressure::IncludeNonUniformDistribution](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~IncludeNonUniformDistribution.html) is set to true.

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)
[ICWPressure::GetCoordinateSystem Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~GetCoordinateSystem.html)
[ICWPressure::CoordSystemType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~CoordSystemType.html)
[ICWPressure::Equation Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~Equation.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
