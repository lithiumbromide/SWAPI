---
title: "Create Secondary Structure System Members Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Secondary_SSMembers_Example_CSharp.htm"
---

# Create Secondary Structure System Members Example (C#)

This example shows how to create two secondary structure system members: one between primary member pair end points and the other on a support plane between a primary member pair.

// ==========================================================================================

// Preconditions:

// 1. Ensure the specified part template exists.

// 2. Open an Immediate window.

// 3. Press F5.

//

// Postconditions:

// 1. Creates **Sketch1** containing two sketch segments.

// 2. Configures the start/end extensions and the member profile.

// 3. Selects the two sketch segments.

// 4. Creates primary **Structure System1** with two primary path segment members (**Member1** and **Member2**).

// 5. Inspect the structure system in the graphics area.

// 6. Press F5 to add a secondary support plane member.

// Creates secondary **Structure System2** (**Member3**).

// 7. Press F5 to edit the support plane member.

// 8. Press F5 to add a secondary between points member.

// Creates secondary **Structure System3** (**Member4**).

// 9. Press F5 to edit the between points member.

//10. Press F5 to add a secondary structure system up to member.

//11. When the macro stops, multi-select a **Member1** vertex
// in the graphics area and **Member2** in the FeatureManager Design tree.

//12. Press F5 to create the secondary **Structure System4** (**Member5**).

//13. Inspect the Immediate window.

// ========================================================================

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using System.Diagnostics;

using System.Runtime.InteropServices;

namespace Secondary

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

private SecondaryMemberBetweenPointsFeatureData memBetweenPointsSecDef;

private SecondaryMemberBetweenPointsFeatureData secMemDatTochange;

private SecondaryMemberSupportPlaneFeatureData memSupportPlaneSecDef;

private object[] segments = new object[3];

private bool stat;

private StructureSystemMemberFeatureData[] memData = new StructureSystemMemberFeatureData[1];

private object[] memDataArray;

private Feature structSys;

private StructureSystemFolder baseSecondarySystem;

private StructureSystemFolder structSysDef;

private StructureSystemFolder structSysSecDef;

private Feature feat;

private StructureSystemFolder structSysModDef;

private object[] outProfiles;

private StructureSystemMemberFeatureData MemberData;

private object[] memberArray;

private Feature profileGrpFeat;

private ProfileGroupFolder profileGrp;

private StructureSystemMemberFeatureData memTochange;

private int I;

private int j;

private SecondaryStructuralMemberFeatureData secDef;

private SecondaryMemberUpToMembersFeatureData UpToMemDef;

private object point;

private object[] Members = new object[1];

public DispatchWrapper[] ObjectArrayToDispatchWrapperArray(object[] Objects)

{

int ArraySize;

ArraySize = Objects.GetUpperBound(0);

var d = new DispatchWrapper[ArraySize + 1];

int ArrayIndex;

var loopTo = ArraySize;

for (ArrayIndex = 0; ArrayIndex <= loopTo; ArrayIndex++)

d[ArrayIndex] = new DispatchWrapper(Objects[ArrayIndex]);

return d;

}

public void Main()

{

double swSheetWidth;

swSheetWidth = 0d;

double swSheetHeight;

swSheetHeight = 0d;

modDoc = (ModelDoc2)swApp.NewDocument(@"C:\ProgramData\SolidWorks\SOLIDWORKS 2023\templates\Part.PRTDOT", 0, swSheetWidth, swSheetHeight);

modDocExt = modDoc.Extension;

modDoc.SketchManager.InsertSketch(true);

stat = modDocExt.SelectByID2("Front Plane", "PLANE", -0.077188654347454d, 0.054268560279924d, 0.00386214196026222d, false, 0, null, 0);

modDoc.ClearSelection2(true);

object skSegment;

skSegment = modDoc.SketchManager.CreateLine(-0.168061d, 0.084736d, 0d, -0.168061d, -0.077684d, 0d);

skSegment = modDoc.SketchManager.CreateLine(0.075216d, 0.107771d, 0d, 0.075216d, -0.006699d, 0d);

modDoc.ClearSelection2(true);

stat = modDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, true, 0, null, 0);

RefPlane myRefPlane;

myRefPlane = (RefPlane)modDoc.FeatureManager.InsertRefPlane(8, 0.03d, 0, 0, 0, 0);

