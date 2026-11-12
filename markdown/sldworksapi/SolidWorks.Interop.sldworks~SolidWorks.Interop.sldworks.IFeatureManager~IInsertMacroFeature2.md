---
title: "IInsertMacroFeature2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "IInsertMacroFeature2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMacroFeature2.html"
---

# IInsertMacroFeature2 Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::IInsertMacroFeature3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~IInsertMacroFeature3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IInsertMacroFeature2( _
   ByVal BaseName As System.String, _
   ByVal ProgId As System.String, _
   ByRef MacroMethods As System.String, _
   ByVal ParamCount As System.Integer, _
   ByRef ParamNames As System.String, _
   ByRef ParamTypes As System.Integer, _
   ByRef ParamValues As System.String, _
   ByVal DimCount As System.Integer, _
   ByRef DimTypes As System.Integer, _
   ByRef DimCountValues As System.Double, _
   ByVal EditBody As Body2, _
   ByVal IconCount As System.Integer, _
   ByRef IconFiles As System.String, _
   ByVal Options As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim BaseName As System.String
Dim ProgId As System.String
Dim MacroMethods As System.String
Dim ParamCount As System.Integer
Dim ParamNames As System.String
Dim ParamTypes As System.Integer
Dim ParamValues As System.String
Dim DimCount As System.Integer
Dim DimTypes As System.Integer
Dim DimCountValues As System.Double
Dim EditBody As Body2
Dim IconCount As System.Integer
Dim IconFiles As System.String
Dim Options As System.Integer
Dim value As Feature

value = instance.IInsertMacroFeature2(BaseName, ProgId, MacroMethods, ParamCount, ParamNames, ParamTypes, ParamValues, DimCount, DimTypes, DimCountValues, EditBody, IconCount, IconFiles, Options)
```

### C#

```csharp
Feature IInsertMacroFeature2(
   System.string BaseName,
   System.string ProgId,
   ref System.string MacroMethods,
   System.int ParamCount,
   ref System.string ParamNames,
   ref System.int ParamTypes,
   ref System.string ParamValues,
   System.int DimCount,
   ref System.int DimTypes,
   ref System.double DimCountValues,
   Body2 EditBody,
   System.int IconCount,
   ref System.string IconFiles,
   System.int Options
)
```

### C++/CLI

```cpp
Feature^ IInsertMacroFeature2(
   System.String^ BaseName,
   System.String^ ProgId,
   System.String^% MacroMethods,
   System.int ParamCount,
   System.String^% ParamNames,
   System.int% ParamTypes,
   System.String^% ParamValues,
   System.int DimCount,
   System.int% DimTypes,
   System.double% DimCountValues,
   Body2^ EditBody,
   System.int IconCount,
   System.String^% IconFiles,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BaseName`:
- `ProgId`:
- `MacroMethods`:
- `ParamCount`:
- `ParamNames`:
- `ParamTypes`:
- `ParamValues`:
- `DimCount`:
- `DimTypes`:
- `DimCountValues`:
- `EditBody`:
- `IconCount`:
- `IconFiles`:
- `Options`:

## VBA Syntax

See [FeatureManager::IInsertMacroFeature2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~IInsertMacroFeature2.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
