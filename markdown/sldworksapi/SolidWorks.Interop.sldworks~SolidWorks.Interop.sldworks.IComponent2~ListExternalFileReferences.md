---
title: "ListExternalFileReferences Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "ListExternalFileReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ListExternalFileReferences.html"
---

# ListExternalFileReferences Method (IComponent2)

Obsolete. Superseded by [IComponent2::ListExternalFileReferences2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~ListExternalFileReferences2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ListExternalFileReferences( _
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
Dim instance As IComponent2
Dim ModelPathName As System.Object
Dim ComponentPathName As System.Object
Dim Feature As System.Object
Dim DataType As System.Object
Dim Status As System.Object
Dim RefEntity As System.Object
Dim FeatCom As System.Object

instance.ListExternalFileReferences(ModelPathName, ComponentPathName, Feature, DataType, Status, RefEntity, FeatCom)
```

### C#

```csharp
void ListExternalFileReferences(
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
void ListExternalFileReferences(
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

See [Component2::ListExternalFileReferences](ms-its:sldworksapivb6.chm::/sldworks~Component2~ListExternalFileReferences.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
