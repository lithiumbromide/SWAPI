---
title: "ListExternalFileReferences2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ListExternalFileReferences2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListExternalFileReferences2.html"
---

# ListExternalFileReferences2 Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::ListExternalReferences](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~ListExternalFileReferences.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ListExternalFileReferences2( _
   ByRef ModelPathName As System.Object, _
   ByRef ComponentPathName As System.Object, _
   ByRef Feature As System.Object, _
   ByRef DataType As System.Object, _
   ByRef Status As System.Object, _
   ByRef RefEntity As System.Object, _
   ByRef FeatCom As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ModelPathName As System.Object
Dim ComponentPathName As System.Object
Dim Feature As System.Object
Dim DataType As System.Object
Dim Status As System.Object
Dim RefEntity As System.Object
Dim FeatCom As System.Object

instance.ListExternalFileReferences2(ModelPathName, ComponentPathName, Feature, DataType, Status, RefEntity, FeatCom)
```

### C#

```csharp
void ListExternalFileReferences2(
   out System.object ModelPathName,
   out System.object ComponentPathName,
   out System.object Feature,
   out System.object DataType,
   out System.object Status,
   out System.object RefEntity,
   out System.object FeatCom
)
```

### C++/CLI

```cpp
void ListExternalFileReferences2(
   [Out] System.Object^ ModelPathName,
   [Out] System.Object^ ComponentPathName,
   [Out] System.Object^ Feature,
   [Out] System.Object^ DataType,
   [Out] System.Object^ Status,
   [Out] System.Object^ RefEntity,
   [Out] System.Object^ FeatCom
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModelPathName`:
- `ComponentPathName`:
- `Feature`:
- `DataType`:
- `Status`:
- `RefEntity`:
- `FeatCom`:

## VBA Syntax

See [ModelDoc2::ListExternalFileReferences2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ListExternalFileReferences2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
