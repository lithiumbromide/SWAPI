---
title: "SetCustomCheckResult Method (ISWDesignCheck)"
project: "SOLIDWORKS Design Checker API Help"
interface: "ISWDesignCheck"
member: "SetCustomCheckResult"
kind: "method"
source: "dsgnchkapi/SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck~SetCustomCheckResult.html"
---

# SetCustomCheckResult Method (ISWDesignCheck)

Sets whether to report results from your SOLIDWORKS Design Check Custom Check validation macro as passed or failed.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCustomCheckResult( _
   ByVal vbIsCheckPassed As System.Boolean, _
   ByVal sfArrayFailedItems As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISWDesignCheck
Dim vbIsCheckPassed As System.Boolean
Dim sfArrayFailedItems As System.Object
Dim value As System.Integer

value = instance.SetCustomCheckResult(vbIsCheckPassed, sfArrayFailedItems)
```

### C#

```csharp
System.int SetCustomCheckResult(
   System.bool vbIsCheckPassed,
   System.object sfArrayFailedItems
)
```

### C++/CLI

```cpp
System.int SetCustomCheckResult(
   System.bool vbIsCheckPassed,
   System.Object^ sfArrayFailedItems
)
```

### Parameters

- `vbIsCheckPassed`: True to add your Custom Check to the **Passed Checks** results list and ignore sfArrayFailedItems, false to add your Custom Check to the **Failed Checks** results list and list sfArrayFailedItems
- `sfArrayFailedItems`: Array of strings of failed items found by your SOLIDWORKS Design Checker Custom Check validation macro; array name must be enclosed within parentheses (see **Example** and **Remarks**)

### Return Value

One of the following [dsgnchkError_e](SOLIDWORKS.Interop.dsgnchk~SOLIDWORKS.Interop.dsgnchk.dsgnchkError_e.html) enumerators:

- 0 = dsgnchkNOErr
- 8 = dsgnchkInvalidCallToAPI

## VBA Syntax

See [SWDesignCheck::SetCustomCheckResult](ms-its:dsgnchkapivb6.chm::/DesignCheckerLib~SWDesignCheck~SetCustomCheckResult.html).

## Examples

**Visual Basic for Applications (VBA)**

+++

‘**********************************************************

‘ If check passes, then pass true to SOLIDWORKS Design Checker API

‘**********************************************************

Sub PassCheck()

Dim swApp As SOLIDWORKS.SldWorks

Dim dcApp As DesignCheckerLib.SWDesignCheck

Set swApp = Application.SldWorks

Set dcApp = swApp.GetAddInObject("SWDesignChecker.SWDesignCheck")

Dim errorCode as Long

errorCode = dcApp.**SetCustomCheckResult**(True, Null)

End Sub

+++

‘**********************************************************

‘ If check fails, then pass false and either a one-dimensional string

‘ array as shown next or pass a two-dimensional string array as shown

‘ in the example after this example

‘**********************************************************

Sub FailedCheck1Dim()

Dim FailedItemsArr() As String

ReDim FailedItemsArr(1 To 4) As String

FailedItemsArr(1) = "Failed Item 1"

FailedItemsArr(2) = "Failed Item 2"

FailedItemsArr(3) = "Failed Item 3"

FailedItemsArr(4) = "Failed Item 4"

Dim swApp As SOLIDWORKS.SldWorks

Dim dcApp As DesignCheckerLib.SWDesignCheck

Set swApp = Application.SldWorks

Set dcApp = swApp.GetAddInObject("SWDesignChecker.SWDesignCheck")

Dim errorCode as Long

errorCode = dcApp.**SetCustomCheckResult**(False, (FailedItemsArr))

End Sub

+++

‘**********************************************************

‘ If check fails, then pass a two-dimensional array

‘ so that failed items are highlighted in the results list

‘ when a user selects them

' Names must be fully qualified for selection with

' [IModelDocExtension::SelectByID2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html)

‘**********************************************************

Sub **FailedCheck2Dim**()

Dim FailedItemsArr() As String

ReDim FailedItemsArr(0 To 2, 0 To 1) As String

FailedItemsArr(0, 0) = "RD2@Drawing View2"

FailedItemsArr(0, 1) = "DIMENSION"

FailedItemsArr(1, 0) = "RD1@Drawing View4"

FailedItemsArr(1, 1) = "DIMENSION"

FailedItemsArr(2, 0) = "My Failed Item 3"

FailedItemsArr(2, 1) = ""

Dim swApp As SOLIDWORKS.SldWorks

Dim dcApp As DesignCheckerLib.SWDesignCheck

Set swApp = Application.SldWorks

Set dcApp = swApp.GetAddInObject("SWDesignChecker.SWDesignCheck")

Dim errorCode as Long

errorCode = dcApp.**SetCustomCheckResult**(False, (FailedItemsArr))

End Sub

+++

‘ Enumerators

Dim FailedItemsArr As String

ReDim FailedItemsArr(0 To 2, 0 To 1) As String

While(...)

‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘

‘ Insert validation logic here

‘ Array of failed item names and types can be added to

‘ array in loop

‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘‘

ReDim preserve FailedItemsArr...

FailedItemsArr(iLoopCount, 0) = "RD2@Drawing View2"

FailedItemsArr(iLoopCount, 1) = "DIMENSION"

Wend

Dim swApp As SOLIDWORKS.SldWorks

Dim dcApp As DesignCheckerLib.SWDesignCheckSet

Set swApp = Application.SldWorks

Set dcApp = swApp.GetAddInObject("SWDesignChecker.SWDesignCheck")

Dim errorCode as Long

errorCode = dcApp.**SetCustomCheckResult** (False, (FailedItemsArr) )

## Examples

[Custom Check Document (VBA)](Custom_Check_Document_Example_VB.htm)

## Remarks

1. Create a Custom Check validation macro. Guidelines for creating this macro appear below. Additionally an example is linked to this topic that you can examine and test.
2. Register the Custom Check macro with SOLIDWORKS Design Checker. See the SOLIDWORKS SOLIDWORKS Design Checker Help for details on how to register the macro. The macro is stored with the standards file.
3. Check the document in SOLIDWORKS Design Checker using the standards file in which the Custom Check validation macro is stored.

Guidelines for creating a Custom Check validation macro:

- You can record the macro using a SOLIDWORKS macro recorder.
- You can have multiple procedures in your Custom Check validation macro.
- Only a zero-argument Custom Check procedure is supported.

If your Custom Check validation macro returns true, then your Custom Check validation macro passed; if your Custom Check validation macro returns false, then your Custom Check validation macro failed. If you provide fully qualified names of the failed items, then these items can be shown highlighted when a user selects them in the results list by using a double array of strings with these characteristics:

- Array has two dimensions.
- Upper dimension contains the size (number) of failed items ,and the lower dimension has a size of 2.

  For example:

  ' Enumerators
  Dim FailedItemsArr As String
  ReDim FailedItemsArr(0 To 2, 0 To 1) As String
  ' Enumerators

  - 0 To 2: reflects the upper dimension size (3) and means that there are 3 failures in the result.
  - 0 To 1: reflects the lower dimension size (2) means that the lower dimension size is 2.
  - It is not mandatory for the array to start with 0; the array can start with any dimension; e.g., (1 To 10) or (11 To 15) or (-5 To -2), etc.
- In the (X,0) positions of the array, you must pass the failed item's name. In the (X,1) positions of the array, you must pass the failed item's type string as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html).

  For example:

  ' Dimension
  FailedItemsArr(0, 0) = "RD2@Drawing View2"
  FailedItemsArr(0, 1) = "DIMENSION"

  FailedItemsArr(1, 0) = "RD1@Drawing View4"
  FailedItemsArr(1, 1) = "DIMENSION"

  FailedItemsArr(2, 0) = "My Failed Item 3"
  FailedItemsArr(2, 1) = "Annotation"
  ' Dimension

  - Having a two-dimensional array or filling (X,1) positions is not mandatory.
  - You can have a single-dimensional array and fill it with strings (i.e., failed entity names).
  - If the type of failed entity is not the specified entity, then it is not shown as selected.
  - If the type of failed entity is not specified or is incorrect, then it is ignored.

## See Also

[ISWDesignCheck Interface](SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck.html)
[ISWDesignCheck Members](SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
