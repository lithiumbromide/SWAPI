---
title: "SetDoubleByName Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "SetDoubleByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetDoubleByName.html"
---

# SetDoubleByName Method (IMacroFeatureData)

Sets a double value by parameter name for the macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDoubleByName( _
   ByVal ParamName As System.String, _
   ByVal ParamValue As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim ParamName As System.String
Dim ParamValue As System.Double

instance.SetDoubleByName(ParamName, ParamValue)
```

### C#

```csharp
void SetDoubleByName(
   System.string ParamName,
   System.double ParamValue
)
```

### C++/CLI

```cpp
void SetDoubleByName(
   System.String^ ParamName,
   System.double ParamValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ParamName`: Name of the parameter
- `ParamValue`: New double value

## VBA Syntax

See [MacroFeatureData::SetDoubleByName](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~SetDoubleByName.html).

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetDoubleByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetDoubleByName.html)
[IMacroFeatureData::GetIntegerByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetIntegerByName.html)
[IMacroFeatureData::GetParameterCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParameterCount.html)
[IMacroFeatureData::GetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParameters.html)
[IMacroFeatureData::IGetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetParameters.html)
[IMacroFeatureData::GetStringByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetStringByName.html)
[IMacroFeatureData::ISetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetParameters.html)
[IMacroFeatureData::SetIntegerByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetIntegerByName.html)
[IMacroFeatureData::SetStringByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetStringByName.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
