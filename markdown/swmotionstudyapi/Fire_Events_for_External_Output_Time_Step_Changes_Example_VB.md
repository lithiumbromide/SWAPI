---
title: "Fire Events for External Output Time Step Changes Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swmotionstudyapi/Fire_Events_for_External_Output_Time_Step_Changes_Example_VB.htm"
---

# Fire Events for External Output Time Step Changes Example (VBA)

This example shows how to listen and catch events for external force and motor output time step changes.

```
'---------------------------------------------------------------------
' Preconditions:
' 1. Start SOLIDWORKS Premium, which includes SOLIDWORKS Motion.
' 2. Verify that the c:\temp folder exists.
' 3. In SOLIDWORKS:
'    a. Start the SOLIDWORKS Motion Study add-in (in
'       SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Motion).
'    b. Open public_documents\samples\tutorial\api\simple-block.sldasm.
'    c. Click MotionStudy1 and select Motion Analysis in the
'       Type of Study list at the upper-left corner of the
'       MotionManager.
' 4. In the IDE:
'    a. Reference the SOLIDWORKS MotionStudy type library.
'    b. Copy and paste this code in the main module.
'    c. Click Insert > Class module and copy and paste this code in the
'       class module.
'
' Postconditions:
' 1. Calculates motion analysis.
' 2. Opens c:\temp\ForceAndMotorValuesVBA.txt for output.
' 3. Sets forces and motors to external.
' 4. Recalculates motion analysis.
' 5. Fires an event for every force and motor output time step change
'    and recalculates and writes the force magnitude or motor speed
'    to c:\temp\ForceAndMotorValuesVBA.txt.
' 6. Open and examine c:\temp\ForceAndMotorValuesVBA.txt.
'
' NOTE: Because this model is used elsewhere, do not save changes.
'------------------------------------------------------------------
Main module
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swMotionMgr As swMotionStudy.MotionStudyManager
Dim swMotionStudy As swMotionStudy.motionStudy
Dim studyName As String
Dim numStudies As Long
Dim eventClass As Class1
```

```
Sub Main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    ' Motion study name
    studyName = "Motion Study 1"
```

```
    ' Get the MotionManager
    Set swMotionMgr = swModelDocExt.GetMotionStudyManager()
    numStudies = swMotionMgr.GetMotionStudyCount()
    Set swMotionStudy = swMotionMgr.GetMotionStudy(studyName)
    If Not swMotionStudy.IsActive Then swMotionStudy.Activate
```

```
    'Calculate the motion study
    swMotionStudy.Calculate
```

```
    ' Set up events
    Set eventClass = New Class1
    eventClass.Init swMotionStudy
```

```
    ' Open output file for writing force and motor values
    Open "c:\temp\ForceAndMotorValuesVBA.txt" For Output As #1
```

```
    ' Set feature Force1 as external force
    Call SetForceExternalFlag("Force1", True)
```

```
    ' Set feature LinearMotor1 as external motor
    Call SetMotorExternalFlag("LinearMotor1", True)
```

```
    ' Fire event at every output time step
    swMotionStudy.SetFireOutputTimeStepEvents (True)
```

```
    'Recalculate the motion study
    swMotionStudy.Calculate
```

```
    ' Close output file
    Close #1
```

```
End Sub
```

```
Private Sub SetForceExternalFlag(ByVal featureName As String, ByVal setFlag As Long)
' Set forces to external; i.e., listen for events
```

```
    Dim swFeature As SldWorks.Feature
    Dim swSimulationFeatureData As SldWorks.SimulationForceFeatureData
    Dim simTypeName As String
    Dim motionFeatures As Variant
    Dim ret As Boolean
    Dim i As Long
```

```
    motionFeatures = swMotionStudy.GetMotionFeatures
    For i = 0 To UBound(motionFeatures)
        Set swFeature = motionFeatures(i)
        simTypeName = swFeature.GetTypeName
        If simTypeName = "AEMLinearForce" Or simTypeName = "AEMTorque" Then
            If swFeature.Name = featureName Then
                Set swSimulationFeatureData = swFeature.GetDefinition
                swSimulationFeatureData.ExternalState = setFlag
                ret = swFeature.ModifyDefinition(swSimulationFeatureData, swModel, Nothing)
                Write #1, "Feature: " & swFeature.Name
                Write #1, "  Listen for events: " & swSimulationFeatureData.ExternalState
                Write #1, " "
            End If
        End If
    Next i
End Sub
```

```
Private Sub SetMotorExternalFlag(ByVal featureName As String, ByVal setFlag As Long)
' Set motors to external; i.e., listen for events
```

```
    Dim swFeature As SldWorks.Feature
    Dim swSimulationFeatureData As SldWorks.SimulationMotorFeatureData
    Dim simTypeName As String
    Dim motionFeatures As Variant
    Dim i As Long
    Dim ret As Boolean
```

```
    motionFeatures = swMotionStudy.GetMotionFeatures
    For i = 0 To UBound(motionFeatures)
        Set swFeature = motionFeatures(i)
        simTypeName = swFeature.GetTypeName
        If simTypeName = "AEMLinearMotor" Or simTypeName = "AEMRotationalMotor" Then
            If swFeature.Name = featureName Then
                Set swSimulationFeatureData = swFeature.GetDefinition
                swSimulationFeatureData.ExternalState = setFlag
                ret = swFeature.ModifyDefinition(swSimulationFeatureData, swModel, Nothing)
                Write #1, "Feature name: " & swFeature.Name
                Write #1, "  Listen for events: " & swSimulationFeatureData.ExternalState
                Write #1, " "
            End If
        End If
    Next i
End Sub
```

