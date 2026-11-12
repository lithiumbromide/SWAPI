---
title: "ISetHoldLines Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "ISetHoldLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetHoldLines.html"
---

# ISetHoldLines Method (ISimpleFilletFeatureData2)

Sets the hold lines (boundaries) for this face blend fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetHoldLines( _
   ByVal Count As System.Integer, _
   ByRef PList As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim Count As System.Integer
Dim PList As System.Object

instance.ISetHoldLines(Count, PList)
```

### C#

```csharp
void ISetHoldLines(
   System.int Count,
   ref System.object PList
)
```

### C++/CLI

```cpp
void ISetHoldLines(
   System.int Count,
   System.Object^% PList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of hold lines
- `PList`: - in-process, unmanaged C++: Pointer to an array of hold lines of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This method corresponds to the Hold lines selection box available when creating face-blend fillets. See the SOLIDWORKS Help for more information about face-blend fillets and hold lines.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetHoldLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetHoldLineCount.html)
[ISimpleFilletFeatureData2::IGetHoldLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetHoldLines.html)
[ISimpleFilletFeatureData2::HoldLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~HoldLines.html)
[ISimpleFilletFeatureData2::CurvatureContinuous Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~CurvatureContinuous.html)
[ISimpleFilletFeatureData2::HelpPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~HelpPoint.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
