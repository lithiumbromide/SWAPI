---
title: "GetDisplayStateFeatureProperties Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetDisplayStateFeatureProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateFeatureProperties.html"
---

# GetDisplayStateFeatureProperties Method (IConfiguration)

Gets the features and their material properties in the specified display state.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayStateFeatureProperties( _
   ByVal DisplayStateName As System.String, _
   ByRef Features As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim DisplayStateName As System.String
Dim Features As System.Object
Dim value As System.Object

value = instance.GetDisplayStateFeatureProperties(DisplayStateName, Features)
```

### C#

```csharp
System.object GetDisplayStateFeatureProperties(
   System.string DisplayStateName,
   out System.object Features
)
```

### C++/CLI

```cpp
System.Object^ GetDisplayStateFeatureProperties(
   System.String^ DisplayStateName,
   [Out] System.Object^ Features
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DisplayStateName`: Name of the display state
- `Features`: Array of [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html) objects

### Return Value

Array of feature properties (see **Remarks**)

## VBA Syntax

See [Configuration::GetDisplayStateFeatureProperties](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetDisplayStateFeatureProperties.html).

## Remarks

The material values returned include the face color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission. Valid values are from 0 to 1 for all variables.

If the return value is all -1 values, then material property values are not assigned to the feature.

The format of return value is an array of doubles as follows:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::GetDisplayStateBodyProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateBodyProperties.html)
[IConfiguration::GetDisplayStateComponentProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateComponentProperties.html)
[IConfiguration::GetDisplayStateComponentVisibility Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateComponentVisibility.html)
[IConfiguration::GetDisplayStateFaceProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateFaceProperties.html)
[IConfiguration::GetDisplayStateProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateProperties.html)
[IConfiguration::GetDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.html)
[IConfiguration::GetDisplayStatesCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStatesCount.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
