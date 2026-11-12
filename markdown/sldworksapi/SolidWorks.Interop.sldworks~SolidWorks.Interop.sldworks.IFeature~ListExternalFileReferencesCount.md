---
title: "ListExternalFileReferencesCount Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "ListExternalFileReferencesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ListExternalFileReferencesCount.html"
---

# ListExternalFileReferencesCount Method (IFeature)

Gets the number of external references on the feature in a part or assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function ListExternalFileReferencesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Integer

value = instance.ListExternalFileReferencesCount()
```

### C#

```csharp
System.int ListExternalFileReferencesCount()
```

### C++/CLI

```cpp
System.int ListExternalFileReferencesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of external references

## VBA Syntax

See [Feature::ListExternalFileReferencesCount](ms-its:sldworksapivb6.chm::/sldworks~Feature~ListExternalFileReferencesCount.html).

## Examples

[Get External References (C#)](Get_External_References_Example_CSharp.htm)
[Get External References (VB.NET)](Get_External_References_Example_VBNET.htm)
[Get External References (VBA)](Get_External_References_Example_VB.htm)

## Remarks

Call this method before calling [IFeature::IListExternalFileReferences2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IListExternalFileReferences2.html) to determine the size of the array.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::ListExternalFileReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ListExternalFileReferences2.html)
[IComponent2::IListExternalFileReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IListExternalFileReferences2.html)
[IComponent2::ListExternalFileReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ListExternalFileReferences2.html)
[IComponent2::ListExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ListExternalFileReferencesCount.html)
[IComponent2::UpdateExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~UpdateExternalFileReferences.html)
[IModelDocExtension::IListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IListExternalFileReferences.html)
[IModelDocExtension::ListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferences.html)
[IModelDocExtension::ListExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferencesCount.html)
[IModelDocExtension::UpdateExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateExternalFileReferences.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
