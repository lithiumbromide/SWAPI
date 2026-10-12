---
title: "Get Gtol Frame Information Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Gtol_Frame_Information_Example_VBNET.htm"
---

# Get Gtol Frame Information Example (VB.NET)

This example shows how to obtain information from a Gtol frame.

'====================================================

'Preconditions:

'1. Open a drawing that contains a GTol created with either SolidWorks 2021 or SolidWorks 2022/2022+.

'2. Open an Immediate window.

'

'Postconditions:

'1. Select a Gtol in the graphics area.

' A Geometric Tolerance PropertyManager opens.

'2. Click on the macro window and press F5.

'3. Gtol format type and schema version print to the Immediate window.

'4. Press F5.

'5. The frame XML schema string prints to the Immediate window.

'6. Press F5.

'7. If the selected Gtol can be converted from 2021, it is attempted.

'8. Inspect the Immediate window.

'9. Press F5.

'10. Gets and sets From and To text and toggles SEPARATE REQUIREMENT.

'11. Inspect the Immediate window.

'12. Press F5.

'13. Gtol frames added and deleted.

'14. Inspect the Immediate window.

'15. Press F5.

'16. Add Indicator tests.

'17. Inspect the Immediate window.

'18. Press F5.

'19. Get Indicator tests.

'20. Inspect the Immediate window.

'21. Press F5.

'22. Delete Indicator tests.

'23. Inspect the Immediate window.

'24. Press F5.

'25. Miscellaneous Indicator tests.

'26. Inspect the Immediate window.

'27. Press F5.

'28. Tolerance type tests.

'29. Inspect the Immediate window.

'30. Press F5.

'31. Get and set symbol XML string.

'32. Inspect the Immediate window.

'====================================================

Imports SolidWorks.Interop.sldworks

Imports SolidWorks.Interop.swconst

Imports System.Runtime.InteropServices

Imports System

Partial Class SolidWorksMacro

Dim swModel As ModelDoc2

Dim boolstatus As Boolean

Dim longstatus As Integer, longwarnings As Integer

Dim swSelMgr As SelectionMgr

Dim swGtol As Gtol

Dim swGtolFrame As GtolFrame

Dim swGtolFrame1 As GtolFrame

Dim FrameCount As Integer

Dim sXMLString As String

Dim iIndicator As Integer

Dim iFrame As Integer

Dim lFormatType As Integer

Dim lFormatType1 As Integer

Dim lSchemaVersion As Integer

Dim sSchemaString As String

Dim swConversionError As swGtolFormatConversionError_e

Dim swFromText As String

Dim swToText As String

Dim swFromText1 As String

Dim swToText1 As String

Dim IndicatorCount As Integer

Dim sDatum As String

Dim lBorderType As swGtolIndicatorBorderType_e

Dim lTolType As swGtolGeomCharSymbol_e

Dim swToleranceType As swGtolGeomCharSymbol_e

Dim swTolType As Integer

Dim pos As Integer

Public Sub main()

swModel = swApp.ActiveDoc

swSelMgr = swModel.SelectionManager

Stop 'in the graphics area select Gtol created with either SolidWorks 2021 or SolidWorks 2022/2022+

Debug.Print("Select object type as defined by swSelectType_e: " & swSelMgr.GetSelectedObjectType3(1, -1))

swGtol = swSelMgr.GetSelectedObject6(1, -1)

swApp.**GetGtolFormatData**(lFormatType, lSchemaVersion)

Debug.Print("Gtol format type as defined by swGtolFormatType_e: " & lFormatType)

Debug.Print("Gtol schema version as defined by swGtolFormatSchemaVersion_e: " & lSchemaVersion)

Stop

sSchemaString = swApp.**GetGtolFrameXMLSchema**

Debug.Print("Gtol frame XML schema: " & sSchemaString)

Stop

boolstatus = swGtol.**CanConvertFormat**

If Not boolstatus = 0 Then

lFormatType1 = swGtol.**GetFormat**

If lFormatType1 = swGtolFormatType_e.GTOL_SW2021 Then

boolstatus = swModel.**GetSaveFlag**

If boolstatus <> 0 Then

swModel.Save()

End If

Debug.Print("SaveFlag BEFORE ConvertFormat is called " & swModel.GetSaveFlag)

swConversionError = swGtol.**ConvertFormat**

boolstatus = swModel.GetSaveFlag 'if successful, converted Gtol document should be dirty and return True

Debug.Print("SaveFlag AFTER ConvertFormat is called " & boolstatus)

