---
title: "GetReferences Method (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "GetReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferences.html"
---

# GetReferences Method (ILibraryFeatureData)

Obsolete. Superseded by [ILibraryFeatureData::GetReferences2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILibraryFeatureData~GetReferences2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReferences( _
   ByRef RefType As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim RefType As System.Object
Dim value As System.Object

value = instance.GetReferences(RefType)
```

### C#

```csharp
System.object GetReferences(
   out System.object RefType
)
```

### C++/CLI

```cpp
System.Object^ GetReferences(
   [Out] System.Object^ RefType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RefType`: Array of reference types as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

Array of references

## VBA Syntax

See [LibraryFeatureData::GetReferences](ms-its:sldworksapivb6.chm::/sldworks~LibraryFeatureData~GetReferences.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::GetReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferencesCount.html)
[ILibraryFeatureData::IGetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetReferences.html)
[ILibraryFeatureData::SetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~SetReferences.html)
[ILibraryFeatureData::ISetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~ISetReferences.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
