---
title: "BreakAllExternalFileReferences2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "BreakAllExternalFileReferences2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~BreakAllExternalFileReferences2.html"
---

# BreakAllExternalFileReferences2 Method (IModelDocExtension)

Breaks all external references and allows you to insert the features of the original part, or parts, if the external references are broken.

## Syntax

### Visual Basic (Declaration)

```vb
Sub BreakAllExternalFileReferences2( _
   ByVal InsertFeatures As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim InsertFeatures As System.Boolean

instance.BreakAllExternalFileReferences2(InsertFeatures)
```

### C#

```csharp
void BreakAllExternalFileReferences2(
   System.bool InsertFeatures
)
```

### C++/CLI

```cpp
void BreakAllExternalFileReferences2(
   System.bool InsertFeatures
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InsertFeatures`: True to insert the features of the original parts if the external references are broken, false to not

### Return Value

See [ModelDocExtension::BreakAllExternalFileReferences2](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~BreakAllExternalFileReferences2.html).

## VBA Syntax

See [ModelDocExtension::BreakAllExternalFileReferences2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~BreakAllExternalFileReferences2.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDoc2::GetExternalReferenceName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetExternalReferenceName.html)
[IModelDoc2::IListAuxiliaryExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IListAuxiliaryExternalFileReferences.html)
[IModelDoc2::ListAuxiliaryExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferences.html)
[IModelDoc2::ListAuxiliaryExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferencesCount.html)
[IModelDoc2::LockAllExternalReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LockAllExternalReferences.html)
[IModelDocExtension::ListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferences.html)
[IModelDocExtension::IListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IListExternalFileReferences.html)
[IModelDocExtension::ListExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferencesCount.html)
[IModelDocExtension::UpdateExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateExternalFileReferences.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