lFormatType1 = swGtol.**GetFormat** 'converted from 2021 to 2022

End If

End If

Stop

boolstatus = swGtol.**GetFromTo**

boolstatus = swGtol.**GetFromToText**(swFromText, swToText)

swFromText = "FromMe"

swToText = "ToYou"

boolstatus = swGtol.**SetFromToText**(True, swFromText, swToText)

boolstatus = swGtol.**GetFromTo**

swFromText1 = ""

swToText1 = ""

boolstatus = swGtol.**GetFromToText**(swFromText1, swToText1) 'should be "FromMe" and "ToMe"

Debug.Print("From text: " & swFromText1)

Debug.Print("To text: " & swToText1)

boolstatus = swGtol.**SeparateRequirement**

If Not boolstatus = 0 Then

swGtol.**SeparateRequirement** = False

Else

swGtol.**SeparateRequirement** = True

End If

Debug.Print("SEPARATE REQUIREMENT ? " & swGtol.**SeparateRequirement**)

Stop

FrameCount = swGtol.**GetFrameCount**

Debug.Print("Frame count: " & FrameCount)

boolstatus = swGtol.**AddFrame**

FrameCount = swGtol.**GetFrameCount** 'frame count should increase by one

Debug.Print("Frame added. Frame count now: " & FrameCount)

boolstatus = swGtol.**DeleteFrame**(FrameCount)

FrameCount = swGtol.**GetFrameCount** 'frame count should decrease by 1, as just added frame was deleted

Debug.Print("Frame deleted. Frame count now: " & FrameCount)

boolstatus = swGtol.**AddFrame**

FrameCount = swGtol.**GetFrameCount** 'frame count should increase by 1

Debug.Print("Frame added. Frame count now: " & FrameCount)

Stop

swGtolFrame = swGtol.**GetFrame**(FrameCount)

IndicatorCount = swGtolFrame.**GetIndicatorCount**

sDatum = "A"

Debug.Print(" ")

Debug.Print("Frame " & FrameCount & " IndicatorCount is " & IndicatorCount & ": AddIndicator test")

'supported border types: swGtolIndicatorBorderType_CollectionPlane, swGtolIndicatorBorderType_OrientationPlane swGtolIndicatorBorderType_IntersectionPlane swGtolIndicatorBorderType_DirectionFeature

'supported tolerance types: swGcsPARALLEL swGcsPERP swGcsANG swGcsCIRCRUNOUT swGcsSYMMETRY

boolstatus = swGtolFrame.**AddIndicator**(swGtolIndicatorBorderType_e.swGtolIndicatorBorderType_IntersectionPlane, swGtolGeomCharSymbol_e.swGcsFLAT, sDatum) 'unsupported TolType

Debug.Print("Unsupported TolType swGcsFLAT. AddIndicator return value is " & boolstatus)

boolstatus = swGtolFrame.**AddIndicator**(swGtolGeomCharSymbol_e.swGcsFLAT, swGtolGeomCharSymbol_e.swGcsSYMMETRY, sDatum) 'unsupported BorderType

Debug.Print("Unsupported BorderType swGcsFLAT. AddIndicator return value is " & boolstatus)

boolstatus = swGtolFrame.**AddIndicator**(swGtolIndicatorBorderType_e.swGtolIndicatorBorderType_IntersectionPlane, swGtolGeomCharSymbol_e.swGcsSYMMETRY, sDatum) 'supported BorderType and TolType

Debug.Print("Supported BorderType swGtolIndicatorBorderType_IntersectionPlane and TolType swGcsSYMMETRY. AddIndicator return value is " & boolstatus)

IndicatorCount = swGtolFrame.**GetIndicatorCount**

Debug.Print("")

Debug.Print("Frame " & FrameCount & " IndicatorCount after one successful AddIndicator is " & IndicatorCount) 'should increase by 1 from AddIndicator success

Debug.Print(" ")

Stop

IndicatorCount = swGtolFrame.**GetIndicatorCount**

iIndicator = 0

IFrame = 0

FrameCount = swGtol.**GetFrameCount**

Debug.Print("FrameCount is " & FrameCount & ": GetIndicator test")

For iFrame = 1 To FrameCount

lBorderType = -1

lTolType = -1

sDatum = ""

swGtolFrame1 = swGtol.**GetFrame**(iFrame)

For iIndicator = 1 To IndicatorCount

boolstatus = swGtolFrame1.**GetIndicator**(iIndicator, lBorderType, lTolType, sDatum)

