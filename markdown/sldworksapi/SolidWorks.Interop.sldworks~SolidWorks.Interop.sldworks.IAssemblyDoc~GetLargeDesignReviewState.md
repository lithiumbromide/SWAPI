---
title: "GetLargeDesignReviewState Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetLargeDesignReviewState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetLargeDesignReviewState.html"
---

# GetLargeDesignReviewState Method (IAssemblyDoc)

Gets the Large Design Review state of this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLargeDesignReviewState() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Integer

value = instance.GetLargeDesignReviewState()
```

### C#

```csharp
System.int GetLargeDesignReviewState()
```

### C++/CLI

```cpp
System.int GetLargeDesignReviewState();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Large Design Review state as defined by

[swLargeDesignReviewState_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLargeDesignReviewState_e.html)

## VBA Syntax

See

[AssemblyDoc::GetLargeDesignReviewState](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetLargeDesignReviewState.html)

.

## Examples

'VBA

'Open an assembly and run the macro.

'==========================================================

Dim swApp As SldWorks.SldWorks

Dim swAssemDoc As SldWorks.AssemblyDoc

Dim boolstatus As Boolean

Dim longstatus As Long, longwarnings As Long

Dim LDRState As Long

Option Explicit

Sub main()

Set swApp = Application.SldWorks

Set swAssemDoc = swApp. ActiveDoc

LDRState = swAssemDoc. GetLargeDesignReviewState

If (LDRState = 0) Then

Debug.Print "LDR State : None"

ElseIf (LDRState = 1) Then

Debug.Print "LDR State : LDR Mode"

Else

Debug.Print "LDR State : LDR with Assembly Edit Mode"

End If

End Sub

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)

[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2024 SP02, Revision Number 32.2
