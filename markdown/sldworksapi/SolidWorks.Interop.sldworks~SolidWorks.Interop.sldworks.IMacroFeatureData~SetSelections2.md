---
title: "SetSelections2 Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "SetSelections2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetSelections2.html"
---

# SetSelections2 Method (IMacroFeatureData)

Sets the selected objects for the macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSelections2( _
   ByVal Objects As System.Object, _
   ByVal SelMarks As System.Object, _
   ByVal DrViews As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim Objects As System.Object
Dim SelMarks As System.Object
Dim DrViews As System.Object

instance.SetSelections2(Objects, SelMarks, DrViews)
```

### C#

```csharp
void SetSelections2(
   System.object Objects,
   System.object SelMarks,
   System.object DrViews
)
```

### C++/CLI

```cpp
void SetSelections2(
   System.Object^ Objects,
   System.Object^ SelMarks,
   System.Object^ DrViews
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Objects`: Array of objects as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) to select (see **Remarks**)
- `SelMarks`: Array of selection marks (integers or longs) for the objects (see **Remarks**)
- `DrViews`: Array of [drawing views](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) (see **Remarks**)

## VBA Syntax

See [MacroFeatureData::SetSelections2](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~SetSelections2.html).

## Examples

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

## Remarks

Early bind the Objects, SelMarks, and DrViews arrays when declaring them to avoid possible problems when using other IMacroFeatureData methods.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetSelectionCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelectionCount.html)
[IMacroFeatureData::GetSelections3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelections3.html)
[IMacroFeatureData::IGetSelections3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections3.html)
[IMacroFeatureData::ISetSelections2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetSelections2.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
