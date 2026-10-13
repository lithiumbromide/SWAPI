---
title: "Add Equation and Evaluate All Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Equation_And_Evaluate_All_Example_VBNET.htm"
---

# Add Equation and Evaluate All Example (VB.NET)

This example shows how to use IEquationMgr interfaces to add an equation to a model and delay evaluation until all equations are added.

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
#Const ccTIMER = 1
```

```vb
    Public Sub Main()
        Dim swModel As ModelDoc2
        swModel = swApp.ActiveDoc
        Dim MyEqu As EquationMgr
        Dim Index As Integer
        Dim lValue As Long
        Dim evalStatus As Long
        #If ccTIMER = 1 Then
            Dim t1 As Single
            Dim t2 As Single
        #Else
            Dim t1     As Date
            Dim t2     As Date
        #End If
        Dim i As Long
        i = 0
        MyEqu = swModel.GetEquationMgr
        If MyEqu.GetCount > 0 Then
            Do While (i < 26)
                MyEqu.Delete(0)
                i = i + 1
            Loop
        End If
        Debug.Print("Delaying evaluation of equations until the end...")
        For Index = Asc("A") To Asc("Z")
        #If ccTIMER = 1 Then
                t1 = Timer
        #Else
            t1 = Now
        #End If
            'Delay solving each equation until after all equations are
             'added (set solve parameter to false)
             'FeatureManager design tree not updated
            lValue = MyEqu.Add2(Index, """" & Microsoft.VisualBasic.Chr(Index) & """=" & Index, False)
        #If ccTIMER = 1 Then
                t2 = Timer
        #Else
            t2 = Now
        #End If
            Debug.Print("Time of evaluation for character " + Microsoft.VisualBasic.Chr(Index) + ": ")
            Debug.Print(t2 - t1)
        Next Index
        Debug.Print("Number of equations added to EquationMgr is " & MyEqu.GetCount)
        'Solve all equations after they have been added
         'FeatureManager design tree updated
        Debug.Print("Evaluating all equations...")
        evalStatus = MyEqu.EvaluateAll()
        Debug.Print("Finished Add2 and EvaluateAll")
        MyEqu = Nothing
        swModel = Nothing
        'swApp.CloseAllDocuments True
        swApp = Nothing
    End Sub
    Public swApp As SldWorks
End Class
```
