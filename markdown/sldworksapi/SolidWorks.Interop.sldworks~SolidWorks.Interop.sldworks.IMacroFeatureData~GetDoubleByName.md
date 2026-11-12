---
title: "GetDoubleByName Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "GetDoubleByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetDoubleByName.html"
---

# GetDoubleByName Method (IMacroFeatureData)

Gets a double value by parameter name.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetDoubleByName( _
   ByVal ParamName As System.String, _
   ByRef ParamValue As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim ParamName As System.String
Dim ParamValue As System.Double

instance.GetDoubleByName(ParamName, ParamValue)
```

### C#

```csharp
void GetDoubleByName(
   System.string ParamName,
   out System.double ParamValue
)
```

### C++/CLI

```cpp
void GetDoubleByName(
   System.String^ ParamName,
   [Out] System.double ParamValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ParamName`: Name of the parameter
- `ParamValue`: Double value

## VBA Syntax

See [MacroFeatureData::GetDoubleByName](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~GetDoubleByName.html).

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::SetDoubleByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetDoubleByName.html)
[IMacroFeatureData::GetIntegerByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetIntegerByName.html)
[IMacroFeatureData::GetParameterCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParameterCount.html)
[IMacroFeatureData::GetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParameters.html)
[IMacroFeatureData::IGetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetParameters.html)
[IMacroFeatureData::ISetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetParameters.html)
[IMacroFeatureData::SetIntegerByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetIntegerByName.html)
[IMacroFeatureData::SetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetParameters.html)
[IMacroFeatureData::GetStringByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetStringByName.html)
[IMacroFeatureData::SetStringByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetStringByName.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
