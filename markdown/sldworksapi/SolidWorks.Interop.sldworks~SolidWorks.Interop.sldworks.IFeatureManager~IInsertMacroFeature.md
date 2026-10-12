---
title: "IInsertMacroFeature Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "IInsertMacroFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMacroFeature.html"
---

# IInsertMacroFeature Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::IInsertMacroFeature3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~IInsertMacroFeature3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IInsertMacroFeature( _
   ByVal BaseName As System.String, _
   ByVal ProgId As System.String, _
   ByRef MacroMethods As System.String, _
   ByVal ParamCount As System.Integer, _
   ByRef ParamNames As System.String, _
   ByRef ParamTypes As System.Integer, _
   ByRef ParamValues As System.String, _
   ByVal EditBody As Body2, _
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
Dim EditBody As Body2
Dim Options As System.Integer
Dim value As Feature

value = instance.IInsertMacroFeature(BaseName, ProgId, MacroMethods, ParamCount, ParamNames, ParamTypes, ParamValues, EditBody, Options)
```

### C#

```csharp
Feature IInsertMacroFeature(
   System.string BaseName,
   System.string ProgId,
   ref System.string MacroMethods,
   System.int ParamCount,
   ref System.string ParamNames,
   ref System.int ParamTypes,
   ref System.string ParamValues,
   Body2 EditBody,
   System.int Options
)
```

### C++/CLI

```cpp
Feature^ IInsertMacroFeature(
   System.String^ BaseName,
   System.String^ ProgId,
   System.String^% MacroMethods,
   System.int ParamCount,
   System.String^% ParamNames,
   System.int% ParamTypes,
   System.String^% ParamValues,
   Body2^ EditBody,
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
- `EditBody`:
- `Options`:

## VBA Syntax

See [FeatureManager::IInsertMacroFeature](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~IInsertMacroFeature.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
