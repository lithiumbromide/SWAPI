---
title: "AddExternalDocuments Method (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "AddExternalDocuments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~AddExternalDocuments.html"
---

# AddExternalDocuments Method (IPackAndGo)

Adds non-SOLIDWORKS files to Pack and Go.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddExternalDocuments( _
   ByVal DocumentNames As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPackAndGo
Dim DocumentNames As System.Object
Dim value As System.Boolean

value = instance.AddExternalDocuments(DocumentNames)
```

### C#

```csharp
System.bool AddExternalDocuments(
   System.object DocumentNames
)
```

### C++/CLI

```cpp
System.bool AddExternalDocuments(
   System.Object^ DocumentNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocumentNames`: Array of paths and filenames of non-SOLIDWORKS files to add to Pack and Go

### Return Value

True if the files are added to Pack and Go, false if not

## VBA Syntax

See [PackAndGo::AddExternalDocuments](ms-its:sldworksapivb6.chm::/sldworks~PackAndGo~AddExternalDocuments.html).

## Examples

[Add and Remove Files from Pack And Go (C#)](Add_and_Remove_Files_from_Pack_and_Go_Example_CSharp.htm)
[Add and Remove Files from Pack and Go (VB.NET)](Add_and_Remove_Files_from_Pack_and_Go_Example_VBNET.htm)
[Add and Remove Files from Pack and Go (VBA)](Add_and_Remove_Files_from_Pack_and_Go_Example_VB.htm)

## Remarks

Duplicate files are not allowed. You can add any type of non-SOLIDWORKS file.

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)
[IPackAndGo::GetExternalDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetExternalDocuments.html)
[IModelDocExtension::GetRenderCustomReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderCustomReferences.html)
[IModelDocExtension::GetRenderStockReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderStockReferences.html)
[IPackAndGo::RemoveExternalDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~RemoveExternalDocuments.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
