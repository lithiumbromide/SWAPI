---
title: "DAssemblyDocEvents_LargeDesignReviewStateChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_LargeDesignReviewStateChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_LargeDesignReviewStateChangeNotifyEventHandler.html"
---

# DAssemblyDocEvents_LargeDesignReviewStateChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the Large Design Review state changes in this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_LargeDesignReviewStateChangeNotifyEventHandler( _
   ByVal PreviousState As System.Short, _
   ByVal newState As System.Short _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_LargeDesignReviewStateChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_LargeDesignReviewStateChangeNotifyEventHandler(
   System.short PreviousState,
   System.short newState
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_LargeDesignReviewStateChangeNotifyEventHandler(
   System.short PreviousState,
   System.short newState
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `PreviousState`: Old LDR state as defined by

[swAssemblyMode_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyMode_e.html)
- `newState`: New LDR state as defined by swAssemblyMode_e

## VBA Syntax

See

[LargeDesignReviewStateChangeNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~LargeDesignReviewStateChangeNotify_EV.html)

.

## Examples

'VBA

'=============================================================

'1. Create a VBA macro with the module code below.

'2. Copy the Class1 code below into a new Class1 module.

'3. Open an assembly

'4. Run the macro.

'5. In the user interface, change the LDR state of the assembly.

'6. A message box appears when the LDR state changes.

'==================================================

'module

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swDocSpecification As SldWorks.DocumentSpecification

Dim swAssemblyEvents As Class1

Dim swAssembly As SldWorks.AssemblyDoc

Option Explicit

Sub main()

Set swApp = Application.SldWorks

Set swModel = swApp. ActiveDoc

Set swAssembly = swModel

' Set up event

Set swAssemblyEvents = New Class1

Set swAssemblyEvents.swAssembly = swAssembly

End Sub

‘Class1 module

Public WithEvents swAssembly As SldWorks.AssemblyDoc

Private Function swAssembly_ LargeDesignReviewStateChangeNotify (ByVal PreviousState As Integer, ByVal NewState As Integer) As Long

If (PreviousState = swAssemblyMode_LDR) Then

If (NewState = swAssemblyMode_LDR_EditAssembly) Then

MsgBox " Document state change from LDR to LDR Edit Assembly Mode", vbOKOnly, "LDR state change"

ElseIf (NewState = swAssemblyMode_LightWeight) Then

MsgBox " Document state change from LDR to LightWeight Assembly Mode", vbOKOnly, "LDR state change"

ElseIf (NewState = swAssemblyMode_Resolved) Then

MsgBox " Document state change from LDR to Resolve Assembly Mode", vbOKOnly, "LDR state change"

Else

MsgBox "Invalid Notification"

End If

ElseIf (PreviousState = swAssemblyMode_LDR_EditAssembly) Then

If (NewState = swAssemblyMode_LightWeight) Then

MsgBox " Document state change from LDR Edit assembly to LightWeight Assembly Mode", vbOKOnly, "LDR state change"

ElseIf (NewState = swAssemblyMode_Resolved) Then

MsgBox " Document state change from LDR Edit assembly to Resolve Assembly Mode", vbOKOnly, "LDR state change"

Else

MsgBox "Invalid notification"

End If

Else

MsgBox "Invalid notification"

End If

## Remarks

If developing a C++ application, use[swAssemblyLargeDesignReviewStateChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html)to register for this notification.

## Availability

SOLIDWORKS 2024 SP02, Revision Number 32.2
