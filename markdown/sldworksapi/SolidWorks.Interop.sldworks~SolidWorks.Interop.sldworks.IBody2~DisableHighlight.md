---
title: "DisableHighlight Property (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "DisableHighlight"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DisableHighlight.html"
---

# DisableHighlight Property (IBody2)

Disables highlighting of the selected body in the graphics area.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisableHighlight As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Boolean

instance.DisableHighlight = value

value = instance.DisableHighlight
```

### C#

```csharp
System.bool DisableHighlight {get; set;}
```

### C++/CLI

```cpp
property System.bool DisableHighlight {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to disable highlighting, false to not

## VBA Syntax

**Visual Basic for Applications (VBA)**

'--------------------------------------------

'

' Preconditions: Model document is open and

' contains at least one body.

'

' Postconditions: None

'

'--------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swPart As SldWorks.PartDoc
Dim swBody As SldWorks.Body2
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim vBodies As Variant
Dim i As Long
Dim sBodySelStr As String, sBodyTypeSelStr As String
Dim bRet As Boolean

Sub main()

Set swApp = Application.SldWorks
Set swPart = swApp.**ActiveDoc**
Set swModel = swPart

vBodies = swPart.**GetBodies2**(swAllBodies, True)
If IsEmpty(vBodies) Then End

Set swModelDocExt = swModel.Extension

For i = 0 To UBound(vBodies)
Set swBody = vBodies(i)
sBodySelStr = swBody.**GetSelectionId**
Select Case swBody.**GetType**
Case swSolidBody
sBodyTypeSelStr = "SOLIDBODY"
Case swSheetBody
sBodyTypeSelStr = "SURFACEBODY"
Case Else
Debug.Assert False
End Select

' Select a body
bRet = swModelDocExt.**SelectByID2**(sBodySelStr, sBodyTypeSelStr, 0#, 0#, 0#, True, 0, Nothing, swSelectOptionDefault): Debug.Assert bRet
' Disable highlighting of the body
swBody.**DisableHighlight** = True

' Select the body again to check that highlighting is off
swModel.**ClearSelection2** True
bRet = swModelDocExt.**SelectByID2**(sBodySelStr, sBodyTypeSelStr, 0#, 0#, 0#, True, 0, Nothing, swSelectOptionDefault): Debug.Assert bRet

' Re-enable highlighting of the body
swBody.**DisableHighlight** = False

' Select the body again to check that highlighting is on
swModel.**ClearSelection2** True
bRet = swModelDocExt.**SelectByID2**(sBodySelStr, sBodyTypeSelStr, 0#, 0#, 0#, True, 0, Nothing, swSelectOptionDefault): Debug.Assert bRet

swModel.**ClearSelection2** True

Next i

End Sub

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
