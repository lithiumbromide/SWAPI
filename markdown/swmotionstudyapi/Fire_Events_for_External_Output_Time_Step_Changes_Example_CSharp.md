---
title: "Fire Events for External Output Time Step Changes Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swmotionstudyapi/Fire_Events_for_External_Output_Time_Step_Changes_Example_CSharp.htm"
---

# Fire Events for External Output Time Step Changes Example (C#)

This example shows how to listen and catch events for external force and motor output time step changes.

```vb
 //--------------------------------------------------
 // Preconditions:
 // 1. Start SOLIDWORKS Premium, which includes SOLIDWORKS Motion.
 // 2. Verify that the c:\temp folder exists.
 // 3. In SOLIDWORKS:
 //    a. Start the SOLIDWORKS Motion Study add-in (in
 //       SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Motion).
 //    b. Open public_documents\samples\tutorial\api\simple-block.sldasm.
 //    c.  Click MotionStudy 1 and select Motion Analysis in the
 //       Type of Study list at the upper-left corner of the MotionManager.
  // 4. In the IDE, reference the SOLIDWORKS Motion Study interop
 //    assembly (right-click the name of the project in the Project
 //    Explorer > click Add Reference >  browse to
 //    install_dir\api\redist > click   SolidWorks.Interop.swmotionstudy).
 //
 // Postconditions:
 // 1. Calculates motion analysis
 // 2. Opens c:\temp\ForceAndMotorValuesCSharp.txt for output.
 // 3. Sets forces and motors to external.
 // 4. Recalculates motion analysis.
  // 5. Fires an event for every force and motor output time step change
 //    and recalculates and writes the force magnitude or motor speed to
 //    c:\temp\ForceAndMotorValuesCSharp.txt.
 // 6. Open and examine c:\temp\ForceAndMotorValuesCSharp.txt.
 //
 // NOTE: Because this model is used elsewhere, do not save changes.
 //--------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.swmotionstudy;
 using System.Runtime.InteropServices;

 namespace MotionExternalForceMotorEventsCSharp.csproj
 {

     partial  class  SolidWorksMacro
     {
         public MotionStudy motionstudy;
         public MotionStudy swMotionStudy;
         public ModelDoc2 swModel;

         public  void Main()
         {
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             MotionStudyManager swMotionMgr = default(MotionStudyManager);
             string studyName = null;
             int numStudies = 0;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = (ModelDocExtension)swModel.Extension;

             // Motion study name
             studyName =  "Motion Study 1";

             // Get the MotionManager
             swMotionMgr = (MotionStudyManager)swModelDocExt.GetMotionStudyManager();
             numStudies = swMotionMgr.GetMotionStudyCount();
             swMotionStudy = (MotionStudy)swMotionMgr.GetMotionStudy(studyName);
             if (!swMotionStudy.IsActive)
                 swMotionStudy.Activate();

             //Calculate the motion study
             swMotionStudy.Calculate();

             // Set up events
             motionstudy = (MotionStudy)swMotionStudy;
             AttachEventHandlers();

             // Set feature Force1 as external force
             SetForceExternalFlag("Force1", true);

             // Set feature LinearMotor1 as external motor
             SetMotorExternalFlag("LinearMotor1", true);

             // Fire event at every output time step
             swMotionStudy.SetFireOutputTimeStepEvents(true);

             //Recalculate the motion study
             swMotionStudy.Calculate();

         }

         private  void SetForceExternalFlag(string featureName, bool setFlag)
         {
             // Set forces to external; i.e., listen for events

             Feature swFeature =  default(Feature);
             SimulationForceFeatureData swSimulationFeatureData =  default(SimulationForceFeatureData);
             string simTypeName = null;
             object[] motionFeatures = null;
             bool ret = false;
             int i = 0;

             motionFeatures = (object[])swMotionStudy.GetMotionFeatures();
             for (i = 0; i <= motionFeatures.GetUpperBound(0); i++)
             {
                 swFeature = (Feature)motionFeatures[i];
                 simTypeName = swFeature.GetTypeName();
                 if (simTypeName == "AEMLinearForce" | simTypeName == "AEMTorque")
                 {
                     if (swFeature.Name == featureName)
                     {
                         System.IO.StreamWriter outputWrite = new System.IO.StreamWriter("c:\\temp\\ForceAndMotorValuesCSharp.txt", true);

                         swSimulationFeatureData = (SimulationForceFeatureData)swFeature.GetDefinition();
                         swSimulationFeatureData.ExternalState = setFlag;
                         ret = swFeature.ModifyDefinition(swSimulationFeatureData, swModel, null);
                         outputWrite.WriteLine("Feature: " + swFeature.Name);
                         outputWrite.WriteLine("  Listen for events: " + swSimulationFeatureData.ExternalState);
                         outputWrite.WriteLine(" ");

                         outputWrite.Close();

                     }
                 }
             }
         }

         private  void SetMotorExternalFlag(string featureName, bool setFlag)
         {
             // Set motors to external; i.e., listen for events

             Feature swFeature =  default(Feature);
             SimulationMotorFeatureData swSimulationFeatureData =  default(SimulationMotorFeatureData);
             string simTypeName = null;
             object[] motionFeatures = null;
             int i = 0;
             bool ret = false;

             motionFeatures = (object[])swMotionStudy.GetMotionFeatures();
             for (i = 0; i <= motionFeatures.GetUpperBound(0); i++)
             {
                 swFeature = (Feature)motionFeatures[i];
                 simTypeName = swFeature.GetTypeName();
                 if (simTypeName == "AEMLinearMotor" | simTypeName == "AEMRotationalMotor")
                 {
                     if (swFeature.Name == featureName)
                     {
                         System.IO.StreamWriter outputWrite = new System.IO.StreamWriter("c:\\temp\\ForceAndMotorValuesCSharp.txt", true);

                         swSimulationFeatureData = (SimulationMotorFeatureData)swFeature.GetDefinition();
                         swSimulationFeatureData.ExternalState = setFlag;
                         ret = swFeature.ModifyDefinition(swSimulationFeatureData, swModel, null);
                         outputWrite.WriteLine("Feature name: " + swFeature.Name);
                         outputWrite.WriteLine("  Listen for events: " + swSimulationFeatureData.ExternalState);
                         outputWrite.WriteLine(" ");

                         outputWrite.Close();
                     }
                 }
             }
         }

         public  void writeOut(object name, double value)
         // Write force and motor values to file
         {

             string Name;

             Name = (string)name;
             System.IO.StreamWriter outputWrite = new System.IO.StreamWriter("c:\\temp\\ForceAndMotorValuesCSharp.txt", true);

             outputWrite.WriteLine("Name: " + Name);
             outputWrite.WriteLine("  Value: " + value.ToString());

             outputWrite.Close();

         }

         public  void AttachEventHandlers()
         {
             AttachSWEvents();
         }

         public  void AttachSWEvents()
         {
             motionstudy.ForceOutputTimeStepChangeNotify +=  this.motionStudy_ForceOutputTimeStepChangeNotify;
             motionstudy.MotorOutputTimeStepChangeNotify +=  this.motionStudy_MotorOutputTimeStepChangeNotify;
             motionstudy.OutputTimeStepChangeNotify +=  this.motionStudy_OutputTimeStepChangeNotify;
             motionstudy.StartCalculateNotify += this.motionStudy_StartCalculateNotify;
             motionstudy.StopCalculateNotify += this.motionStudy_StopCalculateNotify;
         }

         public  int motionStudy_ForceOutputTimeStepChangeNotify(double Time, object ForceNames, object Disp,  object Velocity,  object Acceleration,  object ForceOrTorque,  ref  object ForceTorqueValue)
         {
             // Fire event for every external force or torque output time step change
             MotionStudyProperties swMotionStudyProperties = default(MotionStudyProperties);
             int i = 0;
             double frameRate = 0;
             int numForces = 0;
             double deltaT = 0;
             double pi = 0;
             double w = 0;
             double A = 0;
             object[] arrForceNames;
             double[] arrForceTorqueValue;
             double[] arrAcceleration;

             arrForceNames = (object[])ForceNames;
             arrForceTorqueValue = (double[])ForceTorqueValue;
             arrAcceleration = (double[])Acceleration;

             pi = 3.14159265358979;

             swMotionStudyProperties = (MotionStudyProperties)motionstudy.GetProperties((int)swMotionStudyType_e.swMotionStudyTypeCosmosMotion);
             frameRate = swMotionStudyProperties.GetFrameRate();
             deltaT = 1 / frameRate;
             numForces = motionstudy.GetNumOfExternalForces();

             for (i = 0; i <= numForces - 1; i++)
             {
                 A = (double)arrAcceleration[i];

                 if ((arrForceNames[i].ToString() == "Force1") || (arrForceNames[i].ToString() == "Force2") || (arrForceNames[i].ToString() == "Force3"))
                 {
                     A = 0.8;
                     w = 2 * pi / 1.5;
                 }
                 else  if ((arrForceNames[i].ToString() == "Torque1" | arrForceNames[i].ToString() == "Torque2" | arrForceNames[i].ToString() == "Torque3"))
                 {
                     A = 0.005;
                     w = pi;
                 }
                 else  if ((arrForceNames[i].ToString() == "Action Reaction Force1" | arrForceNames[i].ToString() == "Action Reaction Force2" | arrForceNames[i].ToString() ==  "Action Reaction Force3"))
                 {
                     A = 0.002;
                     w = 2 * pi;
                 }
                 else
                 {
                     A = 0;
                     w = 0;
                 }

                 // Compute the return value and write to file
                 arrForceTorqueValue[i] = A * System.Math.Sin(w * (Time + deltaT));
                 writeOut(arrForceNames[i], arrForceTorqueValue[i]);
             }
             return 1;
         }

         public  int motionStudy_MotorOutputTimeStepChangeNotify(double Time, object MotorNames, object Position,  object Velocity,  object Acceleration,  object ForceOrTorque,  ref  object MotorValue)
         {
             // Fire event for every external motor output time step change
             int numMotors = 0;
             MotionStudyProperties swMotionStudyProperties =  default(MotionStudyProperties);
             double frameRate = 0;
             double deltaT = 0;
             double pi = 0;
             double w = 0;
             double A = 0;
             int i = 0;
             object[] arrMotorNames;
             double[] arrMotorValue;

             arrMotorNames = (object[])MotorNames;
             arrMotorValue = (double[])MotorValue;

             pi = 3.14159265358979;

             swMotionStudyProperties = (MotionStudyProperties)motionstudy.GetProperties((int)swMotionStudyType_e.swMotionStudyTypeCosmosMotion);
             frameRate = swMotionStudyProperties.GetFrameRate();
             deltaT = 1 / frameRate;
             numMotors = motionstudy.GetNumOfExternalMotors();

             for (i = 0; i <= numMotors - 1; i++)
             {
                 if ((arrMotorNames[i].ToString() == "RotaryMotor1") | (arrMotorNames[i].ToString() == "RotaryMotor2"))
                 {
                     A = (pi / 4);
                     w = (pi / 2);
                 }
                 else  if ((arrMotorNames[i].ToString() == "LinearMotor1"))
                 {
                     A = 0.05;
                     w = 2 * pi / 3;
                 }
                 else  if ((arrMotorNames[i].ToString() == "LinearMotor2"))
                 {
                     A = 0.025;
                     w = 2 * pi;
                 }
                 else  if ((arrMotorNames[i].ToString() == "LinearMotor3"))
                 {
                     A = 1.0472;
                     w = 2 * pi;
                 }
                 else
                 {
                     A = 0;
                     w = 0;
                 }

                 //Compute the return value and write to file
                 arrMotorValue[i] = A * System.Math.Sin(w * (Time + deltaT));
                 writeOut(arrMotorNames[i], arrMotorValue[i]);
             }
             return 1;
         }

         public  int motionStudy_OutputTimeStepChangeNotify(double Time)
         {
             // Fire event at every output step

             double myTime = 0;
             myTime = Time;
             return 1;

         }

         public  int motionStudy_StartCalculateNotify(double Time)
         {
             // Fire event when recalculation starts

             double myTime = 0;
             myTime = Time;

             System.IO.StreamWriter outputWrite = new System.IO.StreamWriter("c:\\temp\\ForceAndMotorValuesCSharp.txt", true);
             outputWrite.WriteLine("Recalculation started...");
             outputWrite.WriteLine("  ");
             outputWrite.Close();

             return 1;

         }

         public  int motionStudy_StopCalculateNotify(double Time)
         {
             // Fire event when recalculation stops

             double myTime = 0;
             myTime = Time;

             System.IO.StreamWriter outputWrite = new System.IO.StreamWriter("c:\\temp\\ForceAndMotorValuesCSharp.txt", true);
             outputWrite.WriteLine(" ");
             outputWrite.WriteLine("Recalculation stopped...");
             outputWrite.Close();

             return 1;

         }

         ///  <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
