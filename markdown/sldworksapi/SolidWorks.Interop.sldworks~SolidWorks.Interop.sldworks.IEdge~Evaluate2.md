---
title: "Evaluate2 Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "Evaluate2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Evaluate2.html"
---

# Evaluate2 Method (IEdge)

Evaluates the edge for the specified U parameter.

## Syntax

### Visual Basic (Declaration)

```vb
Function Evaluate2( _
   ByVal Parameter As System.Double, _
   ByVal NumberOfDerivatives As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim Parameter As System.Double
Dim NumberOfDerivatives As System.Integer
Dim value As System.Object

value = instance.Evaluate2(Parameter, NumberOfDerivatives)
```

### C#

```csharp
System.object Evaluate2(
   System.double Parameter,
   System.int NumberOfDerivatives
)
```

### C++/CLI

```cpp
System.Object^ Evaluate2(
   System.double Parameter,
   System.int NumberOfDerivatives
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Parameter`: Curve parameter U value (see

Remarks

)
- `NumberOfDerivatives`: Number of derivatives (see

Remarks

)

### Return Value

Array of doubles

kadov_tag{{<spaces>}}

kadov_tag{{</spaces>}}

(see

Remarks

)

## VBA Syntax

See

[Edge::Evaluate2](ms-its:sldworksapivb6.chm::/sldworks~Edge~Evaluate2.html)

.

## Examples

1. Open a part in SOLIDWORKS.
2. Open an Immediate window.
3. Select an edge.
4. Run this VBA macro:

```
=========================================================
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim boolstatus As BooleanDim longstatus As Long, longwarnings As Long
```

```
Type DoubleRec
     dValue As Double '64 bits, 8 bytes
End Type
```

```
Type Int2Rec
     iLower As Long '4 bytes
     iUpper As Long '4 bytes
End Type
```

```
' Unpack the status double
Function DoubleToLong(ByVal dVal As Double) As Long
    Dim dr As DoubleRec
    Dim i2r As Int2Rec
    ' Set the double value
    dr.dValue = dVal
    ' Copy the values
    LSet i2r = dr
    ' Extract the status value
    DoubleToLong = i2r.iLower
End Function
```

```
Sub main()
```

```
    Dim status As Long
    Set swApp = Application.SldWorks
    Set Part = swApp.ActiveDoc
    Dim myModelView As SldWorks.ModelView
    Set myModelView = Part.ActiveView
    myModelView.FrameState = swWindowState_e.swWindowMaximized
    Dim swSelectMgr As SldWorks.SelectionMgr
    Set swSelectMgr = Part.SelectionManager
    Dim swEdge As SldWorks.Edge
    Set swEdge = swSelectMgr.GetSelectedObject6(1, -1)
    Dim swCurve As SldWorks.Curve
    Dim swCurveParamData As SldWorks.CurveParamData
    Set swCurve = swEdge.GetCurve
    Set swCurveParamData = swEdge.GetCurveParams3
    Debug.Print "The maximum U parameter value is: " & swCurveParamData.UMaxValue
    Debug.Print "The minimum U parameter value is: " & swCurveParamData.UMinValue
    Dim pt As Variant
    pt = swEdge.Evaluate2(swCurveParamData.UMaxValue, 0)
    status = DoubleToLong(pt(UBound(pt)))
    If status Then
        Debug.Print " The evaluated point at UMax is:   = " & pt(0) & ", " & pt(1) & ", " & pt(2)
    Else
        Debug.Print "***** Error!"
    End If
```

```
End Sub
====================================================================
```

## Remarks

Use[IEdge::GetCurveParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams3.html)to determine the valid range of U parameter values for Parameter.

The returned array contains ((NumberOfDerivatives + 1) * 3) + 1 doubles:

[evaluated_point],[evaluated_derivative_1],...[evaluated_derivative_NumberOfDerivatives,**[**`status_code`**]**

where`status_code`is a packed double. After unpacking`status_code`into two longs, the lower long value is 1 for success or 0 for error. See the Example.

| If curve type ICurve::Identity is... | Then the maximum number of derivatives is... |
| --- | --- |
| Line/circle/ellipse | 2 |
| Intersection curve | 2 |
| Constant parameter line | Determined by underlying surface |
| SP-curve | 2 |
| B-curve | Any number |

For a curve of type swCurveTypes_e::TRIMMED_TYPE, the number of derivatives is determined by the base curve as obtained from[ICurve::GetBaseCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~GetBaseCurve.html).

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)

[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
