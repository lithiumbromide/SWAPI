---
title: "SetAllAroundThisSide Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "SetAllAroundThisSide"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetAllAroundThisSide.html"
---

# SetAllAroundThisSide Method (IGtol)

Sets whether this GTol uses an All Around This Side leader.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetAllAroundThisSide( _
   ByVal AllAroundTS As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim AllAroundTS As System.Boolean

instance.SetAllAroundThisSide(AllAroundTS)
```

### C#

```csharp
void SetAllAroundThisSide(
   System.bool AllAroundTS
)
```

### C++/CLI

```cpp
void SetAllAroundThisSide(
   System.bool AllAroundTS
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AllAroundTS`: True to use an All Around This Side leader, false to not

## VBA Syntax

See [Gtol::SetAllAroundThisSide](ms-its:sldworksapivb6.chm::/sldworks~Gtol~SetAllAroundThisSide.html).

## Examples

'VBA Preconditions:

'Open a drawing.

```
Dim swApp As SldWorks
Dim Part As ModelDoc2
Dim myGtol As Gtol
Dim myAnno As Annotation
Dim boolstatus As Boolean
Dim longstatus As Long
Option Explicit
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set Part = swApp.ActiveDoc

    Set myGtol = Part.InsertGtol()
    If Not myGtol Is Nothing Then
       myGtol.SetFrameSymbols2 1, "<IGTOL-SPROF>", False, "", False, "", "", "", ""
       myGtol.SetFrameValues 1, ".031265", "", "", "", ""
       myGtol.SetFrameSymbols2 2, "", False, "", False, "", "", "", ""
       myGtol.SetFrameValues 2, "", "", "", "", ""
       myGtol.SetPTZHeight "", False
       myGtol.SetCompositeFrame False
       myGtol.SetText 4, ""
       myGtol.SetBetweenTwoPoints False, "", ""
       myGtol.SetAllAroundThisSide True
       Set myAnno = myGtol.GetAnnotation()
       If Not myAnno Is Nothing Then
          boolstatus = myAnno.SetPosition(0.801796955941255, 0.800162656875834, 0)
          longstatus = myAnno.SetLeader3(swLeaderStyle_e.swBENT, 0, True, False, False, False)
       End If
    End If
    Part.WindowRedraw

End Sub
```

## Remarks

This property is valid only for bent, perpendicular, and multi-jog leaders. To create bent, perpendicular, and multi-jog leaders, use [IAnnotation::SetLeader3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeader3.html).

Use:

- [IGtol::IsAttached](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~IsAttached.html) to determine whether this symbol is currently using a leader.
- [IGtol::HasExtraLeader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~HasExtraLeader.html) to determine whether this symbol is using a bent leader.
- [IGtol::GetLeaderSide](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetLeaderSide.html) to determine where the leader is attached to the symbol.
- [IGtol::SetLeader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~SetLeader.html) to set the characteristics of the leader on this symbol.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetAllAroundThisSide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetAllAroundThisSide.html)
[IGtol::SetAllOverThisSide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetAllOverThisSide.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
