---
title: "Fire Events for External Output Time Step Changes Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_for_External_Output_Time_Step_Changes_Example_VBNET.htm"
---

# Fire Events for External Output Time Step Changes Example (VB.NET)

This example shows how to listen and catch events for external force and motor output time step changes.

```vb
 '--------------------------------------------------
 ' Preconditions:
 ' 1. Start SOLIDWORKS Design Premium, which includes SOLIDWORKS Motion.
 ' 2. Verify that the c:\temp folder exists.
 ' 3. In SOLIDWORKS Design:
 '    a. Start the SOLIDWORKS Motion Study add-in (in
 '       SOLIDWORKS Design, click Tools > Add-Ins > SOLIDWORKS Motion).
 '    b. Open public_documents\samples\tutorial\api\simple-block.sldasm.
 '    c. Click MotionStudy 1 and select Motion Analysis in the
 '       Type of Study list at the  upper-left corner of the
 '       MotionManager.
 ' 4. In the IDE, reference the SOLIDWORKS Motion Study interop
 '    assembly (right-click the name of the project in the Project
 '    Explorer > click Add Reference >  browse to
 '    install_dir\api\redist > click   SolidWorks.Interop.swmotionstudy).
 '
 ' Postconditions:
 ' 1. Calculates motion analysis.
 ' 2. Opens c:\temp\ForceAndMotorValuesVBNET.txt for output.
 ' 3. Sets forces and motors to external.
 ' 4. Recalculates motion analysis.
 ' 5. Fires an event for every force and motor output time step change
 '    and recalculates and writes the force magnitude or motor speed to
 '    c:\temp\ForceAndMotorValuesVBNET.txt.
 ' 6. Open and examine c:\temp\ForceAndMotorValuesVBNET.txt.
 '
 ' NOTE: Because this model is used elsewhere, do not save changes.
 '--------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.swmotionstudy

 Partial  Class SolidWorksMacro

     Public  WithEvents motionstudy  As MotionStudy
     Public swMotionStudy As MotionStudy
     Public swModel  As ModelDoc2
     Public outputWrite As System.IO.StreamWriter

     Public  Sub Main()

         Dim swModelDocExt As ModelDocExtension
         Dim swMotionMgr As MotionStudyManager
         Dim studyName As  String
         Dim numStudies As  Integer

         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension

         ' Motion study name
         studyName =  "Motion Study 1"

         ' Get the MotionManager
         swMotionMgr = swModelDocExt.GetMotionStudyManager()
         numStudies = swMotionMgr.GetMotionStudyCount()
         swMotionStudy = swMotionMgr.GetMotionStudy(studyName)
         If  Not swMotionStudy.IsActive Then swMotionStudy.Activate()

         'Calculate the motion study
         swMotionStudy.Calculate()

         ' Set up events
         motionstudy = swMotionStudy
         AttachEventHandlers()

         ' Open output file for writing force and motor values
         outputWrite = IO.File.CreateText("c:\temp\ForceAndMotorValuesVBNET.txt")

         ' Set feature Force1 as external force
         Call SetForceExternalFlag("Force1", True)

         ' Set feature LinearMotor1 as external motor
         Call SetMotorExternalFlag("LinearMotor1", True)

         ' Fire event at every output time step
         swMotionStudy.SetFireOutputTimeStepEvents(True)

         'Recalculate the motion study
         swMotionStudy.Calculate()

         ' Close output file
         outputWrite.Close()

     End  Sub

     Private Sub SetForceExternalFlag(ByVal featureName As  String,  ByVal setFlag As  Integer)
         ' Set forces to external; i.e., listen for events

         Dim swFeature As Feature
         Dim swSimulationFeatureData As SimulationForceFeatureData
         Dim simTypeName As  String
         Dim motionFeatures As  Object
         Dim ret As  Boolean
         Dim i As   Integer

         motionFeatures = swMotionStudy.GetMotionFeatures
         For i = 0  To UBound(motionFeatures)
             swFeature = motionFeatures(i)
             simTypeName = swFeature.GetTypeName
             If simTypeName = "AEMLinearForce" Or simTypeName =  "AEMTorque"  Then
                 If swFeature.Name = featureName Then
                     swSimulationFeatureData = swFeature.GetDefinition
                     swSimulationFeatureData.ExternalState = setFlag
                     ret = swFeature.ModifyDefinition(swSimulationFeatureData, swModel, Nothing)
                     outputWrite.WriteLine("Feature: " & swFeature.Name)
                     outputWrite.WriteLine("  Listen for events: " & swSimulationFeatureData.ExternalState)
                     outputWrite.WriteLine(" ")
                 End  If
             End If
         Next i
     End  Sub

     Private Sub SetMotorExternalFlag(ByVal featureName As  String,  ByVal setFlag As  Integer)
         ' Set motors to external; i.e., listen for events

         Dim swFeature As Feature
         Dim swSimulationFeatureData As SimulationMotorFeatureData
         Dim simTypeName As  String
         Dim motionFeatures As  Object
         Dim i As   Integer
         Dim ret As  Boolean

         motionFeatures = swMotionStudy.GetMotionFeatures
         For i = 0  To UBound(motionFeatures)
             swFeature = motionFeatures(i)
             simTypeName = swFeature.GetTypeName
             If simTypeName = "AEMLinearMotor" Or simTypeName =  "AEMRotationalMotor"  Then
                 If swFeature.Name = featureName Then
                     swSimulationFeatureData = swFeature.GetDefinition
                     swSimulationFeatureData.ExternalState = setFlag
                     ret = swFeature.ModifyDefinition(swSimulationFeatureData, swModel, Nothing)
                     outputWrite.WriteLine("Feature name: " & swFeature.Name)
                     outputWrite.WriteLine("  Listen for events: " & swSimulationFeatureData.ExternalState)
                     outputWrite.WriteLine(" ")
                 End  If
             End If
         Next i
     End  Sub

     Sub AttachEventHandlers()
         AttachSWEvents()
     End  Sub

     Sub AttachSWEvents()
         AddHandler motionstudy.ForceOutputTimeStepChangeNotify, AddressOf Me.motionStudy_ForceOutputTimeStepChangeNotify
         AddHandler motionstudy.MotorOutputTimeStepChangeNotify, AddressOf Me.motionStudy_MotorOutputTimeStepChangeNotify
         AddHandler motionstudy.OutputTimeStepChangeNotify, AddressOf Me.motionStudy_OutputTimeStepChangeNotify
         AddHandler motionstudy.StartCalculateNotify, AddressOf Me.motionStudy_StartCalculateNotify
         AddHandler motionstudy.StopCalculateNotify, AddressOf Me.motionStudy_StopCalculateNotify
     End  Sub

     Private Function motionStudy_ForceOutputTimeStepChangeNotify(ByVal Time As  Double,  ByVal ForceNames As Object,  ByVal Disp  As  Object, ByVal Velocity As  Object,  ByVal Acceleration As Object,  ByVal ForceOrTorque  As  Object, ByRef ForceTorqueValue As  Object)  As Integer
         ' Fire event for every external force or torque output time step change
         Dim swMotionStudyProperties As MotionStudyProperties
         Dim i  As  Integer
         Dim frameRate As  Double
         Dim numForces As  Integer
         Dim deltaT As  Double
         Dim pi As  Double
         Dim w As  Double
         Dim A As  Double

         pi = 3.14159265358979

         swMotionStudyProperties = motionstudy.GetProperties(swMotionStudyType_e.swMotionStudyTypeCosmosMotion)
         frameRate = swMotionStudyProperties.GetFrameRate()
         deltaT = 1 / frameRate
         numForces = motionstudy.GetNumOfExternalForces

         For i = 0  To numForces - 1

             A = Acceleration(i)

             If (ForceNames(i) = "Force1"  Or ForceNames(i) =  "Force2"  Or ForceNames(i) =  "Force3")  Then
                 outputWrite.WriteLine("  " & ForceNames(i))
                 A = 0.8
                 w = 2 * pi / 1.5
             ElseIf (ForceNames(i) = "Torque1"  Or ForceNames(i) =  "Torque2"  Or ForceNames(i) =  "Torque3")  Then
                 outputWrite.WriteLine("  " & ForceNames(i))
                 A = 0.005
                 w = pi
             ElseIf (ForceNames(i) = "Action Reaction Force1" Or ForceNames(i) =  "Action Reaction Force2"  Or ForceNames(i) =  "Action Reaction Force3") Then
                 outputWrite.WriteLine("  " & ForceNames(i))
                 A = 0.002
                 w = 2 * pi
             Else
                 outputWrite.WriteLine("  " & ForceNames(i))
                 A = 0
                 w = 0
             End  If

             ' Compute the return value
             ForceTorqueValue(i) = A * Math.Sin(w * (Time + deltaT))
             outputWrite.WriteLine("    Force or torque magnitude: " & ForceTorqueValue(i))

         Next i

     End  Function

     Private Function motionStudy_MotorOutputTimeStepChangeNotify(ByVal Time As  Double,  ByVal MotorNames As Object,  ByVal Position  As  Object, ByVal Velocity As  Object,  ByVal Acceleration As Object,  ByVal ForceOrTorque  As  Object, ByRef MotorValue As  Object)  As Integer
         ' Fire event for every external motor output time step change
         Dim numMotors As   Integer
         Dim swMotionStudyProperties As MotionStudyProperties
         Dim frameRate As  Double
         Dim deltaT As  Double
         Dim pi As  Double
         Dim w As  Double
         Dim A As  Double
         Dim i As  Integer

         pi = 3.14159265358979

         swMotionStudyProperties = motionstudy.GetProperties(swMotionStudyType_e.swMotionStudyTypeCosmosMotion)
         frameRate = swMotionStudyProperties.GetFrameRate()
         deltaT = 1 / frameRate
         numMotors = motionstudy.GetNumOfExternalMotors

         For i = 0  To numMotors - 1

             If (MotorNames(i) = "RotaryMotor1"  Or MotorNames(i) =  "RotaryMotor2")  Then
                 outputWrite.WriteLine("  " & MotorNames(i))
                 A = (pi / 4)
                 w = (pi / 2)
             ElseIf (MotorNames(i) = "LinearMotor1")  Then
                 outputWrite.WriteLine("  " & MotorNames(i))
                 A = 0.05
                 w = 2 * pi / 3
             ElseIf (MotorNames(i) = "LinearMotor2")  Then
                 outputWrite.WriteLine("  " & MotorNames(i))
                 A = 0.025
                 w = 2 * pi
             ElseIf (MotorNames(i) = "LinearMotor3")  Then
                 outputWrite.WriteLine("  " & MotorNames(i))
                 A = 1.0472
                 w = 2 * pi
             Else
                 outputWrite.WriteLine("  LinearMotor")
                 A = 0
                 w = 0
             End  If

             'Compute the return value
             MotorValue(i) = A * Math.Sin(w * (Time + deltaT))
             outputWrite.WriteLine("    Motor speed: " & MotorValue(i))
         Next i
     End  Function

     Private Function motionStudy_OutputTimeStepChangeNotify(ByVal Time As  Double)  As Integer
         ' Fire event at every output step

         Dim myTime As  Double

         myTime = Time

     End  Function

     Private Function motionStudy_StartCalculateNotify(ByVal Time As  Double)  As Integer
         ' Fire event when recalculation starts

         Dim myTime As  Double

         outputWrite.WriteLine("Recalculation started...")
         outputWrite.WriteLine(" ")
         myTime = Time

     End  Function

     Private Function motionStudy_StopCalculateNotify(ByVal Time As  Double)  As Integer
         ' Fire event when recalculation stops

         Dim myTime As  Double

         outputWrite.WriteLine(" ")
         outputWrite.WriteLine("Recalculation stopped...")

         myTime = Time

     End  Function

     '''  <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     '''  </summary>
     Public swApp As SldWorks

 End  Class
```
