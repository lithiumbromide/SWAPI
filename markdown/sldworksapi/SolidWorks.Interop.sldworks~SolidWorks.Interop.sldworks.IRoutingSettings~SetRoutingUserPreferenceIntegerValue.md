---
title: "SetRoutingUserPreferenceIntegerValue Method (IRoutingSettings)"
project: "SOLIDWORKS API Help"
interface: "IRoutingSettings"
member: "SetRoutingUserPreferenceIntegerValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SetRoutingUserPreferenceIntegerValue.html"
---

# SetRoutingUserPreferenceIntegerValue Method (IRoutingSettings)

Sets an integer value for the specified routing user preference.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetRoutingUserPreferenceIntegerValue( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal Value As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingSettings
Dim UserPreferenceValue As System.Integer
Dim Value As System.Integer
Dim value As System.Boolean

value = instance.SetRoutingUserPreferenceIntegerValue(UserPreferenceValue, Value)
```

### C#

```csharp
System.bool SetRoutingUserPreferenceIntegerValue(
   System.int UserPreferenceValue,
   System.int Value
)
```

### C++/CLI

```cpp
System.bool SetRoutingUserPreferenceIntegerValue(
   System.int UserPreferenceValue,
   System.int Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`: User preference as defined in [swUserPreferenceRoutingInteger_e](ms-its:routingapi.chm::/SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swUserPreferenceRoutingInteger_e.html)
- `Value`: Integer value of the specified user preference

### Return Value

True if successful, false if not

## VBA Syntax

See [RoutingSettings::SetRoutingUserPreferenceIntegerValue](ms-its:sldworksapivb6.chm::/sldworks~RoutingSettings~SetRoutingUserPreferenceIntegerValue.html).

## See Also

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.html)
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.html)
[IRoutingSettings::GetRoutingUserPreferenceIntegerValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetRoutingUserPreferenceIntegerValue.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
