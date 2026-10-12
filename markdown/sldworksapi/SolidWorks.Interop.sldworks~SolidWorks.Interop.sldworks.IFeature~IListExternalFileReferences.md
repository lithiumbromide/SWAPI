---
title: "IListExternalFileReferences Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IListExternalFileReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IListExternalFileReferences.html"
---

# IListExternalFileReferences Method (IFeature)

Obsolete. Superseded by [IFeature::IListExternalFileReferences2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IListExternalFileReferences2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub IListExternalFileReferences( _
   ByVal NumRefs As System.Integer, _
   ByRef ModelPathName As System.String, _
   ByRef CompPathName As System.String, _
   ByRef Feature As System.String, _
   ByRef DataType As System.String, _
   ByRef Status As System.Integer, _
   ByRef RefEntity As System.String, _
   ByRef FeatComp As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim NumRefs As System.Integer
Dim ModelPathName As System.String
Dim CompPathName As System.String
Dim Feature As System.String
Dim DataType As System.String
Dim Status As System.Integer
Dim RefEntity As System.String
Dim FeatComp As System.String

instance.IListExternalFileReferences(NumRefs, ModelPathName, CompPathName, Feature, DataType, Status, RefEntity, FeatComp)
```

### C#

```csharp
void IListExternalFileReferences(
   System.int NumRefs,
   out System.string ModelPathName,
   out System.string CompPathName,
   out System.string Feature,
   out System.string DataType,
   out System.int Status,
   out System.string RefEntity,
   out System.string FeatComp
)
```

### C++/CLI

```cpp
void IListExternalFileReferences(
   System.int NumRefs,
   [Out] System.String^ ModelPathName,
   [Out] System.String^ CompPathName,
   [Out] System.String^ Feature,
   [Out] System.String^ DataType,
   [Out] System.int Status,
   [Out] System.String^ RefEntity,
   [Out] System.String^ FeatComp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumRefs`:
- `ModelPathName`:
- `CompPathName`:
- `Feature`:
- `DataType`:
- `Status`:
- `RefEntity`:
- `FeatComp`:

## VBA Syntax

See [Feature::IListExternalFileReferences](ms-its:sldworksapivb6.chm::/sldworks~Feature~IListExternalFileReferences.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
