---
title: "Access Structure System Corner Treatments Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Access_Structure_System_Corner_Treatments__Example_CSharp.htm"
---

# Access Structure System Corner Treatments Example (C#)

This example shows how to access structure system corner treatments.

// ==========================================================================================

// Preconditions:

// 1. Open `public_documents`**\samples\tutorial\weldments\weldment_box.sldprt**.

// 2. Open an Immediate window.

// 3. Press F5.

//

// Postconditions:

// 1. Creates **Structure System1**.

// 2. Configures its weldment profile to have **<GB><round-rods><ROUND BAR 23>**.

// 3. Creates **Corner Management1** containing:

// - **Two member Corner Group1**

// - **Simple Corner Group1**

// - **Complex Corner Group1**

// 4. Press F5 to inspect the corner treatments.

// 5. Inspect the Immediate window.

// 6. Inspect the structure system and its corner management folder in the FeatureManager design tree.

// ========================================================================

using System;

using System.Collections.Generic;

using System.Diagnostics;

using System.Globalization;

using System.IO;

using System.Linq;

using System.Reflection;

using System.Runtime.CompilerServices;

using System.Security;

using System.Text;

using System.Threading.Tasks;

using Microsoft.VisualBasic;

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using System.Runtime.InteropServices;

namespace AccessCorners_CSharp

