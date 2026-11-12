---
title: "Process Body Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Process_Body_Example_CSharp.htm"
---

# Process Body Example (C#)

This example shows how create to a new part with an imported body from the processed body of the original part.

```
//------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document template
//    exists.
// 2. Open a part containing only one solid body.
// 3. Open the Immediate window.
// 4. Run the macro.
//
// Postconditions:
// 1. Creates a new part with an imported body
//    from the processed body of the original part.
// 2. Examine the Immediate window.
//
// NOTE: Differences are best seen in wireframe and with parts
// that contain curved, circular, or both types of faces.
//--------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace ProcessbodyCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
```

```
            // 1 radian = 180º/p = 57.295779513º or approximately 57.3º
            const double RadPerDeg = 1.0 / 57.3;
            const double MaxUAngle = 1.0 * RadPerDeg;
            const double MaxVAngle = 1.0 * RadPerDeg;

            ModelDoc2 swModel = default(ModelDoc2);
            Body2 swBody = default(Body2);
            Body2 swProcBody = default(Body2);
            PartDoc swPart = default(PartDoc);
            PartDoc swNewPart = default(PartDoc);
            Feature swFeat = default(Feature);
            object[] vBodies = null;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swPart = (PartDoc)swModel;
            vBodies = (object[])swPart.GetBodies2((int)swBodyType_e.swSolidBody, false);
            swBody = (Body2)vBodies[0];
            swProcBody = (Body2)swBody.GetProcessedBody2(MaxUAngle, MaxVAngle);
            swNewPart = (PartDoc)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2013\\templates\\part.prtdot", 0, 0, 0);
            swFeat = (Feature)swNewPart.CreateFeatureFromBody3(swProcBody, false, (int)swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck);
            Debug.Print("File = " + swModel.GetPathName());
            Debug.Print("  Body faces            = " + swBody.GetFaceCount());
            Debug.Print("  Processed body faces  = " + swProcBody.GetFaceCount());

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
