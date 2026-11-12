---
title: "ISetReferences Method (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "ISetReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~ISetReferences.html"
---

# ISetReferences Method (ILibraryFeatureData)

Sets the references for the library feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetReferences( _
   ByVal Count As System.Integer, _
   ByRef RefVar As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim Count As System.Integer
Dim RefVar As System.Object

instance.ISetReferences(Count, RefVar)
```

### C#

```csharp
void ISetReferences(
   System.int Count,
   ref System.object RefVar
)
```

### C++/CLI

```cpp
void ISetReferences(
   System.int Count,
   System.Object^% RefVar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of references
- `RefVar`: - in-process, unmanaged C++: Pointer to an array of references

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::GetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferences.html)
[ILibraryFeatureData::GetReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferencesCount.html)
[ILibraryFeatureData::IGetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetReferences.html)
[ILibraryFeatureData::SetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~SetReferences.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
