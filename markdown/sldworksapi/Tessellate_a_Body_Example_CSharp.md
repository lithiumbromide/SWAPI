---
title: "Tessellate a Body Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Tessellate_a_Body_Example_CSharp.htm"
---

# Tessellate a Body Example (C#)

```
//-----------------------------------------------------------------
// Preconditions:
// 1. Verify that the part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Tessellates the body.
// 2. Examine the graphics area and Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//-----------------------------------------------------------------
using System;
```

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Diagnostics;
namespace TessellateABody_CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public SldWorks swApp;
        public void Main()
        {
            int errors = 0;
            int warnings = 0;
            // Get the active document
            ModelDoc2 swModel = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\drive shaft plate.sldprt", (int)swDocumentTypes_e.swDocPART, 0, "", ref errors, ref warnings);
            // Get the document title
            Debug.Print(swModel.GetTitle());
            // Cast down to a part
            PartDoc swPart = (PartDoc)swModel;
            // Variant is returned, which can be dealt with as an object
            // Variant represents an array of references
            System.Object vBodies;
            System.Array aBodies;
            // Get bodies
            vBodies = swPart.GetBodies2((int)swBodyType_e.swAllBodies, false);
            // Cast to an array of bodies
            aBodies = (System.Array)vBodies;
            int iNumBodies = aBodies.Length;
            int iNumSolidBodies = 0;
            int iNumSheetBodies = 0;
            // Loop through array
            Body2 swBody;
            for (int b = 0; b < iNumBodies; b++)
            {
                // Get a body and apply cast
                swBody = (Body2)aBodies.GetValue(b);
                // Now call a method on a body
                int nBodyType = swBody.GetType();
                if (nBodyType == (int)swBodyType_e.swSheetBody)
                {
                    iNumSheetBodies++;
                }
                if (nBodyType == (int)swBodyType_e.swSolidBody)
                {
                    iNumSolidBodies++;
                    Face2 swFace = null;
                    Tessellation swTessellation = null;
                    bool bResult = false;
                    // Pass in null so the whole body will be tessellated
                    swTessellation = (Tessellation)swBody.GetTessellation(null);
                    // Set up the Tessellation object
                    swTessellation.NeedFaceFacetMap = true;
                    swTessellation.NeedVertexParams = true;
                    swTessellation.NeedVertexNormal = true;
                    swTessellation.ImprovedQuality = true;
                    Debug.Print("Tessellation is configured for higher-quality data output.");
                    // How to handle matches across common edges
                    swTessellation.MatchType = (int)swTesselationMatchType_e.swTesselationMatchFacetTopology;
                    // Do it
                    bResult = swTessellation.Tessellate();
                    // Get the number of vertices and facets
                    Debug.Print("Number of vertices: " + swTessellation.GetVertexCount());
                    Debug.Print("Number of facets: " + swTessellation.GetFacetCount());
                    // Now get the facet data per face
                    int[] aFacetIds;
                    int iNumFacetIds;
                    int[] aFinIds;
                    int[] aVertexIds;
                    double[] aVertexCoords1;
                    double[] aVertexCoords2;
                    // Add sketch for this body
                    // Speed things up
                    swModel.SetAddToDB(true);
                    swModel.SetDisplayWhenAdded(false);
                    swModel.Insert3DSketch2(false);
                    // Loop over faces
                    swFace = (Face2)swBody.GetFirstFace();
                    while (swFace != null)
                    {
                        aFacetIds = (int[])swTessellation.GetFaceFacets(swFace);
                        iNumFacetIds = aFacetIds.Length;
                        for (int iFacetIdIdx = 0; iFacetIdIdx < iNumFacetIds; iFacetIdIdx++)
                        {
                            aFinIds = (int[])swTessellation.GetFacetFins(aFacetIds[iFacetIdIdx]);
                            // There should always be three fins per facet
                            for (int iFinIdx = 0; iFinIdx < 3; iFinIdx++)
                            {
                                aVertexIds = (int[])swTessellation.GetFinVertices(aFinIds[iFinIdx]);
                                // Should always be two vertices per fin
                                aVertexCoords1 = (double[])swTessellation.GetVertexPoint(aVertexIds[0]);
                                aVertexCoords2 = (double[])swTessellation.GetVertexPoint(aVertexIds[1]);
                                // Create a line
                                swModel.CreateLine2(aVertexCoords1[0], aVertexCoords1[1], aVertexCoords1[2], aVertexCoords2[0], aVertexCoords2[1], aVertexCoords2[2]);
                            }
                        }
                        swFace = (Face2)swFace.GetNextFace();
                    }
                    // Close sketch
                    swModel.Insert3DSketch2(true);
                    // Clear selection for next pass
                    swModel.ClearSelection2(true);
                    // Restore settings
                    swModel.SetAddToDB(false);
                    swModel.SetDisplayWhenAdded(true);
                }
            }
            return;
        }
    }
}
```
