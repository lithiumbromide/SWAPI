---
title: "GetCenterMarkInfo Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetCenterMarkInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkInfo.html"
---

# GetCenterMarkInfo Method (IView)

Gets information about each center mark that is a feature in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCenterMarkInfo() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetCenterMarkInfo()
```

### C#

```csharp
System.object GetCenterMarkInfo()
```

### C++/CLI

```cpp
System.Object^ GetCenterMarkInfo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [View::GetCenterMarkInfo](ms-its:sldworksapivb6.chm::/sldworks~View~GetCenterMarkInfo.html).

## Remarks

Center marks are now annotations. Previously, center marks were features. This method is only valid for center marks that are features.

The return value is the following array of doubles:

[ numCenterMarks, [ numCenterMarkLines, lineType1, plus1StartPt[3], plus1EndPt[3], lineType2, plus2StartPt[3], plus2EndPt[3], [ lineType, lineStartPt[3], lineEndPt[3] ] ] ]

where:

numCenterMarks = is the number of center marks in this view. See also [IView::GetCenterMarkCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetCenterMarkCount2.html).

The following set of data repeats itself for each center mark in the view. The number of times the information is given is numCenterMarks:

numCenterMarkLines = number of centermark lines in the current center mark. Every center mark has at least two lines. These two lines represent the plus at the center of the circle.

lineType1 = line type associated with the first plus-sign line. See the [swLineTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) enumeration.

plus1StartPt[3] = X,Y,Z start point of the first line in the plus sign.

plus1EndPt[3] = X,Y,Z end point of the first line in the plus sign.

lineType2 = line type associated with the second plus-sign line. See the [swLineTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) enumeration.

plus2StartPt[3] = X,Y,Z start point of the second line in the plus sign.

plus2EndPt[3] = X,Y,Z end point of the second line in the plus sign.

This set of data also repeats itself for the remaining centermark lines in this particular center mark. The number of times this information is given is (numCenterMarkLines - 2):

LineType = line type associated with the second plus-sign line. See the [swLineTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) enumeration.

lineStartPt[3] = X,Y,Z start point for this centermark line.

lineEndPt[3] = X,Y,Z end point for this centermark line.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarks.html)
[IView::GetFirstCenterMark Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterMark.html)
[IView::IGetCenterMarkInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterMarkInfo.html)
[IView::IGetCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterMarks.html)
[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[IView::AutoInsertCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AutoInsertCenterMarks.html)
