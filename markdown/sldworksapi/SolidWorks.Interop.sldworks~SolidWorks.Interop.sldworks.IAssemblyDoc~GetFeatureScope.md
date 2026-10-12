---
title: "GetFeatureScope Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetFeatureScope"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScope.html"
---

# GetFeatureScope Method (IAssemblyDoc)

Gets the components affected by this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureScope( _
   ByVal FeatureIn As Feature _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim FeatureIn As Feature
Dim value As System.Object

value = instance.GetFeatureScope(FeatureIn)
```

### C#

```csharp
System.object GetFeatureScope(
   Feature FeatureIn
)
```

### C++/CLI

```cpp
System.Object^ GetFeatureScope(
   Feature^ FeatureIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FeatureIn`: [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

### Return Value

Array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) affected by this feature

## VBA Syntax

See [AssemblyDoc::GetFeatureScope](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetFeatureScope.html).

## Remarks

Feature scope information is only provided if the assembly is opened in its own window.

This method gets both the components affected and potentially affected by this feature. Thus, not all of the components in this list are necessarily affected by this feature.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::IGetFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetFeatureScope.html)
[IAssemblyDoc::AddToFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddToFeatureScope.html)
[IAssemblyDoc::GetFeatureScopeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScopeCount.html)
[IAssemblyDoc::UpdateFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateFeatureScope.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
