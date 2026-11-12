---
title: "IListExternalFileReferences2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IListExternalFileReferences2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IListExternalFileReferences2.html"
---

# IListExternalFileReferences2 Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::ListExternalReferences](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~ListExternalFileReferences.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub IListExternalFileReferences2( _
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
Dim instance As IModelDoc2
Dim NumRefs As System.Integer
Dim ModelPathName As System.String
Dim CompPathName As System.String
Dim Feature As System.String
Dim DataType As System.String
Dim Status As System.Integer
Dim RefEntity As System.String
Dim FeatComp As System.String

instance.IListExternalFileReferences2(NumRefs, ModelPathName, CompPathName, Feature, DataType, Status, RefEntity, FeatComp)
```

### C#

```csharp
void IListExternalFileReferences2(
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
void IListExternalFileReferences2(
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

See [ModelDoc2::IListExternalFileReferences2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IListExternalFileReferences2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
