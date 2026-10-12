---
title: "Replace Referenced Document Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Replace_Referenced_Document_Example_VB.htm"
---

# Replace Referenced Document Example (VBA)

This example shows how to replace a referenced document with a different document in an assembly.

```
'---------------------------------------------------------------------------------------------------
' Preconditions:
' 1. Create C:\temp\blade shaft.
' 2. Copy these files from C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings
'    to C:\temp\blade shaft:
'    * blade shaft.sldasm
'    * drive shaft.sldprt
'    * drive shaft pin.sldprt
'    * drive shaft plate.sldprt
' 3. Open C:\temp\blade shaft\drive shaft.sldprt and save the file as drive shaft2.sldprt.
' 4. Close drive shaft2.sldprt.
' 5. Open the Immediate window.
'
' Postconditions:
' 1. Replaces C:\temp\blade shaft\drive shaft.sldprt with C:\temp\blade shaft\drive shaft2.sldprt.
' 2. Examine the Immediate window and open C:\temp\blade shaft\blade shaft.sldasm, click Rebuild,
'    click File > Find References and examine the files listed under Name.
'------------------------------------------------------------------------------------------------------
Option Explicit
```

```
Const sReferencingDoc As String = "C:\temp\blade shaft\blade shaft.sldasm"
Const sOldDoc As String = "C:\temp\blade shaft\drive shaft.sldprt"
Const sNewDoc As String = "C:\temp\blade shaft\drive shaft2.sldprt"
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
```

```
    bRet = swApp.ReplaceReferencedDocument(sReferencingDoc, sOldDoc, sNewDoc)
    Debug.Print ("Reference to drive shaft.sldprt replaced with reference to drive shaft2.sldprt? " & bRet)
```

```
End Sub
```
