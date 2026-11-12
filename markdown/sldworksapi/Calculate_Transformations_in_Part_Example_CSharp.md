---
title: "Calculate Transformations in Part Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Calculate_Transformations_in_Part_Example_CSharp.htm"
---

# Calculate Transformations in Part Example (C#)

This example shows how to calculate transformations between solid bodies in a part, which would make one solid body coincide with another solid body if the transformation matrix is applied.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Ensure that the specified part file to
//    open exists.
// 2. Open the Immediate window.
// 3. Run the macro.
//
// Postconditions:
// 1. Opens the specified part file.
// 2. Gets the solid bodies in the specified part file.
// 3. Iterates through the solid bodies in the part
//    and calculates transformations between solid
//    bodies.
// 4. Examine the Immediate window.
//----------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace CoincidenceCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelMgr = default(SelectionMgr);
            string file = null;
            int status = 0;
            int warnings = 0;

            file = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\routing-pipes\\routes\\Framework (Done).SLDPRT";
            swModel = (ModelDoc2)swApp.OpenDoc6(file, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref status, ref warnings);
            if (swModel == null)
                return;

            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            PartDoc swPart = default(PartDoc);
            swPart = (PartDoc)swModel;

            object[] bodies = null;
            Body2 swBody_A = default(Body2);
            Body2 swBody_B = default(Body2);

            //Get solid bodies
            swBodyType_e bodyType = default(swBodyType_e);
            bool visibleOnly = false;
            bodyType = swBodyType_e.swSolidBody;
            visibleOnly = true;
            bodies = (object[])swPart.GetBodies2((int)bodyType, visibleOnly);
            //Iterate through the solid bodies in the part
            //and calculate the transformation matrix between
            //swBody_A and swBody_B
            if (!((bodies == null)))
            {
                int i = 0;
                int j = 0;
                int maxIndex = 0;
                maxIndex = bodies.Length;
                for (i = 0; i <= maxIndex - 1; i++)
                {
                    swBody_A = (Body2)bodies[i];
                    for (j = 0; j <= maxIndex - 1; j++)
                    {
                        if (i != j)
                        {
                            swBody_B = (Body2)bodies[j];

                            MathTransform swXfm = default(MathTransform);
                            bool bResult = false;
                            swXfm = null;
                            bResult = false;
                            bResult = swBody_A.GetCoincidenceTransform2(swBody_B, out swXfm);

                            Debug.Print(i + " -> " + j, swBody_A.Name + " -> " + swBody_B.Name);

                            if (bResult != false)
                            {
                                Debug.Print("\n" + "  Can coincide.");
                                double[] vXfm = null;
                                vXfm = (double[])swXfm.ArrayData;
                                Debug.Print("\n" + "  Rotation:");
                                Debug.Print("\n" + "    " + vXfm[0], vXfm[1], vXfm[2]);
                                Debug.Print("\n" + "    " + vXfm[3], vXfm[4], vXfm[5]);
                                Debug.Print("\n" + "    " + vXfm[6], vXfm[7], vXfm[8]);
                                Debug.Print("\n" + "  Translation:");
                                Debug.Print("\n" + "    " + vXfm[9], vXfm[10], vXfm[11]);
                                Debug.Print("\n" + "  Scaling: " + vXfm[12]);

                            }
                            else
                            {
                                Debug.Print("  Cannot coincide.");
                            }
                        }
                    }
                }
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
