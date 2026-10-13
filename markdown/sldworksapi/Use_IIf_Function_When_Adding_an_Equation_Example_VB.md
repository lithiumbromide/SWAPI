---
title: "Use IIf Function When Adding an Equation Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Use_IIf_Function_When_Adding_an_Equation_Example_VB.htm"
---

# Use IIf Function When Adding an Equation Example (VBA)

This example shows how to use the Visual Basic IIf function when adding an equation.

```
'-----------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\cover_with_dimensions.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Adds an equation using the Visual Basic IIf function.
' 2. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'-----------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swEqnMgr As SldWorks.EquationMgr
    Dim i As Long
    Dim nCount As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swEqnMgr = swModel.GetEquationMgr
    Debug.Print "File = " & swModel.GetPathName
    nCount = swEqnMgr.GetCount
```

```
    ' List the existing equations and their calculated values
    For i = 0 To nCount - 1
        Debug.Print "  Eqn(" & i & ") = " & swEqnMgr.Equation(i)
        Debug.Print "    Value = " & swEqnMgr.Value(i)
    Next i
```

```
   ' Add and solve an equation that uses the Visual Basic IIf function
   ' Delay evaluating the equation by passing false into the third
   ' argument of Add2
    swEqnMgr.Add2 i, ("""TXD2@Scheme15"" = (IIf(""TXD1@Scheme15"">20, 25, 20))+3"), False
    Debug.Print "  Eqn(" & i & ") = " & swEqnMgr.Equation(i)
```

```
    ' Evaluate all equations
    Dim ret As Integer
    ret = swEqnMgr.EvaluateAll
    Debug.Print "    Value = " & swEqnMgr.Value(i)
    Debug.Print "    Index of equation = " & swEqnMgr.Status
```

```
End Sub
```
