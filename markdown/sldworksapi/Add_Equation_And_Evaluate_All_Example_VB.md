---
title: "Add Equation and Evaluate All Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Equation_And_Evaluate_All_Example_VB.htm"
---

# Add Equation and Evaluate All Example (VBA)

This example shows how to use IEquationMgr interface to add an equation to a model and delay evaluation until all equations are added.

```
'------------------------------------------------------------------------
' Preconditions:
' 1. Open any model document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Rebuild the model.
' 2. Observe the 26 (A-Z) new equations in the Equations folder in the
'    FeatureManager design tree.
' 3. Observe the near-zero evaluation time for each equation in the
'    Immediate Window, demonstrating that the evaluations were delayed.
'------------------------------------------------------------------------
Option Explicit
```

```
#Const ccTIMER = 1
```

```
Public Sub Main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
```

```
    Set swApp = Application.SldWorks

    Dim errors As Long
    Dim warnings As Long
```

```
    Set swModel = swApp.ActiveDoc
    Dim MyEqu As SldWorks.EquationMgr
```

```
    Dim Index As Integer
    Dim lValue As Long
    Dim evalStatus As Long
```

```
    #If ccTIMER = 1 Then
        Dim t1 As Single
        Dim t2 As Single
    #Else
        Dim t1 As Date
        Dim t2 As Date
    #End If
```

```
    Dim i As Long
    i = 0
    Set MyEqu = swModel.GetEquationMgr
    If MyEqu.GetCount > 0 Then
         Do While (i < 26)
             MyEqu.Delete (0)
             i = i + 1
         Loop
     End If
```

```
     For Index = Asc("A") To Asc("Z")
         #If ccTIMER = 1 Then
             t1 = Timer
         #Else
             t1 = Now
         #End If
```

```
         'Delay solving each equation until after all equations are
         'added (set solve parameter to false)
         'FeatureManager design tree not updated
         lValue = MyEqu.Add2(Index, """" & Chr$(Index) & """=" & Index, False)
```

```
         #If ccTIMER = 1 Then
            t2 = Timer
         #Else
            t2 = Now
         #End If
```

```
         Debug.Print "Time of evaluation: "
         Debug.Print (t2 - t1)
   Next Index
```

```
   Debug.Print "Number of equations added to EquationMgr is " & MyEqu.GetCount
```

```
   'Solve all equations after they have been added
   'FeatureManager design tree updated
   evalStatus = MyEqu.EvaluateAll
```

```
   Debug.Print "Finished Add2 and EvaluateAll"
```

```
   Set MyEqu = Nothing
   Set swModel = Nothing
   'swApp.CloseAllDocuments True
   Set swApp = Nothing
```

```
End Sub
```
