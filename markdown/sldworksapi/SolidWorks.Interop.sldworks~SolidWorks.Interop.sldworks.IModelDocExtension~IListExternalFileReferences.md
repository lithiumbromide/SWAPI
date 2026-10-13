---
title: "IListExternalFileReferences Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IListExternalFileReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IListExternalFileReferences.html"
---

# IListExternalFileReferences Method (IModelDocExtension)

Gets the names and statuses of the external file references on this part or assembly.

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
   ByRef FeatComp As System.String, _
   ByRef ConfigOption As System.Integer, _
   ByRef ConfigName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim NumRefs As System.Integer
Dim ModelPathName As System.String
Dim CompPathName As System.String
Dim Feature As System.String
Dim DataType As System.String
Dim Status As System.Integer
Dim RefEntity As System.String
Dim FeatComp As System.String
Dim ConfigOption As System.Integer
Dim ConfigName As System.String

instance.IListExternalFileReferences(NumRefs, ModelPathName, CompPathName, Feature, DataType, Status, RefEntity, FeatComp, ConfigOption, ConfigName)
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
   out System.string FeatComp,
   out System.int ConfigOption,
   out System.string ConfigName
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
   [Out] System.String^ FeatComp,
   [Out] System.int ConfigOption,
   [Out] System.String^ ConfigName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumRefs`: Number of external references
- `ModelPathName`: - in-process, unmanaged C++: Pointer to an array of path names of documents of size NumRefs

  - VBA, VB.NET, C#, and C++/CLI: Not supported
- `CompPathName`: - in-process, unmanaged C++: Pointer to an array of path names of referenced components of size NumRefs

  - VBA, VB.NET, C#, and C++/CLI: Not supported
- `Feature`: - in-process, unmanaged C++: Pointer to an array of in-context items (sketches, features, and so on) of size NumRefs

  VBA, VB.NET, C#, and C++/CLI: Not supported
- `DataType`: - in-process, unmanaged C++: Pointer to an array of the type data used to create the items (converted edge or face, converted or offset sketch entity, body, and so on) of size NumRefs

  VBA, VB.NET, C#, and C++/CLI: Not supported
- `Status`: - in-process, unmanaged C++: Array of statuses of the external references as defined in [swExternalReferenceStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExternalReferenceStatus_e.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported
- `RefEntity`: - in-process, unmanaged C++: Pointer to an array of actual items being used and the names of the documents that contain the items of size NumRefs

  - VBA, VB.NET, C#, and C++/CLI: Not supported
- `FeatComp`: - in-process, unmanaged C++: Pointer to an array of the names of the components in which the affected features exist of size NumRefs; this information is only displayed when one or more RefEntity is in a different component in an assembly and does not apply to derived parts
  - VBA, VB.NET, C#, and C++/CLI: Not supported
- `ConfigOption`: Configuration option as defined by [swExternalFileReferencesConfig_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExternalFileReferencesConfig_e.html)
- `ConfigName`: Name of the configuration when configOption is swExternalFileReferencesNamedConfig

## Remarks

Before calling this method, call [IModelDocExtension::ListExternalFileReferencesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~ListExternalFileReferencesCount.html) to specify NumRefs.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::ListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferences.html)
[IModelDocExtension::ListExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferencesCount.html)
[IModelDocExtension::UpdateExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateExternalFileReferences.html)
[IModelDoc2::BreakAllExternalReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~BreakAllExternalReferences.html)
[IModelDoc2::IListAuxiliaryExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IListAuxiliaryExternalFileReferences.html)
[IModelDoc2::ListAuxiliaryExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferences.html)
[IModelDoc2::ListAuxiliaryExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferencesCount.html)
[IModelDoc2::LockAllExternalReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LockAllExternalReferences.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
