---
title: "GetRoutingUserPreferenceStringValue Method (IRoutingSettings)"
project: "SOLIDWORKS API Help"
interface: "IRoutingSettings"
member: "GetRoutingUserPreferenceStringValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetRoutingUserPreferenceStringValue.html"
---

# GetRoutingUserPreferenceStringValue Method (IRoutingSettings)

Gets the string value of the specified routing user preference.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRoutingUserPreferenceStringValue( _
   ByVal UserPreference As System.Integer, _
   ByVal UseDefaultVal As System.Boolean _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingSettings
Dim UserPreference As System.Integer
Dim UseDefaultVal As System.Boolean
Dim value As System.String

value = instance.GetRoutingUserPreferenceStringValue(UserPreference, UseDefaultVal)
```

### C#

```csharp
System.string GetRoutingUserPreferenceStringValue(
   System.int UserPreference,
   System.bool UseDefaultVal
)
```

### C++/CLI

```cpp
System.String^ GetRoutingUserPreferenceStringValue(
   System.int UserPreference,
   System.bool UseDefaultVal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreference`: User preference as defined in [swUserPreferenceRoutingFileLocations_e](ms-its:routingapi.chm::/SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swUserPreferenceRoutingFileLocations_e.html)
- `UseDefaultVal`: True to use the default, false to not

### Return Value

User preference

## VBA Syntax

See [RoutingSettings::GetRoutingUserPreferenceStringValue](ms-its:sldworksapivb6.chm::/sldworks~RoutingSettings~GetRoutingUserPreferenceStringValue.html).

## Examples

See the [IRoutingSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.html) examples.

## See Also

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.html)
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.html)
[IRoutingSettings::SetRoutingUserPreferenceStringValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SetRoutingUserPreferenceStringValue.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
