---
title: "GetRoutingUserPreferenceIntegerValue Method (IRoutingSettings)"
project: "SOLIDWORKS API Help"
interface: "IRoutingSettings"
member: "GetRoutingUserPreferenceIntegerValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetRoutingUserPreferenceIntegerValue.html"
---

# GetRoutingUserPreferenceIntegerValue Method (IRoutingSettings)

Gets the integer value of the specified routing user preference.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRoutingUserPreferenceIntegerValue( _
   ByVal UserPreferenceValue As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingSettings
Dim UserPreferenceValue As System.Integer
Dim value As System.Integer

value = instance.GetRoutingUserPreferenceIntegerValue(UserPreferenceValue)
```

### C#

```csharp
System.int GetRoutingUserPreferenceIntegerValue(
   System.int UserPreferenceValue
)
```

### C++/CLI

```cpp
System.int GetRoutingUserPreferenceIntegerValue(
   System.int UserPreferenceValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`: User preference as defined in [swUserPreferenceRoutingInteger_e](ms-its:routingapi.chm::/SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swUserPreferenceRoutingInteger_e.html)

### Return Value

User preference

## VBA Syntax

See [RoutingSettings::GetRoutingUserPreferenceIntegerValue](ms-its:sldworksapivb6.chm::/sldworks~RoutingSettings~GetRoutingUserPreferenceIntegerValue.html).

## Examples

See the [IRoutingSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.html) examples.

## See Also

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.html)
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.html)
[IRoutingSettings::GetRoutingUserPreferenceIntegerValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetRoutingUserPreferenceIntegerValue.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
