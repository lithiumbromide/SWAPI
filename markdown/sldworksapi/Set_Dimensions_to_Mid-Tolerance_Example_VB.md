---
title: "Set Dimensions to Mid-Tolerance Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Dimensions_to_Mid-Tolerance_Example_VB.htm"
---

# Set Dimensions to Mid-Tolerance Example (VBA)

This example:

- shows how to iterate over all dimensions in a part and set each dimension with tolerance to the middle of the tolerance range.
- does not analyze the overall effect of varying tolerances.

```
'---------------------------------------------------
' Preconditions:
' 1. Open a part that has tolerances set.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a derived configuration based on the current
'    configuration.
' 2. Makes the derived configuration the active configuration.
' 3. Sets all dimensions in the derived configuration with tolerances
'    to mid-tolerance.
' 4. Removes all tolerances from the dimensions.
' 5. Examine the Immediate window.
'---------------------------------------------------------------------------
Option Explicit
```

```
Function GetDimFactor(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swDim As SldWorks.Dimension) As Double
    Const PI                    As Double = 3.14159265
    Const LEN_FACTOR            As Double = 1000#
    Const ANG_FACTOR            As Double = 180# / PI
```

```
    Select Case swDim.GetType
        Case swDimensionParamTypeDoubleLinear
            GetDimFactor = LEN_FACTOR
        Case swDimensionParamTypeDoubleAngular
            GetDimFactor = ANG_FACTOR
        Case Else
            Debug.Assert False
    End Select
End Function
```

```
Function GetDimString(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swDim As SldWorks.Dimension) As String
    Const LEN_STR               As String = " mm"
    Const ANG_STR               As String = " deg"
```

```
    Select Case swDim.GetType
        Case swDimensionParamTypeDoubleLinear
            GetDimString = LEN_STR
        Case swDimensionParamTypeDoubleAngular
            GetDimString = ANG_STR
        Case Else
            Debug.Assert False
    End Select
End Function
```

```
Sub SetDimensionToMidTolerance(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swDim As SldWorks.Dimension)
    Dim nRetval                 As Long
    Dim nDimFactor              As Double
    Dim sDimStr                 As String
    Dim vTolVal                 As Variant
    Dim nOldVal                 As Double
    Dim nNewVal                 As Double
    Dim bRet                    As Boolean
    If swDimensionDriving <> swDim.DrivenState Or swDim.ReadOnly Then
        Exit Sub
    End If
```

```
    ' Might have tolerance values stored from
    ' previous tolerance type, so check current
    ' tolerance type first
    If swTolNONE = swDim.GetToleranceType Then
        Exit Sub
    End If
```

```
    ' Mid-tolerance cannot make sense for a MIN/MAX or symmetric tolerance
    If swTolMIN = swDim.GetToleranceType Or swTolMAX = swDim.GetToleranceType Or swTolSYMMETRIC = swDim.GetToleranceType Then
        Exit Sub
    End If
```

```
    vTolVal = swDim.GetToleranceValues
    If IsEmpty(vTolVal) Then
        Exit Sub
    End If
```

```
    nDimFactor = GetDimFactor(swApp, swModel, swDim)
    sDimStr = GetDimString(swApp, swModel, swDim)
```

```
    nOldVal = swDim.GetSystemValue2("")
    nNewVal = nOldVal + (vTolVal(0) + vTolVal(1)) / 2#
    Debug.Print "    -->"
    Debug.Print "      Old Value    = " & nOldVal * nDimFactor & sDimStr
    Debug.Print "      New Value    = " & nNewVal * nDimFactor & sDimStr
    nRetval = swDim.SetSystemValue3(nNewVal, swSetValue_InThisConfiguration, Empty): Debug.Assert swSetValue_Successful = nRetval
```

```
    ' Changed to mid tolerance, so remove tolerance;
    ' otherwise, change dimension when run again
    bRet = swDim.SetToleranceType(swTolNONE): Debug.Assert bRet
End Sub
```

