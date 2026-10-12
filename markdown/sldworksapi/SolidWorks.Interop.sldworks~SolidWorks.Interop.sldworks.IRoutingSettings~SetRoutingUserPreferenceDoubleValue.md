---
title: "SetRoutingUserPreferenceDoubleValue Method (IRoutingSettings)"
project: "SOLIDWORKS API Help"
interface: "IRoutingSettings"
member: "SetRoutingUserPreferenceDoubleValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SetRoutingUserPreferenceDoubleValue.html"
---

# SetRoutingUserPreferenceDoubleValue Method (IRoutingSettings)

Sets a double value for the specified routing user preference.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetRoutingUserPreferenceDoubleValue( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal Value As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingSettings
Dim UserPreferenceValue As System.Integer
Dim Value As System.Double
Dim value As System.Boolean

value = instance.SetRoutingUserPreferenceDoubleValue(UserPreferenceValue, Value)
```

### C#

```csharp
System.bool SetRoutingUserPreferenceDoubleValue(
   System.int UserPreferenceValue,
   System.double Value
)
```

### C++/CLI

```cpp
System.bool SetRoutingUserPreferenceDoubleValue(
   System.int UserPreferenceValue,
   System.double Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`: User preference as defined in [swUserPreferenceRoutingDouble_e](ms-its:routingapi.chm::/SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swUserPreferenceRoutingDouble_e.html)
- `Value`: Double value of the specified user preference

### Return Value

True if successful, false if not

## VBA Syntax

See [RoutingSettings::SetRoutingUserPreferenceDoubleValue](ms-its:sldworksapivb6.chm::/sldworks~RoutingSettings~SetRoutingUserPreferenceDoubleValue.html).

## See Also

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.html)
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.html)
[IRoutingSettings::GetRoutingUserPreferenceDoubleValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetRoutingUserPreferenceDoubleValue.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
