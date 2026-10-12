---
title: "Duplicate, Delete, and Create Motion Study Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm"
---

# Duplicate, Delete, and Create Motion Study Example (C#)

This example shows how to create a duplicate motion study, delete an existing motion study, and create a new motion study.

```
//------------------------------------------------------------------
// Preconditions:
// 1. Open an assembly document that has a motion study named
//    MotionStudy 1 and a collapsed exploded view.
// 2. Verify that a ray-trace rendering engine is active.
// 3. Add a reference to the SOLIDWORKS Motion Study primary interop
//    assembly (right-click the name of the project in the Project Explorer >
//    click Add Reference > browse to install_dir\api\redist ?
//    click SolidWorks.Interop.swmotionstudy.dll).
// 4. Verify that c:\test exists.
// 5. Open the Immediate window.
//
// Postconditions:
// 1. Observe the graphics area.
// 2. Makes a copy of Motion Study 1 called Motion Study 2.
// 3. Deletes and creates a new motion study for Motion Study 1.
// 4. Runs the animation (i.e., rotates, explodes,
//    stops rotating, and collapses the assembly).
// 5. Saves the motion study as c:\test\Anim1.avi.
// 6. Examine the Immediate window.
// 7. Play c:\test\Anim1.avi.
//------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swmotionstudy;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;
using System.Windows.Forms;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        private void PlayAnimation(MotionStudy SwMotionStudy)
        {
            Debug.Print("");
            int cPlayMode = 0;
            Debug.Print("Current play mode: ");
            cPlayMode = SwMotionStudy.PlayMode;

            //Get current play mode
            switch (cPlayMode)
            {
                case 1:
                    Debug.Print("    Normal");
                    break;
                case 2:
                    Debug.Print("    Loop");
                    break;
                case 3:
                    Debug.Print("    Reciprocate");
                    break;
            }

            //Set play mode to Loop
            int nPlayMode = 0;
            Debug.Print("New play mode: ");
            SwMotionStudy.PlayMode = (int)swAnimationPlayMode_e.swAnimationPlayModeLoop;
            nPlayMode = SwMotionStudy.PlayMode;

            //Get new play mode
            switch (nPlayMode)
            {
                case 1:
                    Debug.Print("    Normal");
                    break;
                case 2:
                    Debug.Print("    Loop");
                    break;
                case 3:
                    Debug.Print("    Reciprocate");
                    break;
            }

            //Set timebar to 0 on timeline
            SwMotionStudy.SetTime(0);

            //Play the animation
            SwMotionStudy.Play();

        }

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            MotionStudyManager swMotionMgr = default(MotionStudyManager);
            MotionStudy swMotionStudy1 = default(MotionStudy);
            AVIParameter swSaveAVIData = null;
            bool boolstatus = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Get the MotionManager
            swMotionMgr = (MotionStudyManager)swModelDocExt.GetMotionStudyManager();
            if ((swMotionMgr == null))
            {
                return;
            }

            //Get the motion study named Motion Study 1
            swMotionStudy1 = (MotionStudy)swMotionMgr.GetMotionStudy("Motion Study 1");
            if ((swMotionStudy1 == null))
            {
                MessageBox.Show("Motion Study 1 is not available.");
                return;
            }

            //Create a copy of the motion study
            swMotionStudy1.Duplicate();

            //Get the supported motion study types
            int MSTypes = 0;
            boolstatus = swMotionStudy1.GetSupportedStudyTypes(out MSTypes);
            Debug.Print("");
            Debug.Print("Supported study types: ");
            Debug.Print("    Assembly: " + ((MSTypes & (int)swMotionStudyType_e.swMotionStudyTypeAssembly) > 0));
            Debug.Print("    PhysicalSimulation: " + ((MSTypes & (int)swMotionStudyType_e.swMotionStudyTypePhysicalSimulation) > 0));
            Debug.Print("    CosmosMotion: " + ((MSTypes & (int)swMotionStudyType_e.swMotionStudyTypeCosmosMotion) > 0));
            Debug.Print("    LegacyCosmosMotion: " + ((MSTypes & (int)swMotionStudyType_e.swMotionStudyTypeLegacyCosmosMotion) > 0));

            //Get the current motion study type
            int CurStudyType = 0;
            CurStudyType = swMotionStudy1.StudyType;
            Debug.Print("");
            Debug.Print("Current study type: ");
            switch (CurStudyType)
            {
                case (int)swMotionStudyType_e.swMotionStudyTypeAssembly:
                    Debug.Print("    Assembly");
                    break;
                case (int)swMotionStudyType_e.swMotionStudyTypePhysicalSimulation:
                    Debug.Print("    PhysicalSimulation");
                    break;
                case (int)swMotionStudyType_e.swMotionStudyTypeCosmosMotion:
                    Debug.Print("    CosmosMotion");
                    break;
                case (int)swMotionStudyType_e.swMotionStudyTypeLegacyCosmosMotion:
                    Debug.Print("    LegacyCosmosMotion");
                    break;
            }

            //Is the motion study active?  If not, activate it
            if (!swMotionStudy1.IsActive)
                swMotionStudy1.Activate();

            //Create an animation of the rotating model
            //Delete any existing animation sequences
            //Set the animation duration to 10 seconds
            boolstatus = swMotionStudy1.CreateByRotateModel(true, (int)swAnimatorAxisOfRotation_e.swRotationAboutYAxis, 1, (int)swAnimatorDirectionOfRotation_e.swRotationClockwise, 10, 0);

            //Play the animation
            PlayAnimation(swMotionStudy1);

            //Stop playing the animation
            swMotionStudy1.Stop();

            //Add an explode to the animation
            //Set the animation duration to 5 seconds
            boolstatus = swMotionStudy1.CreateByExplode(false, 5, 0);

            //Add a collapse to the animation
            //Set the animation duration to 5 seconds
            boolstatus = swMotionStudy1.CreateByCollapse(false, 10, 5);

            //Set duration of animation to 15 seconds
            swMotionStudy1.SetDuration(15);

            //Play the animation
            PlayAnimation(swMotionStudy1);

            //Calculate
            swMotionStudy1.Calculate();
            Debug.Print("");
            Debug.Print("Study duration: " + swMotionStudy1.GetDuration());

            //Play animation
            PlayAnimation(swMotionStudy1);

            //Set and save AVI parameters
            swSaveAVIData = (AVIParameter)swMotionMgr.CreateAVIParameter();
            swSaveAVIData.FramePerSecond = 7.5;
            swSaveAVIData.SaveEntireAnimation = true;
            swSaveAVIData.OutputType = (int)swAnimationOutputType_e.swAnimationOutput_AVI;
            swSaveAVIData.RendererType = (int)swRendererType_e.swRendererType_Solidworks_Screen;
            swSaveAVIData.MotionBlur = true;
            swSaveAVIData.BlurLength = 10;
            swSaveAVIData.BlurOffset = -100;
            swMotionStudy1.Stop();

            //Save animation as .avi file
            swMotionStudy1.SaveToAVI("C:\\test\\Anim1.avi", swSaveAVIData);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
