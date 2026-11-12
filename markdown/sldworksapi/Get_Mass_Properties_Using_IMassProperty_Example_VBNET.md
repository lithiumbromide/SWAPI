---
title: "Get and Override Mass Properties Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mass_Properties_Using_IMassProperty_Example_VBNET.htm"
---

# Get and Override Mass Properties Example (VB.NET)

This example shows how to get and override some mass properties of a part.

```vb
  '-----------------------------------------------------------------------
 ' Preconditions:
 ' 1. Ensure the specified document exists.
 ' 2. Open the Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
  '----------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial  Class  SolidWorksMacro

      Dim Extn  As  ModelDocExtension
      Dim MyMassProp  As MassProperty2
      Dim OvProp  As  MassPropertyOverrideOptions
      Dim swModelDoc  As  ModelDoc2
      Dim pmoi  As  Object
      Dim vValue  As  Object
      Dim value(2)  As  Double
      Dim errors  As Integer
      Dim warnings  As Integer
      Dim val  As  Double

      Sub main()

         swModelDoc = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\advdrawings\98food processor.sldasm",   swDocumentTypes_e.swDocASSEMBLY,   swOpenDocOptions_e.swOpenDocOptions_Silent,   "", errors, warnings)
         Extn = swModelDoc.Extension

          ' Create mass properties and override options
         MyMassProp = Extn.CreateMassProperty2
         OvProp = MyMassProp.GetOverrideOptions
         OvProp.OverrideMass =  True
         OvProp.SetOverrideMassValue(100)
          Dim comArr(8)  As  Double
         comArr(0) = 0.1677
         comArr(1) = 0
         comArr(2) = 0
         comArr(3) = 0
         comArr(4) = 0.21358
         comArr(5) = 0
         comArr(6) = 0
         comArr(7) = 0
         comArr(8) = 0.34772
         OvProp.OverrideMomentsOfInertia =   True
         OvProp.SetOverrideMomentsOfInertiaValue(0, comArr,  "")

          ' Use document property units (MKS)
         MyMassProp.UseSystemUnits =   False

          Debug.Print("Mass properties before override")
          Debug.Print("")

         val = MyMassProp.Mass
          Debug.Print("Mass: " & val)
         val = MyMassProp.Volume
          Debug.Print("Volume: " & val)
         val = MyMassProp.Density
          Debug.Print("Density: " & val)
         val = MyMassProp.SurfaceArea
          Debug.Print("Surface area: " & val)
         pmoi = MyMassProp.PrincipalMomentsOfInertia
          Debug.Print("Principal moments of inertia: Px: " & pmoi(0)    ", Py: " & pmoi(1)   ", and Pz: " & pmoi(2))
         vValue = MyMassProp.GetMomentOfInertia(0)
          Debug.Print("Moments of inertia: Lxx: " & vValue(0)    ", Lxy: " & vValue(1)   ", Lxz: " & vValue(2)   ", Lyx: " & vValue(3)    ", Lyy: " & vValue(4)   ", Lyz: " & vValue(5)   ", Lzx: " & vValue(6)    ", Lzy: " & vValue(7)   ", Lzz: " & vValue(8))

         MyMassProp.SetOverrideOptions(OvProp,  swInConfigurationOpts_e.swThisConfiguration,  Nothing)
         MyMassProp.Recalculate

          Debug.Print("")
          Debug.Print("Mass properties after override")
          Debug.Print("")

         val = MyMassProp.Mass
          Debug.Print("Mass: " & val)
         val = MyMassProp.Volume
          Debug.Print("Volume: " & val)
         val = MyMassProp.Density
          Debug.Print("Density: " & val)
         val = MyMassProp.SurfaceArea
          Debug.Print("Surface area: " & val)
         pmoi = MyMassProp.PrincipalMomentsOfInertia
          Debug.Print("Principal moments of inertia: Px: " & pmoi(0)    ", Py: " & pmoi(1)   ", and Pz: " & pmoi(2))
         vValue = MyMassProp.GetMomentOfInertia(0)
          Debug.Print("Moments of inertia: Lxx: " & vValue(0)    ", Lxy: " & vValue(1)   ", Lxz: " & vValue(2)   ", Lyx: " & vValue(3)    ", Lyy: " & vValue(4)   ", Lyz: " & vValue(5)   ", Lzx: " & vValue(6)    ", Lzy: " & vValue(7)   ", Lzz: " & vValue(8))

      End  Sub
      '''  <summary>
      ''' The SldWorks swApp variable is pre-assigned for you.
      '''  </summary>
      Public swApp  As  SldWorks
```

End Class
