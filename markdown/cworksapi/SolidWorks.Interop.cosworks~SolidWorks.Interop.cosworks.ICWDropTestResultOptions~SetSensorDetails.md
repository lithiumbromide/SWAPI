---
title: "SetSensorDetails Method (ICWDropTestResultOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestResultOptions"
member: "SetSensorDetails"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestResultOptions~SetSensorDetails.html"
---

# SetSensorDetails Method (ICWDropTestResultOptions)

Sets the simulation data sensor that is used to report work flow sensitive data.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSensorDetails( _
   ByVal NSensorOption As System.Integer, _
   ByVal SSensorName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestResultOptions
Dim NSensorOption As System.Integer
Dim SSensorName As System.String

instance.SetSensorDetails(NSensorOption, SSensorName)
```

### C#

```csharp
void SetSensorDetails(
   System.int NSensorOption,
   System.string SSensorName
)
```

### C++/CLI

```cpp
void SetSensorDetails(
   System.int NSensorOption,
   System.String^ SSensorName
)
```

### Parameters

- `NSensorOption`: Sensor option as defined in [swsResultOptionsSensorOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultOptionsSensorOption_e.html)
- `SSensorName`: Sensor name; valid only if NSensorOption = [swsResultOptionsSensorOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultOptionsSensorOption_e.html).swsResultOptionsSensorOption_SpecificSensor

## VBA Syntax

See [CWDropTestResultOptions::SetSensorDetails](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestResultOptions~SetSensorDetails.html).

## See Also

[ICWDropTestResultOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestResultOptions.html)
[ICWDropTestResultOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestResultOptions_members.html)
[ICWDropTestResultOptions::GetSensorDetails Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestResultOptions~GetSensorDetails.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
