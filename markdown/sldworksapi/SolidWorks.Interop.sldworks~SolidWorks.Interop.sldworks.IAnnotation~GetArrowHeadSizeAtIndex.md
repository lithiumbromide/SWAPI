---
title: "GetArrowHeadSizeAtIndex Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetArrowHeadSizeAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadSizeAtIndex.html"
---

# GetArrowHeadSizeAtIndex Method (IAnnotation)

Gets the arrow head size of the specified leader on this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArrowHeadSizeAtIndex( _
   ByVal Index As System.Integer, _
   ByRef UseDoc As System.Boolean, _
   ByRef Length As System.Double, _
   ByRef Width As System.Double, _
   ByRef Height As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim Index As System.Integer
Dim UseDoc As System.Boolean
Dim Length As System.Double
Dim Width As System.Double
Dim Height As System.Double
Dim value As System.Boolean

value = instance.GetArrowHeadSizeAtIndex(Index, UseDoc, Length, Width, Height)
```

### C#

```csharp
System.bool GetArrowHeadSizeAtIndex(
   System.int Index,
   out System.bool UseDoc,
   out System.double Length,
   out System.double Width,
   out System.double Height
)
```

### C++/CLI

```cpp
System.bool GetArrowHeadSizeAtIndex(
   System.int Index,
   [Out] System.bool UseDoc,
   [Out] System.double Length,
   [Out] System.double Width,
   [Out] System.double Height
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of leader on this annotation
- `UseDoc`: TRUE indicates that the document default setting for arrow head size was used, FALSE
  indicates that the Length, Width, and Height values were specified
- `Length`: Length of arrow head
- `Width`: Width of arrow head
- `Height`: Height of arrow head

### Return Value

True if the method succeeds, false if not

## VBA Syntax

See [Annotation::GetArrowHeadSizeAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetArrowHeadSizeAtIndex.html).

## Remarks

The index value is 0-based. Therefore, a valid index value is greater than or equal to 0, but less than the number of leaders on this annotation. Use [IAnnotation::GetArrowHeadCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetArrowHeadCount.html) to find the number of leaders on this annotation. If the index value is invalid, SOLIDWORKS returns the arrowhead style as -1, and returns an S_FALSE status (COM interface).

Use [IAnnotation::SetArrowHeadSizeAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~SetArrowHeadSizeAtIndex.html) to set the arrow head size of a specific leader.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetArrowHeadStyleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadStyleAtIndex.html)
[IAnnotation::SetArrowHeadStyleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadStyleAtIndex.html)

## Availability

SOLIDWORKS 2008 SP1, Revision Number 16.1
