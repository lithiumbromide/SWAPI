---
title: "SetArrowHeadStyleAtIndex Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "SetArrowHeadStyleAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadStyleAtIndex.html"
---

# SetArrowHeadStyleAtIndex Method (IAnnotation)

Sets the arrow head style of a specific leader on this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetArrowHeadStyleAtIndex( _
   ByVal Index As System.Integer, _
   ByVal ArrowHeadStyle As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim Index As System.Integer
Dim ArrowHeadStyle As System.Integer
Dim value As System.Integer

value = instance.SetArrowHeadStyleAtIndex(Index, ArrowHeadStyle)
```

### C#

```csharp
System.int SetArrowHeadStyleAtIndex(
   System.int Index,
   System.int ArrowHeadStyle
)
```

### C++/CLI

```cpp
System.int SetArrowHeadStyleAtIndex(
   System.int Index,
   System.int ArrowHeadStyle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of leader within this annotation (see **Remarks**)
- `ArrowHeadStyle`: Arrowhead style as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

### Return Value

Return status (see **Remarks**)

## VBA Syntax

See [Annotation::SetArrowHeadStyleAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Annotation~SetArrowHeadStyleAtIndex.html).

## Remarks

A valid index value is greater than or equal to 0, but less than the number of leaders on this annotation. Use [IAnnotation::GetArrowHeadCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetArrowHeadCount.html) to find out how many leaders are on this annotation. An index value of -1 is also valid, and indicates that this arrowhead style should be applied to all leaders on this annotation. If the index value is
invalid, SOLIDWORKS returns a retval of -2.

If smart arrowhead style is enabled on this annotation, then this method cannot change
the arrowhead style of individual leaders, and retval is -3. Use [IAnnotation::GetSmartArrowHeadStyle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetSmartArrowHeadStyle.html) to determine if this flag is enabled or disabled.

The return status of this method can have the following values:

| If value equals... | Then the arrowhead style was... |
| --- | --- |
| 0 | Successfully set |
| -1 | Not set because of an unknown error |
| -2 | Not set because of an invalid index value |
| -3 | Not set because of smart arrowhead styles being enabled |
| -4 | Not set because of an invalid arrowhead style value |

If leader display is enabled, then this method changes the visible model. To see those
changes, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to reddraw the graphics window.

Use [IAnnotation::GetArrowHeadStyleAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetArrowHeadStyleAtIndex.html) to get the arrow head style of a specific leader.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::SetArrowHeadSizeAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadSizeAtIndex.html)
[IAnnotation::GetArrowHeadSizeAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadSizeAtIndex.html)
[IAnnotation::GetArrowHeadStyleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadStyleAtIndex.html)
[IAnnotation::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadCount.html)
