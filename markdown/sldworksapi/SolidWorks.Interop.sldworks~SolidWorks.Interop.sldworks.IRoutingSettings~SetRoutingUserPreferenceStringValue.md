---
title: "SetRoutingUserPreferenceStringValue Method (IRoutingSettings)"
project: "SOLIDWORKS API Help"
interface: "IRoutingSettings"
member: "SetRoutingUserPreferenceStringValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SetRoutingUserPreferenceStringValue.html"
---

# SetRoutingUserPreferenceStringValue Method (IRoutingSettings)

Sets a string value for the specified routing user preference.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetRoutingUserPreferenceStringValue( _
   ByVal UserPreference As System.Integer, _
   ByVal Value As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingSettings
Dim UserPreference As System.Integer
Dim Value As System.String
Dim value As System.Boolean

value = instance.SetRoutingUserPreferenceStringValue(UserPreference, Value)
```

### C#

```csharp
System.bool SetRoutingUserPreferenceStringValue(
   System.int UserPreference,
   System.string Value
)
```

### C++/CLI

```cpp
System.bool SetRoutingUserPreferenceStringValue(
   System.int UserPreference,
   System.String^ Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreference`: User preference as defined in [swUserPreferenceRoutingFileLocations_e](ms-its:routingapi.chm::/SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swUserPreferenceRoutingFileLocations_e.html)
- `Value`: String value of the specified user preference

### Return Value

True if successful, false if not

## VBA Syntax

See [RoutingSettings::SetRoutingUserPreferenceStringValue](ms-its:sldworksapivb6.chm::/sldworks~RoutingSettings~SetRoutingUserPreferenceStringValue.html).

## See Also

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.html)
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.html)
[IRoutingSettings::GetRoutingUserPreferenceStringValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetRoutingUserPreferenceStringValue.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
