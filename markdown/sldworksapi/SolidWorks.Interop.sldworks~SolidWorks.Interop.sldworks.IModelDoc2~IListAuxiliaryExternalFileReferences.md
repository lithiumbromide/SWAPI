---
title: "IListAuxiliaryExternalFileReferences Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IListAuxiliaryExternalFileReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IListAuxiliaryExternalFileReferences.html"
---

# IListAuxiliaryExternalFileReferences Method (IModelDoc2)

Gets the names of auxiliary external file references for this model.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IListAuxiliaryExternalFileReferences( _
   ByVal NumRefs As System.Integer, _
   ByRef Feature As System.String, _
   ByRef ExternalFileName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim NumRefs As System.Integer
Dim Feature As System.String
Dim ExternalFileName As System.String

instance.IListAuxiliaryExternalFileReferences(NumRefs, Feature, ExternalFileName)
```

### C#

```csharp
void IListAuxiliaryExternalFileReferences(
   System.int NumRefs,
   out System.string Feature,
   out System.string ExternalFileName
)
```

### C++/CLI

```cpp
void IListAuxiliaryExternalFileReferences(
   System.int NumRefs,
   [Out] System.String^ Feature,
   [Out] System.String^ ExternalFileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumRefs`: Number of external references
- `Feature`: Array of size NumRefs containing the names of features that include auxiliary external references
- `ExternalFileName`: Array of size NumRefs containing the names of the auxiliary external files

## VBA Syntax

See [ModelDoc2::IListAuxiliaryExternalFileReferences](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IListAuxiliaryExternalFileReferences.html).

## Remarks

Call [IModelDoc2::ListAuxiliaryExtenalFileReferencesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferencesCount.html) before calling of this method to determine the size of the arrays.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ListAuxiliaryExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferences.html)
[IModelDocExtension::IListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IListExternalFileReferences.html)
[IModelDocExtension::ListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferences.html)
[IModelDoc2::ListAuxiliaryExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferencesCount.html)
[IModelDoc2::LockAllExternalReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LockAllExternalReferences.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
