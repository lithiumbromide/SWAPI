---
title: "AddRefGeometry Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "AddRefGeometry"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~AddRefGeometry.html"
---

# AddRefGeometry Method (ICWPlot)

Specifies the reference geometry for directional component plots.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddRefGeometry( _
   ByVal NDispType As System.Integer, _
   ByVal DispPlaneAxisCoordSys As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim NDispType As System.Integer
Dim DispPlaneAxisCoordSys As System.Object
Dim value As System.Integer

value = instance.AddRefGeometry(NDispType, DispPlaneAxisCoordSys)
```

### C#

```csharp
System.int AddRefGeometry(
   System.int NDispType,
   System.object DispPlaneAxisCoordSys
)
```

### C++/CLI

```cpp
System.int AddRefGeometry(
   System.int NDispType,
   System.Object^ DispPlaneAxisCoordSys
)
```

### Parameters

- `NDispType`: Type of reference geometry as defined in [swsRefDispType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRefDispType_e.html)
- `DispPlaneAxisCoordSys`: Plane, axis, or coordinate system

### Return Value

Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::AddRefGeometry](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~AddRefGeometry.html).

## Remarks

This method is valid only for the following directional component plots:

- Displacement
- Mode Shape/Amplitude
- Strain
- Stress
- Thermal

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
