---
title: "GetRoutingUserPreferenceToggle Method (IRoutingSettings)"
project: "SOLIDWORKS API Help"
interface: "IRoutingSettings"
member: "GetRoutingUserPreferenceToggle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetRoutingUserPreferenceToggle.html"
---

# GetRoutingUserPreferenceToggle Method (IRoutingSettings)

Gets whether the specified routing user preference is turned on.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRoutingUserPreferenceToggle( _
   ByVal UserPreferenceToggle As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingSettings
Dim UserPreferenceToggle As System.Integer
Dim value As System.Boolean

value = instance.GetRoutingUserPreferenceToggle(UserPreferenceToggle)
```

### C#

```csharp
System.bool GetRoutingUserPreferenceToggle(
   System.int UserPreferenceToggle
)
```

### C++/CLI

```cpp
System.bool GetRoutingUserPreferenceToggle(
   System.int UserPreferenceToggle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceToggle`: User preference as defined in [swUserPreferenceRoutingToggle_e](ms-its:routingapi.chm::/SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swUserPreferenceRoutingToggle_e.html)

### Return Value

True if on, false if off

## VBA Syntax

See [RoutingSettings::GetRoutingUserPreferenceToggle](ms-its:sldworksapivb6.chm::/sldworks~RoutingSettings~GetRoutingUserPreferenceToggle.html).

## Examples

See the [IRoutingSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.html) examples.

## See Also

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.html)
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.html)
[IRoutingSettings::SetRoutingUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SetRoutingUserPreferenceToggle.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
