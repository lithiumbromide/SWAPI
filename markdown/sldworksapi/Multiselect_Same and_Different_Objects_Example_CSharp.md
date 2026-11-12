---
title: "Multiselect Same and Different Objects Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Multiselect_Same and_Different_Objects_Example_CSharp.htm"
---

# Multiselect Same and Different Objects Example (C#)

This example shows how to select multiple faces, multiple edges, and multiple faces and edges.

```
//---------------------------------------------------------
// Preconditions:
// 1. Verify that the part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the part.
// 2. Selects and adds three faces to an array of faces.
// 3. Selects and adds two edges to an array of edges.
// 4. Selects one face and three edges and adds them to an
//    array of entities.
// 5. Multiselects each array of faces, edges, and entities.
// 6. Examine the Immediate window.
//
// NOTE: Because the part is used elsewhere do not save
// changes.
//---------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System.Diagnostics;
using System.Windows.Forms;

namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public PartDoc swPart;

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Face2[] faceArray = new Face2[3];
            Edge[] edgeArray = new Edge[2];
            Entity[] entitiesArray = new Entity[4];
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;
            int nbrSelections = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\box.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;

            //Select three faces and add them to an array of faces
            status = swModelDocExt.SelectByID2("", "FACE", 0.00339003579642849, 0.0165689832048201, 0.0460521566345733, false, 0, null, 0);
            faceArray[0] = (Face2)swSelMgr.GetSelectedObject6(1, -1);
            status = swModelDocExt.SelectByID2("", "FACE", -0.00464858017755887, 0.0299999999999159, -0.00213158882201014, false, 0, null, 0);
            faceArray[1] = (Face2)swSelMgr.GetSelectedObject6(1, -1);
            status = swModelDocExt.SelectByID2("", "FACE", -0.0310506911185371, 0.0299999999999159, -0.016600178364456, false, 0, null, 0);
            faceArray[2] = (Face2)swSelMgr.GetSelectedObject6(1, -1);
            swModel.ClearSelection2(true);

            //Select two edges and them to an array of edges
            status = swModelDocExt.SelectByID2("", "EDGE", -0.0103092369793103, 0.0304904435424191, 0.0457189565300382, false, 0, null, 0);
            edgeArray[0] = (Edge)swSelMgr.GetSelectedObject6(1, -1);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.0437175784318242, 0.0301364202527452, 0.028332486890065, false, 0, null, 0);
            edgeArray[1] = (Edge)swSelMgr.GetSelectedObject6(1, -1);
            swModel.ClearSelection2(true);

            //Select one face and three edges and add them to an array of entities
            status = swModelDocExt.SelectByID2("", "FACE", -0.00725501009526397, 0.0299999999999159, -0.00236379374842954, false, 0, null, 0);
            entitiesArray[0] = (Entity)swSelMgr.GetSelectedObject6(1, -1);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.0435139962395397, 0.0148277472299014, 0.0462522660892546, false, 0, null, 0);
            entitiesArray[1] = (Entity)swSelMgr.GetSelectedObject6(1, -1);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.0441251049156222, -0.000180110278279244, 0.0139372949385006, false, 0, null, 0);
            entitiesArray[2] = (Entity)swSelMgr.GetSelectedObject6(1, -1);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.0303098420922652, 0.000354499639115602, 0.0458113148115444, false, 0, null, 0);
            entitiesArray[3] = (Entity)swSelMgr.GetSelectedObject6(1, -1);
            swModel.ClearSelection2(true);

            //Multiselect faces, edges, and entities using IModelDocExtension::MultiSelect2
            Debug.Print("Number of selections in:");
            nbrSelections = swModelDocExt.MultiSelect2(faceArray, false, null);
            Debug.Print("  face array: " + nbrSelections);
            swModel.ClearSelection2(true);
            nbrSelections = swModelDocExt.MultiSelect2(edgeArray, false, null);
            Debug.Print("  edge array: " + nbrSelections);
            swModel.ClearSelection2(true);
            nbrSelections = swModelDocExt.MultiSelect2(entitiesArray, false, null);
            Debug.Print("  entities (face and edges) array: " + nbrSelections);
            swModel.ClearSelection2(true);

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