```
Back to top
```

### 'Class module

```
Dim WithEvents motionStudy As swMotionStudy.motionStudy
```

```
Private Sub Class_Initialize()
End Sub
```

```
Sub Init(study As swMotionStudy.motionStudy)
    Set motionStudy = study
End Sub
```

```
Private Function motionStudy_ForceOutputTimeStepChangeNotify(ByVal Time As Double, ByVal ForceNames As Variant, ByVal Disp As Variant, ByVal Velocity As Variant, ByVal Acceleration As Variant, ByVal ForceOrTorque As Variant, ForceTorqueValue As Variant) As Long
' Fire event for every external force or torque output time step change
    Dim swMotionStudyProperties As swMotionStudy.motionStudyProperties
    Dim frameRate As Double
    Dim numForces As Long
    Dim deltaT As Double
    Dim pi As Double
    Dim w As Double
    Dim A As Double
```

```
    pi = 3.14159265358979
```

```
    Set swMotionStudyProperties = motionStudy.GetProperties(swMotionStudyTypeCosmosMotion)
    frameRate = swMotionStudyProperties.GetFrameRate()
    deltaT = 1 / frameRate
    numForces = motionStudy.GetNumOfExternalForces
```

```
    For i = 0 To numForces - 1
```

```
        A = Acceleration(i)
```

```
        If (ForceNames(i) = "Force1" Or ForceNames(i) = "Force2" Or ForceNames(i) = "Force3") Then
            Write #1, "  " & ForceNames(i)
            A = 0.8
            w = 2 * pi / 1.5
        ElseIf (ForceNames(i) = "Torque1" Or ForceNames(i) = "Torque2" Or ForceNames(i) = "Torque3") Then
            Write #1, "  " & ForceNames(i)
            A = 0.005
            w = pi
        ElseIf (ForceNames(i) = "Action Reaction Force1" Or ForceNames(i) = "Action Reaction Force2" Or ForceNames(i) = "Action Reaction Force3") Then
            Write #1, "  " & ForceNames(i)
            A = 0.002
            w = 2 * pi
        Else
            Write #1, "  " & ForceNames(i)
            A = 0
            w = 0
        End If
```

```
        ' Compute the return value
        ForceTorqueValue(i) = A * Sin(w * (Time + deltaT))
        Write #1, "    Force or torque magnitude: " & ForceTorqueValue(i)
```

```
    Next i
```

```
End Function
```

```
Private Function motionStudy_MotorOutputTimeStepChangeNotify(ByVal Time As Double, ByVal MotorNames As Variant, ByVal Position As Variant, ByVal Velocity As Variant, ByVal Acceleration As Variant, ByVal ForceOrTorque As Variant, MotorValue As Variant) As Long
' Fire event for every external motors at every output time step change
    Dim numMotors as Long
    Dim swMotionStudyProperties As swMotionStudy.motionStudyProperties
    Dim frameRate As Double
    Dim deltaT As Double
    Dim pi As Double
    Dim w As Double
    Dim A As Double
```

```
    pi = 3.14159265358979
```

```
    Set swMotionStudyProperties = motionStudy.GetProperties(swMotionStudyTypeCosmosMotion)
    frameRate = swMotionStudyProperties.GetFrameRate()
    deltaT = 1 / frameRate
    numMotors = motionStudy.GetNumOfExternalMotors
```

```
    For i = 0 To numMotors - 1
```

```
        If (MotorNames(i) = "RotaryMotor1" Or MotorNames(i) = "RotaryMotor2") Then
            Write #1, "  " & MotorNames(i)
            A = (pi / 4)
            w = (pi / 2)
        ElseIf (MotorNames(i) = "LinearMotor1") Then
            Write #1, "  " & MotorNames(i)
            A = 0.05
            w = 2 * pi / 3
        ElseIf (MotorNames(i) = "LinearMotor2") Then
            Write #1, "  " & MotorNames(i)
            A = 0.025
            w = 2 * pi
        ElseIf (MotorNames(i) = "LinearMotor3") Then
            Write #1, "  " & MotorNames(i)
            A = 1.0472
            w = 2 * pi
        Else
            Write #1, "  LinearMotor"
            A = 0
            w = 0
        End If
```

```
        'Compute the return value
        MotorValue(i) = A * Sin(w * (Time + deltaT))
        Write #1, "    Motor speed: " & MotorValue(i)
    Next i
End Function
```

```
Private Function motionStudy_OutputTimeStepChangeNotify(ByVal Time As Double) As Long
' Fire event at every output step
    myTime = Time
End Function
```

```
Private Function motionStudy_StartCalculateNotify(ByVal Time As Double) As Long
' Fire event when recalculation starts
    Write #1, "Recalculation started..."
    Write #1, " "
    myTime = Time
End Function
```

```
Private Function motionStudy_StopCalculateNotify(ByVal Time As Double) As Long
' Fire event when recalculation stops
    Write #1, " "
    Write #1, "Recalculation stopped..."
    myTime = Time
End Function
```

```
Back to top
```
