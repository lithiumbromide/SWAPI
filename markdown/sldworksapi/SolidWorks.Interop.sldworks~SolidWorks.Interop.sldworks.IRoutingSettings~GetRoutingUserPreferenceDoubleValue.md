---
title: "GetRoutingUserPreferenceDoubleValue Method (IRoutingSettings)"
project: "SOLIDWORKS API Help"
interface: "IRoutingSettings"
member: "GetRoutingUserPreferenceDoubleValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetRoutingUserPreferenceDoubleValue.html"
---

# GetRoutingUserPreferenceDoubleValue Method (IRoutingSettings)

Gets the double value of the specified routing user preference.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRoutingUserPreferenceDoubleValue( _
   ByVal UserPreferenceValue As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingSettings
Dim UserPreferenceValue As System.Integer
Dim value As System.Double

value = instance.GetRoutingUserPreferenceDoubleValue(UserPreferenceValue)
```

### C#

```csharp
System.double GetRoutingUserPreferenceDoubleValue(
   System.int UserPreferenceValue
)
```

### C++/CLI

```cpp
System.double GetRoutingUserPreferenceDoubleValue(
   System.int UserPreferenceValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`: User preference as defined in [swUserPreferenceRoutingDouble_e](ms-its:routingapi.chm::/SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swUserPreferenceRoutingDouble_e.html)

### Return Value

User preference

## VBA Syntax

See [RoutingSettings::GetRoutingUserPreferenceDoubleValue](ms-its:sldworksapivb6.chm::/sldworks~RoutingSettings~GetRoutingUserPreferenceDoubleValue.html).

## Examples

See the [IRoutingSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.html) examples.

## See Also

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.html)
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.html)
[IRoutingSettings::SetRoutingUserPreferenceDoubleValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SetRoutingUserPreferenceDoubleValue.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
