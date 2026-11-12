---
title: "ListExternalFileReferences2 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "ListExternalFileReferences2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ListExternalFileReferences2.html"
---

# ListExternalFileReferences2 Method (IComponent2)

Gets the names and statuses of the external file references on the component.

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
   ByRef FeatCom As System.Object, _
   ByRef ConfigOption As System.Integer, _
   ByRef ConfigName As System.String _
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
Dim ConfigOption As System.Integer
Dim ConfigName As System.String

instance.ListExternalFileReferences2(ModelPathName, ComponentPathName, Feature, DataType, Status, RefEntity, FeatCom, ConfigOption, ConfigName)
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
   out System.object FeatCom,
   out System.int ConfigOption,
   out System.string ConfigName
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
   [Out] System.Object^ FeatCom,
   [Out] System.int ConfigOption,
   [Out] System.String^ ConfigName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModelPathName`: Array of path names of documents
- `ComponentPathName`: Array of path names of referenced components
- `Feature`: Array of in-context items (sketches, features, and so on)
- `DataType`: Array of data used to create the items (converted edge or face, converted or offset sketch entity, body, and so on)
- `Status`: Array of the statuses of the external references as defined in [swExternalReferenceStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExternalReferenceStatus_e.html)
- `RefEntity`: Array of actual items being used and the names of the documents that contain the items
- `FeatCom`: Array of the names of the components in which the affected features exist; this information is only displayed when one or more RefEntity is in a different component in an assembly and does not apply to derived parts
- `ConfigOption`: Configuration options as defined by [swExternalFileReferencesConfig_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExternalFileReferencesConfig_e.html)
- `ConfigName`: Name of the configuration when configOption is swExternalFileReferencesNamedConfig

## VBA Syntax

See [Component2::ListExternalFileReferences2](ms-its:sldworksapivb6.chm::/sldworks~Component2~ListExternalFileReferences2.html).

## Examples

[Get External References (C#)](Get_External_References_Example_CSharp.htm)
[Get External References (VB.NET)](Get_External_References_Example_VBNET.htm)
[Get External References (VBA)](Get_External_References_Example_VB.htm)

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::IListExternalFileReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IListExternalFileReferences2.html)
[IComponent2::ListExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ListExternalFileReferencesCount.html)
[IComponent2::UpdateExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~UpdateExternalFileReferences.html)
[IFeature::IListExternalFileReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IListExternalFileReferences2.html)
[IFeature::ListExternalFileReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ListExternalFileReferences2.html)
[IFeature::ListExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ListExternalFileReferencesCount.html)
[IFeature::UpdateExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~UpdateExternalFileReferences.html)
[IModelDocExtension::IListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IListExternalFileReferences.html)
[IModelDocExtension::ListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferences.html)
[IModelDocExtension::ListExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferencesCount.html)
[IModelDocExtension::UpdateExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateExternalFileReferences.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
