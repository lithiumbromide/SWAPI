---
title: "SetAllOverThisSide Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "SetAllOverThisSide"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetAllOverThisSide.html"
---

# SetAllOverThisSide Method (IGtol)

Sets whether this Gtol uses an All Over This Side leader.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetAllOverThisSide( _
   ByVal AllOverTS As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim AllOverTS As System.Boolean

instance.SetAllOverThisSide(AllOverTS)
```

### C#

```csharp
void SetAllOverThisSide(
   System.bool AllOverTS
)
```

### C++/CLI

```cpp
void SetAllOverThisSide(
   System.bool AllOverTS
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AllOverTS`: True to use an All Over This Side leader, false to not

## VBA Syntax

See [Gtol::SetAllOverThisSide](ms-its:sldworksapivb6.chm::/sldworks~Gtol~SetAllOverThisSide.html).

## Examples

'VBA Preconditions:

'Open a drawing.

```
Dim swApp As SldWorks
Dim Part As ModelDoc2
Dim myGtol As Gtol
Dim myAnno As Annotation
Dim boolstatus As Boolean
Dim longstatus As Long, longwarnings As Long
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
       myGtol.SetAllOverThisSide True
       Set myAnno = myGtol.GetAnnotation()
       If Not myAnno Is Nothing Then
          boolstatus = myAnno.SetPosition(0.801796955941255, 0.800162656875834, 0)
          longstatus = myAnno.SetLeader3(swLeaderStyle_e.swBENT, 0, True, False, False, False)
       End If
    End If
    Part.WindowRedraw
```

```
End Sub
```

## Remarks

This property is valid only for bent, perpendicular, and multi-jog leaders.

Use:

- [IGtol::IsAttached](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~IsAttached.html) to determine whether this symbol is currently using a leader.
- [IGtol::HasExtraLeader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~HasExtraLeader.html) to determine whether this symbol is using a bent leader.
- [IGtol::GetLeaderSide](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetLeaderSide.html) to determine where the leader is attached to the symbol.
- [IGtol::SetLeader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~SetLeader.html) to set the characteristics of the leader on this symbol.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetAllOverThisSide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetAllOverThisSide.html)
[IGtol::SetAllAroundThisSide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetAllAroundThisSide.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
