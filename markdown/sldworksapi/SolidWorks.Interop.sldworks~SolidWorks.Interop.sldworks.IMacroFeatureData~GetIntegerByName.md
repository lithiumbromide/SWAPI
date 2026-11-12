---
title: "GetIntegerByName Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "GetIntegerByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetIntegerByName.html"
---

# GetIntegerByName Method (IMacroFeatureData)

Gets an integer value by parameter name.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetIntegerByName( _
   ByVal ParamName As System.String, _
   ByRef ParamValue As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim ParamName As System.String
Dim ParamValue As System.Integer

instance.GetIntegerByName(ParamName, ParamValue)
```

### C#

```csharp
void GetIntegerByName(
   System.string ParamName,
   out System.int ParamValue
)
```

### C++/CLI

```cpp
void GetIntegerByName(
   System.String^ ParamName,
   [Out] System.int ParamValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ParamName`: Name of the parameter
- `ParamValue`: Integer value

## VBA Syntax

See [MacroFeatureData::GetIntegerByName](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~GetIntegerByName.html).

## Examples

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetDoubleByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetDoubleByName.html)
[IMacroFeatureData::GetParameterCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParameterCount.html)
[IMacroFeatureData::GetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParameters.html)
[IMacroFeatureData::IGetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetParameters.html)
[IMacroFeatureData::ISetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetParameters.html)
[IMacroFeatureData::SetDoubleByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetDoubleByName.html)
[IMacroFeatureData::SetIntegerByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetIntegerByName.html)
[IMacroFeatureData::SetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetParameters.html)
[IMacroFeatureData::GetStringByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetStringByName.html)
[IMacroFeatureData::SetStringByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetStringByName.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
