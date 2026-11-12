---
title: "Get Gtol Frame Information Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Gtol_Frame_Information_Example_CSharp.htm"
---

# Get Gtol Frame Information Example (C#)

This example shows how to obtain information from a Gtol frame.

// ====================================================

// Preconditions:

// 1. Open a drawing that contains a GTol created with either SolidWorks 2021 or SolidWorks 2022/2022+.

// 2. Open an Immediate window.

//

// Postconditions:

// 1. Select a Gtol in the graphics area.

// A Geometric Tolerance PropertyManager opens.

// 2. Click on the macro window and press F5.

// 3. Gtol format type and schema version print to the Immediate window.

// 4. Press F5.

// 5. The frame XML schema string prints to the Immediate window.

// 6. Press F5.

// 7. If the selected Gtol can be converted from 2021, it is attempted.

// 8. Inspect the Immediate window.

// 9. Press F5.

// 10. Gets and sets From and To text and toggles SEPARATE REQUIREMENT.

// 11. Inspect the Immediate window.

// 12. Press F5.

// 13. Gtol frames added and deleted.

// 14. Inspect the Immediate window.

// 15. Press F5.

// 16. Add Indicator tests.

// 17. Inspect the Immediate window.

// 18. Press F5.

// 19. Get Indicator tests.

// 20. Inspect the Immediate window.

// 21. Press F5.

// 22. Delete Indicator tests.

// 23. Inspect the Immediate window.

// 24. Press F5.

// 25. Miscellaneous Indicator tests.

// 26. Inspect the Immediate window.

// 27. Press F5.

// 28. Tolerance type tests.

// 29. Inspect the Immediate window.

// 30. Press F5.

// 31. Get and set symbol XML string.

// 32. Inspect the Immediate window.

// ====================================================

using System;

using System.Collections.Generic;

using System.Linq;

using System.Text;

using System.Threading.Tasks;

using System.Windows;

using System.Windows.Forms;

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using System.Runtime.InteropServices;

using System.Diagnostics;

using Microsoft.VisualBasic;

namespace GetGtolFrameInfo_CSharp

