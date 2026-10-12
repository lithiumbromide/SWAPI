---
title: "GetArrowHeadStyleAtIndex Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetArrowHeadStyleAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadStyleAtIndex.html"
---

# GetArrowHeadStyleAtIndex Method (IAnnotation)

Gets the arrow head style of a specific leader on this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArrowHeadStyleAtIndex( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim Index As System.Integer
Dim value As System.Integer

value = instance.GetArrowHeadStyleAtIndex(Index)
```

### C#

```csharp
System.int GetArrowHeadStyleAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetArrowHeadStyleAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of leader within this annotation (see **Remarks**)

### Return Value

Arrowhead style as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

## VBA Syntax

See [Annotation::GetArrowHeadStyleAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetArrowHeadStyleAtIndex.html).

## Remarks

The index value is 0-based. Therefore, a valid index value is greater than or equal to 0, but less than the number of leaders on this annotation. Use [IAnnotation::GetArrowHeadCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetArrowHeadCount.html) to find the number of leaders on this annotation. If the index value is invalid, SOLIDWORKS returns the arrowhead style as -1, and returns an S_FALSE status (COM interface).

Use [IAnnotation::SetArrowHeadStyleAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~SetArrowHeadStyleAtIndex.html) to set the arrow head style of a specific leader.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::SetArrowHeadStyleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadStyleAtIndex.html)

## Availability

SOLIDWORKS 99, datecode 1999207
