---
title: "Get and Override Mass Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mass_Properties_using_MassProperty_Object_Example_VB.htm"
---

# Get and Override Mass Properties Example (VBA)

This example shows how to get and override some mass properties of a part.

```vb
 '-----------------------------------------------------------------------
' Preconditions:
' 1. Ensure the specified document exists.
' 2. Open the Immediate window.
'
' Postconditions: Inspect the Immediate window.
 '----------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
Dim Extn As SldWorks.ModelDocExtension
Dim MyMassProp As SldWorks.MassProperty2
Dim OvProp As SldWorks.MassPropertyOverrideOptions
Dim swModelDoc As SldWorks.ModelDoc2
Dim pmoi As Variant
Dim vValue As Variant
Dim value(2) As Double
Dim errors As Long
Dim warnings As Long
Dim val As Double
Dim params As Variant

Option Explicit
Sub main()

    Set swApp = Application.SldWorks
    Set swModelDoc = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2020\samples\tutorial\advdrawings\98food processor.sldasm", swDocASSEMBLY, swOpenDocOptions_Silent, "", errors, warnings)
    Set Extn = swModelDoc.Extension

    ' Create mass properties and override options
    Set MyMassProp = Extn.CreateMassProperty2
    Set OvProp = MyMassProp.GetOverrideOptions
     OvProp.OverrideMass = True
     OvProp.SetOverrideMassValue (100)
    Dim comArr(8) As Double
     comArr(0) = 0.1677
     comArr(1) = 0
     comArr(2) = 0
     comArr(3) = 0
     comArr(4) = 0.21358
     comArr(5) = 0
     comArr(6) = 0
     comArr(7) = 0
     comArr(8) = 0.34772
     OvProp.OverrideMomentsOfInertia = True
     OvProp.SetOverrideMomentsOfInertiaValue 0, comArr, ""

    ' Use document property units (MKS)
     MyMassProp.UseSystemUnits = False

     Debug.Print "Mass properties before override"
     Debug.Print ""

    val = MyMassProp.Mass
     Debug.Print "Mass: " & val
    val = MyMassProp.Volume
     Debug.Print "Volume: " & val
    val = MyMassProp.Density
     Debug.Print "Density: " & val
    val = MyMassProp.SurfaceArea
     Debug.Print "Surface area: " & val
     pmoi = MyMassProp.PrincipalMomentsOfInertia
     Debug.Print "Principal moments of inertia: Px: " & pmoi(0) & ", Py: " & pmoi(1) & ", and Pz: " & pmoi(2)
     vValue = MyMassProp.GetMomentOfInertia(0)
     Debug.Print "Moments of inertia: Lxx: " & vValue(0) & ", Lxy: " & vValue(1) & ", Lxz: " & vValue(2) & ", Lyx: " & vValue(3) & ", Lyy: " & vValue(4) & ", Lyz: " & vValue(5) & ", Lzx: " & vValue(6) & ", Lzy: " & vValue(7) & ", Lzz: " & vValue(8)

     MyMassProp.SetOverrideOptions OvProp, swThisConfiguration, Empty
    MyMassProp.Recalculate

     Debug.Print ""
     Debug.Print "Mass properties after override"
     Debug.Print ""

    val = MyMassProp.Mass
     Debug.Print "Mass: " & val
    val = MyMassProp.Volume
     Debug.Print "Volume: " & val
    val = MyMassProp.Density
     Debug.Print "Density: " & val
    val = MyMassProp.SurfaceArea
     Debug.Print "Surface area: " & val
     pmoi = MyMassProp.PrincipalMomentsOfInertia
     Debug.Print "Principal moments of inertia: Px: " & pmoi(0) & ", Py: " & pmoi(1) & ", and Pz: " & pmoi(2)
     vValue = MyMassProp.GetMomentOfInertia(0)
     Debug.Print "Moments of inertia: Lxx: " & vValue(0) & ", Lxy: " & vValue(1) & ", Lxz: " & vValue(2) & ", Lyx: " & vValue(3) & ", Lyy: " & vValue(4) & ", Lyz: " & vValue(5) & ", Lzx: " & vValue(6) & ", Lzy: " & vValue(7) & ", Lzz: " & vValue(8)
     End Sub
```
