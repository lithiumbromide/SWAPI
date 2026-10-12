---
title: "UpdateExternalFileReferences Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "UpdateExternalFileReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateExternalFileReferences.html"
---

# UpdateExternalFileReferences Method (IModelDocExtension)

Updates the external files references on this model.

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
Dim instance As IModelDocExtension
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
- `ConfigName`: Name of configuration; required when configOption set to swExternalFileReferencesNamedConfig
- `UpdateStatus`: Update status option as defined by [swExternalFileReferencesUpdate_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExternalFileReferencesUpdate_e.html)

## VBA Syntax

See [ModelDocExtension::UpdateExternalFileReferences](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~UpdateExternalFileReferences.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::ListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferences.html)
[IModelDocExtension::ListExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferencesCount.html)
[IModelDocExtension::IListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IListExternalFileReferences.html)
[IModelDoc2::BreakAllExternalReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~BreakAllExternalReferences.html)
[IModelDoc2::IListAuxiliaryExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IListAuxiliaryExternalFileReferences.html)
[IModelDoc2::ListAuxiliaryExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferences.html)
[IModelDoc2::ListAuxiliaryExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferencesCount.html)
[IModelDoc2::LockAllExternalReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LockAllExternalReferences.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
