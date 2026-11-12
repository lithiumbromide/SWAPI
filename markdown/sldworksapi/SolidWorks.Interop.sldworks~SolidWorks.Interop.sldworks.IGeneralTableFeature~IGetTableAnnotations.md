---
title: "IGetTableAnnotations Method (IGeneralTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IGeneralTableFeature"
member: "IGetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature~IGetTableAnnotations.html"
---

# IGetTableAnnotations Method (IGeneralTableFeature)

Gets the table annotations for this general table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTableAnnotations( _
   ByVal Count As System.Integer _
) As TableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IGeneralTableFeature
Dim Count As System.Integer
Dim value As TableAnnotation

value = instance.IGetTableAnnotations(Count)
```

### C#

```csharp
TableAnnotation IGetTableAnnotations(
   System.int Count
)
```

### C++/CLI

```cpp
TableAnnotation^ IGetTableAnnotations(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of table annotations

### Return Value

- in-process, unmanaged C++: Pointer to an array of [IGeneralTableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGeneralTableAnnotation.html) objects

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IGeneralTableFeature::GetTableAnnotationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature~GetTableAnnotationCount.html) before calling this method to get the size of the array.

## See Also

[IGeneralTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature.html)
[IGeneralTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature_members.html)
[IGeneralTableFeature::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature~GetTableAnnotations.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
