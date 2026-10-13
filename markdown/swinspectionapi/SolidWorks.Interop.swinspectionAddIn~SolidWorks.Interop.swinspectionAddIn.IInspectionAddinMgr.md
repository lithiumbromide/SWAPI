---
title: "IInspectionAddinMgr Interface"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionAddinMgr"
member: ""
kind: "interface"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr.html"
---

# IInspectionAddinMgr Interface

Allows access to the inspection add-in manager.
**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IInspectionAddinMgr
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionAddinMgr
```

### C#

```csharp
public interface IInspectionAddinMgr
```

### C++/CLI

```cpp
public interface class IInspectionAddinMgr
```

## VBA Syntax

See [InspectionAddinMgr](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionAddinMgr.html).

## Examples

'=========================================================================
'Preconditions:
'1. Activate the SOLIDWORKS Inspection Add-in (**SOLIDWORKS Tools menu > Add-ins... > SOLIDWORKS Inspection**).
'2. Ensure **c:\temp\Export Testing** exists.
'3. Ensure the templates specified in the macro exist.
'4. Open `Public_Documents`**\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\nist_ftc_08_asme1_rc_sw1702_ra.sldprt**.
'5. Select **SOLIDWORKS File menu > Make drawing from part**.
' a. Select default settings in Sheet Format/Size dialog.
' b. In View Palette select all Import Annotations check boxes.
' c. Drag and drop "A" views onto the drawing sheet.
'6. Open an Immediate window.
'
'Postconditions:
' 1. Click OK to close message boxes as they appear.
' 2. Configures general and extraction settings.
' 3. Creates an inspection project.
' 4. Balloons the drawing. (Ballooning starts at Char ID = 17.)
' 5. Displays all the characteristic IDs.
' 6. Adds a vendor named Sample.
' 7. Displays inspection methods, operations, and vendors.
' 8. Exports Inspection reports (Microsoft Excel, 2D PDF, eDrawings) to **c:\temp\Export Testing**.
' 9. Close the Excel spreadsheet after it appears.
'10. Deletes vendor named Sample.
'11. Edits the inspection project by adding a document name.
'12. Re-balloons the drawing.
'13. Edits and applies the balloon settings.
'14. Re-balloons the drawing.
'15. Inspect the Immediate window.
'
'NOTE: Because the drawing is used elsewhere, do not save changes to it.
'================================================================================

Dim swApp As SldWorks.SldWorks
Dim INSPECTIONMgr As SWInspectionAddin.InspectionAddinMgr
Dim InspectionPrj As SWInspectionAddin.InspectionProject
Dim InspectionPrjData As SWInspectionAddin.InspectionProjectData
Dim BalloonSetting As SWInspectionAddin.BalloonSettings
Dim CharData As SWInspectionAddin.CharacteristicsData
Dim OperationList As Variant
Dim OperationIDs As Variant
Dim VendorList As Variant
Dim MethodList As Variant
Dim MethodIDs As Variant
Dim Arr As Variant
Dim TemplatePath As String
Dim FilePath As String
Dim Multisheet As Boolean
Dim Status As Boolean
Dim a As Long
Dim str As String
Dim err As Long
Dim boolstatus As Boolean

Option Explicit
Sub main()

Set swApp = Application.SldWorks

Set INSPECTIONMgr = swApp.GetAddInObject("Inspection.ExtSwAddin")
Set InspectionPrjData = INSPECTIONMgr.**CreateInspectionProjectData**("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS Inspection 2022 Addin\\Templates\\default.swidot")

'General settings
Debug.Print "Inspection general settings..."
Debug.Print ""
InspectionPrjData.**StartNumber** = 17

InspectionPrjData.**Sort** = 1
Debug.Print "Characteristic sort as defined by swiCharacteristicInfoSort_e: " & InspectionPrjData.**Sort**

InspectionPrjData.**Classification** = 0
Debug.Print "Defect classification as defined by swiCharacteristicClassification_e: " & InspectionPrjData.**Classification**

InspectionPrjData.**Extraction** = 0
Debug.Print "Type of extraction as defined by swiCharacteristicInfoExtraction_e: " & InspectionPrjData.**Extraction**

InspectionPrjData.**AutoBalloon** = True
Debug.Print "Autoballoon drawing? " & InspectionPrjData.**AutoBalloon**

'Extraction settings
Debug.Print ""
Debug.Print "Inspection extraction settings..."
Debug.Print ""
InspectionPrjData.**Basic** = True
Debug.Print "Basic dimensioning? " & InspectionPrjData.**Basic**

InspectionPrjData.**SecondaryUnits** = True
Debug.Print "Extract dual dimensions? " & InspectionPrjData.**SecondaryUnits**

'Create inspection project and balloon drawing
Set InspectionPrj = INSPECTIONMgr.**CreateInspectionProject**(InspectionPrjData, True, err)
If InspectionPrj Is Nothing Or Not err = swiErrorCode_e.swiSuccess Then
MsgBox ("Project not created")
End If

'Balloon settings only available after inspection project is created and model is ballooned
Debug.Print ""
Debug.Print "Inspection balloon settings..."
Debug.Print ""
Set BalloonSetting = INSPECTIONMgr.**GetBalloonSettings**()

If Not BalloonSetting Is Nothing Then

Dim offsetType As Long
offsetType = swiBalloonSettingsOffsetTypes_e.swiType_Dimensions

Dim i As Integer
i = 0

For i = 0 To 6

Dim isVis As Boolean
Dim x As Double
Dim y As Double

Status = BalloonSetting.**GetOffsets**(i, isVis, x, y)

Debug.Print "Offset type as defined by swiBalloonSettingsOffsetTypes_e: " & i & ", Balloon in document? " & isVis
Debug.Print "X-offset: " & x & ", Y-offset: " & y

Next i

Debug.Print "BalloonBalloonSetting.as defined by swiBalloonSettingsFit_e: " & BalloonSetting.**Fit**
Debug.Print "BalloonBalloonSetting.as defined by swiBalloonSettingsShape_e: " & BalloonSetting.**Shape**
Debug.Print "BalloonBalloonSetting.as defined by swiBalloonSettingsFit_e: " & BalloonSetting.**KeyCharFit**
Debug.Print "BalloonBalloonSetting.as defined by swiBalloonSettingsShape_e: " & BalloonSetting.**KeyCharShape**
Debug.Print "Prefix: " & BalloonSetting.**Prefix**
Debug.Print "KeyCharPrefix: " & BalloonSetting.**KeyCharPrefix**
Debug.Print "BalloonBalloonSetting.: " & BalloonSetting.**AttachToCharacteristic**
Debug.Print "BalloonBalloonSetting.: " & BalloonSetting.**RotateToMatchCharacteristic**
Debug.Print "BalloonBalloonSetting.as defined by swiBalloonSettingLayer_e: " & BalloonSetting.**Layer**
Debug.Print "BalloonBalloonSetting.: " & BalloonSetting.**UserSpecifiedLayer**

End If

'Get characteristics data
Arr = INSPECTIONMgr.**GetCharacteristicIDs**()

str = "Charactistic IDs: "
str = str & vbNewLine

For i = 0 To UBound(Arr)
'Add code here to get data for each characteristic
'Set CharData = INSPECTIONMgr.**GetCharacteristicsData**(Arr(i))
'Dim charID as Double
'Debug.Print "Characteristic ID = " & Arr(i) & " is a reference dimension? " & CharData.**Reference**
str = str & vbNewLine & Arr(i)
Next

MsgBox (str)

'Get inspection methods
str = "Inspection methods: "
str = str & vbNewLine
MethodList = Empty
Status = INSPECTIONMgr.**GetInspectionMethods**(MethodList, MethodIDs)

If Not Status Then
MsgBox ("Error getting inspection methods")
Else
For a = LBound(MethodList) To UBound(MethodList)
str = str & vbNewLine & MethodList(a)
Next
MsgBox (str)
End If

'Add inspection method
'If Not INSPECTIONMgr.**AddInspectionMethod**("aa") Then
'MsgBox ("Error adding inspection method")
'End If

'Edit inspection method
'If Not INSPECTIONMgr.**EditInspectionMethod**("9", "hh") Then
'MsgBox ("Error editing inspection method")
'End If

'Get operations
OperationList = Empty
OperationIDs = Empty
str = "Operations: "
str = str & vbNewLine

Status = INSPECTIONMgr.**GetOperations**(OperationList, OperationIDs)

If Not Status Then
MsgBox ("Error getting operations")
Else
For a = LBound(OperationList) To UBound(OperationList)
str = str & vbNewLine & OperationList(a)
Next
MsgBox (str)
End If

'Add operation
'If Not INSPECTIONMgr.**AddOperation**("Sample") Then
'MsgBox ("Error adding operation")
'End If

'Add vendor
If Not INSPECTIONMgr.**AddVendor**("Sample", swiVendorsInspectionType_e.swiREDUCED) Then
MsgBox ("Error adding vendor")
End If

'Get vendors
VendorList = Empty
str = "Vendors: "
str = str & vbNewLine
Status = INSPECTIONMgr.**GetVendors**(VendorList)

If Not Status Then
MsgBox ("Error getting vendors")
Else
For a = LBound(VendorList) To UBound(VendorList)
str = str & vbNewLine & VendorList(a)
Next
MsgBox (str)
End If

'Export Inspection report to Microsoft Excel
TemplatePath = "C:\ProgramData\SOLIDWORKS\SOLIDWORKS Inspection 2022 Addin\Templates\PPAP - Dimensional Test Results.xlt"
FilePath = "c:\temp\Export Testing\MyTestexcel.xlsx"
Multisheet = True

If Not InspectionPrj.**ExportToExcel**(TemplatePath, FilePath, Multisheet) Then
MsgBox ("Error exporting to Excel")
End If

'Export Inspection report to 2D PDF
If Not InspectionPrj.**ExportTo2DPDF**("c:\\temp\\Export Testing\\MyTest2DPDF.PDF") Then
MsgBox ("Error exporting to 2D PDF")
End If

'Export Inspection report to 3D PDF - only valid for Parts
'If Not InspectionPrj.**ExportTo3DPDF**("c:\\temp\\\Export Testing\\MyTest3DPDF.PDF") Then
'MsgBox ("Error exporting to 3D PDF")
'End If

'Export Inspection report to eDrawings
If Not InspectionPrj.**ExportToEDrawings**("c:\\temp\\Export Testing\\MyTestEDrawing.edrw") Then
MsgBox ("Error exporting to eDrawings")
End If

'Delete one inspection method
'aa
Dim delMethod(0) As Variant
Dim errorArray As Variant
delMethod(0) = "aa"
'errorArray = INSPECTIONMgr.**DeleteInspectionMethods**(delMethod)

'Delete one operation
'Sample
Dim delOperation(0) As Variant
delOperation(0) = "Sample"
'errorArray = INSPECTIONMgr.**DeleteOperations**(delOperation)

'Delete one vendor
'Sample
Dim delVendor(0) As Variant
delVendor(0) = "Sample"
errorArray = INSPECTIONMgr.**DeleteVendors**(delVendor)

Debug.Print "Vendor Sample deleted? " & errorArray(0)

'Edit inspection project and re-balloon the drawing
Set InspectionPrjData = INSPECTIONMgr.**GetInspectionProjectData**
InspectionPrjData.**DocumentName** = "Test drawing"
boolstatus = INSPECTIONMgr.**EditInspectionProject**(InspectionPrjData)

'Change and apply balloon settings and re-balloon the drawing
Set BalloonSetting = INSPECTIONMgr.**GetBalloonSettings**()
Debug.Print ""
Debug.Print "Balloon setting changes..."
Debug.Print ""

BalloonSetting.**Prefix** = "B"
Debug.Print "Prefix: " & BalloonSetting.**Prefix**

BalloonSetting.**KeyCharPrefix** = "C"
Debug.Print "KeyCharPrefix: " & BalloonSetting.**KeyCharPrefix**

BalloonSetting.**AttachToCharacteristic** = True
Debug.Print "BalloonBalloonSetting.AttachToCharacteristic: " & BalloonSetting.**AttachToCharacteristic**

BalloonSetting.**RotateToMatchCharacteristic** = True
Debug.Print "BalloonBalloonSetting.RotateToMatchCharacteristic: " & BalloonSetting.**RotateToMatchCharacteristic**

BalloonSetting.Layer = 0
Debug.Print "BalloonBalloonSetting.Layer as defined by swiBalloonSettingLayer_e: " & BalloonSetting.**Layer**

Status = BalloonSetting.**Apply**

End Sub

## Remarks

For more information, read:

- [Getting Started](Getting%20Started.html)
- **SOLIDWORKS Inspection Add-in user-interface help > SOLIDWORKS Inspection > SOLIDWORKS Inspection Add-in > Getting Started** and **Customization** topics.

## Accessors

[ISldWorks::GetAddInObject](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetAddInObject.html)

## See Also

[IInspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr_members.html)
[SolidWorks.Interop.swinspectionAddIn Namespace](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn_namespace.html)
