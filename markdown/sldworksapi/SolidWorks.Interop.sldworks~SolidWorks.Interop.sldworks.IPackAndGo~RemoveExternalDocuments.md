---
title: "RemoveExternalDocuments Method (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "RemoveExternalDocuments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~RemoveExternalDocuments.html"
---

# RemoveExternalDocuments Method (IPackAndGo)

Removes the specified non-SOLIDWORKS files from Pack and Go.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveExternalDocuments( _
   ByVal DocumentNames As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPackAndGo
Dim DocumentNames As System.Object
Dim value As System.Boolean

value = instance.RemoveExternalDocuments(DocumentNames)
```

### C#

```csharp
System.bool RemoveExternalDocuments(
   System.object DocumentNames
)
```

### C++/CLI

```cpp
System.bool RemoveExternalDocuments(
   System.Object^ DocumentNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocumentNames`: Array of the paths and filenames of the non-SOLIDWORKS files to remove from Pack and Go

### Return Value

True if all of the specified non-SOLIDWORKS files are removed from Pack and Go, false if not

## VBA Syntax

See [PackAndGo::RemoveExternalDocuments](ms-its:sldworksapivb6.chm::/sldworks~PackAndGo~RemoveExternalDocuments.html).

## Examples

[Add and Remove Files from Pack and Go (C#)](Add_and_Remove_Files_from_Pack_and_Go_Example_CSharp.htm)
[Add and Remove Files from Pack and Go (VB.NET)](Add_and_Remove_Files_from_Pack_and_Go_Example_VBNET.htm)
[Add and Remove Files from Pack and Go (VBA)](Add_and_Remove_Files_from_Pack_and_Go_Example_VB.htm)

## Remarks

In C# applications, you must wrap the array of objects for the DocumentNames parameter using the .NET Framework BStrWrapper class.

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)
[IPackAndGo::AddExternalDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~AddExternalDocuments.html)
[IPackAndGo::GetDocumentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentNames.html)
[IPackAndGo::GetDocumentNamesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentNamesCount.html)
[IPackAndGo::IGetDocumentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IGetDocumentNames.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
