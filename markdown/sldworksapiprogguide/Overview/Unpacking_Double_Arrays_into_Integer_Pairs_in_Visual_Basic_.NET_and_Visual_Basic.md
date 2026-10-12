---
title: "Unpacking and Packing Arrays in Visual Basic .NET and Visual Basic"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Unpacking_Double_Arrays_into_Integer_Pairs_in_Visual_Basic_.NET_and_Visual_Basic.htm"
---

# Unpacking and Packing Arrays in Visual Basic .NET and Visual Basic

Some of the arguments passed from and to SOLIDWORKS using the API contain arrays of doubles. In some functions, elements in these arrays contain two integers packed into a double array element. You can unpack the data from a double to two integers and vice versa.

- [Visual Basic .NET](#NET)
- [Visual Basic for Applications (VBA)](#6)

### Visual Basic .NET

```vb
Imports System.Runtime.InteropServices
Module Module1
    Sub Main()
        Dim iValueIn1 As Integer = 65535
        Dim iValueIn2 As Integer = 345
        Dim dValueOut As Double
        Dim iValueOut1 As Integer
        Dim iValueOut2 As Integer
        DoubleIntConv.Pack(iValueIn1, iValueIn2, dValueOut)
        DoubleIntConv.Unpack(dValueOut, iValueOut1, iValueOut2)
    End Sub

    <System.Runtime.InteropServices.StructLayout(LayoutKind.Explicit)> _
    Public Class DoubleIntConv
        'An 8-byte double contains 2 4-byte ints.
        <System.Runtime.InteropServices.FieldOffset(0)> Private m_Int1 As Integer
        <System.Runtime.InteropServices.FieldOffset(4)> Private m_Int2 As Integer
        <System.Runtime.InteropServices.FieldOffset(0)> Private m_Double As Double

        Private Sub New(ByVal dValue As Double)
            'VB.NET wants these initialized in the constructor
            m_Int1 = 0
            m_Int2 = 0
            m_Double = dValue
        End Sub

        Private Sub New(ByVal iValue1 As Integer, ByVal iValue2 As Integer)
            'VB.NET wants these initialized in the constructor
            m_Double = 0.0
            m_Int1 = iValue1
            m_Int2 = iValue2
        End Sub

        'Use out parameters, so client code can pass in an uninitialized variable
        'Unpack
        Public Shared Sub Unpack(ByVal dIn As Double, ByRef iOut1 As Integer, ByRef iOut2 As Integer)
            Dim cv As DoubleIntConv
            cv = New DoubleIntConv(dIn)
            iOut1 = cv.m_Int1
            iOut2 = cv.m_Int2
        End Sub

        'Use an out parameter, so client code can pass in an uninitialized variable
        'Pack
        Public Shared Sub Pack(ByVal iIn1 As Integer, ByVal iIn2 As Integer, ByRef dOut As Double)
            Dim cv As DoubleIntConv
            cv = New DoubleIntConv(iIn1, iIn2)
            dOut = cv.m_Double
        End Sub
    End Class
End Module
```

[Back to top](#Top)

### Visual Basic for Applications (VBA)

```vb
' Define two types
Type DoubleRec
    dValue As Double
End Type

Type Int2Rec
```

```vb
iLower As Long 'Assuming that a C int has 4 bytes
iUpper As Long
```

```vb
End Type

' Extract two integer values out of a single double value
' by assigning a DoubleRec to the double value and then
' copying the value over to an Int2Rec and
' extracting the integer values
Function ExtractFields(dValue As Double, iLower As Integer, iUpper As Integer)
```

```vb
Dim dr As DoubleRec, i2r As Int2Rec

' Set the double value
dr.dValue = dValue

' Copy the values
LSet i2r = dr

' Extract the values
iLower = i2r.iLower
iUpper = i2r.iUpper
```

```vb
End Function

Private Sub main()
```

```vb
Dim Params As Variant
Dim dElement As Double
Dim SplineDim As Integer
Dim SplineOrder As Integer
Dim SplineNCtrls As Integer
Dim SplinePeriodic As Integer

Set swApp = CreateObject("SldWorks.Application")
Set Part = swApp.ActiveDoc()
Set Sketch = Part.GetActiveSketch()

Params = Sketch.GetSplineParams

dElement = Params(0)
ExtractFields dElement, SplineDim, SplineOrder
dElement = Params(1)
ExtractFields dElement, SplineNCtrls, SplinePeriodic
```

```vb
End Sub

See:
```

-

  ```vb
   Create Reference Curve Example (VB.NET)
  ```
-

  ```vb
   Create Reference Curve Example (VBA)
  ```

[Back to top](#Top)
