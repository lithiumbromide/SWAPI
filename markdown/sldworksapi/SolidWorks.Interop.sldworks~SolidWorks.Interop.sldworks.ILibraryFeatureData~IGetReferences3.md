---
title: "IGetReferences3 Method (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "IGetReferences3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetReferences3.html"
---

# IGetReferences3 Method (ILibraryFeatureData)

Gets the references with respect to the specified scope.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetReferences3( _
   ByVal Scope As System.Integer, _
   ByVal Count As System.Integer, _
   ByRef RefType As System.Integer, _
   ByRef RefName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim Scope As System.Integer
Dim Count As System.Integer
Dim RefType As System.Integer
Dim RefName As System.String
Dim value As System.Object

value = instance.IGetReferences3(Scope, Count, RefType, RefName)
```

### C#

```csharp
System.object IGetReferences3(
   System.int Scope,
   System.int Count,
   out System.int RefType,
   out System.string RefName
)
```

### C++/CLI

```cpp
System.Object^ IGetReferences3(
   System.int Scope,
   System.int Count,
   [Out] System.int RefType,
   [Out] System.String^ RefName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Scope`: Reference scope as defined in [swLibFeatureData_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLibFeatureData_e.html)
- `Count`: Number of references
- `RefType`: - In-process, unmanaged C++: Pointer to an array of type long of reference types as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `RefName`: - In-process, unmanaged C++: Pointer to an array of reference names
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

- In-process, unmanaged C++: Pointer to an array of references

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ILibraryFeatureData::GetReferencesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILibraryFeatureData~GetReferencesCount.html) to determine the size of the array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::GetReferences3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferences3.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
