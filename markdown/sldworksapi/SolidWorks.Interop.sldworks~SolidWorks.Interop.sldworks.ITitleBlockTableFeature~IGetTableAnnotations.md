---
title: "IGetTableAnnotations Method (ITitleBlockTableFeature)"
project: "SOLIDWORKS API Help"
interface: "ITitleBlockTableFeature"
member: "IGetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableFeature~IGetTableAnnotations.html"
---

# IGetTableAnnotations Method (ITitleBlockTableFeature)

Gets all of the title block table annotations in this title block table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTableAnnotations( _
   ByVal Count As System.Integer _
) As TitleBlockTableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As ITitleBlockTableFeature
Dim Count As System.Integer
Dim value As TitleBlockTableAnnotation

value = instance.IGetTableAnnotations(Count)
```

### C#

```csharp
TitleBlockTableAnnotation IGetTableAnnotations(
   System.int Count
)
```

### C++/CLI

```cpp
TitleBlockTableAnnotation^ IGetTableAnnotations(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of annotations in this title block feature

### Return Value

- in-process, unmanaged C++: Pointer to an array of [title block table annotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITitleBlockTableAnnotation.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ITitleBlockTableFeature::GetTableAnnotationCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITitleBlockTableFeature~GetTableAnnotationCount.html) to get the value for Count.

## See Also

[ITitleBlockTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableFeature.html)
[ITitleBlockTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