modDoc.ClearSelection2(true);

stat = modDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, false, 0, null, 0);

modDoc.ClearSelection2(true);

modDoc.SketchManager.InsertSketch(true);

stat = modDocExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.168061313304597d, 0.0544142573846353d, 0, false, 0, null, 0);

stat = modDocExt.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", 0.0752162521083513d, 0.0532390034454423d, 0, true, 0, null, 0);

// Create primary structure system path segment members

structMemDef = (StructureSystemMemberFeatureData)modDocExt.**CreateStructureSystemMemberData**(0);

Debug.Print("Type of structure system member as defined by swStructureSystemMemberType_e: " + structMemDef.**StructureSystemMemberType**);

structMemDef.**StartEndExtendD1** = 1.0d;

structMemDef.**StartEndExtendD2** = 2.0d;

profDef = (StructureSystemMemberProfile)structMemDef.**MemberProfile**;

profDef.ProfileStandard = "ansi inch";

profDef.ProfileType = "c channel";

profDef.ProfileSize = "3 x 5";

PrimDef = (PrimaryStructuralMemberFeatureData)structMemDef;

Debug.Print("Structure system primary member creation type as defined by swStructureSystemMemberCreationType_e: " + PrimDef.**PrimaryMemberType**);

memPathSegDef = (PrimaryMemberPathSegmentFeatureData)PrimDef;

memPathSegDef.MergeTangentMembers = true;

swSelMgr = (SelectionMgr)modDoc.SelectionManager;

var segments = new object[2];

segments[0] = swSelMgr.GetSelectedObject6(1, 0);

segments[1] = swSelMgr.GetSelectedObject6(2, 0);

DispatchWrapper[] dArray;

dArray = ObjectArrayToDispatchWrapperArray(segments);

stat = memPathSegDef.**SetPathSegments**(dArray);

Debug.Print("Path segments successfully set: " + stat);

var PrimMemData = new StructureSystemMemberFeatureData[1];

PrimMemData[0] = structMemDef;

object[] PrimMemDatArray;

PrimMemDatArray = PrimMemData;

Feature structSysFeat;

structSysFeat = modDocExt.**CreateStructureSystem**(PrimMemDatArray, null);

modDoc.ViewZoomtofit();

Debugger.Break();

structSysDef = (StructureSystemFolder)structSysFeat.**GetSpecificFeature2**();

Debug.Print("Number of profile group folders: " + structSysDef.**GetProfileGroupFoldersCount**());

object[] outProfiles;

outProfiles = (object[])structSysDef.**GetProfileGroupFolders**();

var memberArray = default(object[]);

if (outProfiles.Length > 0)

{

var loopTo = outProfiles.GetUpperBound(0);

for (I = 0; I <= loopTo; I++)

{

profileGrpFeat = (Feature)outProfiles[I];

profileGrp = (ProfileGroupFolder)profileGrpFeat.**GetSpecificFeature2**();

if (profileGrp is object)

{

Debug.Print("Number of members in profile group: " + profileGrp.**GetStructureSystemMemberCount**());

memberArray = (object[])profileGrp.**GetStructureSystemMembers**();

if (memberArray.Length > 0)

{

break;

}

}

}

}

// Create secondary structure system support plane member

StructureSystemMemberFeatureData structSecMemDef;

structSecMemDef = (StructureSystemMemberFeatureData)modDocExt.**CreateStructureSystemMemberData**(4); // Secondary Support Plane

Debug.Print("Type of structure system member as defined by swStructureSystemMemberType_e: " + structMemDef.**StructureSystemMemberType**);

structSecMemDef.**StartEndExtendD1** = 0.5d;

structSecMemDef.**StartEndExtendD2** = 0.5d;

StructureSystemMemberProfile secProfDef;

secProfDef = (StructureSystemMemberProfile)structSecMemDef.**MemberProfile**;

secProfDef.ProfileStandard = "ansi inch";

secProfDef.ProfileType = "c channel";

secProfDef.ProfileSize = "3 x 5";

SecondaryStructuralMemberFeatureData SecDef;

SecDef = (SecondaryStructuralMemberFeatureData)structSecMemDef;

Debug.Print("Structure system secondary member creation type as defined by swStructureSystemMemberCreationType_e: " + SecDef.**SecondaryMemberType**);

