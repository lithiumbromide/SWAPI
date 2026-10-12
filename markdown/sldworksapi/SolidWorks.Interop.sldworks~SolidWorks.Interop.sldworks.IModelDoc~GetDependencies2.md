---
title: "GetDependencies2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetDependencies2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetDependencies2.html"
---

# GetDependencies2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetDependencies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetDependencies2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDependencies2( _
   ByVal Traverseflag As System.Boolean, _
   ByVal Searchflag As System.Boolean, _
   ByVal AddReadOnlyInfo As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Traverseflag As System.Boolean
Dim Searchflag As System.Boolean
Dim AddReadOnlyInfo As System.Boolean
Dim value As System.Object

value = instance.GetDependencies2(Traverseflag, Searchflag, AddReadOnlyInfo)
```

### C#

```csharp
System.object GetDependencies2(
   System.bool Traverseflag,
   System.bool Searchflag,
   System.bool AddReadOnlyInfo
)
```

### C++/CLI

```cpp
System.Object^ GetDependencies2(
   System.bool Traverseflag,
   System.bool Searchflag,
   System.bool AddReadOnlyInfo
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Traverseflag`:
- `Searchflag`:
- `AddReadOnlyInfo`:

## VBA Syntax

See [ModelDoc::GetDependencies2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetDependencies2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
