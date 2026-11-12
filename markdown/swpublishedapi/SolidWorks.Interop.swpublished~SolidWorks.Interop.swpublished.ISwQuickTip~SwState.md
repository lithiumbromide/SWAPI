---
title: "SwState Method (ISwQuickTip)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwQuickTip"
member: "SwState"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip~SwState.html"
---

# SwState Method (ISwQuickTip)

Calls this method to advise your add-in of the current add-in state.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SwState( _
   ByVal state As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwQuickTip
Dim state As System.Integer

instance.SwState(state)
```

### C#

```csharp
void SwState(
   System.int state
)
```

### C++/CLI

```cpp
void SwState(
   System.int state
)
```

### Parameters

- `state`: State of SOLIDWORKS application:

  - swQuickTipNoMode = 0x00000000
  - swQuickTipEmptySWFrameMode = 0x00000001
  - swQuickTipEmptyPartMode = 0x00000002
  - swQuickTipSketchingMode = 0x00000004
  - swQuickTipClosedProfileCompletedMode = 0x00000008
  - swQuickTipSketchDoneMode = 0x00000010
  - swQuickTipFirstFeatureDoneMode = 0x00000020
  - swQuickTipEmptyAssemblyMode = 0x00000040
  - swQuickTipAssemblyOneCompMode = 0x00000080
  - swQuickTipAssemblyMultiCompMode = 0x00000100
  - swQuickTipAssemblyMatedMode = 0x00000200
  - swQuickTipAssemblySimulatingMode = 0x00000400
  - swQuickTipEmptyDrawingMode = 0x00000800
  - swQuickTipDrawingOneViewMode = 0x00001000
  - swQuickTipPMBaseFeatureDialogMode = 0x00002000
  - swQuickTipPMYellowErrorMessageMode = 0x00004000 // Display this topic for error conditions when the yellow group box in a PropertyManager is displayed instructing the user to do something before he or she can continue.
  - swQuickTipPMMateDialogMode = 0x00008000
  - swQuickTipSheetMetalMode = 0x00010000
  - swQuickTipSketching3DMode = 0x00020000
  - swQuickTipDrawingEditSheetMode = 0x00040000
  - swQuickTipPMInsertModelViewMode = 0x00080000
  - swQuickTipPMInsertProjectedViewMode = 0x00100000
  - swQuickTipPMInsertComponentMode = 0x00200000
  - swQuickTipPMYellowGuidelinesMode = 0x00400000 // Display this topic if you want Quick Tips to know about the yellow group box in a PropertyManager that is displayed instructing the user to do something before he or she can continue.

## VBA Syntax

See [SwQuickTip::SwState](ms-its:swpublishedapivb6.chm::/swpublished~SwQuickTip~SwState.html).

## Remarks

You can call this method to set the internal state of the Quick Tips portion of your add-in application. For example, you can call this method in response to a menu selection or toolbar button click. This may correspond to beginner, intermediate, or advanced modes. The [ISwQuickTip](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwQuickTip.html) object can then store the state and send a suitable URL when SOLIDWORKS calls [ISwQuickTip::Url](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwQuickTip~Url.html).

## See Also

[ISwQuickTip Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip.html)
[ISwQuickTip Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