memSupportPlaneSecDef = (SecondaryMemberSupportPlaneFeatureData)SecDef;

DispatchWrapper[] eArray;

eArray = ObjectArrayToDispatchWrapperArray(memberArray);

stat = memSupportPlaneSecDef.**SetMemberPairs**(eArray);

Debug.Print("Member pairs set successfully: " + stat);

stat = modDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, true, 0, null, 0);

var Planes = new object[1];

Planes[0] = swSelMgr.GetSelectedObject6(1, 0);

DispatchWrapper[] fArray;

fArray = ObjectArrayToDispatchWrapperArray(Planes);

stat = memSupportPlaneSecDef.**SetIntersectingPlanesAndFaces**(fArray);

Debug.Print("Intersecting plane set successfully: " + stat);

var secMemData = new StructureSystemMemberFeatureData[1];

secMemData[0] = structSecMemDef;

object[] secMemDatArray;

secMemDatArray = secMemData;

Feature structSysFeat2;

structSysFeat2 = modDocExt.**CreateStructureSystem**(null, secMemDatArray);

modDoc.ViewZoomtofit();

Debugger.Break();

// Edit secondary support plane member by changing start/end extensions

baseSecondarySystem = (StructureSystemFolder)structSysFeat2.**GetSpecificFeature2**();

Debug.Print("Number of profile group folders: " + baseSecondarySystem.**GetProfileGroupFoldersCount**());

outProfiles = (object[])baseSecondarySystem.**GetProfileGroupFolders**();

var secMemberData = default(object);

object[] SecMemberArray;

Feature secProfileGrpFeat;

ProfileGroupFolder secProfileGrp;

if (outProfiles.Length > 0)

{

var loopTo1 = outProfiles.GetUpperBound(0);

for (I = 0; I <= loopTo1; I++)

{

secProfileGrpFeat = (Feature)outProfiles[I];

secProfileGrp = (ProfileGroupFolder)secProfileGrpFeat.**GetSpecificFeature2**();

if (secProfileGrp is object)

{

Debug.Print("Number of members in profile group: " + secProfileGrp.**GetStructureSystemMemberCount**());

SecMemberArray = (object[])secProfileGrp.**GetStructureSystemMembers**();

if (SecMemberArray.Length > 0)

{

var loopTo2 = SecMemberArray.GetUpperBound(0);

for (j = 0; j <= loopTo2; j++)

{

secMemberData = SecMemberArray[j];

break;

}

}

}

}

}

StructureSystemMemberFeatureData memTochange;

memTochange = (StructureSystemMemberFeatureData)secMemberData;

Feature SecMemFeat;

SecMemFeat = memTochange.**GetFeature**();

memTochange.**StartEndExtendD1** = 0.2d;

memTochange.**StartEndExtendD2** = 0.1d;

stat = SecMemFeat.**ModifyDefinition**(secMemberData, modDoc, null);

Debugger.Break();

// Create secondary between points member

structSecMemDef = (StructureSystemMemberFeatureData)modDocExt.**CreateStructureSystemMemberData**(5);

Debug.Print("Type of structure system member as defined by swStructureSystemMemberType_e: " + structMemDef.**StructureSystemMemberType**);

secProfDef = (StructureSystemMemberProfile)structSecMemDef.**MemberProfile**;

secProfDef.ProfileStandard = "ansi inch";

secProfDef.ProfileType = "c channel";

secProfDef.ProfileSize = "3 x 5";

SecDef = (SecondaryStructuralMemberFeatureData)structSecMemDef;

Debug.Print("Structure system secondary member creation type as defined by swStructureSystemMemberCreationType_e: " + SecDef.**SecondaryMemberType**);

memBetweenPointsSecDef = (SecondaryMemberBetweenPointsFeatureData)SecDef;

stat = memBetweenPointsSecDef.**SetMemberPairs**(eArray);

Debug.Print("Member pairs successfully set: " + stat);

memBetweenPointsSecDef.**SecondaryMemberOffsetType** = 0;

memBetweenPointsSecDef.**DistanceMember1** = 0.5d;

memBetweenPointsSecDef.**DistanceMember2** = 0.4d;

memBetweenPointsSecDef.**RevDirectionDistanceMember1** = false;

memBetweenPointsSecDef.**RevDirectionDistanceMember2** = false;

secMemData[0] = structSecMemDef;

secMemDatArray = secMemData;

