---
title: "GetSensorDetails Method (ICWDropTestResultOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestResultOptions"
member: "GetSensorDetails"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestResultOptions~GetSensorDetails.html"
---

# GetSensorDetails Method (ICWDropTestResultOptions)

Gets the simulation data sensor that is used to report work flow sensitive data.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetSensorDetails( _
   ByRef NSensorOption As System.Integer, _
   ByRef SSensorName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestResultOptions
Dim NSensorOption As System.Integer
Dim SSensorName As System.String

instance.GetSensorDetails(NSensorOption, SSensorName)
```

### C#

```csharp
void GetSensorDetails(
   out System.int NSensorOption,
   out System.string SSensorName
)
```

### C++/CLI

```cpp
void GetSensorDetails(
   [Out] System.int NSensorOption,
   [Out] System.String^ SSensorName
)
```

### Parameters

- `NSensorOption`: Sensor option as defined in [swsResultOptionsSensorOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultOptionsSensorOption_e.html)
- `SSensorName`: Sensor name; valid only if NSensorOption = [swsResultOptionsSensorOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultOptionsSensorOption_e.html).swsResultOptionsSensorOption_SpecificSensor

## VBA Syntax

See [CWDropTestResultOptions::GetSensorDetails](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestResultOptions~GetSensorDetails.html).

## See Also

[ICWDropTestResultOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestResultOptions.html)
[ICWDropTestResultOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestResultOptions_members.html)
[ICWDropTestResultOptions::SetSensorDetails Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestResultOptions~SetSensorDetails.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
