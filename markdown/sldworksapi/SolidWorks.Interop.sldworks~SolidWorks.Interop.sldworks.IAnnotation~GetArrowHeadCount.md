---
title: "GetArrowHeadCount Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetArrowHeadCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadCount.html"
---

# GetArrowHeadCount Method (IAnnotation)

Gets the number of arrowheads on this symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArrowHeadCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Integer

value = instance.GetArrowHeadCount()
```

### C#

```csharp
System.int GetArrowHeadCount()
```

### C++/CLI

```cpp
System.int GetArrowHeadCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of arrowheads on this annotation

## VBA Syntax

See [Annotation::GetArrowHeadCount](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetArrowHeadCount.html).

## Remarks

This method works with traditional leaders on annotations and [multijog leaders](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMultiJogLeader.html).

Call this method before calling [IAnnotation::GetArrowHeadSizeAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetArrowHeadSizeAtIndex.html) to specify the annotation for which to get the arrow head size.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::SetArrowHeadSizeAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadSizeAtIndex.html)
[IAnnotation::GetArrowHeadStyleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadStyleAtIndex.html)
[IAnnotation::SetArrowHeadStyleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadStyleAtIndex.html)

## Availability

SOLIDWORKS 2008 SP1, Revision Number 16.1
