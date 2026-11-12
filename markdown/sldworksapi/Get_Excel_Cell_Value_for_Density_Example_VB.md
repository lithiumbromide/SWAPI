---
title: "Get Excel Cell Value for Density Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Excel_Cell_Value_for_Density_Example_VB.htm"
---

# Get Excel Cell Value for Density Example (VBA)

This example shows how to get a density value from an active Excel worksheet and use that density for the active part.

```vb
'---------------------------------------------
Sub main()

' Define variable used to hold the ISldWorks object
Dim swApp As Object

' Define variable used to hold the IModelDoc object
Dim Part As Object

' Constant enumerators
Const swDocPART = 1
Const swMaterialPropertyDensity = 7

Set swApp = CreateObject ("SldWorks.Application")

' Get handle to the active SOLIDWORKS Design part
Set Part = swApp.ActiveDoc

' If not a part, then exit
If (Part.GetType <> swDocPART) Then
Exit Sub
End if

' Attaches to the active Excel object
Set xl = GetObject(, "Excel.Application")

' Get handle to the active sheet in Excel
Set xlsh = xl.ActiveSheet

' Gets value in cell A1
density = xlsh.Cells(1,1)

' Set the density in the SOLIDWORKS part
Part.SetUserPreferenceDoubleValue swMaterialPropertyDensity, density

End Sub
```
