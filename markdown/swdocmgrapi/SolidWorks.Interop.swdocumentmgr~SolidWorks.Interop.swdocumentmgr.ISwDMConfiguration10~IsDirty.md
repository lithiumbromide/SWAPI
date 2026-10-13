---
title: "IsDirty Method (ISwDMConfiguration10)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration10"
member: "IsDirty"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration10~IsDirty.html"
---

# IsDirty Method (ISwDMConfiguration10)

Gets whether this configuration is dirty (i.e., needs to be updated).

## Syntax

### Visual Basic (Declaration)

```vb
Function IsDirty() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration10
Dim value As System.Boolean

value = instance.IsDirty()
```

### C#

```csharp
System.bool IsDirty()
```

### C++/CLI

```cpp
System.bool IsDirty();
```

### Return Value

True if the configuration is dirty, false if not

## VBA Syntax

See [SwDMConfiguration10::IsDirty](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration10~IsDirty.html).

## Examples

**Visual Basic for Applications (VBA)**

Option Explicit

Sub main()

Const sLicenseKey As String = "`your_license_key`" ' Specify your license key

Const sDocFileName As String = "c:\test\Wiper_Plate_Assy.SLDASM" ' Specify your document

Dim swClassFact As SwDocumentMgr.SwDMClassFactory

Dim swDocMgr As SwDocumentMgr.SwDMApplication

Dim swDoc As SwDocumentMgr.SwDMDocument

Dim swCfgMgr As SwDocumentMgr.SwDMConfigurationMgr

Dim vCfgNameArr As Variant

Dim vCfgName As Variant

Dim swCfg As SwDocumentMgr.SwDMConfiguration10

Dim nDocType As Long

Dim nRetVal As Long

Dim i As Long

Dim bRet As Boolean

' Determine type of SOLIDWORKS file based on filename extension

If InStr(LCase(sDocFileName), "sldprt") > 0 Then

nDocType = swDmDocumentPart

ElseIf InStr(LCase(sDocFileName), "sldasm") > 0 Then

nDocType = swDmDocumentAssembly

ElseIf InStr(LCase(sDocFileName), "slddrw") > 0 Then

nDocType = swDmDocumentDrawing

Else

' Probably not a SOLIDWORKS file

nDocType = swDmDocumentUnknown

' So cannot open

Exit Sub

End If

Set swClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")

Set swDocMgr = swClassFact.**GetApplication**(sLicenseKey)

Set swDoc = swDocMgr.**GetDocument**(sDocFileName, nDocType, True, nRetVal): Debug.Assert swDmDocumentOpenErrorNone = nRetVal

Set swCfgMgr = swDoc.**ConfigurationManager**

Debug.Print "File = " & swDoc.FullName
Debug.Print " ActiveCfgName = " & swCfgMgr.**GetActiveConfigurationName**

vCfgNameArr = swCfgMgr.**GetConfigurationNames**

For Each vCfgName In vCfgNameArr
Set swCfg = swCfgMgr.**GetConfigurationByName**(vCfgName)
Debug.Print vCfgName & " -> Dirty Flag = " & swCfg.**IsDirty**
Next

End Sub

## Remarks

This method only supports documents saved in SOLIDWORKS 2006 and later.

If the configuration is dirty, then you can update its date by activating the configuration in SOLIDWORKS and saving the document while the configuration is active.

## See Also

[ISwDMConfiguration10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration10.html)
[ISwDMConfiguration10 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration10_members.html)

## Availability

SOLIDWORKS Document Manager API 2008 SP5
