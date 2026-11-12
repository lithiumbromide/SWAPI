---
title: "SetLeader3 Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "SetLeader3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeader3.html"
---

# SetLeader3 Method (IAnnotation)

Sets the leader characteristics for this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLeader3( _
   ByVal LeaderStyle As System.Integer, _
   ByVal LeaderSide As System.Integer, _
   ByVal SmartArrowHeadStyle As System.Boolean, _
   ByVal Perpendicular As System.Boolean, _
   ByVal AllAround As System.Boolean, _
   ByVal Dashed As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim LeaderStyle As System.Integer
Dim LeaderSide As System.Integer
Dim SmartArrowHeadStyle As System.Boolean
Dim Perpendicular As System.Boolean
Dim AllAround As System.Boolean
Dim Dashed As System.Boolean
Dim value As System.Integer

value = instance.SetLeader3(LeaderStyle, LeaderSide, SmartArrowHeadStyle, Perpendicular, AllAround, Dashed)
```

### C#

```csharp
System.int SetLeader3(
   System.int LeaderStyle,
   System.int LeaderSide,
   System.bool SmartArrowHeadStyle,
   System.bool Perpendicular,
   System.bool AllAround,
   System.bool Dashed
)
```

### C++/CLI

```cpp
System.int SetLeader3(
   System.int LeaderStyle,
   System.int LeaderSide,
   System.bool SmartArrowHeadStyle,
   System.bool Perpendicular,
   System.bool AllAround,
   System.bool Dashed
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LeaderStyle`: Leader style as defined in [swLeaderStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderStyle_e.html) (see **Remarks**)
- `LeaderSide`: Leader side as defined in [swLeaderSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderSide_e.html) (see **Remarks**)
- `SmartArrowHeadStyle`: True to enable smart arrowhead style, false to disable it (see **Remarks**)
- `Perpendicular`: True to enable perpendicular bent leader display, false to disable it (see **Remarks**)
- `AllAround`: True to enable all around (weld, surface finish, or Gtol) symbol display, false to disable it (see **Remarks**)
- `Dashed`: True to enable dashed line leader display; false to enable solid-line leader (see **Remarks**)

### Return Value

Indicates whether the operation was successful (see **Remarks**)

## VBA Syntax

See [Annotation::SetLeader3](ms-its:sldworksapivb6.chm::/sldworks~Annotation~SetLeader3.html).

## Examples

[Insert GTol (C#)](Insert_GTol_Example_CSharp.htm)
[Insert GTol (VB.NET)](Insert_GTol_Example_VBNET.htm)
[Insert GTol (VBA)](Insert_GTol_Example_VB.htm)

## Remarks

Not all annotations support all styles of leaders or leader characteristics. Only notes, GTols, surface finish symbols, weld symbols, datum target symbols, and block instances support leaders of any kind.

- Weld symbol leaders can be hidden, but are always bent; straight leaders (swSTRAIGHT) are not supported.
- Datum target symbols can have straight or bent leaders, but cannot be hidden (swNO_LEADER is not supported).
- Only notes support underline leaders (swUNDERLINED).
- GTols are the only type of annotation that supports perpendicular bent leaders.
- GTols and weld symbols are the only types of annotations that support all around leader symbols.
- Datum target symbols are the only type of annotation that supports dashed leaders.

This method sets the characteristics of the annotation, not the individual leaders. You can get or set these characteristics whether leaders are displayed.

| Use... | To... |
| --- | --- |
| IAnnotation::GetDashedLeader | Determine whether this leader is a dashed line or a solid line. |
| IAnnotation::GetLeaderAllARound | Determine whether all around symbol display is enabled or disabled. |
| IAnnotation::GetLeaderPerpendicular | Determine whether perpendicular bent leader display is enabled or disabled. |
| IAnnotation::GetLeaderSide | Get the leader attachment side setting. |
| IAnnotation::GetLeaderStyle | Get style of leader (hidden, straight, bent, or underline). |
| IAnnotation::GetSmartArrowHeadStyle | Determine whether smart arrowhead style is enabled or disabled. |

You can set the leader side, smart arrowhead style, and bent leader values at any time. However, if leader display is disabled, you cannot affect the display of the annotation by setting these values. You can also set the perpendicular bent leader and all around symbol display at any time, but if bent leaders are disabled, you cannot affect the display of the annotation by setting these values.

The return status of this operation can have the following values:

- 0 = Leader characteristics were successfully set
- -1 = Leader characteristics were not set because of an unknown error
- -2 = Leader attachment side setting is invalid
- -3 = Leaders are not supported on this type of annotation
- -4 = Leaders cannot be disabled on this type of annotation
- -5 = Bent leaders cannot be disabled on this type of annotation
- -6 = Underline style leaders are not allowed on this type of annotation

If leader display is enabled, then this method changes the visible model.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetLeader Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeader.html)
[IAnnotation::GetLeaderCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderCount.html)
[IAnnotation::GetLeaderPointsAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderPointsAtIndex.html)
[IAnnotation::GetMultiJogLeaderCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaderCount.html)
[IAnnotation::GetMultiJogLeaders Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaders.html)
[IAnnotation::BentLeaderLength Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~BentLeaderLength.html)
[IAnnotation::LeaderLineStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderLineStyle.html)
[IAnnotation::LeaderThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderThickness.html)
[IAnnotation::LeaderThicknessCustom Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderThicknessCustom.html)
[IAnnotation::UseDocDispLeader Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~UseDocDispLeader.html)
[IAnnotation::SetLeaderAttachmentPointAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeaderAttachmentPointAtIndex.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
