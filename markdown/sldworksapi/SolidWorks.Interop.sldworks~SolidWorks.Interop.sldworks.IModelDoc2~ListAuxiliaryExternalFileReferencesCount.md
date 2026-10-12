---
title: "ListAuxiliaryExternalFileReferencesCount Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ListAuxiliaryExternalFileReferencesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferencesCount.html"
---

# ListAuxiliaryExternalFileReferencesCount Method (IModelDoc2)

Gets the number of auxiliary external file references for this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function ListAuxiliaryExternalFileReferencesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Integer

value = instance.ListAuxiliaryExternalFileReferencesCount()
```

### C#

```csharp
System.int ListAuxiliaryExternalFileReferencesCount()
```

### C++/CLI

```cpp
System.int ListAuxiliaryExternalFileReferencesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of auxiliary file references

## VBA Syntax

See [ModelDoc2::ListAuxiliaryExternalFileReferencesCount](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ListAuxiliaryExternalFileReferencesCount.html).

## Remarks

Call this method before calling [IModelDoc2::IListAuxiliaryExternalFileReferences](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IListAuxiliaryExternalFileReferences.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ListAuxiliaryExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferences.html)
[IModelDoc2::LockAllExternalReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LockAllExternalReferences.html)
[IModelDocExtension::IListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IListExternalFileReferences.html)
[IModelDocExtension::ListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferences.html)
[IModelDocExtension::ListExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferencesCount.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
