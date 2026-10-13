---
title: "SetRoutingUserPreferenceToggle Method (IRoutingSettings)"
project: "SOLIDWORKS API Help"
interface: "IRoutingSettings"
member: "SetRoutingUserPreferenceToggle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SetRoutingUserPreferenceToggle.html"
---

# SetRoutingUserPreferenceToggle Method (IRoutingSettings)

Sets whether the specified routing user preference is turned on or off.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetRoutingUserPreferenceToggle( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal OnFlag As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingSettings
Dim UserPreferenceValue As System.Integer
Dim OnFlag As System.Boolean

instance.SetRoutingUserPreferenceToggle(UserPreferenceValue, OnFlag)
```

### C#

```csharp
void SetRoutingUserPreferenceToggle(
   System.int UserPreferenceValue,
   System.bool OnFlag
)
```

### C++/CLI

```cpp
void SetRoutingUserPreferenceToggle(
   System.int UserPreferenceValue,
   System.bool OnFlag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`: User preference as defined in [swUserPreferenceRoutingToggle_e](ms-its:routingapi.chm::/SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swUserPreferenceRoutingToggle_e.html)
- `OnFlag`: True to turn on, false to turn off

## VBA Syntax

See [RoutingSettings::SetRoutingUserPreferenceToggle](ms-its:sldworksapivb6.chm::/sldworks~RoutingSettings~SetRoutingUserPreferenceToggle.html).

## See Also

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.html)
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.html)
[IRoutingSettings::GetRoutingUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetRoutingUserPreferenceToggle.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
