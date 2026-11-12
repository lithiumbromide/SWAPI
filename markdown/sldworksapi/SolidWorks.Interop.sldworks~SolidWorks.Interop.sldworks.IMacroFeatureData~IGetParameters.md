---
title: "IGetParameters Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "IGetParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetParameters.html"
---

# IGetParameters Method (IMacroFeatureData)

Gets the user-defined parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetParameters( _
   ByVal ParamCount As System.Integer, _
   ByRef ParamNames As System.String, _
   ByRef ParamTypes As System.Integer, _
   ByRef ParamValues As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim ParamCount As System.Integer
Dim ParamNames As System.String
Dim ParamTypes As System.Integer
Dim ParamValues As System.String

instance.IGetParameters(ParamCount, ParamNames, ParamTypes, ParamValues)
```

### C#

```csharp
void IGetParameters(
   System.int ParamCount,
   out System.string ParamNames,
   out System.int ParamTypes,
   out System.string ParamValues
)
```

### C++/CLI

```cpp
void IGetParameters(
   System.int ParamCount,
   [Out] System.String^ ParamNames,
   [Out] System.int ParamTypes,
   [Out] System.String^ ParamValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ParamCount`: Number of user-defined parameters
- `ParamNames`: - in-process, unmanaged C++: Pointer to an array of parameter names of size ParamCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `ParamTypes`: - in-process, unmanaged C++: Pointer to an array of parameter data types of size paramCount as defined in [swMacroFeatureParamType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMacroFeatureParamType_e.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `ParamValues`: - in-process, unmanaged C++: Pointer to an array of parameter values of size ParamCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IMacroFeatureData::GetParameterCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~GetParameterCount.html) to determine the size of the arrays.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetDoubleByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetDoubleByName.html)
[IMacroFeatureData::GetIntegerByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetIntegerByName.html)
[IMacroFeatureData::GetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParameters.html)
[IMacroFeatureData::GetStringByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetStringByName.html)
[IMacroFeatureData::ISetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetParameters.html)
[IMacroFeatureData::SetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetParameters.html)
[IMacroFeatureData::SetStringByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetStringByName.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
