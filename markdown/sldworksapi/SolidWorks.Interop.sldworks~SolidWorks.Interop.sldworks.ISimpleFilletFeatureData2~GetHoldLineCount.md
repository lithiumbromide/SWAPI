---
title: "GetHoldLineCount Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "GetHoldLineCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetHoldLineCount.html"
---

# GetHoldLineCount Method (ISimpleFilletFeatureData2)

Gets the number of hold lines (boundaries) for a face blend fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHoldLineCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Integer

value = instance.GetHoldLineCount()
```

### C#

```csharp
System.int GetHoldLineCount()
```

### C++/CLI

```cpp
System.int GetHoldLineCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of hold lines

## VBA Syntax

See [SimpleFilletFeatureData2::GetHoldLineCount](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~GetHoldLineCount.html).

## Remarks

Call this method before calling [ISimpleFilletFeatureData::IGetHoldLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~IGetHoldLines.html) to get the size of the array for that method.

This method corresponds to the Hold lines selection box available when creating face-blend fillets. See the SOLIDWORKS Help for more information about face-blend fillets and hold lines.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::ISetHoldLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetHoldLines.html)
[ISimpleFilletFeatureData2::HoldLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~HoldLines.html)
[ISimpleFilletFeatureData2::CurvatureContinuous Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~CurvatureContinuous.html)
[ISimpleFilletFeatureData2::HelpPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~HelpPoint.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
