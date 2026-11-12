---
title: "UpdateExternalFileReferences Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "UpdateExternalFileReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~UpdateExternalFileReferences.html"
---

# UpdateExternalFileReferences Method (IFeature)

Updates the external file references on this model.

## Syntax

### Visual Basic (Declaration)

```vb
Sub UpdateExternalFileReferences( _
   ByVal ConfigOption As System.Integer, _
   ByVal ConfigName As System.String, _
   ByVal UpdateStatus As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim ConfigOption As System.Integer
Dim ConfigName As System.String
Dim UpdateStatus As System.Integer

instance.UpdateExternalFileReferences(ConfigOption, ConfigName, UpdateStatus)
```

### C#

```csharp
void UpdateExternalFileReferences(
   System.int ConfigOption,
   System.string ConfigName,
   System.int UpdateStatus
)
```

### C++/CLI

```cpp
void UpdateExternalFileReferences(
   System.int ConfigOption,
   System.String^ ConfigName,
   System.int UpdateStatus
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigOption`: Configuration options as defined by [swExternalFileReferencesConfig_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExternalFileReferencesConfig_e.html)
- `ConfigName`: Name of configuration; required when ConfigOption set to swExternalFileReferencesNamedConfig
- `UpdateStatus`: Update status option as defined by[swExternalFileReferencesUpdate_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExternalFileReferencesUpdate_e.html)

## VBA Syntax

See [Feature::UpdateExternalFileReferences](ms-its:sldworksapivb6.chm::/sldworks~Feature~UpdateExternalFileReferences.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::IListExternalFileReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IListExternalFileReferences2.html)
[IFeature::ListExternalFileReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ListExternalFileReferences2.html)
[IFeature::ListExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ListExternalFileReferencesCount.html)
[IComponent2::IListExternalFileReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IListExternalFileReferences2.html)
[IComponent2::ListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ListExternalFileReferences.html)
[IComponent2::RemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveMaterialProperty2.html)
[IComponent2::UpdateExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~UpdateExternalFileReferences.html)
[IModelDocExtension::IListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IListExternalFileReferences.html)
[IModelDocExtension::ListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferences.html)
[IModelDocExtension::ListExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferencesCount.html)
[IModelDocExtension::UpdateExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateExternalFileReferences.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