structSysFeat2 = modDocExt.**CreateStructureSystem**(null, secMemDatArray);

Debugger.Break();

// Edit between points member by changing start/end extensions and offset type

structSysSecDef = (StructureSystemFolder)structSysFeat2.**GetSpecificFeature2**();

Debug.Print("Number of profile group folders: " + structSysSecDef.**GetProfileGroupFoldersCount**());

object[] outSecProfiles;

outSecProfiles = (object[])structSysSecDef.**GetProfileGroupFolders**();

if (outSecProfiles.Length > 0)

{

var loopTo3 = outSecProfiles.GetUpperBound(0);

for (I = 0; I <= loopTo3; I++)

{

secProfileGrpFeat = (Feature)outSecProfiles[I];

secProfileGrp = (ProfileGroupFolder)secProfileGrpFeat.**GetSpecificFeature2**();

if (secProfileGrp is object)

{

Debug.Print("Number of members in profile group: " + secProfileGrp.**GetStructureSystemMemberCount**());

SecMemberArray = (object[])secProfileGrp.**GetStructureSystemMembers**();

if (SecMemberArray.Length > 0)

{

var loopTo4 = SecMemberArray.GetUpperBound(0);

for (j = 0; j <= loopTo4; j++)

secMemberData = SecMemberArray[j];

}

}

}

}

memTochange = (StructureSystemMemberFeatureData)secMemberData;

SecMemFeat = memTochange.**GetFeature**();

memTochange.**StartEndExtendD1** = 0.2d;

memTochange.**StartEndExtendD2** = 0.1d;

secMemDatTochange = (SecondaryMemberBetweenPointsFeatureData)memTochange;

secMemDatTochange.**SecondaryMemberOffsetType** = 1;

secMemDatTochange.**LengthRatioMember1** = 0.1d;

secMemDatTochange.**LengthRatioMember2** = 0.2d;

stat = SecMemFeat.**ModifyDefinition**(secMemberData, modDoc, null);

Debugger.Break();

//Create secondary structure system up to member

structMemDef = modDocExt.**CreateStructureSystemMemberData**(6);

Debug.Print("Structure system member type as defined by swStructureSystemMemberType_e: " + structMemDef.**StructureSystemMemberType**);

structMemDef.**StartEndExtendD1** = 0.0;
Debug.Print("Start/end direction 1: " + structMemDef.**StartEndExtendD1**);
structMemDef.**StartEndExtendD2** = 0.0;
Debug.Print("Start/end direction 2: " + structMemDef.**StartEndExtendD2**);

profDef = structMemDef.**MemberProfile**;

profDef.**ProfileStandard** = "ansi inch";
profDef.**ProfileType** = "pipe";
profDef.**ProfileSize** = "0.5 sch 40";

secDef = (SecondaryStructuralMemberFeatureData)structMemDef;
Debug.Print("Secondary member type as defined by swStructureSystemMemberCreationType_e: " + secDef.**SecondaryMemberType**);

UpToMemDef = (SecondaryMemberUpToMembersFeatureData)secDef;

UpToMemDef.**MemberPointParametersType** = (int) swSecondaryMemberUpToMembersMemberPointParameters_e.swSecondaryMemberUpToMembersMemberPointParameters_FromPoint;

Debugger.Break(); //Multi-select a Member1 vertex in the graphics area and Member2 in the FeatureManager Design tree

point = swSelMgr.GetSelectedObject6(1, 0);
Members[0] = swSelMgr.GetSelectedObject6(2, 0);

UpToMemDef.**SetFromPoint**(point);

DispatchWrapper[] gArray;
gArray = ObjectArrayToDispatchWrapperArray(Members);
UpToMemDef.**SetFromPointMembers(**gArray);

UpToMemDef.**SecondaryMemberOffsetType** = (int) swSecondaryMemberUpToMembersDistanceFromEndType_e.swSecondaryMemberUpToMembersDistanceFromEndType_Distance;
UpToMemDef.**DistanceMember** = 0.1;
UpToMemDef.**RevDirectionDistanceMember** = false;

memData[0] = structMemDef;
memDataArray = memData;

Feature structSysFeat3;
structSysFeat3 = modDocExt.**CreateStructureSystem**(null, memDataArray);

}

// The SldWorks swApp variable is pre-assigned for you.

public SldWorks swApp;

}

}
