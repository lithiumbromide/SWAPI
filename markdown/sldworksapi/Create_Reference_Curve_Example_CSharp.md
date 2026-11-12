---
title: "Create Reference Curve Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Reference_Curve_Example_CSharp.htm"
---

# Create Reference Curve Example (C#)

This example shows how to create a reference curve by first creating a temporary spline curve.

```
//----------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document template exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens a new part document.
// 2. Adds a reference curve to the part document.
// 3. Selects an endpoint on the reference curve
//    and prints to the Immediate window the
//    endpoint's position and coordinates.
// 4. Examine the graphics area and Immediate window.
//----------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace EdgePointCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            PartDoc swPart = default(PartDoc);
            Body2 swBody = default(Body2);
            Curve[] swCurve = new Curve[1];
            object vCurve = null;
            ReferenceCurve swRefCurve = default(ReferenceCurve);
            object swSelObj = null;
            SelectionMgr swSelMgr = default(SelectionMgr);
            EdgePoint swEdgePoint = default(EdgePoint);
            bool bRet = false;
            int nRetVal = 0;
            int iDim = 0;
            int iOrd = 0;
            int incp = 0;
            int iper = 0;
            double[] dprops = new double[2];
            double[] knots = new double[10];
            double[] cPoints = new double[18];
            object vprops = null;
            object vknots = null;
            object vcPoints = null;
            int selType = 0;
            double x = 0;
            double y = 0;
            double z = 0;
            int iValueIn1 = 65535;
            int iValueIn2 = 345;
            double dValueOut = 0;
            DoubleIntConv.Pack(iValueIn1, iValueIn2, ref dValueOut);

            //Open new part document and create a body
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SolidWorks 2015\\templates\\Part.prtdot", 0, 0, 0);
            swPart = (PartDoc)swModel;
            swBody = (Body2)swPart.CreateNewBody();

            //Create a curve
            //Set properties
            iDim = 3;
            iOrd = 4;
            incp = 6;
            iper = 0;
            DoubleIntConv.Pack(iDim, iOrd, ref dprops[0]);
            DoubleIntConv.Pack(incp, iper, ref dprops[1]);
            vprops = dprops;

            //Set knots
            knots[0] = 0;
            knots[1] = 0;
            knots[2] = 0;
            knots[3] = 0;
            knots[4] = 0.33096;
            knots[5] = 0.72;
            knots[6] = 1;
            knots[7] = 1;
            knots[8] = 1;
            knots[9] = 1;
            vknots = knots;

            //Set control points
            cPoints[0] = 0;
            cPoints[1] = 0;
            cPoints[2] = 0;
            cPoints[3] = 0.008703;
            cPoints[4] = 0.016501;
            cPoints[5] = 0;
            cPoints[6] = 0.027636;
            cPoints[7] = 0.052399;
            cPoints[8] = 0;
            cPoints[9] = 0.069472;
            cPoints[10] = -0.011297;
            cPoints[11] = 0;
            cPoints[12] = 0.090421;
            cPoints[13] = 0.017622;
            cPoints[14] = 0;
            cPoints[15] = 0.099188;
            cPoints[16] = 0.029725;
            cPoints[17] = 0;
            vcPoints = cPoints;

            //Create a spline curve
            swCurve[0] = (Curve)swBody.AddProfileBspline((vprops), (vknots), (vcPoints));
            vCurve = (object)swCurve;

            //Create a reference curve
            swRefCurve = (ReferenceCurve)swModel.FeatureReferenceCurve(1, (vCurve), true, "", out nRetVal);

            //Rebuild to display curve
            swModel.EditRebuild3();

            //Get endpoint on reference curve
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            bRet = swModelDocExt.SelectByID2("Unknown", "POINTREF", 0, 0, 0, false, 0, null, 0);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            selType = swSelMgr.GetSelectedObjectType3(1, -1);
            Debug.Print("Type of selection: " + selType);
            if ((int)swSelectType_e.swSelPOINTREFS == selType)
            {
                swSelObj = (object)swSelMgr.GetSelectedObject6(1, -1);
                swEdgePoint = (EdgePoint)swSelObj;
                Debug.Print(" Position of the endpoint: " + swEdgePoint.Position);
                swEdgePoint.GetPointCoordinates(out x, out y, out z);
                Debug.Print(" Endpoint coordinates: " + x + ", " + y + ", and " + z);
            }

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;

    }

    [System.Runtime.InteropServices.StructLayout(LayoutKind.Explicit)]
    public class DoubleIntConv
    {

        //An 8-byte double contains 2 4-byte integers
        [System.Runtime.InteropServices.FieldOffset(0)]
        private int m_Int1;
        [System.Runtime.InteropServices.FieldOffset(4)]
        private int m_Int2;
        [System.Runtime.InteropServices.FieldOffset(0)]
        private double m_Double;

        private DoubleIntConv(double dValue)
        {
            //C# wants these initialized in the constructor
            m_Int1 = 0;
            m_Int2 = 0;
            m_Double = dValue;
        }

        private DoubleIntConv(int iValue1, int iValue2)
        {
            //C# wants these initialized in the constructor
            m_Double = 0.0;
            m_Int1 = iValue1;
            m_Int2 = iValue2;
        }

        // Use an out parameter, so client code can pass in an uninitialized variable
        public static void Pack(int iIn1, int iIn2, ref double dOut)
        {
            DoubleIntConv cv = null;
            cv = new DoubleIntConv(iIn1, iIn2);
            dOut = cv.m_Double;
        }

    }
}
```
