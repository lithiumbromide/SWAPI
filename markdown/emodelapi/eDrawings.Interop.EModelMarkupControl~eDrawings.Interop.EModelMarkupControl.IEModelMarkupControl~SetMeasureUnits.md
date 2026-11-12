---
title: "SetMeasureUnits Method (IEModelMarkupControl)"
project: "eDrawings API Help"
interface: "IEModelMarkupControl"
member: "SetMeasureUnits"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~SetMeasureUnits.html"
---

# SetMeasureUnits Method (IEModelMarkupControl)

Sets measurement units.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMeasureUnits( _
   ByVal DistanceUnit As EMVDistanceUnit, _
   ByVal AngleUnit As EMVAngleUnit _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelMarkupControl
Dim DistanceUnit As EMVDistanceUnit
Dim AngleUnit As EMVAngleUnit

instance.SetMeasureUnits(DistanceUnit, AngleUnit)
```

### C#

```csharp
void SetMeasureUnits(
   EMVDistanceUnit DistanceUnit,
   EMVAngleUnit AngleUnit
)
```

### C++/CLI

```cpp
void SetMeasureUnits(
   EMVDistanceUnit DistanceUnit,
   EMVAngleUnit AngleUnit
)
```

### Parameters

- `DistanceUnit`: Distance unit as defined in [EMVDistanceUnit](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.EMVDistanceUnit.html)
- `AngleUnit`: Angle unit as defined in [EMVAngleUnit](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.EMVAngleUnit.html)

## VBA Syntax

See [EModelMarkupControl::SetMeasureUnits](ms-its:emodelapivb6.chm::/EModelViewMarkup~EModelMarkupControl~SetMeasureUnits.html).

## See Also

[IEModelMarkupControl Interface](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl.html)
[IEModelMarkupControl Members](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl_members.html)

## Availability

eDrawings API 2017 SP3
