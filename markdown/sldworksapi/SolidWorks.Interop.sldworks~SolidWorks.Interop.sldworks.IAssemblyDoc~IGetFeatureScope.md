---
title: "IGetFeatureScope Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IGetFeatureScope"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetFeatureScope.html"
---

# IGetFeatureScope Method (IAssemblyDoc)

Gets the components affected by this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFeatureScope( _
   ByVal FeatureIn As Feature, _
   ByVal NumComponents As System.Integer _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim FeatureIn As Feature
Dim NumComponents As System.Integer
Dim value As Component2

value = instance.IGetFeatureScope(FeatureIn, NumComponents)
```

### C#

```csharp
Component2 IGetFeatureScope(
   Feature FeatureIn,
   System.int NumComponents
)
```

### C++/CLI

```cpp
Component2^ IGetFeatureScope(
   Feature^ FeatureIn,
   System.int NumComponents
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FeatureIn`: [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)
- `NumComponents`: Number of components affected by this feature

### Return Value

Array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) of size NumComponents

## VBA Syntax

See [AssemblyDoc::IGetFeatureScope](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~IGetFeatureScope.html).

## Remarks

Feature scope information is only provided if the assembly is opened in its own window.

COM users must call [IAssemblyDoc::GetFeatureScopeCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~GetFeatureScopeCount.html) before calling this method.

This method gets both the components affected and potentially affected by this feature. Thus, not all of the components in this list are necessarily affected by this feature.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScope.html)
[IAssemblyDoc::AddToFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddToFeatureScope.html)
[IAssemblyDoc::GetFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScope.html)
[IAssemblyDoc::GetFeatureScopeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScopeCount.html)
[IAssemblyDoc::UpdateFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateFeatureScope.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