{

public partial class SolidWorksMacro

{

private ModelDoc2 modDoc;

private FeatureManager swFeatMgr;

private SelectionMgr swSelMgr;

private ModelDocExtension modDocExt;

private StructureSystemMemberFeatureData structMemDef;

private StructureSystemMemberProfile profDef;

private PrimaryStructuralMemberFeatureData PrimDef;

private PrimaryMemberPathSegmentFeatureData memPathSegDef;

private object[] segments = new object[6];

private object[] tsegments = new object[1];

private object[] csegments = new object[2];

private bool stat;

private StructureSystemMemberFeatureData[] memData = new StructureSystemMemberFeatureData[1];

private object memDataArray;

private Feature feat;

private int i;

private int k;

private int l;

private int m;

private int x;

private int Y;

private Feature swFeat;

private ComplexCornerTreatmentFeatureData complexCrnr;

private string strCornerName;

private object[] featArr;

private int Count;

private StructureSystemFolder swStructSysFolder;

private CornerManagementFolder swCornerMgmtFolder;

private object[] grpArr;

private int grpCnt;

private CornerTreatmentGroupFolder crnrGrpFolder;

private object[] crnrArr;

private int crnrCnt;

private Feature crnrFeat;

private CornerTreatmentFeatureData crnrFeat2;

private SimpleCornerTreatmentFeatureData simpleCrnr;

private TwoMemberCornerTreatmentFeatureData twoMbrCrnr;

private CornerMember member;

private object[] varBodyMem;

private object obj;

private int objType;

private CornerMember tmember;

private object[] crnrMbrArr;

private CornerMember crnrMbr;

private Feature feat1;

private bool status;

private CornerMember pmember;

private object[] varPlanarMem;

public DispatchWrapper[] ObjectArrayToDispatchWrapperArray(object[] Objects)

{

int ArraySize;

ArraySize = Objects.GetUpperBound(0);

DispatchWrapper[] d = new DispatchWrapper[ArraySize + 1];

int ArrayIndex;

for (ArrayIndex = 0; ArrayIndex <= ArraySize; ArrayIndex++)

d[ArrayIndex] = new DispatchWrapper(Objects[ArrayIndex]);

return d;

}

public void Main()

{

modDoc = (ModelDoc2)swApp.ActiveDoc;

modDocExt = modDoc.Extension;

swSelMgr = (SelectionMgr)modDoc.SelectionManager;

swFeatMgr = modDoc.FeatureManager;

// Create Structure System1

Debug.Print("Create Structure System1");

Debug.Print("");

stat = modDocExt.SelectByID2("Line4@3DSketch1", "EXTSKETCHSEGMENT", 0, 0, 0, true, 0, null/* TODO Change to default(_) if this is not a reference type */, 0);

stat = modDocExt.SelectByID2("Line1@Sketch2", "EXTSKETCHSEGMENT", 0, 0, 0, true, 0, null/* TODO Change to default(_) if this is not a reference type */, 0);

stat = modDocExt.SelectByID2("Line3@3DSketch1", "EXTSKETCHSEGMENT", 0, 0, 0, true, 0, null/* TODO Change to default(_) if this is not a reference type */, 0);

stat = modDocExt.SelectByID2("Line6@3DSketch1", "EXTSKETCHSEGMENT", 0, 0, 0, true, 0, null/* TODO Change to default(_) if this is not a reference type */, 0);

stat = modDocExt.SelectByID2("Line3@Sketch1", "EXTSKETCHSEGMENT", 0, 0, 0, true, 0, null/* TODO Change to default(_) if this is not a reference type */, 0);

stat = modDocExt.SelectByID2("Line4@Sketch1", "EXTSKETCHSEGMENT", 0, 0, 0, true, 0, null/* TODO Change to default(_) if this is not a reference type */, 0);

structMemDef = (StructureSystemMemberFeatureData)modDocExt.**CreateStructureSystemMemberData**(0);

Debug.Print("Type of structure system member as defined by swStructureSystemMemberType_e: " + structMemDef.**StructureSystemMemberType**);

profDef = (StructureSystemMemberProfile)structMemDef.**MemberProfile**;

profDef.**ProfileStandard** = "GB";

profDef.**ProfileType** = "round-rods";

profDef.**ProfileSize** = "ROUND BAR 23";

PrimDef = (PrimaryStructuralMemberFeatureData)structMemDef;

Debug.Print("Structure system primary member creation type as defined by swStructureSystemMemberCreationType_e: " + PrimDef.**PrimaryMemberType**);

memPathSegDef = (PrimaryMemberPathSegmentFeatureData)PrimDef;

segments[0] = swSelMgr.GetSelectedObject6(1, 0);

segments[1] = swSelMgr.GetSelectedObject6(2, 0);

segments[2] = swSelMgr.GetSelectedObject6(3, 0);

segments[3] = swSelMgr.GetSelectedObject6(4, 0);

segments[4] = swSelMgr.GetSelectedObject6(5, 0);

segments[5] = swSelMgr.GetSelectedObject6(6, 0);

DispatchWrapper[] dArray;

dArray = ObjectArrayToDispatchWrapperArray(segments);

stat = memPathSegDef.**SetPathSegments**(dArray);

Debug.Print("Path segments set successfully: " + stat);

memData[0] = structMemDef;

memDataArray = memData;

modDocExt.**CreateStructureSystem**(memDataArray, null);

modDoc.ViewZoomtofit();

System.Diagnostics.Debugger.Break();

// Inspect corner treatments

featArr = (object[])swFeatMgr.**GetCornerManagementFolders**();

Count = featArr.GetUpperBound(0);

for (i = 0; i <= Count; i++)

{

swFeat = (Feature)featArr[i];

Debug.Print(swFeat.Name);

swCornerMgmtFolder = (CornerManagementFolder)swFeat.GetSpecificFeature2();

swFeat = swCornerMgmtFolder.**GetFeature**();

swFeat = (Feature)swCornerMgmtFolder.**GetStructureSystemFolder**();

Debug.Print(swFeat.Name);

swStructSysFolder = (StructureSystemFolder)swFeat.GetSpecificFeature2();

Debug.Print("Number of profile groups: " + swStructSysFolder.**GetProfileGroupFoldersCount**());

grpCnt = swCornerMgmtFolder.**GetTreatmentGroupFolderCount**();

Debug.Print("Number of corner treatment groups: " + grpCnt);

grpArr = (object[])swCornerMgmtFolder.**GetTreatmentGroupFolders**();

for (k = 0; k <= grpCnt - 1; k++)

{

crnrGrpFolder = (CornerTreatmentGroupFolder)grpArr[k];

swFeat = crnrGrpFolder.**GetFeature**();

Debug.Print("");

Debug.Print(swFeat.Name);

Debug.Print("Corner group folder type as defined by swCornerType_e: " + crnrGrpFolder.**Type**);

crnrCnt = crnrGrpFolder.GetCornerTreatmentCount();

Debug.Print("Number of corner treatments: " + crnrCnt);

crnrArr = (object[])crnrGrpFolder.**GetCornerTreatments**();

for (x = 0; x <= crnrCnt - 1; x++)

{

crnrFeat = (Feature)crnrArr[x];

Debug.Print(crnrFeat.Name);

crnrFeat2 = (CornerTreatmentFeatureData)crnrFeat.**GetDefinition**();

Debug.Print("Corner type as defined by swCornerType_e: " + crnrFeat2.**CornerType**);

Debug.Print("Ignore corner treatment? " + crnrFeat2.**IgnoreCornerTreatment**);

Debug.Print("Allow extension? " + crnrFeat2.**AllowExtension**);

Debug.Print("");

crnrFeat2.**AccessSelections**(modDoc, null);

strCornerName = crnrFeat.Name;

if (crnrFeat2.CornerType == 0)

{

Debug.Print("Simple corner treatment");

simpleCrnr = (SimpleCornerTreatmentFeatureData)crnrFeat2;

Debug.Print("Corner treatment trim type as defined by swCornerTreatmentTrimType_e: " + simpleCrnr.**CornerTreatmentTrimType**);

Debug.Print("Planar trim option as defined by swCornerTreatmentPlanarTrimOptions_e: " + simpleCrnr.**PlanarTrimOption**);

Debug.Print("Planar trim tool type as defined by swCornerTreatmentPlanarTrimToolType_e: " + simpleCrnr.**PlanarTrimToolType**);

Debug.Print("Weld trim gap: " + simpleCrnr.**WeldTrimGap**);

}

else if (crnrFeat2.CornerType == 1)

{

Debug.Print("Two member corner treatment");

twoMbrCrnr = (TwoMemberCornerTreatmentFeatureData)crnrFeat2;

Debug.Print("Corner treatment trim type as defined by swCornerTreatmentTrimType_e: " + twoMbrCrnr.**CornerTreatmentTrimType**);

Debug.Print("Planar trim option as defined by swCornerTreatmentPlanarTrimOptions_e: " + twoMbrCrnr.**PlanarTrimOption**);

Debug.Print("Weld trim gap: " + twoMbrCrnr.**WeldTrimGap**);

// Change some settings

twoMbrCrnr.**CornerTreatmentTrimType** = 1; // Body trim

twoMbrCrnr.**WeldTrimGap** = 0.001;

crnrMbrArr = (object[])twoMbrCrnr.**GetCornerGroupMembers**();

Debug.Print("Corner members:");

for (Y = 0; Y <= 1; Y++)

{

crnrMbr = (CornerMember)crnrMbrArr[Y];

Debug.Print("Trim order: " + crnrMbr.**TrimOrder**);

feat1 = (Feature)crnrMbr.**GetUnderlyingMemberFeature**();

Debug.Print("Member feature: " + feat1.Name);

}

twoMbrCrnr.**SwapMembers**(); // Make other member the trim tool

}

else if (crnrFeat2.**CornerType** == 2)

{

Debug.Print("Complex corner treatment");

complexCrnr = (ComplexCornerTreatmentFeatureData)crnrFeat2;

Debug.Print("Planar trim tool type as defined by swCornerTreatmentPlanarTrimToolType_e: " + complexCrnr.**PlanarTrimToolType**);

Debug.Print("Planar trim option as defined by swCornerTreatmentPlanarTrimOptions_e: " + complexCrnr.**PlanarTrimOption**);

varBodyMem = (object[])complexCrnr.**GetBodyTrimMembers**();

if (varBodyMem[0] != null)

{

for (l = 0; l <= varBodyMem.GetUpperBound(0); l++)

{

member = (CornerMember)varBodyMem[l];

Debug.Print("Body trim member: " + ((Feature)member.**GetUnderlyingMemberFeature**()).Name);

Debug.Print("Body trim order: " + member.**TrimOrder**);

Debug.Print("Body weld gap: " + member.**WeldGap**);

}

}

complexCrnr.**SetTrimToolMember**(varBodyMem[0]);

obj = complexCrnr.**GetTrimToolMember**(out objType);

if (objType == (int)swTrimToolMemberObjectType_e.swTrimToolMemberObjectType_swCornerMember)

tmember = (CornerMember)obj;

else if (objType == (int)swTrimToolMemberObjectType_e.swTrimToolMemberObjectType_swCornerTreatmentFeature)

{

feat = (Feature)obj;

Debug.Print("Trim tool: " + feat.Name);

}

if (tmember != null)

{

Debug.Print("Trim tool member: " + ((Feature)(tmember.**GetUnderlyingMemberFeature**())).Name);

Debug.Print("Trim tool member trim order: " + tmember.**TrimOrder**);

Debug.Print("Trim tool member weld gap: " + tmember.**WeldGap**);

}

varPlanarMem = (object[])complexCrnr.**GetPlanarTrimMembers**();

if (varPlanarMem != null)

{

for (m = 0; m <= varPlanarMem.GetUpperBound(0); m++)

{

pmember = (CornerMember)varPlanarMem[m];

Debug.Print("Planar trim member: " + ((Feature)pmember.**GetUnderlyingMemberFeature**()).Name);

Debug.Print("Planar trim member trim order: " + pmember.**TrimOrder**);

Debug.Print("Planar trim member weld gap: " + pmember.**WeldGap**);

}

}

}

feat = crnrFeat2.**GetFeature**();

status = feat.**ModifyDefinition**(crnrFeat2, modDoc, null);

if (status == false)

crnrFeat2.**ReleaseSelectionAccess**();

}

}

}

}

// The SldWorks swApp variable is pre-assigned for you.

public SldWorks swApp;

}

}
