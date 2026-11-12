---
title: "GetDisplayStateBodyProperties Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetDisplayStateBodyProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateBodyProperties.html"
---

# GetDisplayStateBodyProperties Method (IConfiguration)

Gets the bodies and their material properties in the specified display state.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayStateBodyProperties( _
   ByVal DisplayStateName As System.String, _
   ByRef Bodies As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim DisplayStateName As System.String
Dim Bodies As System.Object
Dim value As System.Object

value = instance.GetDisplayStateBodyProperties(DisplayStateName, Bodies)
```

### C#

```csharp
System.object GetDisplayStateBodyProperties(
   System.string DisplayStateName,
   out System.object Bodies
)
```

### C++/CLI

```cpp
System.Object^ GetDisplayStateBodyProperties(
   System.String^ DisplayStateName,
   [Out] System.Object^ Bodies
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DisplayStateName`: Name of the display state
- `Bodies`: Array of [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html) objects

### Return Value

Array of body properties (see **Remarks**)

## VBA Syntax

See [Configuration::GetDisplayStateBodyProperties](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetDisplayStateBodyProperties.html).

## Remarks

The material values returned include the face color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission. Valid values are from 0 to 1 for all variables.

If the return value is -1 values, then material property values are not assigned to the feature.

The format of the return value is an array of doubles as follows:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::GetDisplayStateComponentProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateComponentProperties.html)
[IConfiguration::GetDisplayStateComponentVisibility Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateComponentVisibility.html)
[IConfiguration::GetDisplayStateFaceProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateFaceProperties.html)
[IConfiguration::GetDisplayStateFeatureProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateFeatureProperties.html)
[IConfiguration::GetDisplayStateProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateProperties.html)
[IConfiguration::GetDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.html)
[IConfiguration::GetDisplayStatesCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStatesCount.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