```
Sub ProcessDimension(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swDim As SldWorks.Dimension)
    Dim nDimFactor              As Double
    Dim sDimStr                 As String
    Dim vTolVal                 As Variant
    Dim bRet                    As Boolean
```

```
    nDimFactor = GetDimFactor(swApp, swModel, swDim)
    sDimStr = GetDimString(swApp, swModel, swDim)
```

```
    Debug.Print "    " & swDim.FullName
    Debug.Print "      Value        = " & swDim.GetSystemValue2("") * nDimFactor & sDimStr
    Debug.Print "      Driven       = " & swDim.DrivenState
    Debug.Print "      ReadOnly     = " & swDim.ReadOnly
```

```
    vTolVal = swDim.GetToleranceValues
    If IsEmpty(vTolVal) Then
        Debug.Print "      No tolerance information"
        Exit Sub
    End If
```

```
    Debug.Print "      TolType      = " & swDim.GetToleranceType
    Debug.Print "      FitType      = " & swDim.GetToleranceFitValues
    Debug.Print "      MaxTol       = " & vTolVal(1) * nDimFactor & sDimStr
    Debug.Print "      MinTol       = " & vTolVal(0) * nDimFactor & sDimStr
End Sub
```

```
Sub ProcessMassProps(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2)
    Dim swDocExt                As SldWorks.ModelDocExtension
    Dim swMass                  As SldWorks.MassProperty
```

```
    Set swDocExt = swModel.Extension
    Set swMass = swDocExt.CreateMassProperty
    Debug.Print "    Mass             = " & swMass.Mass * 1000# & " g"
    Debug.Print "    Surface Area     = " & swMass.SurfaceArea * 1000000# & " mm^2"
    Debug.Print "    Volume           = " & swMass.Volume * 1000000000# & " mm^3"
    Debug.Print "    Density          = " & swMass.Density & " kg/m^3"
    Debug.Print "    CenterOfMass     = (" & swMass.CenterOfMass(0) * 1000# & ", " & swMass.CenterOfMass(1) * 1000# & ", " & swMass.CenterOfMass(2) * 1000# & ") mm"
End Sub
```

```
Sub main()
```

```
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swConf                  As SldWorks.Configuration
    Dim swMidConf               As SldWorks.Configuration
    Dim swConfMgr               As SldWorks.ConfigurationManager
    Dim swFeat                  As SldWorks.Feature
    Dim swDispDim               As SldWorks.DisplayDimension
    Dim swDim                   As SldWorks.Dimension
    Dim bRet                    As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swConf = swModel.GetActiveConfiguration
    Set swConfMgr = swModel.ConfigurationManager
    Set swMidConf = swConfMgr.AddConfiguration(swConf.Name & " - mid tolerance", "mid tolerance", "mid tolerance", 1, swConf.Name, "mid tolerance"): Debug.Assert Not swMidConf Is Nothing
    Set swFeat = swModel.FirstFeature
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Nominal Tolerance:"
    ProcessMassProps swApp, swModel
    Debug.Print "  -----------------------------"
```

```
    Do While Not swFeat Is Nothing
        Debug.Print "  " & swFeat.Name
        Set swDispDim = swFeat.GetFirstDisplayDimension
        Do While Not swDispDim Is Nothing
            Set swDim = swDispDim.GetDimension
            ProcessDimension swApp, swModel, swDim
            SetDimensionToMidTolerance swApp, swModel, swDim
            Set swDispDim = swFeat.GetNextDisplayDimension(swDispDim)
        Loop
        Set swFeat = swFeat.GetNextFeature
    Loop
```

```
    bRet = swModel.ForceRebuild3(False): Debug.Assert bRet
```

```
    Debug.Print "  Middle Tolerance:"
    ProcessMassProps swApp, swModel
    Debug.Print "  -----------------------------"

End Sub
```
