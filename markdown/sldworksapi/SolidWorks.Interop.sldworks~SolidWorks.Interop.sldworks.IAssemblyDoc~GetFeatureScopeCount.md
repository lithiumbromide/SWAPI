---
title: "GetFeatureScopeCount Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetFeatureScopeCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScopeCount.html"
---

# GetFeatureScopeCount Method (IAssemblyDoc)

Gets the number of components affected by this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureScopeCount( _
   ByVal FeatureIn As Feature _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim FeatureIn As Feature
Dim value As System.Integer

value = instance.GetFeatureScopeCount(FeatureIn)
```

### C#

```csharp
System.int GetFeatureScopeCount(
   Feature FeatureIn
)
```

### C++/CLI

```cpp
System.int GetFeatureScopeCount(
   Feature^ FeatureIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FeatureIn`: [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

### Return Value

Number of components affected by this feature

## VBA Syntax

See [AssemblyDoc::GetFeatureScopeCount](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetFeatureScopeCount.html).

## Remarks

Call this method before calling [IAssemblyDoc::IGetFeatureScope](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~IGetFeatureScope.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::UpdateFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateFeatureScope.html)
[IAssemblyDoc::RemoveFromFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~RemoveFromFeatureScope.html)
[IAssemblyDoc::IGetFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetFeatureScope.html)
[IAssemblyDoc::GetFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScope.html)
[IAssemblyDoc::AddToFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddToFeatureScope.html)
[IAssemblyDoc::IGetFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetFeatureScope.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
