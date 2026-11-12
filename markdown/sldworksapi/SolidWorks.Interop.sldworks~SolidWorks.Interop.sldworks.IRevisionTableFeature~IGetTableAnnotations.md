---
title: "IGetTableAnnotations Method (IRevisionTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IRevisionTableFeature"
member: "IGetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature~IGetTableAnnotations.html"
---

# IGetTableAnnotations Method (IRevisionTableFeature)

Gets the revision table annotations for this revision table.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTableAnnotations( _
   ByVal Count As System.Integer _
) As RevisionTableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionTableFeature
Dim Count As System.Integer
Dim value As RevisionTableAnnotation

value = instance.IGetTableAnnotations(Count)
```

### C#

```csharp
RevisionTableAnnotation IGetTableAnnotations(
   System.int Count
)
```

### C++/CLI

```cpp
RevisionTableAnnotation^ IGetTableAnnotations(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of revision table annotations

### Return Value

- in-process, unmanaged C++: Pointer to an array of the [revision table annotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableAnnotation.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IRevisionTableFeature::GetTableAnnotationCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableFeature~GetTableAnnotationCount.html) before calling this method to get the value of Count.

## See Also

[IRevisionTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature.html)
[IRevisionTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature_members.html)
[IRevisionTableFeature::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature~GetTableAnnotations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
