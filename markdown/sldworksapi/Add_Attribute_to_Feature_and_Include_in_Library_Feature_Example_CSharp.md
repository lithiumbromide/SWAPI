---
title: "Add Attribute to Feature and Include in Library Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_CSharp.htm"
---

# Add Attribute to Feature and Include in Library Feature Example (C#)

This example shows how to add an attribute to a feature and include that attribute with the feature if the feature is saved as a library feature. This example also includes instructions on how to verify that the attribute is included on each instance of the library feature.

```
//-----------------------------------------------------------------
// Preconditions:
// 1. Open a new part document.
// 2. Sketch a rectangle and extrude it.
// 3. Sketch a straight slot that fits on a face of
//    of the just-created extrude and cut-extrude the slot.
//
//    NOTE: The cut-extrude must be named Cut-Extrude1.
//
// 4. Open the Immediate window.
//
// Postconditions:
// 1. Adds the cut-extrude feature to the part document with
//    an attribute of TestAttribute, which is visible in the
//    FeatureManager design tree.
// 2. Examine the Immediate window.
// 3. To verify that the attribute is included in a library feature:
//    a. Click Design Library on the Task Pane.
//       1. Click Add to Library.
//       2. Click Cut-Extrude1 in the flyout FeatureManager design tree.
//       3. Type a file name for the library feature.
//       4. Select the folder where to save the library feature.
//       5. Click OK.
//    b. Open an existing model document and drag-and-drop the
//       just-created library feature on the model and click OK.
//    c. Expand the just-dropped library feature in the FeatureManager
//       design tree to verify that Cut-Extrude1 and TestAttribute appear
//       beneath the just-dropped library feature in the FeatureManager
//       design tree.
//-------------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Diagnostics;
using System;

namespace NameAttributeCSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Feature swFeature = default(Feature);
            SolidWorks.Interop.sldworks.Attribute swAttribute = default(SolidWorks.Interop.sldworks.Attribute);
            AttributeDef swAttributeDef = default(AttributeDef);
            Face2 swFace = default(Face2);
            Parameter swParameter = default(Parameter);
            Object[] Faces = null;
            bool @bool = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = swModel.Extension;
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;

            // Create attribute
            swAttributeDef = (AttributeDef)swApp.DefineAttribute("TestPropagationOfAttribute");
            @bool = swAttributeDef.AddParameter("TestAttribute", (int)swParamType_e.swParamTypeDouble, 2.0, 0);
            @bool = swAttributeDef.Register();

            // Select the feature to which to add the attribute
            @bool = swModelDocExt.SelectByID2("Cut-Extrude1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            Debug.Print("Name of feature to which to add attribute: " + swFeature.Name);

            // Add the attribute to one of the feature's faces
            Faces = (Object[])swFeature.GetFaces();
            swFace = (Face2)Faces[0];
            swAttribute = swAttributeDef.CreateInstance5(swModel, swFace, "TestAttribute", 0, (int)swInConfigurationOpts_e.swAllConfiguration);
            swAttribute.IncludeInLibraryFeature = true;
            Debug.Print("Include attribute in library feature? " + swAttribute.IncludeInLibraryFeature);
            Debug.Print("Name of attribute: " + swAttribute.GetName());
```

// Get name of parameter
swParameter = (

Parameter)swAttribute.**GetParameter**("TestAttribute");
Debug.Print("Parameter name: " + swParameter.**GetName**());

```
            swModel.ForceRebuild3(false);

        }

        public SldWorks swApp;

    }

}
```
