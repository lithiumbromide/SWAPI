---
title: "GetStringByName Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "GetStringByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetStringByName.html"
---

# GetStringByName Method (IMacroFeatureData)

Gets a string value by the name of the parameter for the macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetStringByName( _
   ByVal ParamName As System.String, _
   ByRef ParamValue As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim ParamName As System.String
Dim ParamValue As System.String

instance.GetStringByName(ParamName, ParamValue)
```

### C#

```csharp
void GetStringByName(
   System.string ParamName,
   out System.string ParamValue
)
```

### C++/CLI

```cpp
void GetStringByName(
   System.String^ ParamName,
   [Out] System.String^ ParamValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ParamName`: Name of the parameter
- `ParamValue`: String value

## VBA Syntax

See [MacroFeatureData::GetStringByName](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~GetStringByName.html).

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetDoubleByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetDoubleByName.html)
[IMacroFeatureData::GetIntegerByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetIntegerByName.html)
[IMacroFeatureData::GetParameterCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParameterCount.html)
[IMacroFeatureData::GetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParameters.html)
[IMacroFeatureData::IGetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetParameters.html)
[IMacroFeatureData::SetDoubleByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetDoubleByName.html)
[IMacroFeatureData::SetIntegerByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetIntegerByName.html)
[IMacroFeatureData::SetStringByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetStringByName.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
