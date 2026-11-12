---
title: "GetNumDependencies Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetNumDependencies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetNumDependencies.html"
---

# GetNumDependencies Method (IModelDoc2)

Gets the number of strings returned by [IModelDoc2::GetDependencies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetDependencies2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNumDependencies( _
   ByVal Traverseflag As System.Integer, _
   ByVal Searchflag As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Traverseflag As System.Integer
Dim Searchflag As System.Integer
Dim value As System.Integer

value = instance.GetNumDependencies(Traverseflag, Searchflag)
```

### C#

```csharp
System.int GetNumDependencies(
   System.int Traverseflag,
   System.int Searchflag
)
```

### C++/CLI

```cpp
System.int GetNumDependencies(
   System.int Traverseflag,
   System.int Searchflag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Traverseflag`: True to traverse down into all dependent files, false for only the highest level within the dependencies
- `Searchflag`: True to apply the current search criteria, false to return the dependent file information as it was stored

### Return Value

Number of strings returned by [IModelDoc2::GetDependencies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetDependencies2.html)

## VBA Syntax

See [ModelDoc2::GetNumDependencies](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetNumDependencies.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IGetNumDependencies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetNumDependencies2.html)
[IModelDoc2::IGetDependencies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetDependencies2.html)
[ISldWorks::GetDocumentDependencies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentDependencies2.html)
[ISldWorks::GetDocumentDependenciesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentDependenciesCount.html)
[ISldWorks::IGetDocumentDependencies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocumentDependencies2.html)
[ISldWorks::IGetDocumentDependenciesCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocumentDependenciesCount2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
