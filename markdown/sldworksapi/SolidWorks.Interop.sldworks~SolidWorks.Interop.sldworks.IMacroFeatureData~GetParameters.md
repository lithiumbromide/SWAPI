---
title: "GetParameters Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "GetParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParameters.html"
---

# GetParameters Method (IMacroFeatureData)

Gets the user-defined parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetParameters( _
   ByRef ParamNames As System.Object, _
   ByRef ParamTypes As System.Object, _
   ByRef ParamValues As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim ParamNames As System.Object
Dim ParamTypes As System.Object
Dim ParamValues As System.Object

instance.GetParameters(ParamNames, ParamTypes, ParamValues)
```

### C#

```csharp
void GetParameters(
   out System.object ParamNames,
   out System.object ParamTypes,
   out System.object ParamValues
)
```

### C++/CLI

```cpp
void GetParameters(
   [Out] System.Object^ ParamNames,
   [Out] System.Object^ ParamTypes,
   [Out] System.Object^ ParamValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ParamNames`: Array of parameter names
- `ParamTypes`: Array of parameter data types as defined in [swMacroFeatureParamType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMacroFeatureParamType_e.html)
- `ParamValues`: Array of the parameter values

## VBA Syntax

See [MacroFeatureData::GetParameters](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~GetParameters.html).

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetDoubleByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetDoubleByName.html)
[IMacroFeatureData::GetIntegerByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetIntegerByName.html)
[IMacroFeatureData::GetParameterCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParameterCount.html)
[IMacroFeatureData::GetStringByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetStringByName.html)
[IMacroFeatureData::IGetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetParameters.html)
[IMacroFeatureData::ISetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetParameters.html)
[IMacroFeatureData::SetDoubleByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetDoubleByName.html)
[IMacroFeatureData::SetIntegerByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetIntegerByName.html)
[IMacroFeatureData::SetStringByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetStringByName.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
