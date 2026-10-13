---
title: "Insert and Use Plane with Manipulator Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swpublishedapi/Insert_and_Use_Plane_with_Manipulator_Example_CSharp.htm"
---

# Insert and Use Plane with Manipulator Example (C#)

This example shows how to insert a plane with a manipulator.

//--------------------------------------------------------------
// Preconditions:
// 1. In the IDE:
// a. Click **Project > Add Reference > COM >**
// **SolidWorks.Interop.swpublished**.
// b. Click **Project > Add Reference > COM >**
// **Microsoft.Basic.**
// c. Copy the code in [SolidWorksMacro.cs](#solidworksmacro.cs) to your project
// and create a class and copy the code in [Class1.cs](#class1.cs)
// to that class.
// d. Open the Immediate window.
// 2. Ensure that the specified part document exists.
//
// Postconditions:
// 1. Part document opens.
// 2. Plane with manipulator is displayed.
// 3. Distance, angles, height, and width of the plane are
// printed to the Immediate window.
// 4. Click and hold the right-mouse button and drag the
// plane up and down, which calls the handler. The handle
// index is printed to the Immediate window at each drag.
// 5. Click and hold the right-mouse button and rotate the plane,
// which calls the handler. The handle index
// is printed to the Immediate window at each rotation.
//
// NOTE: Because the part document is used elsewhere, do not
// save any changes when closing the document.
//---------------------------------------------------------------

// SolidWorksMacro.cs

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using SolidWorks.Interop.swpublished;
using Microsoft.VisualBasic;

namespace PlaneManipulatorCSharp.csproj
{
partial class SolidWorksMacro
{
public Class1 swHdlr;
public Manipulator swManipulator;
public PlaneManipulator swPlaneManipulator;

public void Main()
{
ModelDoc2 swModelDoc = default(ModelDoc2);
ModelViewManager swModelViewMgr = default(ModelViewManager);

string fileName = null;
int errors = 0;
int warnings = 0;

swHdlr = new Class1();

fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\SOLIDWORKS 2018\\samples\\tutorial\\fillets\\knob.sldprt";
swModelDoc = (ModelDoc2)swApp.**OpenDoc6**(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

// Create the plane with a manipulator
swModelViewMgr = (ModelViewManager)swModelDoc.**ModelViewManager**;
swManipulator = (Manipulator)swModelViewMgr.**CreateManipulator**((int)swManipulatorType_e.swPlaneManipulator, swHdlr);
swPlaneManipulator = (PlaneManipulator)swManipulator.**GetSpecificManipulator**();

// Set the distance of plane
swPlaneManipulator.**Distance** = 0.04;
Debug.Print("Distance = " + swPlaneManipulator.**Distance**);

//Set the angles of plane
swPlaneManipulator.**XAngle** = 2 * PiVal() / 180;
Debug.Print("X = " + swPlaneManipulator.**XAngle**);

swPlaneManipulator.**YAngle** = 10 * PiVal() / 180;
Debug.Print("Y = " + swPlaneManipulator.**YAngle**);

// Set the height and width of plane
swPlaneManipulator.**Height** = 0.1;
Debug.Print("Height = " + swPlaneManipulator.**Height**);

swPlaneManipulator.**Width** = 0.075;
Debug.Print("Width = " + swPlaneManipulator.**Width**);

// Set the color of plane to red
swPlaneManipulator.**Color** = Information.RGB(255, 0, 0);

// Update the plane's properties
swPlaneManipulator.**Update**();

// Show the plane with the manipulator
swManipulator.**Show**(swModelDoc);

}

public double PiVal()
{
// Set PI
return 4 * System.Math.Atan(1);
}

/// <summary>
/// The SldWorks swApp variable is pre-assigned for you.
/// </summary>

public SldWorks swApp;
}
}

[Back to top](#top)

// Class1.cs

```vb
using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swpublished;
 using System;
 using System.Diagnostics;
 using System.Runtime;

 [System.Runtime.InteropServices.ComVisibleAttribute(true)]
 public  class  Class1 : SwManipulatorHandler2
 {

     public  void SwManipulatorHandler2_OnUpdateDrag(object pManipulator, long handleIndex, object newPosMathPt)
     {
         Debug.Print("SwManipulatorHandler2_OnUpdateDrag");
         Debug.Print("  HandleIndex      = " + handleIndex);
         PlaneManipulator swRetManip = default(PlaneManipulator);
         swRetManip = (PlaneManipulator)pManipulator;

         if ((handleIndex == 8))
         {
             double retDist = 0;
             retDist = swRetManip.Distance;
         }
         else
         {
             double angleX = 0;
             double angleY = 0;
             angleX = swRetManip.XAngle;
             angleY = swRetManip.YAngle;
         }

     }

     public  bool SwManipulatorHandler2_OnDelete(object pManipulator)
     {
         return  false;
     }

     public  void SwManipulatorHandler2_OnDirectionFlipped(object pManipulator)
     {

     }

     public  bool SwManipulatorHandler2_OnDoubleValueChanged(object pManipulator, long Id, double Value)
     {
         return  false;
     }

     public  void SwManipulatorHandler2_OnEndNoDrag(object pManipulator, long handleIndex)
     {

     }

     public  void SwManipulatorHandler2_OnHandleRmbSelected(object pManipulator, long handleIndex)
     {

     }

     public  bool SwManipulatorHandler2_OnHandleLmbSelected(object pManipulator)
     {
         return  false;
     }

     public  void SwManipulatorHandler2_OnHandleSelected(object pManipulator, long handleIndex)
     {

     }

     public  void SwManipulatorHandler2_OnItemSetFocus(object pManipulator, long Id)
     {

     }

     public  bool SwManipulatorHandler2_OnLmbSelected(object pManipulator)
     {
         return  false;
     }

     public  bool SwManipulatorHandler2_OnStringValueChanged(object pManipulator, long Id, string Value)
     {
         return  false;
     }

     public  void SwManipulatorHandler2_OnEndDrag(object pMani, long index)
     {

     }

     public  bool OnDelete(object pManipulator)
     {
         return  false;
     }

     public  void OnDirectionFlipped(object pManipulator)
     {

     }

     public  bool OnDoubleValueChanged(object pManipulator, int handleIndex, ref  double Value)
     {
         return  false;
     }

     public  void OnEndDrag(object pManipulator, int handleIndex)
     {

     }

     public  void OnEndNoDrag(object pManipulator, int handleIndex)
     {

     }

     public  bool OnHandleLmbSelected(object pManipulator)
     {
         return  false;
     }

     public  void OnHandleRmbSelected(object pManipulator, int handleIndex)
     {

     }

     public  void OnHandleSelected(object pManipulator, int handleIndex)
     {

     }

     public  void OnItemSetFocus(object pManipulator, int handleIndex)
     {

     }

     public  bool OnStringValueChanged(object pManipulator, int handleIndex, ref  string Value)
     {
         return  false;
     }

     public  void OnUpdateDrag(object pManipulator, int handleIndex, object newPosMathPt)
     {

     }

 }
```

[Back to top](#top)
