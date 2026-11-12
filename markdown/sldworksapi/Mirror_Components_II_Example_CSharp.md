---
title: "Mirror Components II Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Mirror_Components_II_Example_CSharp.htm"
---

# Mirror Components II Example (C#)

This example shows how to mirror components in an assembly.

```vb
 //---------------------------------------------------------------------------------
 // Preconditions:
 // 1. Open C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2020\samples\tutorial\advdrawings\98food processor.sldasm.
 // 2. Ensure that c:\API\MirrorComps exists.
```

//

```vb
 // Postconditions:
 // 1. Creates Plane4 mirror plane.
 // 2. Creates mirror copies of gear- caddy-1 and middle-gear-1, both aligned to component origins.
 // 3. Creates mirror copies of shaft gear-1 and middle-gear plate-1, aligned to PLANE2 and PLANE3, respectively.
 // 4. Creates opposite-hand versions of base plate-1 and shaft gear insert-1, called FileName1.sldprt and FileName2.sldprt, respectively, and stored in c:\API\MirrorComps.
 // 5. Replaces FileName1.sldprt with check1.sldprt in c:\API\MirrorComps.
 // 6. Creates MirrorComponent1 in the FeatureManager design tree.
 // 7. Modifies MirrorComponent1 to change the mirror type, the align to origin component orientations, and the align to selection orientations.
```

//

```vb
 // NOTE: Because the model is used elsewhere, do not save any changes to it.
```

//---------------------------------------------------------------------------------------

```vb
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace MirrorComponent_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

                 private   ModelDoc2 swModel;
                private   AssemblyDoc swAssem;
                private   Feature swFeat;
                private   Feature mirrorPlane;
                private   FeatureManager FeatMgr;
                private   MirrorComponentFeatureData swMirroCompFeatData;
                private   RefPlane myRefPlane;
                private   swMirrorComponentOrientation2_e[] compsToMirrorOrientationonOrigin =   new   swMirrorComponentOrientation2_e[2];
                private   swMirrorComponentOrientation2_e[] compsToMirrorOrientationonPlane =   new   swMirrorComponentOrientation2_e[2];
                private   Feature mirrorPlane2;
                private   Feature mirrorPlane3;
                private   bool[] FlipDir =   new   bool[2];
                private   object flipDirVar;
                private   object orientationArray;
                private   object orientationSelPlanArray;
                private   string[] mirrorCompFileNames =   new   string[2];
                private   string mirrorCompFolder;
                private   object namesVar;
                private   string[] replaceLocations =   new   string[2];
                private   object replaceLocationsArray;
                private   int importOptions;
                private   MirrorComponentFeatureData modifyFeatdef;
                private   swMirrorComponentOrientation2_e[] compsToMirrorOrientationonOrigin2 =   new   swMirrorComponentOrientation2_e[2];
                private   swMirrorComponentOrientation2_e[] compsToMirrorOrientationonPlane2 =   new   swMirrorComponentOrientation2_e[2];
                private   object orientationArray2;
                private   object orientationArrayPlane2;
                private   object swCompInst =   null;
                private   DispatchWrapper[] CTI =   new   DispatchWrapper[2];
                private   DispatchWrapper[] CTSP =   new   DispatchWrapper[2];
                private   DispatchWrapper[] CTMOH =   new   DispatchWrapper[2];
                private   DispatchWrapper[] ARef =   new   DispatchWrapper[2];
                private   bool boolstatus;
                private   bool retVal;
```

```vb
                public   void Main()
               {
                    swModel = (ModelDoc2)swApp.ActiveDoc;
                    FeatMgr = swModel.FeatureManager;
```

```vb
                    // Create mirror component feature data object
                    swMirroCompFeatData = (MirrorComponentFeatureData)FeatMgr.CreateDefinition((int)swFeatureNameID_e.swFmMirrorComponent);
```

```vb
                    // Create mirror plane
                    boolstatus = swModel.Extension.SelectByID2("",   "FACE", 0.104250921669188, -0.000236987012272039, -0.0597199999999418,   true, 0,   null/* TODO Change to default(_) if this is not a reference type */, 0);
                    myRefPlane = (RefPlane)swModel.FeatureManager.InsertRefPlane(8, 0.01, 0, 0, 0, 0);
```

```vb
                    swAssem = (AssemblyDoc)swModel;
```

```vb
                    mirrorPlane = (Feature)swAssem.FeatureByName("PLANE4");
```

```vb
                  // Specify components to instance align to component origins
                    swCompInst = swAssem.GetComponentByName("gear- caddy-1");
                    CTI[0] =   new   DispatchWrapper(swCompInst);
```

```vb
                    swCompInst = swAssem.GetComponentByName("middle-gear-1");
                    CTI[1] =   new   DispatchWrapper(swCompInst);
```

```vb
                    // Specify components to instance align to alignment references
                    swCompInst = swAssem.GetComponentByName("shaft gear-1");
                    CTSP[0] =   new   DispatchWrapper(swCompInst);
```

```vb
                    swCompInst = swAssem.GetComponentByName("middle-gear plate-1");
                    CTSP[1] =   new   DispatchWrapper(swCompInst);
```

```vb
                    // Specify components for which to create new opposite-hand versions
                    swCompInst = swAssem.GetComponentByName("base plate-1");
                    CTMOH[0] =   new   DispatchWrapper(swCompInst);
```

```vb
                    swCompInst = swAssem.GetComponentByName("shaft gear insert-1");
                    CTMOH[1] =   new   DispatchWrapper(swCompInst);
```

