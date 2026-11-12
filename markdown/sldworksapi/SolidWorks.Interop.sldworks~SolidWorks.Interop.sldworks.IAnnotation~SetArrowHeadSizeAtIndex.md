---
title: "SetArrowHeadSizeAtIndex Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "SetArrowHeadSizeAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadSizeAtIndex.html"
---

# SetArrowHeadSizeAtIndex Method (IAnnotation)

Sets the size of the arrow head of the specified leader on this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetArrowHeadSizeAtIndex( _
   ByVal Index As System.Integer, _
   ByVal UseDoc As System.Boolean, _
   ByVal Length As System.Double, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double _
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

value = instance.SetArrowHeadSizeAtIndex(Index, UseDoc, Length, Width, Height)
```

### C#

```csharp
System.bool SetArrowHeadSizeAtIndex(
   System.int Index,
   System.bool UseDoc,
   System.double Length,
   System.double Width,
   System.double Height
)
```

### C++/CLI

```cpp
System.bool SetArrowHeadSizeAtIndex(
   System.int Index,
   System.bool UseDoc,
   System.double Length,
   System.double Width,
   System.double Height
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of leader on this annotation
- `UseDoc`: True to use the document default setting for arrow head size, false to use the specified Length, Width, and Height values
- `Length`: Length of leader on this annotation
- `Width`: Width of leader on this annotation
- `Height`: Height of leader on this annotation

## VBA Syntax

See [Annotation::SetArrowHeadSizeAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Annotation~SetArrowHeadSizeAtIndex.html).

## Remarks

Use [IAnnotation::GetArrowHeadSizeAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetArrowHeadSizeAtIndex.html) to get the arrow head size of a specific leader.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadCount.html)
[IAnnotation::GetArrowHeadStyleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadStyleAtIndex.html)
[IAnnotation::SetArrowHeadStyleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadStyleAtIndex.html)

## Availability

SOLIDWORKS 2008 SP1, Revision Number 16.1
