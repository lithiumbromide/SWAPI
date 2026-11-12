---
title: "GetExternalDocuments Method (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "GetExternalDocuments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetExternalDocuments.html"
---

# GetExternalDocuments Method (IPackAndGo)

Gets the paths and filenames of the non-SOLIDWORKS files added to Pack And Go.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExternalDocuments( _
   ByRef DocumentNames As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPackAndGo
Dim DocumentNames As System.Object
Dim value As System.Boolean

value = instance.GetExternalDocuments(DocumentNames)
```

### C#

```csharp
System.bool GetExternalDocuments(
   out System.object DocumentNames
)
```

### C++/CLI

```cpp
System.bool GetExternalDocuments(
   [Out] System.Object^ DocumentNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocumentNames`: Array of strings of the paths and filenames of the non-SOLIDWORKS files added to Pack and Go

### Return Value

True if the paths and filenames of the non-SOLIDWORKS files are returned, false if not

## VBA Syntax

See [PackAndGo::GetExternalDocuments](ms-its:sldworksapivb6.chm::/sldworks~PackAndGo~GetExternalDocuments.html).

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)
[IPackAndGo::AddExternalDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~AddExternalDocuments.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
