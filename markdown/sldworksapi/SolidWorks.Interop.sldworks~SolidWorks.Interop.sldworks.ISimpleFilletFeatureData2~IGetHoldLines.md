---
title: "IGetHoldLines Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "IGetHoldLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetHoldLines.html"
---

# IGetHoldLines Method (ISimpleFilletFeatureData2)

Gets the hold lines (boundaries) for a face blend fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetHoldLines( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim Count As System.Integer
Dim value As System.Object

value = instance.IGetHoldLines(Count)
```

### C#

```csharp
System.object IGetHoldLines(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ IGetHoldLines(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of hold lines

### Return Value

- in-process, unmanaged C++: Pointer to an array of hold lines of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISimpleFilletFeatureData2::GetHoldLineCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~GetHoldLineCount.html) before using this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

This method corresponds to the Hold lines selection box available when creating face-blend fillets. See the SOLIDWORKS Help for more information about face-blend fillets and hold lines.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::HoldLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~HoldLines.html)
[ISimpleFilletFeatureData2::CurvatureContinuous Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~CurvatureContinuous.html)
[ISimpleFilletFeatureData2::HelpPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~HelpPoint.html)
[ISimpleFilletFeatureData2::ISetHoldLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetHoldLines.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
