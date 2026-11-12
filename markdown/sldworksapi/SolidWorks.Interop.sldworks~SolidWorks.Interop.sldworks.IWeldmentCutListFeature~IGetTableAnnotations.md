---
title: "IGetTableAnnotations Method (IWeldmentCutListFeature)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentCutListFeature"
member: "IGetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~IGetTableAnnotations.html"
---

# IGetTableAnnotations Method (IWeldmentCutListFeature)

Gets the weldment cut list annotations for this weldment cut list table.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTableAnnotations( _
   ByVal Count As System.Integer _
) As WeldmentCutListAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentCutListFeature
Dim Count As System.Integer
Dim value As WeldmentCutListAnnotation

value = instance.IGetTableAnnotations(Count)
```

### C#

```csharp
WeldmentCutListAnnotation IGetTableAnnotations(
   System.int Count
)
```

### C++/CLI

```cpp
WeldmentCutListAnnotation^ IGetTableAnnotations(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of weldment cut list annotations for this weldment cut list feature

### Return Value

- in-process, unmanaged C++: Pointer to an array of [weldment cut-list annotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentCutListAnnotation.html) for this weldment cut list table

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IWeldmentCutListFeature::GetTableAnnotationCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentCutListFeature~GetTableAnnotationCount.html) to get Count.

## See Also

[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.html)
[IWeldmentCutListFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature_members.html)
[IWeldmentCutListFeature::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~GetTableAnnotations.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
