---
title: "SetOverrideDefaultParameter Method (ISheetMetalFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFeatureData"
member: "SetOverrideDefaultParameter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetOverrideDefaultParameter.html"
---

# SetOverrideDefaultParameter Method (ISheetMetalFeatureData)

Obsolete. Superseded by [ISheetMetalFeatureData::SetOverrideDefaultParameter2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetOverrideDefaultParameter2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetOverrideDefaultParameter( _
   ByVal OverrideDefaultParameter As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalFeatureData
Dim OverrideDefaultParameter As System.Boolean
Dim value As System.Integer

value = instance.SetOverrideDefaultParameter(OverrideDefaultParameter)
```

### C#

```csharp
System.int SetOverrideDefaultParameter(
   System.bool OverrideDefaultParameter
)
```

### C++/CLI

```cpp
System.int SetOverrideDefaultParameter(
   System.bool OverrideDefaultParameter
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OverrideDefaultParameter`: True to override the default parameters, false to not

### Return Value

Result code as defined in [swSheetMetalModifierError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalModifierError_e.html)

## VBA Syntax

See [SheetMetalFeatureData::SetOverrideDefaultParameter](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalFeatureData~SetOverrideDefaultParameter.html).

## See Also

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.html)
[ISheetMetalFeatureData::GetOverrideDefaultParameter Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~GetOverrideDefaultParameter.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
