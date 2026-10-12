---
title: "Roll Back Model Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Roll_Back_Model_Example_CSharp.htm"
---

# Roll Back Model Example (C#)

This example shows how to step through the FeatureManager design tree of a model by rolling back to each feature in reverse sequence. Running an example like this can provide insight into the design intent of the user.

```
//-----------------------------------
// Preconditions:
// 1. Open a part or assembly document.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Observe the FeatureManager design tree
//    while the macro executes.
// 2. Examine the Immediate window to see the
//    names of the features rolled back and forward.
//
// NOTE: The delay between steps is set to 1 second.
//-----------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;
using System.Collections;

namespace EditRollbackCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelView swModelView = default(ModelView);
            PartDoc swPart = default(PartDoc);
            AssemblyDoc swAssy = default(AssemblyDoc);
            FeatureManager swFeatMgr = default(FeatureManager);
            Feature swFeat = default(Feature);
            object[] featFace = null;
            Face2 swFace = default(Face2);
            object rect = null;
            string featureName = null;
            ArrayList featName = new ArrayList();
            string nameString;
            int docType = 0;
            int i = 0;
            int j = 0;
            bool status = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelView = (ModelView)swModel.ActiveView;
            rect = null;
            swFeatMgr = (FeatureManager)swModel.FeatureManager;

            swFeat = (Feature)swModel.FirstFeature();
            docType = swModel.GetType();
            switch (docType)
            {
                case (int)swDocumentTypes_e.swDocPART:
                    swPart = (PartDoc)swModel;
                    break;
                case (int)swDocumentTypes_e.swDocASSEMBLY:
                    swAssy = (AssemblyDoc)swModel;
                    break;
                default:
                    Debug.Print("Open a part or assembly document, then rerun this macro.");
                    break;
            }

            while ((swFeat != null))
            {
                featureName = swFeat.Name;
                featName.Add(featureName);
                swFeat = (Feature)swFeat.GetNextFeature();
            }

            // Playback each feature in the FeatureManager design tree
            for (i = 0; i <= ((featName.Count) - 1); i++)
            {
                nameString = (string)featName[i];
                Debug.Print(nameString);
                status = swFeatMgr.EditRollback((int)swMoveRollbackBarTo_e.swMoveRollbackBarToAfterFeature, nameString);
                // Do not assert because you may be trying to roll back or roll forward
                // to a feature that cannot be rolled back or forward to; for example,
                // the Lighting or Annotations folder
                //Debug.Assert status

                // Remove any previous highlights
                swModelView.GraphicsRedraw(rect);
                // Highlight feature if it has any geometry
                switch (docType)
                {
                    case (int)swDocumentTypes_e.swDocPART:
                        swPart = (PartDoc)swModel;
                        swFeat = (Feature)swPart.FeatureByName(nameString);
                        break;
                    case (int)swDocumentTypes_e.swDocASSEMBLY:
                        swAssy = (AssemblyDoc)swModel;
                        swFeat = (Feature)swAssy.FeatureByName(nameString);
                        break;
                }

                featFace = (object[])swFeat.GetFaces();
                if (featFace != null)
                {
                    for (j = 0; j <= ((featFace.GetUpperBound(0))); j++)
                    {
                        swFace = (Face2)featFace[j];
                        swFace.Highlight(true);
                    }
                }

                // Only pause if rollback is successful
                if (status)
                {
                    // Pause for 1 second
                    System.Threading.Thread.Sleep(1000);
                    // Allow SOLIDWORKS Design to refresh screen
                    System.Windows.Forms.Application.DoEvents();
                }
            }
            // Remove highlight from last feature
            swModelView.GraphicsRedraw(rect);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
