---
title: "Select All Fillets Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_All_Fillets_Example_VB.htm"
---

# Select All Fillets Example (VBA)

Selecting all of the fillets on an active part is done by iterating through all of the features with IModelDoc2::FirstFeature and IFeature::GetNextFeature. For each feature, check the type with IFeature::GetTypeName and compare it to the "Fillet" and "VarFillet" constants to see if the current feature is a fillet. If the feature is a fillet, then place the fillet in an IEntity object and select the entity.

```vb
'------------------------------------------------------------------
'
' Preconditions:
'     (1) Part document is open.
'     (2) Fillets exist on the part.
'
' Postconditions: All of the fillets are selected.
'
'------------------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim Model As SldWorks.ModelDoc2
Dim CurFeature As SldWorks.feature
Dim CurEntity As SldWorks.entity
Dim SelData As SldWorks.SelectData

Sub main()
    ' Get the SOLIDWORKS Design object and the active model
    Set swApp = GetObject(, "SldWorks.Application")
    Set Model = swApp.ActiveDoc

    ' Get the first feature on the part
    Set CurFeature = Model.FirstFeature
    ' For all of the features on the part
    Do While Not CurFeature Is Nothing
       ' If the current feature is one of the fillet types,
       ' then select the current fillet
        If CurFeature.GetTypeName = "Fillet" Or CurFeature.GetTypeName = "VarFillet" Then
            Set CurEntity = CurFeature
            CurEntity.Select4 True, SelData
        End If
        'Go to the next feature
        Set CurFeature = CurFeature.GetNextFeature
    Loop
End Sub
```
