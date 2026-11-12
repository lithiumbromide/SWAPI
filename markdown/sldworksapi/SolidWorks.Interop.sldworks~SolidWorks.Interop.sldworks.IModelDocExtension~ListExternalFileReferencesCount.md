---
title: "ListExternalFileReferencesCount Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ListExternalFileReferencesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferencesCount.html"
---

# ListExternalFileReferencesCount Method (IModelDocExtension)

Gets the number of external references on this part or assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function ListExternalFileReferencesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
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

See [ModelDocExtension::ListExternalFileReferencesCount](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ListExternalFileReferencesCount.html).

## Examples

[Get External References (VBA)](Get_External_References_Example_VB.htm)
[Get External References (VB.NET)](Get_External_References_Example_VBNET.htm)
[Get External References (C#)](Get_External_References_Example_CSharp.htm)

## Remarks

Call this method before calling [IModelDocExtension::IListExternalFileReferences](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IListExternalFileReferences.html) to get the number of external references on the part.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::IListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IListExternalFileReferences.html)
[IModelDocExtension::ListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferences.html)
[IModelDocExtension::UpdateExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateExternalFileReferences.html)
[IModelDoc2::BreakAllExternalReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~BreakAllExternalReferences.html)
[IModelDoc2::IListAuxiliaryExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IListAuxiliaryExternalFileReferences.html)
[IModelDoc2::ListAuxiliaryExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferences.html)
[IModelDoc2::ListAuxiliaryExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferencesCount.html)
[IModelDoc2::LockAllExternalReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LockAllExternalReferences.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
