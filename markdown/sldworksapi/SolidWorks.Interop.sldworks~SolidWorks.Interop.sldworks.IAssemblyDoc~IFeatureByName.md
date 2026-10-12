---
title: "IFeatureByName Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IFeatureByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IFeatureByName.html"
---

# IFeatureByName Method (IAssemblyDoc)

Returns the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object for the named feature in the assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function IFeatureByName( _
   ByVal Name As System.String _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Name As System.String
Dim value As Feature

value = instance.IFeatureByName(Name)
```

### C#

```csharp
Feature IFeatureByName(
   System.string Name
)
```

### C++/CLI

```cpp
Feature^ IFeatureByName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the feature

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [AssemblyDoc::IFeatureByName](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~IFeatureByName.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::FeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~FeatureByName.html)
