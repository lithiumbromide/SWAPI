---
title: "GetOverrideDefaultParameter Method (ISheetMetalFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFeatureData"
member: "GetOverrideDefaultParameter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~GetOverrideDefaultParameter.html"
---

# GetOverrideDefaultParameter Method (ISheetMetalFeatureData)

Obsolete. Superseded by [ISheetMetalFeatureData::GetOverrideDefaultParameter2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~GetOverrideDefaultParameter2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOverrideDefaultParameter( _
   ByRef OverrideDefaultParameter As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalFeatureData
Dim OverrideDefaultParameter As System.Boolean
Dim value As System.Integer

value = instance.GetOverrideDefaultParameter(OverrideDefaultParameter)
```

### C#

```csharp
System.int GetOverrideDefaultParameter(
   out System.bool OverrideDefaultParameter
)
```

### C++/CLI

```cpp
System.int GetOverrideDefaultParameter(
   [Out] System.bool OverrideDefaultParameter
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OverrideDefaultParameter`: True if the default parameters are overridden, false if not

### Return Value

Result code as defined in [swSheetMetalModifierError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalModifierError_e.html)

## VBA Syntax

See [SheetMetalFeatureData::GetOverrideDefaultParameter](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalFeatureData~GetOverrideDefaultParameter.html).

## See Also

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.html)
[ISheetMetalFeatureData::SetOverrideDefaultParameter Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetOverrideDefaultParameter.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
