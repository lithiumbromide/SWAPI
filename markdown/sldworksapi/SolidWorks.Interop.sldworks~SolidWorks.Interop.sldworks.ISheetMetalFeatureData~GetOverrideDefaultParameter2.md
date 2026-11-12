---
title: "GetOverrideDefaultParameter2 Method (ISheetMetalFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFeatureData"
member: "GetOverrideDefaultParameter2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~GetOverrideDefaultParameter2.html"
---

# GetOverrideDefaultParameter2 Method (ISheetMetalFeatureData)

Gets whether the specified default parameter is overridden in this sheet metal feature in a multibody sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOverrideDefaultParameter2( _
   ByVal Parameter As System.Integer, _
   ByRef OverrideDefaultParameter As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalFeatureData
Dim Parameter As System.Integer
Dim OverrideDefaultParameter As System.Boolean
Dim value As System.Integer

value = instance.GetOverrideDefaultParameter2(Parameter, OverrideDefaultParameter)
```

### C#

```csharp
System.int GetOverrideDefaultParameter2(
   System.int Parameter,
   out System.bool OverrideDefaultParameter
)
```

### C++/CLI

```cpp
System.int GetOverrideDefaultParameter2(
   System.int Parameter,
   [Out] System.bool OverrideDefaultParameter
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Parameter`: Default parameter as defined in [swSheetMetalOverrideDefaultParameters_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSheetMetalOverrideDefaultParameters_e.html)
- `OverrideDefaultParameter`: True if Parameter is overridden, false if not

### Return Value

Result code as defined in [swSheetMetalModifierError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalModifierError_e.html)

## VBA Syntax

See [SheetMetalFeatureData::GetOverrideDefaultParameter2](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalFeatureData~GetOverrideDefaultParameter2.html).

## Examples

[Set Override Option for Auto Relief Default Parameters (C#)](Set_Override_Option_for_Auto_Relief_Default_Parameters_Example_CSharp.htm)
[Set Override Option for Auto Relief Default Parameters (VB.NET)](Set_Override_Option_for_Auto_Relief_Default_Parameters_Example_VBNET.htm)
[Set Override Option for Auto Relief Default Parameters (VBA)](Set_Override_Option_for_Auto_Relief_Default_Parameters_Example_VB.htm)

## Remarks

This property is only valid for multibody sheet metal parts created in SOLIDWORKS 2013 and later.

## See Also

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.html)
[ISheetMetalFeatureData::SetOverrideDefaultParameter2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetOverrideDefaultParameter2.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
