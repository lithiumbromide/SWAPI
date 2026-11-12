---
title: "InsertMacroFeature Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertMacroFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMacroFeature.html"
---

# InsertMacroFeature Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertMacroFeature3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMacroFeature3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMacroFeature( _
   ByVal BaseName As System.String, _
   ByVal ProgId As System.String, _
   ByVal MacroMethods As System.Object, _
   ByVal ParamNames As System.Object, _
   ByVal ParamTypes As System.Object, _
   ByVal ParamValues As System.Object, _
   ByVal EditBody As Body2, _
   ByVal Options As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim BaseName As System.String
Dim ProgId As System.String
Dim MacroMethods As System.Object
Dim ParamNames As System.Object
Dim ParamTypes As System.Object
Dim ParamValues As System.Object
Dim EditBody As Body2
Dim Options As System.Integer
Dim value As Feature

value = instance.InsertMacroFeature(BaseName, ProgId, MacroMethods, ParamNames, ParamTypes, ParamValues, EditBody, Options)
```

### C#

```csharp
Feature InsertMacroFeature(
   System.string BaseName,
   System.string ProgId,
   System.object MacroMethods,
   System.object ParamNames,
   System.object ParamTypes,
   System.object ParamValues,
   Body2 EditBody,
   System.int Options
)
```

### C++/CLI

```cpp
Feature^ InsertMacroFeature(
   System.String^ BaseName,
   System.String^ ProgId,
   System.Object^ MacroMethods,
   System.Object^ ParamNames,
   System.Object^ ParamTypes,
   System.Object^ ParamValues,
   Body2^ EditBody,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BaseName`:
- `ProgId`:
- `MacroMethods`:
- `ParamNames`:
- `ParamTypes`:
- `ParamValues`:
- `EditBody`:
- `Options`:

## VBA Syntax

See [FeatureManager::InsertMacroFeature](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertMacroFeature.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
