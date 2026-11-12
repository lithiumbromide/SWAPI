---
title: "Trap Error When Closing PropertyManager Page Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Trap_Error_When_Closing_PropertyManager_Page_Example_VB.NET.htm"
---

# Trap Error When Closing PropertyManager Page Example (VB.NET)

This example shows how to cancel the closing of a PropertyManager page if your application detects an error.

```vb
...
Sub OnClose(ByVal reason As Integer) Implements PropertyManagerPage2Handler4.OnClose
' This function must contain code, even if it does nothing, to prevent the
' .NET runtime environment from doing garbage collection at the wrong time.
Dim IndentSize As Integer
IndentSize = System.Diagnostics.Debug.IndentSize
System.Diagnostics.Debug.WriteLine(IndentSize)

If reason = SwConst.swPropertyManagerPageCloseReasons_e.swPropertyManagerPageClose_Okay Then
Dim e As New System.Runtime.InteropServices.COMException("cancel close", 1)

Throw e
End If
End Sub
...
```