Debug.Print("Frame: " & iFrame & " Indicator index: " & iIndicator & " (BorderType as defined by swGtolIndicatorBorderType_e = " & lBorderType & " " & "TolType as defined by swGtolGeomCharSymbol_e = " & lTolType & " " & "Datum = " & sDatum & ")")

Next

Next

Debug.Print(" ")

Stop

Debug.Print("Frame " & FrameCount & " DeleteIndicator test")

boolstatus = swGtolFrame.**DeleteIndicator**(IndicatorCount)

Debug.Print("DeleteIndicator return value is " & boolstatus)

IndicatorCount = swGtolFrame.**GetIndicatorCount** 'should decrease by 1, as indicator deleted

Debug.Print("IndicatorCount is " & IndicatorCount & " after DeleteIndicator")

Stop

Debug.Print(" ")

Debug.Print("Miscellaneous Indicator test:")

boolstatus = swGtolFrame.**AddIndicator**(swGtolIndicatorBorderType_e.swGtolIndicatorBorderType_OrientationPlane, swGtolGeomCharSymbol_e.swGcsANG, sDatum) 'add indicator for different BorderType and TolType

Debug.Print("Supported swGtolIndicatorBorderType_OrientationPlane BorderType AddIndicator return value is " & boolstatus)

IndicatorCount = swGtolFrame.**GetIndicatorCount** 'should increase by 1

Debug.Print("Frame " & FrameCount & " IndicatorCount after one successful AddIndicator is " & IndicatorCount) 'should increase by 1

boolstatus = swGtolFrame.**GetIndicator**(IndicatorCount, lBorderType, lTolType, sDatum)

Debug.Print("Frame " & FrameCount & " just added GetIndicator: " & " (BorderType = " & lBorderType & " " & "TolType = " & lTolType & " " & "Datum = " & sDatum & ")")

If Not sDatum = "B" Then

sDatum = "B"

Else

sDatum = "A"

End If

boolstatus = swGtolFrame.**SetIndicator**(IndicatorCount, swGtolIndicatorBorderType_e.swGtolIndicatorBorderType_IntersectionPlane, swGtolGeomCharSymbol_e.swGcsPERP, sDatum)

Debug.Print("Indicator " & IndicatorCount & " SetIndicator return value is " & boolstatus)

boolstatus = swGtolFrame.**GetIndicator**(IndicatorCount, lBorderType, lTolType, sDatum)

Debug.Print("Indicator " & IndicatorCount & " SetIndicator values " & " (BorderType = " & lBorderType & " " & "TolType = " & lTolType & " " & "Datum = " & sDatum & ")")

Debug.Print(" ")

Stop

swGtolFrame = swGtol.**GetFrame**(swGtol.**GetFrameCount**)

Debug.Print("Frame " & 2 & " ToleranceType test")

boolstatus = swGtolFrame.**GetFrameToleranceType**(swToleranceType)

Debug.Print("GetFrameToleranceType " & "returned " & boolstatus)

Debug.Print("GetFrameToleranceType " & "before set returned tolerance type as defined by swGtolGeomCharSymbol_e: " & swToleranceType)

boolstatus = swGtolFrame.**SetFrameToleranceType**(swGtolGeomCharSymbol_e.swGcsROUND)

Debug.Print("SetFrameToleranceType " & "returned " & boolstatus)

boolstatus = swGtolFrame.**GetFrameToleranceType**(swTolType)

Debug.Print("GetFrameToleranceType " & "returned " & boolstatus)

Debug.Print("GetFrameToleranceType " & "after set returned tolerance type as defined by swGtolGeomCharSymbol_e: " & swTolType)

Debug.Print("")

Stop

sXMLString = swGtolFrame.**GetSymbolXml**

Debug.Print("Symbol XML string: " & sXMLString)

'Set a new symbol XML string of last added frame

pos = -1

pos = InStr(1, sXMLString, ".01") 'Note: converted Gtol has tolerance format of .01, not 0.01

If Not pos = -1 Then

sXMLString = Replace(sXMLString, ".01", ".02")

Else

pos = InStr(1, sXMLString, ".02")

If Not pos = -1 Then

sXMLString = Replace(sXMLString, ".02", ".01")

End If

End If

boolstatus = swGtolFrame.**SetSymbolXml**(sXMLString)

Debug.Print("New symbol XML string: " & sXMLString)

End Sub

''' <summary>

''' The SldWorks swApp variable is pre-assigned for you.

''' </summary>

Public swApp As SldWorks

End Class
