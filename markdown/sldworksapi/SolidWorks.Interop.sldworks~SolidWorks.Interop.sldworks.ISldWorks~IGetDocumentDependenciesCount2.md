---
title: "IGetDocumentDependenciesCount2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IGetDocumentDependenciesCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocumentDependenciesCount2.html"
---

# IGetDocumentDependenciesCount2 Method (ISldWorks)

Gets the size of the array needed for a call to [ISldWorks::IGetDocumetnDependencies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IGetDocumentDependencies2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDocumentDependenciesCount2( _
   ByVal Document As System.String, _
   ByVal Traverseflag As System.Boolean, _
   ByVal Searchflag As System.Boolean, _
   ByVal AddReadOnlyInfo As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Document As System.String
Dim Traverseflag As System.Boolean
Dim Searchflag As System.Boolean
Dim AddReadOnlyInfo As System.Boolean
Dim value As System.Integer

value = instance.IGetDocumentDependenciesCount2(Document, Traverseflag, Searchflag, AddReadOnlyInfo)
```

### C#

```csharp
System.int IGetDocumentDependenciesCount2(
   System.string Document,
   System.bool Traverseflag,
   System.bool Searchflag,
   System.bool AddReadOnlyInfo
)
```

### C++/CLI

```cpp
System.int IGetDocumentDependenciesCount2(
   System.String^ Document,
   System.bool Traverseflag,
   System.bool Searchflag,
   System.bool AddReadOnlyInfo
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Document`: Name of the document
- `Traverseflag`: True if you want to traverse down into all dependent files, false if you want only the highest level within the dependencies
- `Searchflag`: Set this argument to True if you want to use the search rules to find dependencies, false looks where the documents were last saved
- `AddReadOnlyInfo`: True if you want to have read-only information with the filenames, false if not

### Return Value

Number of strings returned by [ISldWorks::IGetDocumetnDependencies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IGetDocumentDependencies2.html)

## VBA Syntax

See [SldWorks::IGetDocumentDependenciesCount2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IGetDocumentDependenciesCount2.html).

## Remarks

If SearchFlag is set to True, then the current directory is set to the directory of the document file. This is the same as interactively clikcing the References button in the File Open dialog.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetDocumentDependencies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentDependencies2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
