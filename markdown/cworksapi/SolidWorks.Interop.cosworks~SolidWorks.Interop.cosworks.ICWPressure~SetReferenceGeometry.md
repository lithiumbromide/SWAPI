---
title: "SetReferenceGeometry Method (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "SetReferenceGeometry"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~SetReferenceGeometry.html"
---

# SetReferenceGeometry Method (ICWPressure)

Sets the face, edge, plane, or axis to be used to set the direction of this pressure.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetReferenceGeometry( _
   ByVal RefEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
Dim RefEntity As System.Object

instance.SetReferenceGeometry(RefEntity)
```

### C#

```csharp
void SetReferenceGeometry(
   System.object RefEntity
)
```

### C++/CLI

```cpp
void SetReferenceGeometry(
   System.Object^ RefEntity
)
```

### Parameters

- `RefEntity`: Face, edge, plane, or axis

## VBA Syntax

See [CWPressure::SetReferenceGeometry](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~SetReferenceGeometry.html).

## Remarks

This method is valid only if [ICWPressure::PressureType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~PressureType.html) is [swsPressureType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsPressureType_e.html).swsPressureTypeUseReferenceGeometry.

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)
[ICWPressure::DirectionType Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~DirectionType.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
