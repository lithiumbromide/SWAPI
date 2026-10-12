---
title: "Set Tolerances and Compare Geometry Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swutilitiesapi/Set_Tolerances_and_Compare_Geometry_CSharp.htm"
---

# Set Tolerances and Compare Geometry Example (C#)

his example shows how to set the tolerances and then compare the volume and geometry of two versions of the same part using the SOLIDWORKS Utilities API.

```
'------------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Utilities as an add-in
'    (in SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Utilities).
' 2. Add the SOLIDWORKS Utilities interop assembly as a reference
'    (right-click the project in Project Explorer, click Add Reference >
'    browse to install_dir\api\redist > SolidWorks.Interop.gtswutilities.dll).
' 3. Verify that the specified files exist.
' 4. Verify that C:\test\ exists.
'
' Postconditions:
' 1. Creates a geometry comparison report, C:\test\Report\gtReportIndex.htm.
' 2. Gets position and angular tolerance statuses.
' 3. Gets face and volume comparison statuses.
' 4. Examine the Immediate window, graphics area, and C:\test\Report\gtReportIndex.htm.
'
' NOTE: Because the parts are used elsewhere, do not save changes.
'-------------------------------------------------------------------------
```

```vb
using SOLIDWORKS.Interop.sldworks;
using SOLIDWORKS.Interop.swconst;
using SOLIDWORKS.Interop.gtswutilities;
using System;
using System.Diagnostics;
namespace SetTolerancesAndCompareGeometry_CSharp.csproj
{
    partial class SOLIDWORKSMacro
    {
        PartDoc Part;

        public void Main()
        {
            Part = (PartDoc)swApp.ActiveDoc;

            gtcocswUtilities swUtil = default(gtcocswUtilities);
            gtcocswCompareGeometry swUtilCompGeom = default(gtcocswCompareGeometry);
            gtcocswUtilOptions OUtils = default(gtcocswUtilOptions);
            string file1 = null;
            string file2 = null;
            string reportname = null;
            int errorcode = 0;
            double posTol = 0;
            double angTol = 0;
            bool AddToDesignBinder = false;
            bool OverwriteReport = false;

            reportname = "C:\\test\\Report";
            AddToDesignBinder = false;
            OverwriteReport = true;

            // Get pointer to SOLIDWORKS Utilities interface
            swUtil = (gtcocswUtilities)swApp.GetAddInObject("Utilities.UtilitiesApp");

            // Get pointer to SOLIDWORKS Compare Geometry tool
            swUtilCompGeom = (gtcocswCompareGeometry)swUtil.GetToolInterface((int)gtSwTools_e.gtSwToolGeomDiff, out errorcode);

            // Get SOLIDWORKS Utilities options
            OUtils = swUtil.options;
            posTol = 0.0001;
            // Meters
            angTol = 1E-06;
            // Radians
            // Set position tolerance
            errorcode = OUtils.SetPositionTolerance(posTol);
            Debug.Print("Position tolerance is set." + " gtError_e: " + errorcode);
            // Set angular tolerance
            errorcode = OUtils.SetAngularTolerance(angTol);
            Debug.Print("Angular tolerance is set." + " gtError_e: " + errorcode);
            Debug.Print("");
            int volDiffStatus = 0;
            int faceDiffStatus = 0;
            file1 = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\swutilities\\bracket_a.sldprt";
            file2 = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\swutilities\\bracket_b.sldprt";

            // Compare the geometry of the faces and volumes and save results to a report
            errorcode = swUtilCompGeom.CompareGeometry3(file1, "", file2, "", (int)gtGdfOperationOption_e.gtGdfFaceAndVolumeCompare, (int)gtResultOptions_e.gtResultSaveReport, reportname, AddToDesignBinder, OverwriteReport, ref volDiffStatus,
            ref faceDiffStatus);
            if (!(errorcode == (int)gtError_e.gtNOErr))
            {
                Debug.Print("Error comparing geometries. Inspect gtError_e = " + errorcode + " in the API help.");
            }
            diffStatus("Volume comparison", volDiffStatus);
            diffStatus("Face comparison", faceDiffStatus);

            // Perform any necessary cleanup
            errorcode = swUtilCompGeom.Close();
        }

        public void diffStatus(string name, int diffCode)
        {
            Debug.Print(name);
            switch (diffCode)
            {
                case (int)gtVolDiffStatusOptionType_e.gtSuccess:
                    Debug.Print("Succeeded");
                    break;
                case (int)gtVolDiffStatusOptionType_e.gtNotPerformed:
                    Debug.Print("Not performed");
                    break;
                case (int)gtVolDiffStatusOptionType_e.gtCanceled:
                    Debug.Print("Canceled");
                    break;
                case (int)gtVolDiffStatusOptionType_e.gtFailed:
                    Debug.Print("Failed");
                    break;
                case (int)gtVolDiffStatusOptionType_e.gtIdenticalParts:
                    Debug.Print("Identical parts");
                    break;
                case (int)gtVolDiffStatusOptionType_e.gtDifferentParts:
                    Debug.Print("Different parts");
                    break;
                case (int)gtVolDiffStatusOptionType_e.gtNoSolidBody:
                    Debug.Print("No solid body found");
                    break;
                case (int)gtVolDiffStatusOptionType_e.gtAlreadySaved:
                    Debug.Print("Already saved");
                    break;
            }
            Debug.Print("");
        }
        public SldWorks swApp;
    }
}
```
