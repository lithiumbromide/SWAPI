---
title: "IGetBendLines Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetBendLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBendLines.html"
---

# IGetBendLines Method (IView)

Gets the bendlines in a [flat-pattern drawing view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IsFlatPatternView.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBendLines( _
   ByVal NumberOfBendLine As System.Integer _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim NumberOfBendLine As System.Integer
Dim value As SketchSegment

value = instance.IGetBendLines(NumberOfBendLine)
```

### C#

```csharp
SketchSegment IGetBendLines(
   System.int NumberOfBendLine
)
```

### C++/CLI

```cpp
SketchSegment^ IGetBendLines(
   System.int NumberOfBendLine
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumberOfBendLine`: Number of [bendlines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) in a flat-pattern drawing view

### Return Value

- in-process, unmanaged C++: Pointer to an array of bendlines in a flat-pattern view

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IView::GetBendLineCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetBendLineCount.html) to get NumberOfBendLine.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetBendLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendLines.html)
[ISketchSegment::IsBendLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IsBendLine.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