```vb
                    // Specify align to origins component orientations
                    compsToMirrorOrientationonOrigin[0] =   swMirrorComponentOrientation2_e.swOrientation_MirroredX_MirroredY;
                    compsToMirrorOrientationonOrigin[1] =   swMirrorComponentOrientation2_e.swOrientation_MirroredAndFlippedX_MirroredY;
                    orientationArray = compsToMirrorOrientationonOrigin;
```

```vb
                    // Specify align to selection component orientations
                    compsToMirrorOrientationonPlane[0] =   swMirrorComponentOrientation2_e.swOrientation_MirroredX_MirroredAndFlippedY;
                    compsToMirrorOrientationonPlane[1] =   swMirrorComponentOrientation2_e.swOrientation_MirroredAndFlippedX_MirroredAndFlippedY;
                    orientationSelPlanArray = compsToMirrorOrientationonPlane;
```

```vb
                    // Specify the alignment references for the align to selection components
                    mirrorPlane2 = (Feature)swAssem.FeatureByName("PLANE2");
                    ARef[0] =   new   DispatchWrapper(mirrorPlane2);
```

```vb
                    mirrorPlane3 = (Feature)swAssem.FeatureByName("PLANE3");
                    ARef[1] =   new   DispatchWrapper(mirrorPlane3);
```

```vb
                    // Specify whether to reverse the direction of alignment
                    FlipDir[0] =   false;
                    FlipDir[1] =   false;
                    flipDirVar = FlipDir;
```

```vb
                    // Specify the opposite-hand version folder
                    mirrorCompFolder =   @"C:\API\MirrorComps";
```

```vb
                    // Specify opposite-hand version file names
                    mirrorCompFileNames[0] = ("FileName1");
                    mirrorCompFileNames[1] = ("FileName2");
                    namesVar = mirrorCompFileNames;
```

```vb
                    // Specify replacement locations for the opposite-hand versions
                    replaceLocations[0] = (@"C:\API\check1.SLDPRT");
                    replaceLocations[1] = ("");
                    replaceLocationsArray = replaceLocations;
```

```vb
                    // Specify transfer options for the opposite-hand versions
                    importOptions = (int)swMirrorPartOptions_e.swMirrorPartOptions_ImportSolids;
```

```vb
                    swMirroCompFeatData.MirrorPlane = mirrorPlane;
                    swMirroCompFeatData.MirrorType = (int)swMirrorComponentMirrorType_e.swMirrorType_ComponentOrigin;
                    swMirroCompFeatData.ComponentsToInstanceAlignToComponentOrigin = CTI;
                    swMirroCompFeatData.ComponentOrientationsAlignToComponentOrigin = orientationArray;
                    swMirroCompFeatData.ComponentsToInstanceAlignToSelection = CTSP;
                    swMirroCompFeatData.ComponentOrientationsAlignToSelection = orientationSelPlanArray;
                    swMirroCompFeatData.AlignmentReferences = ARef;
                  swMirroCompFeatData.FlipDirections = flipDirVar;
                    swMirroCompFeatData.SyncFlexibleSubAssemblies =   true;
                    swMirroCompFeatData.OppositeHandComponents = CTMOH;
                    swMirroCompFeatData.CreateDerivedConfigurations =   false;
                    swMirroCompFeatData.PlaceFilesInOneFolder =   true;
                    swMirroCompFeatData.MirrorComponentsFolderLocation = mirrorCompFolder;
                    swMirroCompFeatData.MirroredComponentFilenames = namesVar;
                    swMirroCompFeatData.NameModifierType = (int)swMirrorComponentNameModifier_e.swMirrorComponentName_Custom;
                    swMirroCompFeatData.ReplaceFileLocations = replaceLocationsArray;
                    swMirroCompFeatData.MirrorTransferOptions = importOptions;
                    swMirroCompFeatData.DimXpertScheme =   true;
                    swMirroCompFeatData.BreakLinksToOriginalPart =   false;
                    swMirroCompFeatData.PreserveZAxis =   true;
                    swMirroCompFeatData.PropagateFromOriginalPart =   false;
```

```vb
                    // Create MirrorComponent1
                    swFeat = FeatMgr.CreateFeature(swMirroCompFeatData);
```

```vb
                    // Modify MirrorComponent1
                    modifyFeatdef = (MirrorComponentFeatureData)swFeat.GetDefinition();
```

```vb
                  // Change mirror type to center of mass
                    modifyFeatdef.MirrorType = (int)swMirrorComponentMirrorType_e.swMirrorType_CenterOfMass;
```

```vb
                    // Modify align to origin component orientations
                    compsToMirrorOrientationonOrigin2[0] =   swMirrorComponentOrientation2_e.swOrientation_MirroredAndFlippedX_MirroredAndFlippedY;
                    compsToMirrorOrientationonOrigin2[1] =   swMirrorComponentOrientation2_e.swOrientation_MirroredX_MirroredAndFlippedY;
                    orientationArray2 = compsToMirrorOrientationonOrigin2;
                    modifyFeatdef.ComponentOrientationsAlignToComponentOrigin = orientationArray2;
```

```vb
                    // Modify align to selection component orientations
                  compsToMirrorOrientationonPlane2[0] =   swMirrorComponentOrientation2_e.swOrientation_MirroredAndFlippedX_MirroredY;
                    compsToMirrorOrientationonPlane2[1] =   swMirrorComponentOrientation2_e.swOrientation_MirroredX_MirroredY;
                  orientationArrayPlane2 = compsToMirrorOrientationonPlane2;
                    modifyFeatdef.ComponentOrientationsAlignToSelection = orientationArrayPlane2;
```

```vb
                    retVal = swFeat.ModifyDefinition(modifyFeatdef, swModel,   null);
                }

         public SldWorks swApp;

     }
 }
```
