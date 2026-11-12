---
title: "IGetReferences Method (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "IGetReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetReferences.html"
---

# IGetReferences Method (ILibraryFeatureData)

Obsolete. Superseded by [ILibraryFeatureData::IGetReferences2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILibraryFeatureData~IGetReferences2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetReferences( _
   ByVal Count As System.Integer, _
   ByRef RefType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim Count As System.Integer
Dim RefType As System.Integer
Dim value As System.Object

value = instance.IGetReferences(Count, RefType)
```

### C#

```csharp
System.object IGetReferences(
   System.int Count,
   out System.int RefType
)
```

### C++/CLI

```cpp
System.Object^ IGetReferences(
   System.int Count,
   [Out] System.int RefType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of references
- `RefType`: - in-process, unmanaged C++: Pointer to an array of type long of reference types as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

- in-process, unmanaged C++: Pointer to an array of references

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ILibraryFeatureData::GetReferencesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILibraryFeatureData~GetReferencesCount.html) to determine the size of the array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::GetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferences.html)
[ILibraryFeatureData::SetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~SetReferences.html)
[ILibraryFeatureData::ISetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~ISetReferences.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
