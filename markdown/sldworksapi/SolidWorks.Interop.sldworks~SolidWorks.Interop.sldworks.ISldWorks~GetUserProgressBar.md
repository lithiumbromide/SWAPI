---
title: "GetUserProgressBar Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetUserProgressBar"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserProgressBar.html"
---

# GetUserProgressBar Method (ISldWorks)

Gets a progress indicator.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUserProgressBar( _
   ByRef PProgressBar As UserProgressBar _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim PProgressBar As UserProgressBar
Dim value As System.Boolean

value = instance.GetUserProgressBar(PProgressBar)
```

### C#

```csharp
System.bool GetUserProgressBar(
   out UserProgressBar PProgressBar
)
```

### C++/CLI

```cpp
System.bool GetUserProgressBar(
   [Out] UserProgressBar^ PProgressBar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PProgressBar`: [IUserProgressBar](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar.html)

### Return Value

True if the progress indicator object is returned, false if not

## VBA Syntax

See [SldWorks::GetUserProgressBar](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetUserProgressBar.html).

## Examples

[Start, Update, and Stop Progress Indicator (VBA)](Start,_Update,_and_Stop_User_Progress_Indicator_Example_VB.htm)
[Start, Update, and Stop Progress Indicator (VB.NET)](Start,_Update,_and_Stop_User_Progress_Bar_Example_VBNET.htm)
[Start, Update, and Stop Progress Indicator (C#)](Start,_Update,_and_Stop_User_Progress_Bar_Example_CSharp.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[IStatusBarPane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStatusBarPane.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
