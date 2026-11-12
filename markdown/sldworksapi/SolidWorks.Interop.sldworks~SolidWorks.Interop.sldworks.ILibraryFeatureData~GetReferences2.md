---
title: "GetReferences2 Method (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "GetReferences2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferences2.html"
---

# GetReferences2 Method (ILibraryFeatureData)

Obsolete. Superseded by [ILibraryFeatureData::GetReferences3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILibraryFeatureData~GetReferences3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReferences2( _
   ByVal Scope As System.Integer, _
   ByRef RefType As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim Scope As System.Integer
Dim RefType As System.Object
Dim value As System.Object

value = instance.GetReferences2(Scope, RefType)
```

### C#

```csharp
System.object GetReferences2(
   System.int Scope,
   out System.object RefType
)
```

### C++/CLI

```cpp
System.Object^ GetReferences2(
   System.int Scope,
   [Out] System.Object^ RefType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Scope`: Reference scope as defined in [swLibFeatureData_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLibFeatureData_e.html)
- `RefType`: Array of reference types as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

Array of references

## VBA Syntax

See [LibraryFeatureData::GetReferences2](ms-its:sldworksapivb6.chm::/sldworks~LibraryFeatureData~GetReferences2.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::IGetReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetReferences2.html)
[ILibraryFeatureData::SetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~SetReferences.html)
[ILibraryFeatureData::ISetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~ISetReferences.html)

## Availability

SOLIDWORKS 2010 SP1, Revision Number 18.1
