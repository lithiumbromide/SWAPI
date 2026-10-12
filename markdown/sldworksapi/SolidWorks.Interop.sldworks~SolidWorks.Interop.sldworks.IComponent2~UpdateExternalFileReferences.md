---
title: "UpdateExternalFileReferences Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "UpdateExternalFileReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~UpdateExternalFileReferences.html"
---

# UpdateExternalFileReferences Method (IComponent2)

Updates the external file references of this model.

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
Dim instance As IComponent2
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

- `ConfigOption`: Configuration option as defined [swExternalFileReferencesConfig_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExternalFileReferencesConfig_e.html)
- `ConfigName`: Name of configuration; required when ConfigOption set to swExternalFileReferencesNamedConfig
- `UpdateStatus`: Update status option as defined by [swExternalFileReferencesUpdate_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExternalFileReferencesUpdate_e.html)

## VBA Syntax

See [Component2::UpdateExternalFileReferences](ms-its:sldworksapivb6.chm::/sldworks~Component2~UpdateExternalFileReferences.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::IListExternalFileReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IListExternalFileReferences2.html)
[IComponent2::ListExternalFileReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ListExternalFileReferences2.html)
[IFeature::IListExternalFileReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IListExternalFileReferences2.html)
[IFeature::ListExternalFileReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ListExternalFileReferences2.html)
[IFeature::UpdateExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~UpdateExternalFileReferences.html)
[IModelDocExtension::IListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IListExternalFileReferences.html)
[IModelDocExtension::ListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferences.html)
[IModelDocExtension::UpdateExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateExternalFileReferences.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
