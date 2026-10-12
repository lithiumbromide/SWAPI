---
title: "ListExternalFileReferencesCount Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "ListExternalFileReferencesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ListExternalFileReferencesCount.html"
---

# ListExternalFileReferencesCount Method (IComponent2)

Gets the number of external references on the component.

## Syntax

### Visual Basic (Declaration)

```vb
Function ListExternalFileReferencesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
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

See [Component2::ListExternalFileReferencesCount](ms-its:sldworksapivb6.chm::/sldworks~Component2~ListExternalFileReferencesCount.html).

## Examples

[Get External References (VBA)](Get_External_References_Example_VB.htm)
[Get External References (VB.NET)](Get_External_References_Example_VBNET.htm)
[Get External References (C#)](Get_External_References_Example_CSharp.htm)

## Remarks

Call this method before calling [IComponent2::IListExternalFileReferences2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IListExternalFileReferences2.html) to get the number of external references of the component.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::ListExternalFileReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ListExternalFileReferences2.html)
[IFeature::IListExternalFileReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IListExternalFileReferences2.html)
[IFeature::ListExternalFileReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ListExternalFileReferences2.html)
[UpdateExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~UpdateExternalFileReferences.html)
[IComponent2::UpdateExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~UpdateExternalFileReferences.html)
[IModelDocExtension::ListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IListExternalFileReferences.html)
[IModelDocExtension::ListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferences.html)
[IModelDocExtension::UpdateExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateExternalFileReferences.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