{

public partial class SolidWorksMacro

{

private ModelDoc2 swModel;

private bool boolstatus;

private int longstatus;

private int longwarnings;

private SelectionMgr swSelMgr;

private Gtol swGtol;

private GtolFrame swGtolFrame;

private GtolFrame swGtolFrame1;

private int FrameCount;

private string sXMLString;

private int iIndicator;

private int iFrame;

private int lFormatType;

private int lFormatType1;

private int lSchemaVersion;

private string sSchemaString;

private swGtolFormatConversionError_e swConversionError;

private string swFromText;

private string swToText;

private string swFromText1;

private string swToText1;

private int IndicatorCount;

private string sDatum;

private int lBorderType;

private int lTolType;

private int swToleranceType;

private int swTolType;

private int pos;

public void Main()

{

swModel = (ModelDoc2)swApp.ActiveDoc;

swSelMgr = (SelectionMgr)swModel.SelectionManager;

System.Diagnostics.Debugger.Break(); // in the graphics area select Gtol created with either SolidWorks 2021 or SolidWorks 2022/2022+

Debug.Print("Select object type as defined by swSelectType_e: " + swSelMgr.GetSelectedObjectType3(1, -1));

swGtol = (Gtol)swSelMgr.GetSelectedObject6(1, -1);

swApp.**GetGtolFormatData**(out lFormatType, out lSchemaVersion);

Debug.Print("Gtol format type as defined by swGtolFormatType_e: " + lFormatType);

Debug.Print("Gtol schema version as defined by swGtolFormatSchemaVersion_e: " + lSchemaVersion);

System.Diagnostics.Debugger.Break();

sSchemaString = swApp.**GetGtolFrameXMLSchema**();

Debug.Print("Gtol frame XML schema: " + sSchemaString);

System.Diagnostics.Debugger.Break();

boolstatus = swGtol.**CanConvertFormat**();

if (boolstatus != false)

{

lFormatType1 = swGtol.**GetFormat**();

if (lFormatType1 == (int)swGtolFormatType_e.GTOL_SW2021)

{

boolstatus = swModel.**GetSaveFlag**();

if (boolstatus != false)

swModel.Save();

Debug.Print("SaveFlag BEFORE ConvertFormat is called " + swModel.GetSaveFlag());

swConversionError = (swGtolFormatConversionError_e)swGtol.**ConvertFormat**();

boolstatus = swModel.GetSaveFlag(); // if successful, converted Gtol document should be dirty and return True

Debug.Print("SaveFlag AFTER ConvertFormat is called " + boolstatus);

lFormatType1 = swGtol.**GetFormat**(); // converted from 2021 to 2022

}

}

System.Diagnostics.Debugger.Break();

boolstatus = swGtol.**GetFromTo**();

boolstatus = swGtol.**GetFromToText**(out swFromText, out swToText);

swFromText = "FromMe";

swToText = "ToYou";

boolstatus = swGtol.**SetFromToText**(true, swFromText, swToText);

boolstatus = swGtol.**GetFromTo**();

swFromText1 = "";

swToText1 = "";

boolstatus = swGtol.**GetFromToText**(out swFromText1, out swToText1); // should be "FromMe" and "ToMe"

Debug.Print("From text: " + swFromText1);

Debug.Print("To text: " + swToText1);

boolstatus = swGtol.**SeparateRequirement**;

if (boolstatus != false)

swGtol.**SeparateRequirement** = false;

else

swGtol.**SeparateRequirement** = true;

Debug.Print("SEPARATE REQUIREMENT ? " + swGtol.**SeparateRequirement**);

System.Diagnostics.Debugger.Break();

FrameCount = swGtol.**GetFrameCount**();

Debug.Print("Frame count: " + FrameCount);

boolstatus = swGtol.**AddFrame**();

FrameCount = swGtol.**GetFrameCount**(); // frame count should increase by one

Debug.Print("Frame added. Frame count now: " + FrameCount);

boolstatus = swGtol.**DeleteFrame**(FrameCount);

FrameCount = swGtol.**GetFrameCount**(); // frame count should decrease by 1, as just added frame was deleted

Debug.Print("Frame deleted. Frame count now: " + FrameCount);

boolstatus = swGtol.**AddFrame**();

FrameCount = swGtol.**GetFrameCount**(); // frame count should increase by 1

Debug.Print("Frame added. Frame count now: " + FrameCount);

System.Diagnostics.Debugger.Break();

swGtolFrame = (GtolFrame)swGtol.**GetFrame**(FrameCount);

IndicatorCount = swGtolFrame.**GetIndicatorCount**();

sDatum = "A";

Debug.Print(" ");

Debug.Print("Frame " + FrameCount + " IndicatorCount is " + IndicatorCount + ": AddIndicator test");

// supported border types: swGtolIndicatorBorderType_CollectionPlane, swGtolIndicatorBorderType_OrientationPlane swGtolIndicatorBorderType_IntersectionPlane swGtolIndicatorBorderType_DirectionFeature

// supported tolerance types: swGcsPARALLEL swGcsPERP swGcsANG swGcsCIRCRUNOUT swGcsSYMMETRY

boolstatus = swGtolFrame.**AddIndicator**((int)swGtolIndicatorBorderType_e.swGtolIndicatorBorderType_IntersectionPlane, (int)swGtolGeomCharSymbol_e.swGcsFLAT, sDatum); // unsupported TolType

Debug.Print("Unsupported TolType swGcsFLAT. AddIndicator return value is " + boolstatus);

boolstatus = swGtolFrame.**AddIndicator**((int)swGtolGeomCharSymbol_e.swGcsFLAT, (int)swGtolGeomCharSymbol_e.swGcsSYMMETRY, sDatum); // unsupported BorderType

Debug.Print("Unsupported BorderType swGcsFLAT. AddIndicator return value is " + boolstatus);

boolstatus = swGtolFrame.**AddIndicator**((int)swGtolIndicatorBorderType_e.swGtolIndicatorBorderType_IntersectionPlane, (int)swGtolGeomCharSymbol_e.swGcsSYMMETRY, sDatum); // supported BorderType and TolType

Debug.Print("Supported BorderType swGtolIndicatorBorderType_IntersectionPlane and TolType swGcsSYMMETRY. AddIndicator return value is " + boolstatus);

IndicatorCount = swGtolFrame.**GetIndicatorCount**();

Debug.Print("");

Debug.Print("Frame " + FrameCount + " IndicatorCount after one successful AddIndicator is " + IndicatorCount); // should increase by 1 from AddIndicator success

Debug.Print(" ");

System.Diagnostics.Debugger.Break();

IndicatorCount = swGtolFrame.**GetIndicatorCount**();

iIndicator = 0;

iFrame = 0;

FrameCount = swGtol.GetFrameCount();

Debug.Print("FrameCount is " + FrameCount + ": GetIndicator test");

for (iFrame = 1; iFrame <= FrameCount; iFrame++)

{

//lBorderType = -1;

//lTolType = -1;

sDatum = "";

swGtolFrame1 = (GtolFrame)swGtol.**GetFrame**(iFrame);

for (iIndicator = 1; iIndicator <= IndicatorCount; iIndicator++)

{

boolstatus = swGtolFrame1.**GetIndicator**(iIndicator, out lBorderType, out lTolType, out sDatum);

Debug.Print("Frame: " + iFrame + " Indicator index: " + iIndicator + " (BorderType as defined by swGtolIndicatorBorderType_e = " + lBorderType + " " + "TolType as defined by swGtolGeomCharSymbol_e = " + lTolType + " " + "Datum = " + sDatum + ")");

}

}

Debug.Print(" ");

System.Diagnostics.Debugger.Break();

Debug.Print("Frame " + FrameCount + " DeleteIndicator test");

boolstatus = swGtolFrame.**DeleteIndicator**(IndicatorCount);

Debug.Print("DeleteIndicator return value is " + boolstatus);

IndicatorCount = swGtolFrame.**GetIndicatorCount**(); // should decrease by 1, as indicator deleted

Debug.Print("IndicatorCount is " + IndicatorCount + " after DeleteIndicator");

System.Diagnostics.Debugger.Break();

Debug.Print(" ");

Debug.Print("Miscellaneous Indicator test:");

boolstatus = swGtolFrame.**AddIndicator**((int)swGtolIndicatorBorderType_e.swGtolIndicatorBorderType_OrientationPlane, (int)swGtolGeomCharSymbol_e.swGcsANG, sDatum); // add indicator for different BorderType and TolType

Debug.Print("Supported swGtolIndicatorBorderType_OrientationPlane BorderType AddIndicator return value is " + boolstatus);

IndicatorCount = swGtolFrame.**GetIndicatorCount**(); // should increase by 1

Debug.Print("Frame " + FrameCount + " IndicatorCount after one successful AddIndicator is " + IndicatorCount); // should increase by 1

boolstatus = swGtolFrame.**GetIndicator**(IndicatorCount, out lBorderType, out lTolType, out sDatum);

Debug.Print("Frame " + FrameCount + " just added GetIndicator: " + " (BorderType = " + lBorderType + " " + "TolType = " + lTolType + " " + "Datum = " + sDatum + ")");

if (sDatum != "B")

sDatum = "B";

else

sDatum = "A";

boolstatus = swGtolFrame.**SetIndicator**(IndicatorCount, (int)swGtolIndicatorBorderType_e.swGtolIndicatorBorderType_IntersectionPlane, (int)swGtolGeomCharSymbol_e.swGcsPERP, sDatum);

Debug.Print("Indicator " + IndicatorCount + " SetIndicator return value is " + boolstatus);

boolstatus = swGtolFrame.**GetIndicator**(IndicatorCount, out lBorderType, out lTolType, out sDatum);

Debug.Print("Indicator " + IndicatorCount + " SetIndicator values " + " (BorderType = " + lBorderType + " " + "TolType = " + lTolType + " " + "Datum = " + sDatum + ")");

Debug.Print(" ");

System.Diagnostics.Debugger.Break();

swGtolFrame = (GtolFrame)swGtol.**GetFrame**(swGtol.GetFrameCount());

Debug.Print("Frame " + 2 + " ToleranceType test");

boolstatus = swGtolFrame.**GetFrameToleranceType**(out swToleranceType);

Debug.Print("GetFrameToleranceType " + "returned " + boolstatus);

Debug.Print("GetFrameToleranceType " + "before set returned tolerance type as defined by swGtolGeomCharSymbol_e: " + swToleranceType);

boolstatus = swGtolFrame.**SetFrameToleranceType**((int)swGtolGeomCharSymbol_e.swGcsROUND);

Debug.Print("SetFrameToleranceType " + "returned " + boolstatus);

boolstatus = swGtolFrame.**GetFrameToleranceType**(out swTolType);

Debug.Print("GetFrameToleranceType " + "returned " + boolstatus);

Debug.Print("GetFrameToleranceType " + "after set returned tolerance type as defined by swGtolGeomCharSymbol_e: " + swTolType);

Debug.Print("");

System.Diagnostics.Debugger.Break();

sXMLString = swGtolFrame.**GetSymbolXml**();

Debug.Print("Symbol XML string: " + sXMLString);

// Set a new symbol XML string of last added frame

pos = -1;

pos = Strings.InStr(1, sXMLString, ".01"); // Note: converted Gtol has tolerance format of .01, not 0.01

if (pos != -1)

sXMLString = Strings.Replace(sXMLString, ".01", ".02");

else

{

pos = Strings.InStr(1, sXMLString, ".02");

if (pos != -1)

sXMLString = Strings.Replace(sXMLString, ".02", ".01");

}

boolstatus = swGtolFrame.**SetSymbolXml**(sXMLString);

Debug.Print("New symbol XML string: " + sXMLString);

}

// The SldWorks swApp variable is pre-assigned for you.

public SldWorks swApp;

}

}
