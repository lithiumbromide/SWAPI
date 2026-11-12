---
title: "ListAuxiliaryExternalFileReferences Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ListAuxiliaryExternalFileReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferences.html"
---

# ListAuxiliaryExternalFileReferences Method (IModelDoc2)

Gets the names of auxiliary external file references for this model.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ListAuxiliaryExternalFileReferences( _
   ByRef Feature As System.Object, _
   ByRef ExternalFileName As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Feature As System.Object
Dim ExternalFileName As System.Object

instance.ListAuxiliaryExternalFileReferences(Feature, ExternalFileName)
```

### C#

```csharp
void ListAuxiliaryExternalFileReferences(
   out System.object Feature,
   out System.object ExternalFileName
)
```

### C++/CLI

```cpp
void ListAuxiliaryExternalFileReferences(
   [Out] System.Object^ Feature,
   [Out] System.Object^ ExternalFileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Feature`: Array containing the names of features that include auxiliary external references
- `ExternalFileName`: Array containing the names of the auxiliary external files

## VBA Syntax

See [ModelDoc2::ListAuxiliaryExternalFileReferences](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ListAuxiliaryExternalFileReferences.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ListAuxiliaryExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferencesCount.html)
[IModelDoc2::IListAuxiliaryExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IListAuxiliaryExternalFileReferences.html)
[IModelDoc2::LockAllExternalReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LockAllExternalReferences.html)
[IModelDocExtension::ListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferences.html)
[IModelDocExtension::ListExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferencesCount.html)
[IModelDocExtension::IListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IListExternalFileReferences.html)
[IFeatureManager::InsertMacroFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMacroFeature3.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
