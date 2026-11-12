---
title: "GetCoordinateSystem Method (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "GetCoordinateSystem"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~GetCoordinateSystem.html"
---

# GetCoordinateSystem Method (ICWPressure)

Gets the coordinate system that defines this nonuniform pressure.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCoordinateSystem() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
Dim value As System.Object

value = instance.GetCoordinateSystem()
```

### C#

```csharp
System.object GetCoordinateSystem()
```

### C++/CLI

```cpp
System.Object^ GetCoordinateSystem();
```

### Return Value

Coordinate system

## VBA Syntax

See [CWPressure::GetCoordinateSystem](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~GetCoordinateSystem.html).

## Remarks

This method is valid only if [ICWPressure::IncludeNonUniformDistribution](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~IncludeNonUniformDistribution.html) is set to true.

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)
[ICWPressure::SetCoordinateSystem Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~SetCoordinateSystem.html)
[ICWPressure::CoordSystemType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~CoordSystemType.html)
[ICWPressure::Equation Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~Equation.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
